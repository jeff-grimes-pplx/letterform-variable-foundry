"""Apertide original skeleton/outline engine. No font or image is read here.

Centerline cubic Beziers are expanded by an elliptical nib (vertical stems
thicker than horizontals). Fixed parameter subdivision keeps every master
interpolation-compatible. Cubic Hermite fits to the analytic offset envelope
preserve tangent continuity at smooth joins. Overlapping parts are left as
overlapping contours (consistent direction) so variable interpolation stays
compatible; static instances get overlap removal at compile time.
See ../LICENSE.txt. Engine version 1.1.
"""
from dataclasses import dataclass
from math import hypot, sqrt, cos, atan2
from fontTools.pens.recordingPen import RecordingPen

TENSION = (0.64, 0.56, 0.64, 0.56)  # NE, SE, SW, NW handle ratios
BLADE = 16  # degrees: every free terminal is cut 16 deg off the nearest axis


import re as _re


def xform_d(d, sx, sy, dx, dy):
    """Apply an affine transform to an SVG path string made of M/L/C/Z commands."""
    out = []
    for tok in _re.findall(r'[MLCZ]|-?\d+(?:\.\d+)?', d):
        out.append(tok)
    res = []; i = 0; nums = []
    def flush():
        nonlocal nums
        pts = []
        for j in range(0, len(nums), 2):
            pts.append(f'{nums[j] * sx + dx:.2f} {nums[j + 1] * sy + dy:.2f}')
        nums = []
        return ' '.join(pts)
    for tok in out:
        if tok in 'MLCZ':
            if nums:
                res.append(flush())
            res.append(tok)
        else:
            nums.append(float(tok))
    if nums:
        res.append(flush())
    return ''.join(t if t in 'MLCZ' else t + ' ' for t in res).strip()


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(a, s): return (a[0] * s, a[1] * s)
def mix(a, b, t): return add(mul(a, 1 - t), mul(b, t))


def cubic(p, t):
    u = 1 - t
    return tuple(u * u * u * p[0][i] + 3 * u * u * t * p[1][i] + 3 * u * t * t * p[2][i] + t * t * t * p[3][i] for i in (0, 1))


def deriv(p, t):
    u = 1 - t
    return tuple(3 * u * u * (p[1][i] - p[0][i]) + 6 * u * t * (p[2][i] - p[1][i]) + 3 * t * t * (p[3][i] - p[2][i]) for i in (0, 1))


def signed_area(contour):
    """contour: list of (type, points) where points are on-curve/off-curve tuples; area from on-curve polygon."""
    pts = [seg[-1] for seg in contour]
    a = 0
    for i in range(len(pts)):
        x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % len(pts)]
        a += x0 * y1 - x1 * y0
    return a / 2


class Path:
    """Centerline path in glyph-local coordinates (before sidebearing shift)."""

    def __init__(self):
        self.segs = []; self.current = None; self.start = None; self.closed = False
        self.widths = []  # per segment (w0, w1) nib multipliers
        self._w = 1.0

    def M(self, x, y, wd=1.0):
        self.current = (x, y); self.start = self.current; self._w = wd; return self

    def L(self, x, y, wd=None):
        wd = self._w if wd is None else wd
        self.segs.append(('L', (self.current, (x, y)))); self.widths.append((self._w, wd))
        self.current = (x, y); self._w = wd; return self

    def C(self, x1, y1, x2, y2, x, y, wd=None):
        wd = self._w if wd is None else wd
        self.segs.append(('C', (self.current, (x1, y1), (x2, y2), (x, y)))); self.widths.append((self._w, wd))
        self.current = (x, y); self._w = wd; return self

    def Q(self, cx, cy, x, y, k0=0.56, k1=0.56, wd=None):
        """Cubic turn from the current point to (x, y); both tangents aim at corner (cx, cy).
        k0/k1 are handle lengths as fractions of the distance to the corner (0.5523 = ellipse)."""
        x0, y0 = self.current
        return self.C(x0 + (cx - x0) * k0, y0 + (cy - y0) * k0, x + (cx - x) * k1, y + (cy - y) * k1, x, y, wd)

    def Z(self):
        if hypot(*sub(self.current, self.start)) > 1e-6:
            raise ValueError('closed centerline must end exactly at its start')
        self.closed = True; return self

    def svg(self, dx=0):
        out = [f'M{self.start[0] + dx:.2f} {self.start[1]:.2f}']
        for typ, pts in self.segs:
            out.append(typ + ' '.join(f'{x + dx:.2f} {y:.2f}' for x, y in pts[1:]))
        if self.closed:
            out.append('Z')
        return ' '.join(out)


