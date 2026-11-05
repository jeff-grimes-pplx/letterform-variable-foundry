"""Apertide punctuation, symbols, currency, math and arrows. Original drawings.
Every recipe returns a Drawing. Names follow the Adobe Glyph List where one exists."""
from geometry import BLADE, Path
from kit import Kit, B, X, C, A, D
import letters

SYMBOLS = {}   # name -> (unicode or None, recipe)


def sym(name, uni=None):
    def deco(fn):
        SYMBOLS[name] = (uni, fn); return fn
    return deco


def dotsize(d): return d.s * 1.06


# ---------------------------------------------------------------- spaces
@sym('space', 0x20)
def space(d):
    k = Kit(d, 240, 0, 0); return k.g

@sym('uni00A0', 0xA0)
def nbspace(d):
    k = Kit(d, 240, 0, 0); return k.g

@sym('uni2009', 0x2009)
def thinspace(d):
    k = Kit(d, 110, 0, 0); return k.g

@sym('uni2007', 0x2007)
def figurespace(d):
    k = Kit(d, 0, 0, 0, raw=True)
    k.g.set_raw_width(tabular_width(d)); return k.g


def tabular_width(d):
    return max(round(letters.build(c, d).advance) for c in '0123456789')


# ---------------------------------------------------------------- dots and commas
def comma_tail(k, cx, cy, size):
    """Curved tail hanging from a squared dot (comma, quotes). Tapers toward the tip."""
    p = Path().M(cx + size * 0.12, cy + size * 0.08, 0.92).C(cx + size * 0.12, cy - size * 0.45, cx - size * 0.10, cy - size * 0.85, cx - size * 0.46, cy - size * 1.22, 0.56)
    k.st(p, 0.78, None, B)

@sym('period', 0x2E)
def period(d):
    ds = dotsize(d); k = Kit(d, ds, 60, 60, raw=True); k.dot(k.w / 2, ds / 2); return k.g

@sym('comma', 0x2C)
def comma(d):
    ds = dotsize(d); k = Kit(d, ds, 60, 60, raw=True); k.dot(k.w / 2, ds / 2); comma_tail(k, k.w / 2, ds * 0.42, ds); return k.g

@sym('colon', 0x3A)
def colon(d):
    ds = dotsize(d); k = Kit(d, ds, 60, 60, raw=True); k.dot(k.w / 2, ds / 2); k.dot(k.w / 2, X - ds / 2); return k.g

@sym('semicolon', 0x3B)
def semicolon(d):
    ds = dotsize(d); k = Kit(d, ds, 60, 60, raw=True); k.dot(k.w / 2, ds / 2); comma_tail(k, k.w / 2, ds * 0.42, ds); k.dot(k.w / 2, X - ds / 2); return k.g

@sym('ellipsis', 0x2026)
def ellipsis(d):
    ds = dotsize(d); k = Kit(d, ds * 3 + 240, 60, 60, raw=True)
    for i in range(3):
        k.dot(ds / 2 + i * (ds + 120), ds / 2)
    return k.g

@sym('periodcentered', 0xB7)
def periodcentered(d):
    ds = dotsize(d); k = Kit(d, ds, 60, 60, raw=True); k.dot(k.w / 2, 270 + 20 * d.kb); return k.g

@sym('bullet', 0x2022)
def bullet(d):
    r_ = 118 + 24 * d.kb; k = Kit(d, 2 * r_, 70, 70, raw=True); k.ellipse(r_, 290, r_, r_); return k.g

@sym('exclam', 0x21)
def exclam(d):
    ds = dotsize(d); k = Kit(d, ds, 70, 70, raw=True); k.dot(k.w / 2, ds / 2)
    k.st(Path().M(k.w / 2, C, 1.0).L(k.w / 2, ds + 92 + 20 * d.kb, 0.80)); return k.g

@sym('exclamdown', 0xA1)
def exclamdown(d):
    g = exclam(d); g.transform(-1, -1, g.advance, X); return g

@sym('question', 0x3F)
def question(d):
    k = Kit(d, 430, 44, 44); ds = dotsize(d); l, r, m = k.l, k.r, k.m
    rx = r - m; ry = k.hook_ry(rx, 180)
    p = Path().M(l + 2, k.ct - k.hook_ry(rx, 150)).Q(l + 2, k.ct, m, k.ct, 0.52, 0.56).Q(r, k.ct, r, k.ct - ry, 0.56, 0.60 - 0.05 * d.kb)
    p.C(r, k.ct - ry - 100, m + 10, 420, m + 10, 330, 1 - 0.18 * d.kb).L(m + 10, ds + 90 + 20 * d.kb)
    k.st(p, 1, B, None); k.dot(m + 10, ds / 2); return k.g

@sym('questiondown', 0xBF)
def questiondown(d):
    g = question(d); g.transform(-1, -1, g.advance, X); return g


# ---------------------------------------------------------------- quotes
def quote_stroke(k, x, ytop, length):
    k.st(Path().M(x, ytop, 1.0).L(x - 10, ytop - length, 0.78))

@sym('quotesingle', 0x27)
def quotesingle(d):
    k = Kit(d, d.s, 50, 50, raw=True); quote_stroke(k, k.w / 2 + 5, C + 10, 230); return k.g

