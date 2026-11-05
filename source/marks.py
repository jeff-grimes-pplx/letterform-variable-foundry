"""Apertide combining marks (zero advance, anchored) and base-letter anchors.

Lowercase marks are drawn above x-height with their `_top` anchor at (0, X);
`.case` variants are flatter and sit above cap height with `_top` at (0, C).
Below marks carry `_bottom` at (0, 0); the ogonek carries `_ogonek`.
"""
from geometry import Path
from kit import Kit, B, X, C, A, D
import symbols

MARKS = {}  # name -> (unicode or None, recipe(d))


def mark(name, uni=None):
    def deco(fn):
        MARKS[name] = (uni, fn); return fn
    return deco


def zero_kit(d):
    k = Kit(d, 0, 0, 0, raw=True); k.g.left = 0.0; k.g.right = 0.0; k.g.advance = 0.0; return k


GAP = 72          # x-height to mark bottom
CGAP = 46         # cap height to mark bottom


def top_params(case):
    """(y0 = mark bottom, height factor, anchor y)"""
    return (C + CGAP, 0.80, C) if case else (X + GAP, 1.0, X)


_NARROW = [1.0]   # extra horizontal factor while a `.i` mark (for the narrow i/j bases) is being drawn


def mw(d):
    """Horizontal factor for marks: follows the width axis partially (0.93 Condensed, 1.07 Extended)
    and narrows a little as the weight grows so neighbouring marks keep clear of each other."""
    return (0.70 + 0.30 * d.f) * (1 - 0.08 * d.kb) * _NARROW[0]


def ms(d):
    """Stroke factor for marks: accents are lighter than stems as the weight grows."""
    return 1 - 0.30 * d.kb


# ----------------------------------------------------------------- above marks
def acute_shape(k, cx, y0, hf, lean=1):
    hgt = 165 * hf; dx = 86 * hf * mw(k.d)
    p = Path().M(cx + lean * dx * 0.5, y0 + hgt, 0.96).L(cx - lean * dx * 0.5, y0 + 8, 0.80)
    k.st(p, 0.86 * ms(k.d), B, None)

def make_acute(d, case=False, lean=1):
    k = zero_kit(d); y0, hf, ay = top_params(case); acute_shape(k, 0, y0, hf, lean); k.anchor('_top', 0, ay); return k.g

@mark('acutecomb', 0x0301)
def acutecomb(d): return make_acute(d)

@mark('acutecomb.case')
def acutecomb_case(d): return make_acute(d, True)

@mark('gravecomb', 0x0300)
def gravecomb(d): return make_acute(d, lean=-1)

@mark('gravecomb.case')
def gravecomb_case(d): return make_acute(d, True, lean=-1)


def wedge(k, y0, hf, up=True, half=124):
    hgt = 150 * hf; sc = 0.84 * ms(k.d); half = half * mw(k.d)
    if up:   # circumflex
        k.dia(-half, y0 + 6, -5, y0 + hgt, sc); k.dia(5, y0 + hgt, half, y0 + 6, sc); k.bar(y0 + hgt - k.d.h * 0.42, -5, 5, sc)
    else:    # caron
        k.dia(-half, y0 + hgt, -5, y0 + 6, sc); k.dia(5, y0 + 6, half, y0 + hgt, sc); k.bar(y0 + k.d.h * 0.42, -5, 5, sc)

@mark('circumflexcomb', 0x0302)
def circumflexcomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); wedge(k, y0, hf, True); k.anchor('_top', 0, ay); return k.g

@mark('circumflexcomb.case')
def circumflexcomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); wedge(k, y0, hf, True); k.anchor('_top', 0, ay); return k.g

@mark('caroncomb', 0x030C)
def caroncomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); wedge(k, y0, hf, False); k.anchor('_top', 0, ay); return k.g

@mark('caroncomb.case')
def caroncomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); wedge(k, y0, hf, False); k.anchor('_top', 0, ay); return k.g

@mark('caroncomb.alt')
def caroncomb_alt(d):
    """Vertical wedge used after d, l, t, L. `_top` at (0, 0) = letter top; sits to the right."""
    k = zero_kit(d); hgt = 190
    k.st(Path().M(18, 0, 0.92).L(-18, -hgt, 0.66), 0.86 * ms(d), None, B); k.anchor('_top', 0, 0); return k.g