@dataclass
class Design:
    weight: float = 400
    width: float = 100

    def __post_init__(self):
        w = self.weight
        # Vertical stem thickness, units/em. 200→46, 400→82, 800→142.
        self.s = 46 + (w - 200) * 0.18 if w <= 400 else 82 + (w - 400) * 0.15
        # Horizontal stroke thickness: modest contrast that grows with weight.
        self.h = self.s * (0.90 - (w - 200) * 0.00017)
        # Skeleton width factor. 75→0.78, 100→1.0, 125→1.24.
        self.f = 0.78 + (self.width - 75) * 0.0088 if self.width <= 100 else 1 + (self.width - 100) * 0.0096
        # Condensed masters use a lighter nib so counters survive; heavier weights need more of it.
        kw = max(0.0, (w - 400) / 400)
        self.s *= (1 - (0.34 + 0.18 * kw) * (1 - self.f)) if self.f < 1 else (1 + 0.08 * (self.f - 1))
        self.cap = 700; self.xheight = 520; self.asc = 740; self.desc = -210
        self.over_cap = 12; self.over_x = 10
        # Boldness parameter: Light -0.6, Regular 0, Black 1. Recipes use it for
        # optical corrections (opening counters, thinning crowded diagonals).
        self.k = (self.s - 82) / 60
        self.kb = max(0.0, self.k)

    def W(self, v):
        return v * self.f * (1 + 0.07 * self.kb)

    def derive(self, nib_mult):
        """Copy with a heavier/lighter nib (for small figures that are scaled down later)."""
        d2 = Design(self.weight, self.width)
        d2.s = self.s * nib_mult; d2.h = self.h * nib_mult
        d2.k = (d2.s - 82) / 60; d2.kb = max(0.0, d2.k)
        return d2

    def SB(self, v):
        """Sidebearing: follows width partially and tightens as weight grows."""
        return v * (0.80 + 0.20 * self.f) - (self.s - 82) * 0.05