@sym('quotedbl', 0x22)
def quotedbl(d):
    k = Kit(d, d.s * 2 + 110, 50, 50, raw=True); quote_stroke(k, d.s / 2 + 5, C + 10, 230); quote_stroke(k, k.w - d.s / 2 + 5, C + 10, 230); return k.g

def curly(k, cx, top):
    """Closing-quote shape: squared dot plus tail."""
    ds = dotsize(k.d); k.dot(cx, top - ds / 2); comma_tail(k, cx, top - ds * 0.58, ds)

@sym('quoteright', 0x2019)
def quoteright(d):
    ds = dotsize(d); k = Kit(d, ds, 50, 50, raw=True); curly(k, k.w / 2, C + 10); return k.g

@sym('quoteleft', 0x2018)
def quoteleft(d):
    g = quoteright(d); bb = _bounds(g); g.transform(-1, -1, g.advance, bb[1] + bb[3]); return g

@sym('quotesinglbase', 0x201A)
def quotesinglbase(d):
    return comma(d)

@sym('quotedblright', 0x201D)
def quotedblright(d):
    ds = dotsize(d); k = Kit(d, ds * 2 + 90, 50, 50, raw=True); curly(k, ds / 2, C + 10); curly(k, k.w - ds / 2, C + 10); return k.g

@sym('quotedblleft', 0x201C)
def quotedblleft(d):
    g = quotedblright(d); bb = _bounds(g); g.transform(-1, -1, g.advance, bb[1] + bb[3]); return g

@sym('quotedblbase', 0x201E)
def quotedblbase(d):
    ds = dotsize(d); k = Kit(d, ds * 2 + 90, 60, 60, raw=True)
    for cx in (ds / 2, k.w - ds / 2):
        k.dot(cx, ds / 2); comma_tail(k, cx, ds * 0.42, ds)
    return k.g

def chevron(k, x0, x1, y0, y1, scale=0.80, left=True):
    """Angle bracket between x0..x1 pointing left (or right), vertical extent y0..y1."""
    ym = (y0 + y1) / 2
    if left:
        k.line(x1, y1, x0, ym, scale); k.line(x0, ym, x1, y0, scale)
    else:
        k.line(x0, y1, x1, ym, scale); k.line(x1, ym, x0, y0, scale)

@sym('guilsinglleft', 0x2039)
def guilsinglleft(d):
    k = Kit(d, 200, 44, 44); chevron(k, k.l, k.r, 90, 430, left=True); return k.g

@sym('guilsinglright', 0x203A)
def guilsinglright(d):
    k = Kit(d, 200, 44, 44); chevron(k, k.l, k.r, 90, 430, left=False); return k.g

@sym('guillemotleft', 0xAB)
def guillemotleft(d):
    k = Kit(d, 420, 44, 44); ww = (k.r - k.l) * 0.44
    chevron(k, k.l, k.l + ww, 90, 430, left=True); chevron(k, k.r - ww, k.r, 90, 430, left=True); return k.g

@sym('guillemotright', 0xBB)
def guillemotright(d):
    k = Kit(d, 420, 44, 44); ww = (k.r - k.l) * 0.44
    chevron(k, k.l, k.l + ww, 90, 430, left=False); chevron(k, k.r - ww, k.r, 90, 430, left=False); return k.g

@sym('minute', 0x2032)
def minute(d):
    k = Kit(d, 150, 40, 40); k.st(Path().M(k.r, C + 10, 1.0).L(k.l, 470, 0.72)); return k.g

@sym('second', 0x2033)
def second(d):
    k = Kit(d, 340 + 190 * d.kb, 40, 40); dx = (k.r - k.l) * 0.42
    k.st(Path().M(k.l + dx, C + 10, 1.0).L(k.l, 470, 0.72)); k.st(Path().M(k.r, C + 10, 1.0).L(k.r - dx, 470, 0.72)); return k.g


# ---------------------------------------------------------------- dashes and strokes
def dash(d, width, y, bearings=40, scale=0.96):
    k = Kit(d, width, bearings, bearings); k.bar(y, k.l - d.s * 0.3, k.r + d.s * 0.3, scale); return k.g

@sym('hyphen', 0x2D)
def hyphen(d): return dash(d, 300, 276 + 10 * d.kb)

@sym('uni2010', 0x2010)
def hyphentwo(d): return dash(d, 300, 276 + 10 * d.kb)

@sym('uni2011', 0x2011)
def nbhyphen(d): return dash(d, 300, 276 + 10 * d.kb)

@sym('endash', 0x2013)
def endash(d): return dash(d, 560, 276 + 10 * d.kb, 30)

@sym('emdash', 0x2014)
def emdash(d): return dash(d, 1000, 276 + 10 * d.kb, 20)

@sym('minus', 0x2212)
def minus(d):
    k = mathbox(d); k.bar(300, k.l, k.r, 0.92); return k.g

@sym('underscore', 0x5F)
def underscore(d):
    k = Kit(d, 560, 0, 0); k.bar(-110, k.l - d.s * 0.3, k.r + d.s * 0.3, 0.92); return k.g

