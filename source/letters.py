"""Apertide's 52 letters and ten figures. Original numerical drawings.

Width axis: skeleton coordinates move, the nib does not scale with width.
Weight axis: the nib grows; `kb` (0 at Regular, 1 at Black) opens counters,
lowers bars, widens hooked glyphs and relaxes curve tension so no inner offset
is tighter than the nib. Free terminals carry the family blade cut.
"""
from math import radians, tan, sin, cos
from geometry import Drawing, Path, BLADE

B = 'blade'
# box widths; a tuple adds the second value times kb (extra room for heavy masters)
WIDTHS = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', [(590, 50), 495, 530, 545, 445, 430, 550, 510, 178, (360, 40), 505, 430, (680, 60), 530, 570, 485, 570, 505, (495, 30), 525, 525, 570, 800, 540, 545, 495]))
WIDTHS.update(dict(zip('abcdefghijklmnopqrstuvwxyz', [(440, 30), 450, (430, 20), 450, (445, 36), (290, 30), 450, 440, 80, (190, 40), 430, (170, 90), 700, 440, 460, 450, 450, (290, 20), (400, 36), (300, 40), 440, 455, 660, 430, 455, 405])))
WIDTHS.update(dict(zip('0123456789', [475, 280, 445, 445, 480, 450, 470, 430, 470, 470])))
BEARINGS = {c: (52, 48) for c in WIDTHS}
for c in 'BDEFHILNPR': BEARINGS[c] = (64, 50)
for c in 'CGOQ': BEARINGS[c] = (42, 42)
for c in 'AVWXY': BEARINGS[c] = (18, 18)
for c in 'Z': BEARINGS[c] = (34, 34)
for c in 'FT': BEARINGS[c] = (26, 26)
for c in 'aceos': BEARINGS[c] = (40, 38)
for c in 'bdghnopqu': BEARINGS[c] = (50, 46)
for c in 'vwxy': BEARINGS[c] = (22, 22)
BEARINGS.update({'z': (30, 30), 'f': (20, 8), 't': (22, 22), 'r': (54, 24), 'i': (60, 60), 'j': (12, 46), 'l': (50, 36), 'J': (30, 48), 'K': (64, 24), 'R': (64, 30), 'E': (64, 42), 'L': (64, 36), 'S': (40, 40), 'U': (56, 56), 'm': (50, 46), 'k': (50, 22)})
for c in '0123456789': BEARINGS[c] = (46, 46)
BEARINGS['1'] = (30, 54)
# dotless bases for composites
WIDTHS['ı'] = 80; WIDTHS['ȷ'] = (190, 40); BEARINGS['ı'] = (60, 60); BEARINGS['ȷ'] = (12, 46)


def box_width(ch, d):
    v = WIDTHS[ch]
    return v if isinstance(v, (int, float)) else v[0] + v[1] * d.kb