def tilde_shape(k, y0, hf):
    hgt = 150 * hf; half = 160 * mw(k.d)
    p = Path().M(-half, y0 + hgt * 0.22).C(-half * 0.55, y0 + hgt * 1.12, -half * 0.22, y0 + hgt * 1.12, 0, y0 + hgt * 0.62)
    p.C(half * 0.22, y0 + hgt * 0.12, half * 0.55, y0 + hgt * 0.12, half, y0 + hgt * 1.02)
    k.st(p, (0.80 - 0.24 * k.kb) * ms(k.d), B, B)

@mark('tildecomb', 0x0303)
def tildecomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); tilde_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g

@mark('tildecomb.case')
def tildecomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); tilde_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g


@mark('macroncomb', 0x0304)
def macroncomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); hw_ = 148 * mw(d); k.bar(y0 + 62 * hf, -hw_, hw_, 0.92 * ms(d)); k.anchor('_top', 0, ay); return k.g

@mark('macroncomb.case')
def macroncomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); hw_ = 148 * mw(d); k.bar(y0 + 62 * hf, -hw_, hw_, 0.92 * ms(d)); k.anchor('_top', 0, ay); return k.g


def breve_shape(k, y0, hf):
    hgt = 170 * hf; half = 132 * mw(k.d); rx = half; ry = k.hook_ry(rx, hgt - 20)
    yb = y0 + k.d.h * 0.42
    p = Path().M(-half, yb + ry).Q(-half, yb, 0, yb, 0.56, 0.56).Q(half, yb, half, yb + ry, 0.56, 0.56)
    k.st(p, 0.84 * ms(k.d))

@mark('brevecomb', 0x0306)
def brevecomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); breve_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g

@mark('brevecomb.case')
def brevecomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); breve_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g


@mark('dotaccentcomb', 0x0307)
def dotaccentcomb(d):
    k = zero_kit(d); k.dot(0, 672, 1.06 * ms(d)); k.anchor('_top', 0, X); return k.g

@mark('dotaccentcomb.case')
def dotaccentcomb_case(d):
    k = zero_kit(d); k.dot(0, C + CGAP + 56, 1.0 * ms(d)); k.anchor('_top', 0, C); return k.g

@mark('dieresiscomb', 0x0308)
def dieresiscomb(d):
    # two dots a little smaller than the i dot, set close: the mark stays within an i's advance at Regular
    k = zero_kit(d); sc = 0.84 * ms(d); ds = symbols.dotsize(d) * sc; off = ds / 2 + (30 + 0.14 * d.s) * mw(d)
    k.dot(-off, 672, sc); k.dot(off, 672, sc); k.anchor('_top', 0, X); return k.g

@mark('dieresiscomb.case')
def dieresiscomb_case(d):
    k = zero_kit(d); sc = 0.80 * ms(d); ds = symbols.dotsize(d) * sc; off = ds / 2 + (32 + 0.14 * d.s) * mw(d)
    k.dot(-off, C + CGAP + 52, sc); k.dot(off, C + CGAP + 52, sc); k.anchor('_top', 0, C); return k.g


def ring_shape(k, y0, hf):
    rr = 74 * (0.5 + 0.5 * hf) + 10 * k.kb; k.ring(0, y0 + k.d.h * 0.4 + rr, rr, rr, 0.78 * ms(k.d))

@mark('ringcomb', 0x030A)
def ringcomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); ring_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g

@mark('ringcomb.case')
def ringcomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); ring_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g


def hungar_shape(k, y0, hf):
    for cx in (-72 * mw(k.d), 72 * mw(k.d)):
        hgt = 160 * hf; dx = 84 * hf * mw(k.d)
        k.st(Path().M(cx + dx * 0.5, y0 + hgt, 0.90).L(cx - dx * 0.5, y0 + 8, 0.74), 0.80 * ms(k.d), B, None)

@mark('hungarumlautcomb', 0x030B)
def hungarumlautcomb(d):
    k = zero_kit(d); y0, hf, ay = top_params(False); hungar_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g

@mark('hungarumlautcomb.case')
def hungarumlautcomb_case(d):
    k = zero_kit(d); y0, hf, ay = top_params(True); hungar_shape(k, y0, hf); k.anchor('_top', 0, ay); return k.g


@mark('uni0312', 0x0312)
def commaturnedabovecomb(d):
    """Turned comma above (ģ)."""
    k = zero_kit(d); cm = symbols.comma(d); bb = symbols._bounds(cm); sc = 0.84
    cm.transform(sc, sc, 0, 0); bb = symbols._bounds(cm)
    cm.transform(-1, -1, 0, 0)  # rotate 180 degrees about origin
    bb = symbols._bounds(cm)
    k.g.absorb(cm, -(bb[0] + bb[2]) / 2, X + GAP + 10 - bb[1]); k.anchor('_top', 0, X); return k.g