@sym('slash', 0x2F)
def slash(d):
    k = Kit(d, 330, 10, 10); k.dia(k.w * 0.08, -40, k.w * 0.92, 760, 0.90); return k.g

@sym('backslash', 0x5C)
def backslash(d):
    k = Kit(d, 330, 10, 10); k.dia(k.w * 0.08, 760, k.w * 0.92, -40, 0.90); return k.g

@sym('fraction', 0x2044)
def fraction(d):
    k = Kit(d, 300, -30, -30); k.dia(k.w * 0.02, -20, k.w * 0.98, 720, 0.84); return k.g

@sym('bar', 0x7C)
def bar_(d):
    k = Kit(d, d.s, 70, 70, raw=True); k.vert(k.w / 2, -176, 776, 0.94); return k.g

@sym('brokenbar', 0xA6)
def brokenbar(d):
    k = Kit(d, d.s, 70, 70, raw=True); k.vert(k.w / 2, -176, 220, 0.94); k.vert(k.w / 2, 380, 776, 0.94); return k.g


# ---------------------------------------------------------------- brackets
@sym('parenleft', 0x28)
def parenleft(d):
    k = Kit(d, 250, 46, 30, extra_kb=40); l, r = k.l, k.r
    k.st(Path().M(r, 776).C(l - 24, 560, l - 24, 40, r, -176), 0.92); return k.g

@sym('parenright', 0x29)
def parenright(d):
    g = parenleft(d); g.transform(-1, 1, g.advance, 0); return g

@sym('bracketleft', 0x5B)
def bracketleft(d):
    k = Kit(d, 230, 70, 30); l, r = k.l, k.r
    k.vert(l, -176, 776, 0.94); k.bar(776 - d.h * 0.45, l, r, 0.90); k.bar(-176 + d.h * 0.45, l, r, 0.90); return k.g

@sym('bracketright', 0x5D)
def bracketright(d):
    g = bracketleft(d); g.transform(-1, 1, g.advance, 0); return g

@sym('braceleft', 0x7B)
def braceleft(d):
    k = Kit(d, 330, 40, 30, extra_kb=50); l, r, m = k.l, k.r, k.m; yc = 300; sc = 0.88
    rx = max(m - l, k.nib * sc * 1.15); x0 = r - rx * 0.0; xm = l + rx  # spine x
    ry1 = k.hook_ry(max(r - xm, 1), 120); ry2 = k.hook_ry(max(xm - l, 1), 110)
    p = Path().M(r, 776).Q(xm, 776, xm, 776 - ry1, 0.56, 0.56).L(xm, yc + ry2).Q(xm, yc, l, yc, 0.56, 0.56)
    p.Q(xm, yc, xm, yc - ry2, 0.56, 0.56).L(xm, -176 + ry1).Q(xm, -176, r, -176, 0.56, 0.56)
    k.st(p, sc); return k.g

@sym('braceright', 0x7D)
def braceright(d):
    g = braceleft(d); g.transform(-1, 1, g.advance, 0); return g


# ---------------------------------------------------------------- marks of speech and symbols
@sym('asterisk', 0x2A)
def asterisk(d):
    k = Kit(d, 400, 30, 30); cx, cy, rr = k.m, 560, 160
    from math import cos, sin, radians
    for ang in (90, 30, -30):
        a = radians(ang); k.line(cx - rr * cos(a), cy - rr * sin(a), cx + rr * cos(a), cy + rr * sin(a), 0.84)
    return k.g

@sym('numbersign', 0x23)
def numbersign(d):
    k = Kit(d, 560, 30, 30); w = k.w
    k.dia(w * 0.28, 0, w * 0.40, C, 0.80); k.dia(w * 0.58, 0, w * 0.70, C, 0.80)
    k.bar(220, k.l - 10, k.r + 10, 0.88); k.bar(470, k.l - 10, k.r + 10, 0.88); return k.g

@sym('ampersand', 0x26)
def ampersand(d):
    """Round lower bowl, a smaller upper loop, a straight tail to the lower right and a short
    terminal at mid right. Heavy masters widen the box and lighten the stroke so both counters stay open."""
    k = Kit(d, 620, 40, 30, extra_kb=70); l, r, m, w = k.l, k.r, k.m, k.w; cb, ct = k.cb, k.ct; kb = d.kb
    p = Path().M(r - 4, 230 + 10 * kb).Q(r - 4, cb, w * 0.50, cb, 0.54, 0.56).Q(l, cb, l, 250 + 10 * kb, 0.56, 0.62)
    p.C(l, 380 + 10 * kb, w * 0.42, 430, w * 0.58, 530).C(w * 0.76, 640, w * 0.74, ct, w * 0.44, ct)
    p.C(w * 0.14, ct, w * 0.10, 560, w * 0.26, 450 - 10 * kb).L(r + 14, 10)
    k.st(p, 1.0 - 0.16 * kb, B, None); return k.g

