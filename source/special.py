"""Apertide special letters, ligatures, figure variants, case punctuation.
Everything here is drawn from the same engine; nothing is derived from another font."""
from geometry import Drawing, Path
from kit import Kit, B, X, C, A, D
import letters
import symbols
from symbols import _bounds

SPECIAL = {}  # name -> (unicode or None, recipe)


def sp(name, uni=None):
    def deco(fn):
        SPECIAL[name] = (uni, fn); return fn
    return deco


def shell(d, advance):
    """Empty Drawing with an exact advance and zero bearings (parts are absorbed into it)."""
    g = Drawing(d, 0, 0, 0); g.left = 0.0; g.right = 0.0; g.w = advance; g.advance = advance; return g


def bb_of(g): return _bounds(g)


# ------------------------------------------------------------------ Æ Œ æ œ
@sp('AE', 0xC6)
def AE(d):
    k = Kit(d, 860, 18, 42); w, l, r, s, h = k.w, k.l, k.r, d.s, d.h; kb = d.kb
    xs = w * 0.50                                    # E stem
    k.dia(l, 0, xs - s * 0.45, C, 0.95)              # A diagonal
    k.vert(xs, 0, C); k.bar(C - h / 2, xs, r); k.bar(368 - 10 * kb, xs, r - w * 0.05); k.bar(h / 2, xs, r)
    k.bar(236 - 10 * kb, w * 0.16, xs)
    k.anchor('top', (xs + l) / 2, C); k.anchor('bottom', xs, 0); return k.g

@sp('ae', 0xE6)
def ae(d):
    a = letters.build('a', d); e = letters.build('e', d)
    s = d.s
    ax = a.advance - a.right - s / 2 - a.left           # a stem centre, box coords of a
    shift = (a.left + ax) - (e.left + s / 2)            # e's left extreme on a's stem
    g = shell(d, shift + e.advance - 4)
    g.absorb(a, 0, 0); g.absorb(e, shift, 0)
    bb = bb_of(g); g.anchors['top'] = ((bb[0] + bb[2]) / 2, X); g.anchors['bottom'] = ((bb[0] + bb[2]) / 2, 0); return g

@sp('OE', 0x152)
def OE(d):
    o = letters.build('O', d); e = letters.build('E', d); s = d.s
    o.transform(0.90, 1, 0, 0)
    shift = (o.advance - o.right * 0.90 - s / 2 * 0.9) - (e.left + s / 2) + s * 0.1
    g = shell(d, shift + e.advance)
    g.absorb(o, 0, 0); g.absorb(e, shift, 0)
    bb = bb_of(g); g.anchors['top'] = ((bb[0] + bb[2]) / 2, C); g.anchors['bottom'] = ((bb[0] + bb[2]) / 2, 0); return g

@sp('oe', 0x153)
def oe(d):
    o = letters.build('o', d); e = letters.build('e', d); s = d.s
    shift = (o.advance - o.right - s / 2) - (e.left + s / 2)
    g = shell(d, shift + e.advance - 4)
    g.absorb(o, 0, 0); g.absorb(e, shift, 0)
    bb = bb_of(g); g.anchors['top'] = ((bb[0] + bb[2]) / 2, X); g.anchors['bottom'] = ((bb[0] + bb[2]) / 2, 0); return g


# ------------------------------------------------------------------ ß ẞ
def eszett(k, top, stem_top, waist, cap=False):
    l, r, m, w = k.l, k.r, k.m, k.w; h = k.d.h; kb = k.kb
    yt = top + 10 - h / 2; xr = r - 10
    ry = k.hook_ry(xr - w * 0.40, 150 + 10 * kb)
    p = Path().M(l, 0).L(l, yt - k.hook_ry(w * 0.40 - l, 150 + 30 * kb)).Q(l, yt, w * 0.40, yt, 0.56, 0.56)
    p.Q(xr, yt, xr, yt - ry, 0.56, 0.60 - 0.05 * kb).C(xr, yt - ry - 150, w * 0.76, waist + 80, w * 0.50, waist)
    k.st(p, 1 - 0.10 * kb)
    rxb = r - w * 0.46; ryb = k.hook_ry(rxb, (waist - k.cb) / 2)
    q = Path().M(w * 0.42, waist).Q(r, waist, r, waist - ryb, 0.56, 0.62 - 0.05 * kb).Q(r, k.cb, w * 0.50, k.cb, 0.62 - 0.05 * kb, 0.56).L(w * 0.34, k.cb + 6)
    k.st(q, 1 - 0.10 * kb, None, B)