def build(ch, d):
    if ch not in WIDTHS:
        raise KeyError(ch)
    g = Drawing(d, box_width(ch, d), *BEARINGS[ch]); w = g.w; s = d.s; h = d.h; l = s / 2; r = w - s / 2; m = w / 2
    X = 520; C = 700; A = 740; D = -210; kb = d.kb
    xt = X + 10 - h / 2; ct = C + 12 - h / 2; xb = -10 + h / 2; cb = -12 + h / 2  # overshoot centerlines
    T = 0.60 - 0.05 * kb   # squarer family tension (NE/SW quadrants)
    R = 0.555              # round tension
    nib = s / 2            # inner radius must stay above this

    def st(path, scale=1.0, c0=None, c1=None, contrast=1.0):
        g.stroke(path, scale, contrast, True, c0, c1)

    def loop(bottom=0, top=X, left=l, right=r, over=10, scale=1.0, tension=None):
        return g.loop(left, bottom - over + h / 2 * scale, right, top + over - h / 2 * scale, scale, tension)

    def vert(x, y0=0, y1=X): g.line(x, y0, x, y1)
    def bar(y, x0=l, x1=r, scale=1.0): g.line(x0, y, x1, y, scale)
    def dia(x0, y0, x1, y1, scale=0.95): g.diag(x0, y0, x1, y1, scale)
    def hw(x0, y0, x1, y1, scale=0.95): return g.diag_hw(x0, y0, x1, y1, scale)

    def hook_ry(rx, want):
        """Vertical radius for a quarter turn with horizontal radius rx so the inner
        offset never cusps: ry**2/rx >= nib and rx**2/ry >= nib. Prefers `want`."""
        lo = (nib * 1.08 * rx) ** 0.5; hi = rx * rx / (nib * 1.08) if rx > 0 else want
        return max(lo, min(hi, want)) if hi >= lo else lo

    def shoulder(left, right, top=X):
        """n/m/h arch: straight stem rise, round-over, straight drop on the right."""
        rx = (right - left); yt = top + 10 - h / 2
        p = Path().M(left, top * (0.64 - 0.06 * kb)).Q(left, yt, left + rx * 0.46, yt, 0.70 - 0.08 * kb, 0.56)
        p.Q(right, yt, right, yt - (yt - top * 0.56), 0.56, 0.62 - 0.05 * kb).L(right, 0)
        st(p)

    def cee(height, lower=0):
        """C/c: two squarer quadrants on the left, open terminals on the right."""
        yt = height + 10 - h / 2; yb = lower - 10 + h / 2; cy = (yt + yb) / 2
        rxt = (r - 4) - (m + 0.04 * w); rxb = (r - 2) - (m - 0.02 * w)
        ryt = hook_ry(rxt, yt - (lower + height * (0.78 - 0.04 * kb)))
        ryb = hook_ry(rxb, lower + height * (0.22 + 0.04 * kb) - yb)
        p = Path().M(r - 4, yt - ryt)
        p.Q(r - 4, yt, m + 0.04 * w, yt, 0.52, 0.56)           # top right quadrant, open
        p.Q(l, yt, l, cy, 0.58, T)                              # top left
        p.Q(l, yb, m - 0.02 * w, yb, T, 0.58)                   # bottom left
        p.Q(r - 2, yb, r - 2, yb + ryb, 0.56, 0.52)
        st(p, 1, B, B)

    def ess(height, over=10):
        top = height + over - h / 2; bot = -over + h / 2
        th = 1 - 0.16 * kb                           # spine thins as weight grows
        rx = (r - 6) - m
        yB = height * (0.70 - 0.02 * kb); yC = height * (0.30 + 0.02 * kb)
        ryA = hook_ry(rx, top - height * 0.79); ryD = hook_ry(rx, height * 0.21 - bot)
        # heavy masters stop the terminal turns early (phi < 90deg): the aperture between the
        # terminal and the spine stays open instead of closing into a slit
        phi = radians(90 - 34 * max(0.0, min(1.0, kb))); kk = 4 / 3 * tan(phi / 4)
        def arc_end(cx, cy, rxa, rya, sx, sy):
            """Elliptical arc leaving the extreme point (cx, cy) horizontally towards sx and turning
            by phi towards sy. Returns the end point, the control next to the extreme and the control
            next to the end (cubic approximation of the arc)."""
            E = (cx + sx * rxa * sin(phi), cy + sy * rya * (1 - cos(phi)))
            tangent = (sx * rxa * cos(phi), sy * rya * sin(phi))   # direction of travel at E
            c_near = (cx + sx * kk * rxa, cy)
            c_far = (E[0] - kk * tangent[0], E[1] - kk * tangent[1])
            return E, c_near, c_far
        Et, c1t, c2t = arc_end(m, top, rx, ryA, +1, -1)              # top terminal: rightwards, then down
        Eb, c1b, c2b = arc_end(m, bot, rx + 2, ryD, -1, +1)          # bottom terminal: leftwards, then up
        p = Path().M(Et[0], Et[1], 1.0)
        p.C(c2t[0], c2t[1], c1t[0], c1t[1], m, top)                 # top right, open terminal
        p.Q(l + 2, top, l + 2, yB, 0.56, 0.52)                       # top left
        p.C(l + 2, yB - height * 0.16, w * 0.32, height * 0.56, m, height * 0.505, th)
        p.C(w * 0.68, height * 0.45, r - 2, yC + height * 0.16, r - 2, yC, 1.0)
        p.Q(r - 2, bot, m, bot, 0.52, 0.56)                          # bottom right
        p.C(c1b[0], c1b[1], c2b[0], c2b[1], Eb[0], Eb[1])            # bottom left, open terminal
        st(p, 1 - 0.10 * kb, B, B)

    def bowl_right(ytop, ybot, xl, xr, kt=None, kbm=None, x0=None, x1=None):
        """Right half bowl from (x0, ytop) over to the right and back to (x1, ybot).
        x0/x1 default to xl; B passes offsets so its two bowls never share a cut edge."""
        kt = kt or (0.62 - 0.05 * kb); kbm = kbm or (0.62 - 0.05 * kb)
        cy = (ytop + ybot) / 2; x0 = xl if x0 is None else x0; x1 = xl if x1 is None else x1
        p = Path().M(x0, ytop).L(xl + (xr - xl) * 0.12, ytop)
        p.Q(xr, ytop, xr, cy, kt, 0.56).Q(xr, ybot, xl + (xr - xl) * 0.12, ybot, 0.56, kbm).L(x1, ybot)
        st(p)

    def thin_for(rx):
        """Nib multiplier at the end of a turn whose horizontal radius is rx: a tight
        hook thins as it turns instead of folding over itself."""
        return 1.0 if rx >= nib * 1.12 else max(0.62, rx / (nib * 1.12))

    def tail_right(x, ytop, ybot_center, xend, rise=None):
        """Vertical stem that turns right into a flat tail (l, t)."""
        rx = min((xend - x) * 0.72, 150 + 60 * kb); ry = hook_ry(rx, rise or (120 + 40 * kb)); tw = thin_for(rx)
        p = Path().M(x, ytop).L(x, ybot_center + ry).Q(x, ybot_center, x + rx, ybot_center, 0.56, 0.56, tw).L(xend, ybot_center, tw)
        st(p, 1, None, B)

    def tail_left(x, ytop, ybot_center, xend, rise=None):
        """Vertical stem that turns left into a flat tail (j)."""
        rx = min((x - xend) * 0.72, 150 + 60 * kb); ry = hook_ry(rx, rise or (120 + 40 * kb)); tw = thin_for(rx)
        p = Path().M(x, ytop).L(x, ybot_center + ry).Q(x, ybot_center, x - rx, ybot_center, 0.56, 0.56, tw).L(xend, ybot_center, tw)
        st(p, 1, None, B)

    if ch == 'A':
        dia(l, 0, m - 13, C); dia(m + 13, C, r, 0); bar(C - h / 2, m - 13, m + 13); bar(238 + 26 * kb, w * 0.235, w * 0.765, 0.96 - 0.12 * kb)
    elif ch == 'B':
        jy = 376 - 24 * kb; vert(l, 0, C)
        bowl_right(C - h / 2, jy, l, r - 12 - 6 * kb, x1=l + 3)
        bowl_right(jy, h / 2, l, r, x0=l - 3)
    elif ch == 'C':
        cee(C)
    elif ch == 'D':
        vert(l, 0, C)
        p = Path().M(l, C - h / 2).L(w * 0.30, C - h / 2).Q(r, C - h / 2, r, C / 2, 0.66 - 0.06 * kb, 0.56).Q(r, h / 2, w * 0.30, h / 2, 0.56, 0.66 - 0.06 * kb).L(l, h / 2)
        st(p)
    elif ch in ('E', 'F'):
        vert(l, 0, C); bar(C - h / 2, l, r); bar(368 - 10 * kb, l, r - w * 0.08)
        if ch == 'E':
            bar(h / 2, l, r)
    elif ch == 'G':
        cee(C); gy = 306 - 16 * kb; bar(gy, m + 4, r + 2); vert(r, 140, gy)
    elif ch == 'H':
        vert(l, 0, C); vert(r, 0, C); bar(338 - 12 * kb)
    elif ch == 'I':
        vert(m, 0, C)
    elif ch == 'J':
        rx = (r - l) / 2; ry = hook_ry(rx, 190 + 30 * kb)
        p = Path().M(r, C).L(r, cb + ry).Q(r, cb, r - rx, cb, 0.56, 0.56).Q(l + 2, cb, l + 2, cb + hook_ry(rx - 2, 150 + 20 * kb), 0.56, 0.50)
        st(p, 1, None, B)
    elif ch == 'K':
        vert(l, 0, C); dia(l, 292, r, C, 0.93); dia(l + 0.22 * (r - l), 282 + 0.22 * (C - 292), r + 6, 0, 0.95)
    elif ch == 'L':
        vert(l, 0, C); bar(h / 2)
    elif ch == 'M':
        sc = 0.92 - 0.22 * kb; vert(l, 0, C); vert(r, 0, C); dia(l, C, m - 10, 226 - 40 * kb, sc); dia(m + 10, 226 - 40 * kb, r, C, sc)
    elif ch == 'N':
        vert(l, 0, C); vert(r, 0, C); dia(l, C, r, 0, 0.93 - 0.12 * kb)
    elif ch in ('O', 'Q'):
        loop(0, C, over=12)
        if ch == 'Q':
            dia(w * 0.60, 160, w + s * 0.1, -100, 0.86)
    elif ch in ('P', 'R'):
        jy = 368 - 26 * kb; vert(l, 0, C)
        bowl_right(C - h / 2, jy, l, r)
        if ch == 'R':
            dia(w * 0.46, jy, r + 4, 0, 0.94)
    elif ch == 'S':
        ess(C, 12)
    elif ch == 'T':
        bar(C - h / 2); vert(m, 0, C - h / 2)
    elif ch == 'U':
        rx = (r - l) / 2; ry = hook_ry(rx, 220 + 20 * kb)
        p = Path().M(l, C).L(l, cb + ry).Q(l, cb, m, cb, 0.56, 0.56).Q(r, cb, r, cb + ry, 0.56, 0.56).L(r, C)
        st(p)
    elif ch == 'V':
        dia(l, C, m - 11, 0); dia(m + 11, 0, r, C); bar(h / 2, m - 11, m + 11)
    elif ch == 'W':
        k_ = 0.93 - 0.18 * kb
        dia(l, C, w * 0.27, 0, k_); dia(w * 0.27, 0, m, 540 - 30 * kb, k_); dia(m, 537 - 30 * kb, w * 0.73, 0, k_); dia(w * 0.73, 0, r, C, k_)
    elif ch == 'X':
        dia(l, C, r, 0, 0.94 - 0.12 * kb); dia(l, 0, r, C, 0.94 - 0.12 * kb)
    elif ch == 'Y':
        dia(l, C, m, 296, 0.94); dia(m, 299, r, C, 0.94); vert(m, 0, 312)
    elif ch == 'Z':
        zs = 0.98 - 0.04 * kb; zh = hw(r, C, l, 0, zs); bar(C - h / 2); dia(r - zh, C - h + 3, l + zh, h - 3, zs); bar(h / 2)
    elif ch == 'a':
        bt = 322 + 46 * kb; loop(0, bt)
        rx = r - m; ry = hook_ry(rx, xt - 342)
        p = Path().M(l + 4, 396 - 30 * kb).Q(l + 4, xt, m - 0.02 * w, xt, 0.50, 0.56).Q(r, xt, r, xt - ry, 0.56, 0.58).L(r, 0)
        st(p, 1, B, None)
    elif ch in ('b', 'd', 'p', 'q'):
        loop()
        if ch in ('b', 'p'):
            vert(l, D if ch == 'p' else 0, X if ch == 'p' else A)
        else:
            vert(r, D if ch == 'q' else 0, X if ch == 'q' else A)
    elif ch == 'c':
        cee(X)
    elif ch == 'e':
        by = 268 - 60 * kb; wb = 1 - 0.14 * kb                      # bar: lower and lighter in the heavy masters
        rx = r - m; ryt = hook_ry(rx, xt - by - 10); ryb = hook_ry(rx - 6, 112 + 20 * kb - xb)
        # the terminal is an elliptical arc from the bottom centre; heavy weights stop the
        # turn early (phi < 90deg) so the aperture stays open under the bar
        phi = radians(90 - 32 * max(0.0, min(1.0, kb))); kk = 4 / 3 * tan(phi / 4); rxb = rx - 6
        P = (m + rxb * sin(phi), xb + ryb * (1 - cos(phi)))
        c2 = (P[0] - kk * rxb * cos(phi), P[1] - kk * ryb * sin(phi)); c1 = (m + kk * rxb, xb)
        p = Path().M(P[0], P[1]).C(c2[0], c2[1], c1[0], c1[1], m, xb).Q(l, xb, l, xb + hook_ry(rx, 240), 0.56, T)
        p.Q(l, xt, m, xt, T, 0.56).Q(r, xt, r, xt - ryt, 0.56, 0.56).L(r, by, wb).L(l + 4, by, wb)
        st(p, 1, -BLADE - 26 * max(0.0, min(1.0, kb)), None)   # explicit cut angle: blade at Regular, steeper as the terminal turns early
    elif ch == 'f':
        x = d.W(90) + 10 * kb; rx = min(w - 4 - x, 150); ry = hook_ry(rx, 150)
        p = Path().M(x, 0).L(x, 782 - h / 2 - ry).Q(x, 782 - h / 2, x + rx, 782 - h / 2, 0.56, 0.52).L(w + 12, 782 - h / 2 - 8)
        st(p, 1, None, B); bar(500, l, w - 6)
    elif ch == 'g':
        loop(); rx = (r - l) * 0.5 + 6; ry = hook_ry(rx, 130 + 30 * kb); yb = D + 20 - 10 * kb + h / 2
        p = Path().M(r, X).L(r, yb + ry).Q(r, yb, r - rx, yb, 0.56, 0.56).L(l - 10, yb)
        st(p, 1, None, B)
    elif ch in ('h', 'n'):
        vert(l, 0, A if ch == 'h' else X); shoulder(l, r)
    elif ch == 'i':
        vert(m); g.dot(m, 672, 1.06)
    elif ch == 'ı':
        vert(m)
    elif ch in ('j', 'ȷ'):
        tail_left(r, X, D + 24 + h / 2, l - 14 - 10 * kb, 120 + 50 * kb)
        if ch == 'j':
            g.dot(r, 672, 1.06)
    elif ch == 'k':
        vert(l, 0, A); dia(l, 208, r, X, 0.93); dia(l + 0.22 * (r - l), 198 + 0.22 * (X - 208), r + 3, 0, 0.94)
    elif ch == 'l':
        tail_right(l, A, h / 2 - 4, r + 6, 130 + 50 * kb)
    elif ch == 'm':
        vert(l); mid = w * 0.5; shoulder(l, mid); shoulder(mid, r)
    elif ch == 'o':
        loop()
    elif ch == 'r':
        vert(l); rx = (r - l) * 0.62; ry = hook_ry(rx, 170 + 30 * kb)
        p = Path().M(l, xt + 30 - ry).Q(l, xt + 30, l + rx, xt + 30, 0.56, 0.52).L(r + 6, xt + 30 - 12)
        st(p, 1, None, B)
    elif ch == 's':
        ess(X)
    elif ch == 't':
        x = d.W(108) + 10 * kb; tail_right(x, 676, xb, r + 6, 130 + 50 * kb); bar(500, l, r)
    elif ch == 'u':
        rx = (r - l) / 2; ry = hook_ry(rx, 190 + 20 * kb)
        p = Path().M(l, X).L(l, xb + ry).Q(l, xb, m, xb, 0.56, 0.56).Q(r, xb, r, xb + ry, 0.56, 0.56).L(r, X - 3)
        st(p); vert(r, 0, X)
    elif ch == 'v':
        dia(l, X, m - 7, 0); dia(m + 7, 0, r, X); bar(h / 2, m - 7, m + 7)
    elif ch == 'w':
        k_ = 0.93 - 0.18 * kb
        dia(l, X, w * 0.27, 0, k_); dia(w * 0.27, 0, m, 420 - 30 * kb, k_); dia(m, 417 - 30 * kb, w * 0.73, 0, k_); dia(w * 0.73, 0, r, X, k_)
    elif ch == 'x':
        dia(l, X, r, 0, 0.94 - 0.12 * kb); dia(l, 0, r, X, 0.94 - 0.12 * kb)
    elif ch == 'y':
        tx, ty = w * 0.16, D; jy = 34
        jx = r + (tx - r) * (X - jy) / (X - ty)
        dia(l, X, jx, jy, 0.90); g.diag(r, X, tx, ty, 0.94, 16)
    elif ch == 'z':
        zs = 0.98 - 0.04 * kb; zh = hw(r, X, l, 0, zs); bar(X - h / 2); dia(r - zh, X - h + 3, l + zh, h - 3, zs); bar(h / 2)
    elif ch == '0':
        loop(0, C, over=12)
    elif ch == '1':
        x = w * 0.70; st(Path().M(l, 540).L(x, C - h / 2), 0.94, B, None); vert(x, 0, C - h / 2)
    elif ch == '2':
        rx = r - m; ry = hook_ry(rx, 150 + 20 * kb)
        p = Path().M(l + 2, ct - hook_ry(rx, 150)).Q(l + 2, ct, m, ct, 0.50, 0.56).Q(r, ct, r, ct - ry, 0.56, 0.62 - 0.05 * kb)
        kx, ky = w * 0.40, 236; dx_, dy_ = kx - l, ky - h / 2
        p.C(r, ct - ry - 110, kx + dx_ * 0.42, ky + dy_ * 0.42, kx, ky).L(l, h / 2).L(r, h / 2)
        st(p, 1, B, None)
    elif ch == '3':
        jy = 374 - 10 * kb; rxt = (r - 4) - m; ryt = hook_ry(rxt, (ct - jy) / 2); rxb = r - m; ryb = hook_ry(rxb, (jy - cb) / 2)
        p = Path().M(l + 2, ct - hook_ry(rxt, 130)).Q(l + 2, ct, m, ct, 0.50, 0.56).Q(r - 4, ct, r - 4, ct - ryt, 0.56, T).Q(r - 4, jy, w * 0.42, jy, T, 0.56)
        st(p, 1, B, None)
        p = Path().M(w * 0.30, jy + 3).Q(r, jy + 3, r, jy - ryb, 0.56, T).Q(r, cb, m, cb, T, 0.56).Q(l + 2, cb, l + 2, cb + hook_ry(rxb, 130), 0.56, 0.50)
        st(p, 1, None, B)
    elif ch == '4':
        x = w * 0.74; by = 236 - 10 * kb; vert(x, 0, C); dia(x - 8, C, l, by, 0.90); bar(by, l, w - s * 0.1)
    elif ch == '5':
        jy = 400 - 10 * kb; rx = r - m; ry = hook_ry(rx, 190)
        bar(C - h / 2, l + 14 - s / 2, r - 6); g.line(l + 14, C, l + 4, jy - 20)
        p = Path().M(l + 5, jy).L(m - 0.08 * w, jy + 30).Q(r, jy + 30, r, jy + 30 - ry, 0.60, 0.58).Q(r, cb, m, cb, 0.58, 0.56).Q(l + 2, cb, l + 2, cb + hook_ry(rx, 130), 0.56, 0.50)
        st(p, 1, None, B)
    elif ch == '6':
        top_ = 440 + 16 * kb; loop(0, top_)
        rx = (r - 2) - m + 0.14 * w; ry = hook_ry(rx, 180)
        p = Path().M(l, 214).L(l, ct - hook_ry(r - l - 40, 300)).Q(l, ct, m + 0.14 * w, ct, 0.56, 0.52).L(r - 6, ct - 8)
        st(p, 1, None, B)
    elif ch == '7':
        sh = hw(r, C, w * 0.27, 0, 0.96); bar(C - h / 2); dia(r - sh, C - h + 3, w * 0.27, 0, 0.96)
    elif ch == '8':
        loop(0, 372 - 8 * kb, left=l, right=r); loop(362 - 8 * kb, C, left=l + 12, right=r - 12, over=12)
    elif ch == '9':
        bot_ = 268 - 16 * kb; loop(bot_, C, over=12)
        p = Path().M(r, 494).L(r, cb + hook_ry(r - l - 40, 300)).Q(r, cb, m - 0.14 * w, cb, 0.56, 0.52).L(l + 6, cb + 8)
        st(p, 1, None, B)
    return g