@sym('at', 0x40)
def at(d):
    k = Kit(d, 820, 40, 40); w, l, r, m = k.w, k.l, k.r, k.m; kb = d.kb
    il, ir, ib, it = w * 0.30, w * 0.64, 150, 470
    k.loop(il, ib, ir, it, scale=0.86 - 0.26 * kb)
    p = Path().M(ir, it).L(ir, ib + 40).C(ir, 150 - 30, w * 0.80, 140, w * 0.86, 230)
    p.C(w * 0.96, 400, w * 0.90, 620, w * 0.66, 700).C(w * 0.40, 790, l - 10, 700, l - 10, 400)
    p.C(l - 10, 120, w * 0.22, -40, w * 0.56, -40).C(w * 0.68, -40, w * 0.78, -14, w * 0.86, 30)
    k.st(p, 0.86 - 0.20 * kb, None, B); return k.g

@sym('percent', 0x25)
def percent(d):
    k = Kit(d, 740, 30, 30); w = k.w
    k.loop(k.l, 390, w * 0.42, C, scale=0.86); k.loop(w * 0.58, 0, k.r, 310, scale=0.86)
    k.dia(w * 0.24, -10, w * 0.76, 710, 0.76); return k.g

@sym('perthousand', 0x2030)
def perthousand(d):
    """The percent layout plus a third ring at an explicit gap; the box is widened to fit."""
    k = Kit(d, 740, 30, 30); w = k.w; sw = d.s * 0.86; gap = 40 + 24 * d.kb
    k.loop(k.l, 390, w * 0.42, C, scale=0.86); k.loop(w * 0.58, 0, k.r, 310, scale=0.86)
    rw2 = k.r - w * 0.58; x3l = k.r + sw + gap; x3r = x3l + rw2
    k.loop(x3l, 0, x3r, 310, scale=0.86)
    k.dia(w * 0.24, -10, w * 0.76, 710, 0.76)
    k.g.set_raw_width(x3r + d.s / 2); return k.g

@sym('degree', 0xB0)
def degree(d):
    k = Kit(d, 300, 40, 40); rr = (k.r - k.l) / 2; k.ring(k.m, C - rr - d.h * 0.4, rr, rr, 0.84); return k.g

@sym('section', 0xA7)
def section(d):
    """Section sign: a central ring whose left and right sides continue straight into S-style
    hooks (point-symmetric). Each hook turns over the top and comes back down to a terminal at
    about the middle of its lobe, clear of the ring. Heavy masters shrink the ring and lighten the stroke."""
    k = Kit(d, 450, 40, 40); l, r, m, w, h = k.l, k.r, k.m, k.w, d.h; kb = d.kb
    sc = 0.88 - 0.20 * kb; hs = h * sc
    cy = 346; rx = (m - (l + 2)) * 0.82; ry = 80 - 6 * kb
    k.ring(m, cy, rx, ry, sc)
    top = 714 - hs / 2
    xl = m - rx                                                # ring's left side = hook's left side
    ryl = k.hook_ry(rx, 140)
    rxh = (r - 6) - m
    lobe = top - (cy + ry)
    end_y = cy + ry + hs / 2 + 0.42 * lobe                     # terminal ends mid-lobe, clear of the ring
    ryh = min(k.hook_ry(rxh, 150), max(60, top - end_y - 8))
    def hook(sign):
        R = lambda x, y: (m + sign * (x - m), cy + sign * (y - cy))
        p = Path().M(*R(xl, cy)).L(*R(xl, top - ryl)).Q(*R(xl, top), *R(m, top), 0.52, 0.56)
        p.Q(*R(r - 6, top), *R(r - 6, top - ryh), 0.56, 0.52).L(*R(r - 6, end_y))
        k.st(p, sc, None, B)
    hook(+1); hook(-1); return k.g

@sym('paragraph', 0xB6)
def paragraph(d):
    """Pilcrow: two stems, a top bar and a stroked left bowl that closes back onto the first stem."""
    k = Kit(d, 600, 40, 40, extra_kb=40); l, r, w = k.l, k.r, k.w; kb = d.kb; sc = 0.92 - 0.06 * kb
    x1, x2 = w * 0.56, w * 0.82; top = C - d.h / 2 * sc; bot = 300 + d.h / 2 * sc
    k.vert(x1, -120, C, sc); k.vert(x2, -120, C, sc); k.bar(top, x1 - 10, r, sc)
    cy = (top + bot) / 2; rx = x1 - l; ry = (top - bot) / 2
    p = Path().M(x1 + 4, top).Q(x1 - rx, top, x1 - rx, cy, 0.60, 0.56).Q(x1 - rx, bot, x1 + 4, bot, 0.56, 0.60)
    k.st(p, sc); return k.g

@sym('dagger', 0x2020)
def dagger(d):
    k = Kit(d, 420, 30, 30); k.st(Path().M(k.m, C + 6, 1.0).L(k.m, -120, 0.78)); k.bar(500, k.l, k.r, 0.92); return k.g

@sym('daggerdbl', 0x2021)
def daggerdbl(d):
    k = Kit(d, 420, 30, 30); k.st(Path().M(k.m, C + 6, 1.0).L(k.m, -120, 0.90)); k.bar(500, k.l, k.r, 0.92); k.bar(60, k.l, k.r, 0.92); return k.g