@sp('germandbls', 0xDF)
def germandbls(d):
    k = Kit(d, 520, 64, 36, extra_kb=30); eszett(k, 782, A, 392 - 12 * d.kb); k.anchor('top', k.m, X); k.anchor('bottom', k.m, 0); return k.g

@sp('uni1E9E', 0x1E9E)
def Germandbls(d):
    k = Kit(d, 560, 64, 36, extra_kb=30); eszett(k, C, C, 372 - 12 * d.kb, True); k.anchor('top', k.m, C); k.anchor('bottom', k.m, 0); return k.g


# ------------------------------------------------------------------ Þ þ Ð ð
@sp('Thorn', 0xDE)
def Thorn(d):
    k = Kit(d, 485, 64, 50); l, r = k.l, k.r; h = d.h; kb = d.kb
    k.vert(l, 0, C); top_, bot_ = 580 - h / 2, 150 + h / 2 - 20 * kb; cy = (top_ + bot_) / 2
    p = Path().M(l, top_).L(l + (r - l) * 0.12, top_).Q(r, top_, r, cy, 0.62 - 0.05 * kb, 0.56).Q(r, bot_, l + (r - l) * 0.12, bot_, 0.56, 0.62 - 0.05 * kb).L(l, bot_)
    k.st(p); k.anchor('top', k.m, C); k.anchor('bottom', k.m, 0); return k.g

@sp('thorn', 0xFE)
def thorn(d):
    k = Kit(d, 450, 50, 46); l, r = k.l, k.r
    k.loop(l, 0, r, X); k.vert(l, D, A); k.anchor('top', l, A); k.anchor('bottom', k.m, 0); return k.g