class Drawing:
    def __init__(self, d, width=500, left=45, right=45):
        self.d = d; self.w = d.W(width); self.left = d.SB(left); self.right = d.SB(right)
        self.advance = self.left + self.w + self.right
        self.contours = []  # list of lists of ('L',(pt,)) or ('C',(c1,c2,pt))
        self.skeleton = []
        self.anchors = {}   # name -> (x, y) in final glyph coordinates

    def anchor(self, name, x, y):
        """Anchor in box coordinates (sidebearing added here)."""
        self.anchors[name] = (x + self.left, y)

    def transform(self, sx=1.0, sy=1.0, dx=0.0, dy=0.0):
        """Affine transform of finished contours and anchors (used for small figures)."""
        f = lambda p: (p[0] * sx + dx, p[1] * sy + dy)
        new = []
        for start, segs in self.contours:
            new.append((f(start), [('L', f(sg[1])) if sg[0] == 'L' else ('C', f(sg[1]), f(sg[2]), f(sg[3])) for sg in segs]))
        if sx * sy < 0:  # reflection flips winding: reverse every contour
            rev = []
            for start, segs in new:
                pts = [start] + [sg[-1] for sg in segs]
                nsegs = []
                for i in range(len(segs) - 1, -1, -1):
                    sg = segs[i]; prev = pts[i]
                    nsegs.append(('L', prev) if sg[0] == 'L' else ('C', sg[2], sg[1], prev))
                rev.append((pts[-1], nsegs))
            new = rev
        self.contours = new
        self.anchors = {k: f(v) for k, v in self.anchors.items()}
        self.advance = self.advance * abs(sx)
        for sk in self.skeleton:
            sk['d'] = xform_d(sk['d'], sx, sy, dx, dy); sk['s'] = round(sk['s'] * abs(sx), 2); sk['h'] = round(sk['h'] * abs(sy), 2)

    def absorb(self, other, dx=0.0, dy=0.0):
        """Append another drawing's contours (already in its own glyph coordinates)."""
        f = lambda p: (p[0] + dx, p[1] + dy)
        for start, segs in other.contours:
            self.contours.append((f(start), [('L', f(sg[1])) if sg[0] == 'L' else ('C', f(sg[1]), f(sg[2]), f(sg[3])) for sg in segs]))
        for sk in other.skeleton:
            sk2 = dict(sk); sk2['d'] = xform_d(sk['d'], 1, 1, dx, dy); self.skeleton.append(sk2)
        for k, v in other.anchors.items():
            self.anchors.setdefault(k, f(v))

    # -- contour emission -------------------------------------------------
    def _emit(self, start, segs, clockwise=True):
        """segs: list of ('L', end) or ('C', c1, c2, end). Normalizes direction."""
        area = 0
        pts = [start] + [s[-1] for s in segs]
        for i in range(len(pts)):
            x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % len(pts)]
            area += x0 * y1 - x1 * y0
        is_cw = area < 0  # y-up: negative signed area == clockwise
        if is_cw != clockwise:
            # reverse
            rev = []
            cur_start = pts[-1]
            allpts = [start]
            for s in segs:
                allpts.append(s[-1])
            # rebuild reversed
            n = len(segs)
            new_segs = []
            for i in range(n - 1, -1, -1):
                s = segs[i]
                prev_pt = start if i == 0 else segs[i - 1][-1]
                if s[0] == 'L':
                    new_segs.append(('L', prev_pt))
                else:
                    new_segs.append(('C', s[2], s[1], prev_pt))
            start, segs = cur_start, new_segs
        self.contours.append((start, segs))

    def polygon(self, points):
        pts = [(x + self.left, y) for x, y in points]
        self._emit(pts[0], [('L', p) for p in pts[1:]] + [('L', pts[0])], clockwise=True)

    def rect(self, x0, y0, x1, y1):
        self.polygon([(x0, y0), (x0, y1), (x1, y1), (x1, y0)])

    def ellipse(self, cx, cy, rx, ry, k=0.5523):
        """Filled ellipse (no counter)."""
        sh = lambda x, y: (x + self.left, y)
        segs = [('C', sh(cx + k * rx, cy + ry), sh(cx + rx, cy + k * ry), sh(cx + rx, cy)),
                ('C', sh(cx + rx, cy - k * ry), sh(cx + k * rx, cy - ry), sh(cx, cy - ry)),
                ('C', sh(cx - k * rx, cy - ry), sh(cx - rx, cy - k * ry), sh(cx - rx, cy)),
                ('C', sh(cx - rx, cy + k * ry), sh(cx - k * rx, cy + ry), sh(cx, cy + ry))]
        self._emit(sh(cx, cy + ry), segs, clockwise=True)
        self.skeleton.append({'d': f'M{cx + self.left:.2f} {cy:.2f}', 's': round(2 * rx, 2), 'h': round(2 * ry, 2), 'w': [[1.0, 1.0]],
                              'cap0': None, 'cap1': None, 'closed': False, 'kind': 'dot'})

    def set_raw_width(self, w):
        self.w = w; self.advance = self.left + self.w + self.right

    def diag_hw(self, x0, y0, x1, y1, scale=1.0):
        ang = atan2(abs(x1 - x0), abs(y1 - y0))  # from vertical, 0..pi/2
        t = self.d.s * scale * (0.90 + 0.10 * cos(ang))  # a little lighter when more horizontal
        return t / (2 * max(0.25, cos(ang)))

    def diag(self, x0, y0, x1, y1, scale=1.0, cut1=0.0):
        """Diagonal stem with horizontal end cuts; perpendicular thickness compensated.
        cut1 tilts the end cut at (x1, y1) by that many degrees (blade terminals)."""
        from math import tan, radians
        hw = self.diag_hw(x0, y0, x1, y1, scale)
        self.skeleton.append({'d': f'M{x0 + self.left:.2f} {y0:.2f}L{x1 + self.left:.2f} {y1:.2f}',
                              's': round(self.d.s * scale, 2), 'h': round(self.d.s * scale, 2), 'w': [[1.0, 1.0]],
                              'cap0': None, 'cap1': 'blade' if cut1 else None, 'closed': False, 'kind': 'diag'})
        if cut1:
            # move the two end corners along the stem edges so the cut line rotates
            dx = (x1 - x0) / (y1 - y0) if y1 != y0 else 0.0
            tt = tan(radians(cut1))
            # corner at x1-hw: cut line y = y1 + (x - x1) * tt; edge x = x1 - hw + dx*(y - y1)
            ya = y1 + (-hw) * tt / (1 - dx * tt); yb = y1 + (hw) * tt / (1 - dx * tt)
            pa = (x1 - hw + dx * (ya - y1), ya); pb = (x1 + hw + dx * (yb - y1), yb)
            self.polygon([(x0 - hw, y0), (x0 + hw, y0), pb, pa])
        else:
            self.polygon([(x0 - hw, y0), (x0 + hw, y0), (x1 + hw, y1), (x1 - hw, y1)])

    def dot(self, x, y, scale=1.0):
        from math import tan, radians
        s = self.d.s * scale * 1.06; rise = s * tan(radians(BLADE))
        self.skeleton.append({'d': f'M{x + self.left:.2f} {y:.2f}', 's': round(s, 2), 'h': round(s, 2), 'w': [[1.0, 1.0]],
                              'cap0': None, 'cap1': None, 'closed': False, 'kind': 'dot'})
        self.polygon([(x - s / 2, y - s / 2), (x - s / 2, y + s / 2 - rise / 2), (x + s / 2, y + s / 2 + rise / 2), (x + s / 2, y - s / 2)])

    def stroke(self, path, scale=1.0, contrast=1.0, record=True, cap0=None, cap1=None):
        """cap0/cap1: absolute angle (degrees) of the terminal cut line at the start/end
        of an open stroke; None = cut perpendicular to the stroke."""
        rx0 = self.d.s / 2 * scale; ry0 = self.d.h / 2 * scale * contrast
        if record:
            self.skeleton.append({'d': path.svg(self.left), 's': round(2 * rx0, 2), 'h': round(2 * ry0, 2),
                                  'w': [list(map(lambda v: round(v, 3), w)) for w in path.widths],
                                  'cap0': cap0, 'cap1': cap1, 'closed': path.closed})

        def off(typ, p, t, side, wseg):
            k = t * t * (3 - 2 * t)
            wm = wseg[0] + (wseg[1] - wseg[0]) * k
            rx = rx0 * wm; ry = ry0 * wm
            pos = mix(p[0], p[1], t) if typ == 'L' else cubic(p, t)
            dv = sub(p[-1], p[0]) if typ == 'L' else deriv(p, t)
            mag = max(1e-9, hypot(*dv)); n = (-dv[1] / mag, dv[0] / mag)
            den = max(1e-9, sqrt(rx * rx * n[0] * n[0] + ry * ry * n[1] * n[1]))
            o = (side * rx * rx * n[0] / den, side * ry * ry * n[1] / den)
            if typ == 'C':
                # Curvature clamp: on the inside of a bend the offset may not exceed the
                # radius of curvature (prevents swallowtail loops in heavy masters).
                u = 1 - t
                a2 = tuple(6 * u * (p[2][i] - 2 * p[1][i] + p[0][i]) + 6 * t * (p[3][i] - 2 * p[2][i] + p[1][i]) for i in (0, 1))
                cross = dv[0] * a2[1] - dv[1] * a2[0]
                if abs(cross) > 1e-9:
                    R = mag ** 3 / abs(cross)
                    inner = (cross > 0 and side > 0) or (cross < 0 and side < 0)
                    olen = hypot(*o)
                    if inner and olen > R * 0.97:
                        o = mul(o, R * 0.97 / olen)
            return add(pos, o)
        rx, ry = rx0, ry0

        sides = []
        for side in (1, -1):
            pieces = []
            for (typ, p), wseg in zip(path.segs, path.widths):
                n = 1 if typ == 'L' else 4
                for i in range(n):
                    a = i / n; b = (i + 1) / n; delta = b - a
                    p0 = off(typ, p, a, side, wseg); p3 = off(typ, p, b, side, wseg)
                    eps = 1e-4

                    def slope(t):
                        return mul(sub(off(typ, p, t + eps, side, wseg), off(typ, p, t - eps, side, wseg)), 1 / (2 * eps))
                    p1 = add(p0, mul(slope(a), delta / 3)); p2 = sub(p3, mul(slope(b), delta / 3))
                    pieces.append([p0, p1, p2, p3, typ])
            # Miter the joins where the centerline has a corner: both offset sides meet at
            # the intersection of their tangent lines (bounded miter), which removes the
            # bevel notch on the outside and the self-intersection on the inside.
            limit = 2.6 * max(rx, ry)
            npieces = len(pieces)
            rng = range(npieces if path.closed else npieces - 1)
            for i in rng:
                A = pieces[i]; B = pieces[(i + 1) % npieces]
                if hypot(*sub(A[3], B[0])) < 0.05:
                    continue
                da = sub(A[3], A[2]) if A[4] == 'C' else sub(A[3], A[0])
                db = sub(B[1], B[0]) if B[4] == 'C' else sub(B[3], B[0])
                den = da[0] * db[1] - da[1] * db[0]
                if abs(den) < 1e-9:
                    continue
                w_ = sub(B[0], A[3])
                t = (w_[0] * db[1] - w_[1] * db[0]) / den
                X = add(A[3], mul(da, t))
                if hypot(*sub(X, A[3])) > limit or hypot(*sub(X, B[0])) > limit:
                    continue
                if A[4] == 'C':
                    A[2] = add(A[2], sub(X, A[3]))
                A[3] = X
                if B[4] == 'C':
                    B[1] = add(B[1], sub(X, B[0]))
                B[0] = X
            if not path.closed:
                for which, ang in ((0, cap0), (1, cap1)):
                    if ang is None:
                        continue
                    from math import radians, sin, degrees
                    seg = path.segs[0] if which == 0 else path.segs[-1]
                    wseg = path.widths[0] if which == 0 else path.widths[-1]
                    typ, p = seg
                    cpt = p[0] if which == 0 else p[-1]
                    if ang == 'blade':
                        # centerline tangent at this terminal
                        tv = deriv(p, 0.0 if which == 0 else 1.0) if typ == 'C' else sub(p[1], p[0])
                        perp = (degrees(atan2(tv[1], tv[0])) + 90) % 180
                        axis = min((0, 90, 180), key=lambda a_: abs(a_ - perp))
                        ang = axis + (BLADE if perp > axis else -BLADE)
                        if abs(perp - axis) < 2:
                            ang = axis - BLADE
                    ncut = (-sin(radians(ang)), cos(radians(ang)))  # normal of the cut line
                    pc = pieces[0] if which == 0 else pieces[-1]
                    n = 1 if typ == 'L' else 4
                    a = 0.0 if which == 0 else (n - 1) / n
                    b = 1.0 / n if which == 0 else 1.0
                    f = lambda t: (off(typ, p, t, side, wseg)[0] - cpt[0]) * ncut[0] + (off(typ, p, t, side, wseg)[1] - cpt[1]) * ncut[1]
                    # the free end parameter moves along [lo, hi] until the side meets the cut line
                    if which == 1:
                        lo, hi = a + (b - a) * 0.15, b + (b - a) * 1.2
                    else:
                        lo, hi = a - (b - a) * 1.2, b - (b - a) * 0.15
                    flo, fhi = f(lo), f(hi)
                    if flo * fhi > 0:
                        continue  # no crossing: keep the perpendicular cut
                    for _ in range(40):
                        mid = (lo + hi) / 2; fm = f(mid)
                        if flo * fm <= 0:
                            hi, fhi = mid, fm
                        else:
                            lo, flo = mid, fm
                    tstar = (lo + hi) / 2
                    eps = 1e-4
                    slope = lambda t: mul(sub(off(typ, p, t + eps, side, wseg), off(typ, p, t - eps, side, wseg)), 1 / (2 * eps))
                    if which == 1:
                        a2, b2 = a, tstar
                    else:
                        a2, b2 = tstar, b
                    delta = b2 - a2
                    q0 = off(typ, p, a2, side, wseg); q3 = off(typ, p, b2, side, wseg)
                    if typ == 'C':
                        pc[0], pc[1], pc[2], pc[3] = q0, add(q0, mul(slope(a2), delta / 3)), sub(q3, mul(slope(b2), delta / 3)), q3
                    else:
                        pc[0], pc[3] = q0, q3
                    # keep the mitered join on the inner end of this piece intact
                    if which == 1 and npieces > 1 and typ == 'C':
                        pc[0] = pieces[-2][3]
                    if which == 0 and npieces > 1 and typ == 'C':
                        pc[3] = pieces[1][0]
            sides.append([tuple(pc) for pc in pieces])
        L, R = sides
        sh = lambda p: (p[0] + self.left, p[1])
        if path.closed:
            for pieces, cw in ((L, None), (R, None)):
                segs = [('L', sh(p3)) if typ == 'L' else ('C', sh(p1), sh(p2), sh(p3)) for p0, p1, p2, p3, typ in pieces]
                self._emit(sh(pieces[0][0]), segs, clockwise=True)
            # the smaller contour is the counter: flip it
            a0 = abs(self._area(self.contours[-2])); a1 = abs(self._area(self.contours[-1]))
            idx = -1 if a1 < a0 else -2
            start, segs = self.contours[idx]
            self.contours.pop(idx)
            self._emit(start, segs, clockwise=False)
        else:
            segs = [('L', sh(p3)) if typ == 'L' else ('C', sh(p1), sh(p2), sh(p3)) for p0, p1, p2, p3, typ in L]
            segs.append(('L', sh(R[-1][3])))
            for p0, p1, p2, p3, typ in reversed(R):
                segs.append(('L', sh(p0)) if typ == 'L' else ('C', sh(p2), sh(p1), sh(p0)))
            segs.append(('L', sh(L[0][0])))
            self._emit(sh(L[0][0]), segs, clockwise=True)

    def _area(self, contour):
        start, segs = contour
        pts = [start] + [s[-1] for s in segs]
        a = 0
        for i in range(len(pts)):
            x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % len(pts)]
            a += x0 * y1 - x1 * y0
        return a / 2

    def line(self, x0, y0, x1, y1, scale=1.0, contrast=1.0):
        self.stroke(Path().M(x0, y0).L(x1, y1), scale, contrast)

    def loop(self, x0, y0, x1, y1, scale=1.0, tension=None):
        """Closed bowl centerline. Apertide tension: NE and SW quadrants squarer than NW/SE."""
        ne, se, sw, nw = tension or TENSION
        cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; rx = (x1 - x0) / 2; ry = (y1 - y0) / 2
        p = (Path().M(cx, y1)
             .C(cx + ne * rx, y1, x1, cy + ne * ry, x1, cy)
             .C(x1, cy - se * ry, cx + se * rx, y0, cx, y0)
             .C(cx - sw * rx, y0, x0, cy - sw * ry, x0, cy)
             .C(x0, cy + nw * ry, cx - nw * rx, y1, cx, y1).Z())
        self.stroke(p, scale); return p

    # -- output -----------------------------------------------------------
    def draw(self, pen):
        """Emit contours, dropping zero-length segments and snapping a closing segment
        that lands on the start point (prevents degenerate slivers after rounding)."""
        def same(a, b):
            return abs(a[0] - b[0]) < 0.05 and abs(a[1] - b[1]) < 0.05
        for start, segs in self.contours:
            clean = []; cur = start
            for s in segs:
                end = s[-1]
                if s[0] == 'L' and same(cur, end):
                    continue
                if s[0] == 'C' and same(cur, end) and same(cur, s[1]) and same(cur, s[2]):
                    continue
                clean.append(s); cur = end
            if clean and same(clean[-1][-1], start):
                last = clean[-1]
                if last[0] == 'L':
                    clean.pop()
                else:
                    clean[-1] = ('C', last[1], last[2], start)
            if len(clean) < 2:
                continue
            pen.moveTo(start)
            for s in clean:
                if s[0] == 'L':
                    pen.lineTo(s[1])
                else:
                    pen.curveTo(s[1], s[2], s[3])
            pen.closePath()