@sym('copyright', 0xA9)
def copyright(d):
    k = Kit(d, 760, 36, 36); rr = (k.r - k.l) / 2; cy = 350; k.ring(k.m, cy, rr, rr, 0.80)
    inner = letters.build('C', d.derive(1.55 - 0.40 * d.kb)); sc = 0.46
    inner.transform(sc, sc, 0, 0)
    bb = _bounds(inner); dx = k.m + k.g.left - (bb[0] + bb[2]) / 2; dy = cy - (bb[1] + bb[3]) / 2
    k.g.absorb(inner, dx, dy); return k.g

@sym('registered', 0xAE)
def registered(d):
    k = Kit(d, 760, 36, 36); rr = (k.r - k.l) / 2; cy = 350; k.ring(k.m, cy, rr, rr, 0.80)
    inner = letters.build('R', d.derive(1.55 - 0.40 * d.kb)); sc = 0.46
    inner.transform(sc, sc, 0, 0)
    bb = _bounds(inner); dx = k.m + k.g.left - (bb[0] + bb[2]) / 2; dy = cy - (bb[1] + bb[3]) / 2
    k.g.absorb(inner, dx, dy); return k.g

@sym('trademark', 0x2122)
def trademark(d):
    k = Kit(d, 780, 30, 30); sc = 0.50
    t = letters.build('T', d.derive(1.9)); t.transform(sc, sc, 0, 0)
    m_ = letters.build('M', d.derive(1.9)); m_.transform(sc, sc, 0, 0)
    bt = _bounds(t); bm = _bounds(m_); top = C
    k.g.absorb(t, k.g.left - bt[0], top - bt[3]); k.g.absorb(m_, k.g.left + k.w - (bm[2] - bm[0]) - bm[0], top - bm[3]); return k.g

@sym('ordfeminine', 0xAA)
def ordfeminine(d):
    k = Kit(d, 330, 30, 30); sc = 0.60; a = letters.build('a', d.derive(1.42 - 0.34 * d.kb)); a.transform(sc, sc, 0, 0)
    bb = _bounds(a); k.g.absorb(a, k.g.left + k.w / 2 - (bb[0] + bb[2]) / 2, C - bb[3]); return k.g

@sym('ordmasculine', 0xBA)
def ordmasculine(d):
    k = Kit(d, 330, 30, 30); sc = 0.60; o = letters.build('o', d.derive(1.42 - 0.34 * d.kb)); o.transform(sc, sc, 0, 0)
    bb = _bounds(o); k.g.absorb(o, k.g.left + k.w / 2 - (bb[0] + bb[2]) / 2, C - bb[3]); return k.g


def _bounds(g):
    xs = []; ys = []
    for start, segs in g.contours:
        for p in [start] + [pt for sg in segs for pt in sg[1:]]:
            xs.append(p[0]); ys.append(p[1])
    return min(xs), min(ys), max(xs), max(ys)


# ---------------------------------------------------------------- currency
def stubs(k, x, scale=0.70):
    k.vert(x, C - 30, C + 80, scale); k.vert(x, -84, 24, scale)   # stubs overlap the S strokes