@sp('Eth', 0xD0)
def Eth(d):
    g = letters.build('D', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    k.bar(350, s / 2 - 80, s / 2 + 110, 0.92); return g

@sp('Dcroat', 0x110)
def Dcroat(d):
    return Eth(d)

@sp('eth', 0xF0)
def eth(d):
    k = Kit(d, 460, 46, 46); l, r, m, w = k.l, k.r, k.m, k.w; kb = d.kb
    top_ = 450 + 10 * kb
    k.loop(l, 0, r, top_)
    p = Path().M(r, top_ * 0.62).C(r, top_ + 150, w * 0.74, 700, w * 0.40, 772)
    k.st(p, 0.96, None, B)
    k.dia(w * 0.28, 560, w * 0.80, 740, 0.70)
    k.anchor('top', m, A); k.anchor('bottom', m, 0); return k.g

@sp('dcroat', 0x111)
def dcroat(d):
    g = letters.build('d', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    xs = g.advance - g.right - s / 2
    k.bar(640, xs - 120, xs + 70, 0.92); return g


# ------------------------------------------------------------------ Ø ø Ħ ħ Ł ł Ŧ ŧ Ŋ ŋ ĸ ŉ Ŀ ŀ Ĳ ĳ
@sp('Oslash', 0xD8)
def Oslash(d):
    g = letters.build('O', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right
    k.dia(w * 0.10, -50, w * 0.90, C + 50, 0.74); return g

@sp('oslash', 0xF8)
def oslash(d):
    g = letters.build('o', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right
    k.dia(w * 0.10, -50, w * 0.90, X + 50, 0.74); return g

@sp('Hbar', 0x126)
def Hbar(d):
    g = letters.build('H', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right; s = d.s
    k.bar(590, s / 2 - 70, w - s / 2 + 70, 0.90); return g

@sp('hbar', 0x127)
def hbar(d):
    g = letters.build('h', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    k.bar(640, s / 2 - 90, s / 2 + 110, 0.90); return g

@sp('Lslash', 0x141)
def Lslash(d):
    g = letters.build('L', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    k.line(s / 2 - 100, 230, s / 2 + 100, 420, 0.80); return g

@sp('lslash', 0x142)
def lslash(d):
    g = letters.build('l', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    k.line(s / 2 - 96, 250, s / 2 + 96, 440, 0.80); return g

@sp('Tbar', 0x166)
def Tbar(d):
    g = letters.build('T', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right
    k.bar(380, w / 2 - 110, w / 2 + 110, 0.92); return g

@sp('tbar', 0x167)
def tbar(d):
    g = letters.build('t', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right; s = d.s
    k.bar(240, s / 2 + 10, w - s / 2 - 10, 0.92); return g

def eng_tail(k, x, y0):
    rx = 140 + 40 * k.kb; yb = D + 24 + k.d.h / 2; ry = k.hook_ry(rx, 130 + 40 * k.kb); tw = k.thin_for(rx)
    p = Path().M(x, y0).L(x, yb + ry).Q(x, yb, x - rx, yb, 0.56, 0.56, tw).L(x - rx - 30, yb, tw)
    k.st(p, 1, None, B)

@sp('Eng', 0x14A)
def Eng(d):
    g = letters.build('N', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    eng_tail(k, g.advance - g.left - g.right - s / 2, 120); return g

@sp('eng', 0x14B)
def eng(d):
    g = letters.build('n', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; s = d.s
    eng_tail(k, g.advance - g.left - g.right - s / 2, 120); return g

@sp('kgreenlandic', 0x138)
def kgreenlandic(d):
    k = Kit(d, 430, 50, 22); l, r = k.l, k.r
    k.vert(l, 0, X); k.dia(l, 208, r, X, 0.93); k.dia(l + 0.22 * (r - l), 198 + 0.22 * (X - 208), r + 3, 0, 0.94); return k.g

@sp('napostrophe', 0x149)
def napostrophe(d):
    q = symbols.quoteright(d); n = letters.build('n', d)
    g = shell(d, q.advance - 30 + n.advance); g.absorb(q, 0, 0); g.absorb(n, q.advance - 30, 0); return g

@sp('Ldot', 0x13F)
def Ldot(d):
    L = letters.build('L', d); dot = symbols.periodcentered(d)
    g = shell(d, L.advance + dot.advance - 40); g.absorb(L, 0, 0); g.absorb(dot, L.advance - 60, 90); return g

@sp('ldot', 0x140)
def ldot(d):
    l_ = letters.build('l', d); dot = symbols.periodcentered(d)
    g = shell(d, l_.advance + dot.advance - 20); g.absorb(l_, 0, 0); g.absorb(dot, l_.advance - 40, 0); return g

@sp('IJ', 0x132)
def IJ(d):
    i = letters.build('I', d); j = letters.build('J', d)
    g = shell(d, i.advance + j.advance - 20); g.absorb(i, 0, 0); g.absorb(j, i.advance - 20, 0); return g

@sp('ij', 0x133)
def ij(d):
    i = letters.build('i', d); j = letters.build('j', d)
    g = shell(d, i.advance + j.advance - 10); g.absorb(i, 0, 0); g.absorb(j, i.advance - 10, 0); return g

@sp('longs', 0x17F)
def longs(d):
    k = Kit(d, 240, 20, 30, extra_kb=30); w = k.w; kb = d.kb; h = d.h
    x = d.W(90) + 10 * kb; rx = min(w - 4 - x, 150); ry = k.hook_ry(rx, 150)
    p = Path().M(x, 0).L(x, 782 - h / 2 - ry).Q(x, 782 - h / 2, x + rx, 782 - h / 2, 0.56, 0.52).L(w + 12, 782 - h / 2 - 8)
    k.st(p, 1, None, B); return k.g


# ------------------------------------------------------------------ ligatures
def f_terminal_end(f, d):
    """x where the f's hook terminal ends (glyph coords)."""
    return f.left + f.w + 12

def f_into_stem(k, f, x_stem, d):
    """The f redrawn for a ligature: stem, crossbar and an arch that runs straight into the
    following stem (no free terminal, so nothing protrudes above the join)."""
    s = d.s; h = d.h; kb = d.kb; top_c = 782 - h / 2
    xf = f.left + d.W(90) + 10 * kb
    rx = min(150, (x_stem + s / 2 - xf) * 0.52); ry = k.hook_ry(rx, 150)
    p = Path().M(xf, 0).L(xf, top_c - ry).Q(xf, top_c, xf + rx, top_c, 0.56, 0.52).L(x_stem + s / 2, top_c)
    k.st(p); k.bar(500, f.left + s / 2, f.left + f.w - 6)
    return top_c

def f_hook_to(k, f, x_end, d):
    """The f redrawn for the fi ligature: stem, crossbar and a hook whose cut terminal ends at x_end
    (shorter than the free f's hook when the following dot needs the room)."""
    s = d.s; h = d.h; kb = d.kb; top_c = 782 - h / 2
    xf = f.left + d.W(90) + 10 * kb
    rx = min(150, max(60, (x_end - xf) * 0.62)); ry = k.hook_ry(rx, 150)
    p = Path().M(xf, 0).L(xf, top_c - ry).Q(xf, top_c, xf + rx, top_c, 0.56, 0.52).L(x_end, top_c - 8)
    k.st(p, 1, None, B); k.bar(500, f.left + s / 2, f.left + f.w - 6)

@sp('f_i')
def f_i(d):
    """f with its hook trimmed so the i keeps its dot: the pair is fitted, never fused, so fi
    stays distinct from fl at every size."""
    f = letters.build('f', d); i = letters.build('i', d); s = d.s
    ds = symbols.dotsize(d) * 1.06
    xi = f_terminal_end(f, d) - 6 + s * 0.42                   # i stem centre: tucked under the hook's end
    x_end = min(f_terminal_end(f, d), xi - ds / 2 - 34)         # hook ends clear of the dot
    adv = xi + s / 2 + i.right
    g = shell(d, adv); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    f_hook_to(k, f, x_end, d); k.vert(xi, 0, X); k.dot(xi, 672, 1.06)
    g.anchors['caret_1'] = (xi - s / 2 - 10, 0); return g

@sp('f_l')
def f_l(d):
    """f whose arch lands on the l stem."""
    f = letters.build('f', d); l_ = letters.build('l', d); s = d.s
    xl = f_terminal_end(f, d) + s * 0.30
    shift = xl - (l_.left + s / 2)
    g = shell(d, shift + l_.advance); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    top_c = f_into_stem(k, f, xl, d); g.absorb(l_, shift, 0); k.vert(xl, A - 40, top_c)
    g.anchors['caret_1'] = (xl - s / 2 - 10, 0); return g

def ff_first(k, xf, x_next, top_c):
    """First f of ff: its arch runs straight into the next stem."""
    rx = min(150, (x_next - xf) * 0.5); ry = k.hook_ry(rx, 150)
    p = Path().M(xf, 0).L(xf, top_c - ry).Q(xf, top_c, xf + rx, top_c, 0.56, 0.52).L(x_next, top_c)
    k.st(p)

def ff_with(second, d):
    f = letters.build('f', d); kb = d.kb; h = d.h; s = d.s
    xf1 = f.left + d.W(90) + 10 * kb
    step = f.advance - 46 - 20 * kb
    g = shell(d, step + second.advance); k = Kit(d, 0, 0, 0, raw=True); k.g = g
    xf2 = step + xf1; top_c = 782 - h / 2
    ff_first(k, xf1, xf2, top_c); g.absorb(second, step, 0); k.bar(500, xf1 - s / 2, xf2 + 4)
    carets = [(xf2 - s / 2 - 10, 0)] + [(x + step, y) for n, (x, y) in sorted(second.anchors.items()) if n.startswith('caret_')]
    g.anchors = {f'caret_{i + 1}': c for i, c in enumerate(carets)}; return g

@sp('f_f')
def f_f(d): return ff_with(letters.build('f', d), d)

@sp('f_f_i')
def f_f_i(d): return ff_with(f_i(d), d)

@sp('f_f_l')
def f_f_l(d): return ff_with(f_l(d), d)


# ------------------------------------------------------------------ figures
FIG_NAMES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def tabular(ch, d):
    g = letters.build(ch, d); tw = symbols.tabular_width(d); dx = (tw - g.advance) / 2
    g.transform(1, 1, dx, 0); g.advance = tw; return g

def small_figure(ch, d, dy, scale=0.60):
    g = letters.build(ch, d.derive(1.46 - 0.30 * d.kb)); g.transform(scale, scale, 0, dy)
    # tighten bearings a little: small figures sit closer together
    g.transform(1, 1, -8, 0); g.advance -= 16; return g

for _i, _n in enumerate(FIG_NAMES):
    _ch = str(_i)
    SPECIAL[_n + '.tf'] = (None, (lambda ch: lambda d: tabular(ch, d))(_ch))
    SPECIAL[_n + '.numr'] = (None, (lambda ch: lambda d: small_figure(ch, d, 280))(_ch))
    SPECIAL[_n + '.dnom'] = (None, (lambda ch: lambda d: small_figure(ch, d, 0))(_ch))

SUPS = {'zero': 0x2070, 'one': 0xB9, 'two': 0xB2, 'three': 0xB3, 'four': 0x2074, 'five': 0x2075, 'six': 0x2076, 'seven': 0x2077, 'eight': 0x2078, 'nine': 0x2079}
for _i, _n in enumerate(FIG_NAMES):
    _ch = str(_i)
    SPECIAL[_n + 'superior'] = (SUPS[_n], (lambda ch: lambda d: small_figure(ch, d, 320))(_ch))
    SPECIAL[_n + 'inferior'] = (0x2080 + _i, (lambda ch: lambda d: small_figure(ch, d, -130))(_ch))


def prebuilt_fraction(d, num, den):
    n = small_figure(num, d, 280); fr = symbols.fraction(d); dn = small_figure(den, d, 0)
    g = shell(d, n.advance + fr.advance + dn.advance)
    g.absorb(n, 0, 0); g.absorb(fr, n.advance, 0); g.absorb(dn, n.advance + fr.advance, 0); return g

@sp('onequarter', 0xBC)
def onequarter(d): return prebuilt_fraction(d, '1', '4')

@sp('onehalf', 0xBD)
def onehalf(d): return prebuilt_fraction(d, '1', '2')

@sp('threequarters', 0xBE)
def threequarters(d): return prebuilt_fraction(d, '3', '4')

@sp('zero.zero')
def zero_slashed(d):
    g = letters.build('0', d); k = Kit(d, 0, 0, 0, raw=True); k.g = g; w = g.advance - g.left - g.right
    k.dia(w * 0.30, 170, w * 0.70, 530, 0.62); return g

@sp('zero.tf.zero')
def zero_tf_slashed(d):
    g = zero_slashed(d); tw = symbols.tabular_width(d); dx = (tw - g.advance) / 2
    g.transform(1, 1, dx, 0); g.advance = tw; return g


# ------------------------------------------------------------------ case punctuation
def raised(fn, dy):
    def rec(d):
        g = fn(d); g.transform(1, 1, 0, dy(d) if callable(dy) else dy); return g
    return rec

CASE_SHIFTS = {
    'hyphen': lambda d: 74 - 10 * d.kb, 'endash': lambda d: 74 - 10 * d.kb, 'emdash': lambda d: 74 - 10 * d.kb,
    'parenleft': 50, 'parenright': 50, 'bracketleft': 50, 'bracketright': 50, 'braceleft': 50, 'braceright': 50,
    'guillemotleft': 90, 'guillemotright': 90, 'guilsinglleft': 90, 'guilsinglright': 90,
    'periodcentered': lambda d: 80 - 20 * d.kb, 'bullet': 60, 'exclamdown': 180, 'questiondown': 180,
    'at': 0,
}
for _name, _dy in CASE_SHIFTS.items():
    if _name == 'at':
        continue
    SPECIAL[_name + '.case'] = (None, raised(symbols.SYMBOLS[_name][1], _dy))