# ----------------------------------------------------------------- narrow marks for i and j
# The i advance is 200 units at Regular while the lowercase wedge, tilde, macron and breve are 330-380 wide, so on
# ı/ȷ they overhung the neighbours' side bearings (dîner, Nîmes, îî). Foundry practice is a narrower set for the
# narrow bases: same recipes, same stroke, same height, horizontal extent reduced by a fixed factor.
NARROW_I = {'circumflexcomb': 0.68, 'tildecomb': 0.62, 'macroncomb': 0.72, 'brevecomb': 0.70, 'dieresiscomb': 0.86}


def _narrowed(fn, factor):
    def recipe(d):
        _NARROW[0] = factor
        try:
            return fn(d)
        finally:
            _NARROW[0] = 1.0
    return recipe


for _n, _f in NARROW_I.items():
    MARKS[_n + '.i'] = (None, _narrowed(MARKS[_n][1], _f))


# ----------------------------------------------------------------- below marks
@mark('cedillacomb', 0x0327)
def cedillacomb(d):
    k = zero_kit(d); kb = d.kb
    p = Path().M(-2, 6, 0.9).L(20, -62, 0.9).C(78, -62, 98, -104, 76, -148, 0.9).C(56, -186, -6, -196, -56, -170, 0.72)
    k.st(p, 0.80 * ms(d), None, B); k.anchor('_bottom', 0, 0); return k.g

@mark('ogonekcomb', 0x0328)
def ogonekcomb(d):
    k = zero_kit(d)
    p = Path().M(14, d.h * 0.45, 0.9).C(-50, -40, -64, -126, -4, -168, 0.86).C(36, -196, 78, -190, 112, -162, 0.72)   # starts inside the base stroke so the union merges
    k.st(p, 0.80 * ms(d), None, B); k.anchor('_ogonek', 0, 0); return k.g

@mark('dotbelowcomb', 0x0323)
def dotbelowcomb(d):
    k = zero_kit(d); k.dot(0, -118, 1.0 * ms(d)); k.anchor('_bottom', 0, 0); return k.g

@mark('uni0326', 0x0326)
def commabelowcomb(d):
    k = zero_kit(d); cm = symbols.comma(d); sc = 0.84; cm.transform(sc, sc, 0, 0); bb = symbols._bounds(cm)
    k.g.absorb(cm, -(bb[0] + bb[2]) / 2, -78 - bb[3]); k.anchor('_bottom', 0, 0); return k.g


# ----------------------------------------------------------------- base anchors
ASCENDER = set('bdfhklt')


def stem_x(ch, g, d):
    """x of the stem that should carry an accent on ascender letters (box coords)."""
    s = d.s
    if ch in 'bhkl': return s / 2
    if ch == 'd': return g.w - s / 2
    if ch == 'f': return d.W(90) + 10 * d.kb
    if ch == 't': return d.W(108) + 10 * d.kb
    return g.w / 2


def add_base_anchors(ch, g, d):
    """Attach top/bottom/ogonek anchors to a finished letter Drawing."""
    bb = symbols._bounds(g); cx = (bb[0] + bb[2]) / 2 - g.left   # box coords
    s = d.s
    if ch.isupper():
        g.anchor('top', cx, C)
    elif ch in ASCENDER:
        g.anchor('top', stem_x(ch, g, d), {'t': 676, 'f': 782}.get(ch, A))   # f: above its hook
    elif ch == 'r':
        g.anchor('top', (s / 2 + cx) / 2 + 6, X)   # over the stem side of the r, clear of the next letter's mark
    else:
        g.anchor('top', cx, X)
    if ch == 'y':
        g.anchor('bottom', g.w * 0.50, D + 20)   # below the tail, clear of the descender stroke
    else:
        g.anchor('bottom', cx, 0)
    og = {'a': g.w - s / 2 - 4, 'e': g.w * 0.70, 'i': g.w / 2, 'ı': g.w / 2, 'u': g.w - s / 2, 'o': g.w * 0.62,
          'A': g.w * 0.86, 'E': g.w - s * 0.5, 'I': g.w / 2, 'U': g.w * 0.68, 'O': g.w * 0.62}
    if ch in og:
        g.anchor('ogonek', og[ch], 0)
    return g