@sym('dollar', 0x24)
def dollar(d):
    g = letters.build('S', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; stubs(k, g.w / 2, 0.72); return g

@sym('cent', 0xA2)
def cent(d):
    g = letters.build('c', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    k.vert(g.w / 2, X - 30, X + 90, 0.70); k.vert(g.w / 2, -96, 24, 0.70); return g

@sym('sterling', 0xA3)
def sterling(d):
    k = Kit(d, 520, 40, 40); l, r, w, m = k.l, k.r, k.w, k.m; ct = k.ct
    xs = w * 0.30; rx = xs - l + 20
    p = Path().M(w * 0.82, ct - k.hook_ry(w * 0.80 - w * 0.50, 150)).Q(w * 0.82, ct, w * 0.50, ct, 0.52, 0.56).Q(xs, ct, xs, ct - k.hook_ry(w * 0.50 - xs, 180), 0.56, 0.58)
    rxb = min(xs - l + 10, 120); ryb = k.hook_ry(rxb, 130)
    p.L(xs, d.h / 2 + ryb).Q(xs, d.h / 2, xs - rxb, d.h / 2, 0.56, 0.56).L(l - 4, d.h / 2)
    k.st(p, 1, B, None); k.bar(d.h / 2, l, r); k.bar(330, l - 10, w * 0.62, 0.92); return k.g

@sym('yen', 0xA5)
def yen(d):
    k = Kit(d, 560, 20, 20); l, r, m = k.l, k.r, k.m
    k.dia(l, C, m, 330, 0.92); k.dia(m, 333, r, C, 0.92); k.vert(m, 0, 350)
    k.bar(300, k.w * 0.16, k.w * 0.84, 0.90); k.bar(160, k.w * 0.16, k.w * 0.84, 0.90); return k.g

@sym('Euro', 0x20AC)
def euro(d):
    g = letters.build('C', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    k.bar(400, -30, g.w * 0.66, 0.90); k.bar(270, -30, g.w * 0.62, 0.90); return g

@sym('currency', 0xA4)
def currency(d):
    kb = d.kb; k = Kit(d, 500 + 70 * kb, 30, 30); m = k.m; cy = 330; rr = (k.r - k.l) * 0.30 + 26 * kb
    sc = 0.80 - 0.16 * kb   # keep the counter open in the heavy masters
    k.ring(m, cy, rr, rr, sc)
    for sx_, sy_ in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        k.line(m + sx_ * rr * 0.6, cy + sy_ * rr * 0.6, m + sx_ * rr * 1.35, cy + sy_ * rr * 1.35, sc - 0.04)
    return k.g

@sym('uni20B9', 0x20B9)
def rupee(d):
    """Indian rupee: an R bowl hanging from the top bar, a second bar crossing the bowl below
    the top one, and the leg running from the bowl's bottom to the lower left (one connected form)."""
    k = Kit(d, 540, 40, 40); l, r, w = k.l, k.r, k.w; kb = d.kb; top = C - d.h / 2; y2 = 524 - 8 * kb; yb = 290 + 14 * kb
    k.bar(top, l, r, 0.96); k.bar(y2, l, r, 0.96)
    ry = (top - yb) / 2; sc = 0.94 - 0.18 * kb
    p = Path().M(w * 0.44, top).Q(r, top, r, top - ry, 0.60, 0.56).Q(r, yb, w * 0.44, yb, 0.56, 0.60)
    k.st(p, sc); k.dia(w * 0.50, yb + 2, w * 0.06, 0, 0.92); return k.g

@sym('uni20BD', 0x20BD)
def ruble(d):
    g = letters.build('P', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    k.bar(190, -60, g.w * 0.62, 0.92); return g

@sym('uni20A9', 0x20A9)
def won(d):
    g = letters.build('W', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    k.bar(420, 10, g.w - 10, 0.82); k.bar(280, 40, g.w - 40, 0.82); return g

@sym('uni20BA', 0x20BA)
def lira(d):
    k = Kit(d, 480, 30, 40); l, r, w = k.l, k.r, k.w; x = w * 0.36; cb = k.cb
    rx = (r - x) * 0.6; ry = k.hook_ry(rx, 200)
    p = Path().M(x, C).L(x, cb + ry).Q(x, cb, x + rx, cb, 0.56, 0.56).Q(r, cb, r, cb + k.hook_ry(r - x - rx, 220), 0.56, 0.52)
    k.st(p, 1, None, B); k.dia(w * 0.12, 300, w * 0.62, 470, 0.80); k.dia(w * 0.12, 450, w * 0.62, 620, 0.80); return k.g


# ---------------------------------------------------------------- math
def mathbox(d, width=560, bearings=46):
    return Kit(d, width, bearings, bearings)

@sym('plus', 0x2B)
def plus(d):
    k = mathbox(d); cy = 300; k.bar(cy, k.l, k.r, 0.92); k.vert(k.m, cy - (k.r - k.l) / 2, cy + (k.r - k.l) / 2, 0.92); return k.g

@sym('plusminus', 0xB1)
def plusminus(d):
    k = mathbox(d); cy = 340; hl = (k.r - k.l) / 2 * 0.86
    k.bar(cy, k.l, k.r, 0.92); k.vert(k.m, cy - hl, cy + hl, 0.92); k.bar(40, k.l, k.r, 0.92); return k.g

@sym('multiply', 0xD7)
def multiply(d):
    k = mathbox(d); cy = 300; hl = (k.r - k.l) / 2 * 0.80
    k.line(k.m - hl, cy - hl, k.m + hl, cy + hl, 0.86); k.line(k.m - hl, cy + hl, k.m + hl, cy - hl, 0.86); return k.g

@sym('divide', 0xF7)
def divide(d):
    k = mathbox(d); cy = 300; ds = dotsize(d) * 0.92; k.bar(cy, k.l, k.r, 0.92)
    k.dot(k.m, cy + 150, 0.92); k.dot(k.m, cy - 150, 0.92); return k.g

@sym('equal', 0x3D)
def equal(d):
    k = mathbox(d); k.bar(380, k.l, k.r, 0.92); k.bar(220, k.l, k.r, 0.92); return k.g

@sym('notequal', 0x2260)
def notequal(d):
    k = mathbox(d); k.bar(380, k.l, k.r, 0.92); k.bar(220, k.l, k.r, 0.92); k.dia(k.m - 70, 80, k.m + 70, 520, 0.80); return k.g

@sym('less', 0x3C)
def less(d):
    k = mathbox(d); cy = 300; k.line(k.r, cy + 230, k.l, cy, 0.90); k.line(k.l, cy, k.r, cy - 230, 0.90); return k.g

@sym('greater', 0x3E)
def greater(d):
    g = less(d); g.transform(-1, 1, g.advance, 0); return g

@sym('lessequal', 0x2264)
def lessequal(d):
    k = mathbox(d); cy = 360; k.line(k.r, cy + 200, k.l, cy, 0.88); k.line(k.l, cy, k.r, cy - 200, 0.88); k.bar(40, k.l, k.r, 0.88); return k.g

@sym('greaterequal', 0x2265)
def greaterequal(d):
    g = lessequal(d); g.transform(-1, 1, g.advance, 0); return g

@sym('logicalnot', 0xAC)
def logicalnot(d):
    k = mathbox(d); k.bar(330, k.l, k.r, 0.92); k.vert(k.r, 150, 330, 0.92); return k.g

@sym('asciitilde', 0x7E)
def asciitilde(d):
    k = mathbox(d); cy = 300; l, r, w = k.l, k.r, k.w
    k.st(Path().M(l, cy - 50).C(l + (r - l) * 0.20, cy + 70, l + (r - l) * 0.40, cy + 70, k.m, cy).C(l + (r - l) * 0.60, cy - 70, l + (r - l) * 0.80, cy - 70, r, cy + 50), 0.88 - 0.16 * d.kb); return k.g

@sym('approxequal', 0x2248)
def approxequal(d):
    k = mathbox(d); l, r = k.l, k.r
    for cy in (390, 210):
        k.st(Path().M(l, cy - 40).C(l + (r - l) * 0.20, cy + 60, l + (r - l) * 0.40, cy + 60, k.m, cy).C(l + (r - l) * 0.60, cy - 60, l + (r - l) * 0.80, cy - 60, r, cy + 40), 0.84)
    return k.g

@sym('asciicircum', 0x5E)
def asciicircum(d):
    k = Kit(d, 440, 30, 30); k.dia(k.l, 440, k.m - 6, C, 0.82); k.dia(k.m + 6, C, k.r, 440, 0.82); k.bar(C - d.h * 0.41, k.m - 6, k.m + 6, 0.82); return k.g

@sym('infinity', 0x221E)
def infinity(d):
    """Figure eight: each lobe is one open stroke from the crossing back to the crossing,
    overshooting a little along the tangent so the two strokes cover each other at the centre."""
    from math import sqrt
    k = Kit(d, 760, 40, 40); cx, cy = k.m, 300; a = (k.r - k.l) / 2; b = 150 + 12 * d.kb; sc = 0.86 - 0.1 * d.kb
    e = d.s * sc * 0.6; u = 1 / sqrt(2); kx = 0.30 * a; ky = 0.55 * b
    # right lobe, clockwise, in unmirrored coordinates: (c1, c2, end) triples
    segs = [((cx + 0.26 * a, cy + 0.26 * a), (cx + 0.52 * a - kx, cy + b), (cx + 0.52 * a, cy + b)),
            ((cx + 0.52 * a + kx, cy + b), (cx + a, cy + ky), (cx + a, cy)),
            ((cx + a, cy - ky), (cx + 0.52 * a + kx, cy - b), (cx + 0.52 * a, cy - b)),
            ((cx + 0.52 * a - kx, cy - b), (cx + 0.26 * a, cy - 0.26 * a), (cx - e * u, cy + e * u))]
    start = (cx - e * u, cy - e * u)
    for sign in (+1, -1):
        X = lambda pt: (cx + sign * (pt[0] - cx), pt[1])
        p = Path().M(*X(start))
        for c1, c2, end in segs:
            p.C(*X(c1), *X(c2), *X(end))
        k.st(p, sc)
    return k.g

@sym('uni2206', 0x2206)
def increment(d):
    k = Kit(d, 600, 20, 20); k.dia(k.l, 0, k.m - 12, C, 0.94); k.dia(k.m + 12, C, k.r, 0, 0.94); k.bar(C - d.h / 2, k.m - 12, k.m + 12, 0.94); k.bar(d.h / 2, k.l, k.r); return k.g

@sym('uni2211', 0x2211)
def summation(d):
    k = Kit(d, 560, 40, 40); l, r, m, h = k.l, k.r, k.m, d.h
    xa, ya = m + 30, 350
    k.bar(C - h / 2, l, r); k.bar(h / 2, l, r)
    hw1 = k.g.diag_hw(l, C - h, xa, ya, 0.92); s1 = (xa - l - hw1) / (C - h - ya)
    k.dia(l + hw1 - 2 * s1, C - h + 2, xa, ya, 0.92)             # left edge passes through the top bar's corner
    hw2 = k.g.diag_hw(xa, ya, l, h, 0.92); s2 = (xa - l - hw2) / (ya - h)
    k.dia(xa, ya + 3, l + hw2 - 2 * s2, h - 2, 0.92)             # ... and the bottom bar's corner; starts 3 units inside the upper diagonal
    return k.g

@sym('radical', 0x221A)
def radical(d):
    k = Kit(d, 620, 20, 20); w = k.w
    k.dia(k.l, 300, w * 0.32, 0, 0.84); k.dia(w * 0.32, 0, w * 0.70, 760, 0.94); k.bar(760 - d.h / 2, w * 0.70, k.r, 0.94); return k.g

@sym('lozenge', 0x25CA)
def lozenge(d):
    k = Kit(d, 520, 30, 30); m = k.m; cy = 350; ry = 370
    k.dia(k.l, cy, m, cy + ry, 0.86); k.dia(m, cy + ry - 3, k.r - 2, cy, 0.86); k.dia(k.r, cy, m, cy - ry, 0.86); k.dia(m, cy - ry + 3, k.l + 2, cy, 0.86); return k.g

@sym('uni220F', 0x220F)
def product(d):
    k = Kit(d, 600, 40, 40); k.vert(k.l + 20, 0, C); k.vert(k.r - 20, 0, C); k.bar(C - d.h / 2, k.l - 20, k.r + 20); return k.g

@sym('pi', 0x3C0)
def pi(d):
    k = Kit(d, 560, 30, 30); w = k.w; kb = d.kb
    k.bar(X - d.h / 2, k.l - 24, k.r + 24, 0.94)
    k.vert(w * 0.30, 0, X - d.h / 2 - 10 + 20, 0.94)
    # right leg: straight down then a short turn to the right (tail)
    xr = w * 0.70; rx = min(k.r + 10 - xr, 120); ry = k.hook_ry(rx, 110 + 10 * kb)
    p = Path().M(xr, X - d.h / 2 + 10).L(xr, d.h / 2 + ry).Q(xr, d.h / 2, xr + rx, d.h / 2, 0.56, 0.56)
    k.st(p, 0.94, None, B); return k.g

@sym('uni03A9', 0x3A9)
def Omega(d):
    k = Kit(d, 660, 30, 30); l, r, m, w, h = k.l, k.r, k.m, k.w, d.h; kb = d.kb
    hb = h / 2 + 70 + 20 * kb; cy = 420 - 10 * kb
    k.bar(h / 2, l, w * 0.34); k.bar(h / 2, w * 0.66, r)
    k.vert(w * 0.32, h / 2, hb + 6); k.vert(w * 0.68, h / 2, hb + 6)
    rxs = (w * 0.32) - (l + 6)
    p = Path().M(w * 0.32, hb).Q(l + 6, hb, l + 6, cy, 0.60, k.hook_ry(rxs, 120) / max(1, cy - hb) * 0.9)
    p.Q(l + 6, k.ct, m, k.ct, 0.56, 0.56).Q(r - 6, k.ct, r - 6, cy, 0.56, 0.56)
    p.Q(r - 6, hb, w * 0.68, hb, k.hook_ry(rxs, 120) / max(1, cy - hb) * 0.9, 0.60)
    k.st(p); return k.g

@sym('partialdiff', 0x2202)
def partialdiff(d):
    k = Kit(d, 520, 30, 30); l, r, m, w, h = k.l, k.r, k.m, k.w, d.h; kb = d.kb
    k.loop(l, 0, r, X)
    top = A - 14 - h / 2; rx = (r - 4) - m + 0.08 * w; ry = k.hook_ry(rx, 150 + 10 * kb)
    p = Path().M(r - 4, X * 0.55).L(r - 4, top - ry).Q(r - 4, top, m - 0.08 * w, top, 0.56, 0.56).Q(m - 0.08 * w - rx * 0.5, top, m - 0.08 * w - rx * 0.5, top - 40 - 10 * kb, 0.56, 0.56)
    k.st(p, 0.98, None, B); return k.g

@sym('integral', 0x222B)
def integral(d):
    k = Kit(d, 360 + 60 * d.kb, 40, 40); l, r, m, h = k.l, k.r, k.m, d.h; kb = d.kb
    top = A + 20 - h / 2; bot = D + 10 + h / 2; sc = 0.94 - 0.06 * kb
    rxt = (r - 2) - (m + 10); ryt = k.hook_ry(rxt, 150); rxb = (m - 10) - (l + 2); ryb = k.hook_ry(rxb, 150)
    p = Path().M(r - 2, top - ryt).Q(r - 2, top, m + 14, top, 0.56, 0.56)
    p.C(m + 14, top - 240, m - 14, bot + 240, m - 14, bot + ryb)          # gentle spine, vertical tangents at both ends
    p.Q(m - 14, bot, l + 2, bot, 0.56, 0.56)
    k.st(p, sc, None, None); return k.g   # butt caps: a blade cut folds into the thick hook at wide widths

@sym('mu', 0xB5)
def mu(d):
    g = letters.build('u', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; k.vert(d.s / 2, D, 190); return g


# ---------------------------------------------------------------- arrows
def arrow(d, direction):
    k = Kit(d, 640, 40, 40); l, r, m = k.l, k.r, k.m; cy = 300; head = 220
    if direction in ('right', 'left'):
        k.bar(cy, l, r, 0.90)
        tip = r if direction == 'right' else l; sgn = -1 if direction == 'right' else 1
        k.line(tip, cy, tip + sgn * head, cy + head * 0.78, 0.90); k.line(tip, cy, tip + sgn * head, cy - head * 0.78, 0.90)
    else:
        top, bot = 760, -160; k.vert(m, bot, top, 0.90)
        tip = top if direction == 'up' else bot; sgn = -1 if direction == 'up' else 1
        k.line(m, tip, m - head * 0.78, tip + sgn * head, 0.90); k.line(m, tip, m + head * 0.78, tip + sgn * head, 0.90)
    return k.g

@sym('arrowright', 0x2192)
def arrowright(d): return arrow(d, 'right')

@sym('arrowleft', 0x2190)
def arrowleft(d): return arrow(d, 'left')

@sym('arrowup', 0x2191)
def arrowup(d): return arrow(d, 'up')

@sym('arrowdown', 0x2193)
def arrowdown(d): return arrow(d, 'down')
