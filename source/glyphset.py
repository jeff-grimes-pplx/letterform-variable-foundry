"""Apertide glyph set: assembles every glyph for one master (Design) as either an
outline Drawing or a component recipe, with Unicode mapping and glyph order."""
import unicodedata
from collections import OrderedDict
from fontTools import agl
from geometry import Design, Drawing
import letters, symbols, marks, special
from kit import X, C, A, D

MARK_NAME = {0x300: 'gravecomb', 0x301: 'acutecomb', 0x302: 'circumflexcomb', 0x303: 'tildecomb', 0x304: 'macroncomb',
             0x306: 'brevecomb', 0x307: 'dotaccentcomb', 0x308: 'dieresiscomb', 0x30A: 'ringcomb', 0x30B: 'hungarumlautcomb',
             0x30C: 'caroncomb', 0x327: 'cedillacomb', 0x328: 'ogonekcomb', 0x323: 'dotbelowcomb', 0x326: 'uni0326', 0x312: 'uni0312'}
BELOW = {'cedillacomb', 'dotbelowcomb', 'uni0326'}
CARON_ALT = {0x10F, 0x13E, 0x165, 0x13D}          # ď ľ ť Ľ
COMMA_BELOW_INSTEAD = {0x136, 0x137, 0x13B, 0x13C, 0x145, 0x146, 0x156, 0x157, 0x122}   # Ķ ķ Ļ ļ Ņ ņ Ŗ ŗ Ģ
COMMA_ABOVE_INSTEAD = {0x123}                     # ģ
ASC = set('bdfhklt')

LATIN1 = [cp for cp in range(0xC0, 0x100) if unicodedata.category(chr(cp)).startswith('L')]
EXT_A = list(range(0x100, 0x180))
EXT_B = [0x218, 0x219, 0x21A, 0x21B, 0x1E9E]
EXT_ADD = [0x1E02, 0x1E03, 0x1E0A, 0x1E0B, 0x1E1E, 0x1E1F, 0x1E40, 0x1E41, 0x1E56, 0x1E57, 0x1E60, 0x1E61, 0x1E6A, 0x1E6B,
           0x1E80, 0x1E81, 0x1E82, 0x1E83, 0x1E84, 0x1E85, 0x1EF2, 0x1EF3, 0x1E8E, 0x1E8F, 0x1EBC, 0x1EBD, 0x1EF8, 0x1EF9,
           0x1E04, 0x1E05, 0x1E0C, 0x1E0D, 0x1E24, 0x1E25, 0x1E32, 0x1E33, 0x1E36, 0x1E37, 0x1E42, 0x1E43, 0x1E44, 0x1E45,
           0x1E46, 0x1E47, 0x1E5A, 0x1E5B, 0x1E62, 0x1E63, 0x1E6C, 0x1E6D, 0x1E92, 0x1E93, 0x1EA0, 0x1EA1, 0x1EB8, 0x1EB9,
           0x1ECA, 0x1ECB, 0x1ECC, 0x1ECD, 0x1EE4, 0x1EE5, 0x1EF4, 0x1EF5]


def gname(cp):
    return agl.UV2AGL.get(cp) or 'uni%04X' % cp


def composite_plan():
    """List of (name, cp, base_char, [(markname, anchor_pair)]) for every composite."""
    plan = []
    drawn = {u for _, (u, _) in special.SPECIAL.items() if u} | {u for _, (u, _) in symbols.SYMBOLS.items() if u} | {ord(c) for c in letters.WIDTHS}
    for cp in LATIN1 + EXT_A + EXT_B + EXT_ADD:
        if cp in drawn:
            continue
        ch = chr(cp); nfd = unicodedata.normalize('NFD', ch)
        if len(nfd) < 2:
            continue
        base = nfd[0]; combs = [ord(c) for c in nfd[1:]]
        if base not in letters.WIDTHS:
            continue
        if cp in COMMA_BELOW_INSTEAD:
            combs = [0x326]
        if cp in COMMA_ABOVE_INSTEAD:
            combs = [0x312]
        items = []
        for mc in combs:
            mn = MARK_NAME.get(mc)
            if mn is None:
                items = None; break
            if cp in CARON_ALT and mn == 'caroncomb':
                items.append(('caroncomb.alt', 'alt')); continue
            if mn in BELOW:
                items.append((mn, 'bottom'))
            elif mn == 'ogonekcomb':
                items.append((mn, 'ogonek'))
            else:
                if base.isupper() or base in ASC:
                    mn = mn + '.case'
                elif base in 'ij' and mn in marks.NARROW_I:
                    mn = mn + '.i'      # narrow set for the narrow bases (î ĩ ī ĭ ï ĵ)
                items.append((mn, 'top'))
        if items is None:
            continue
        if base in 'ij' and any(a == 'top' for _, a in items):
            base = 'ı' if base == 'i' else 'ȷ'
        plan.append((gname(cp), cp, base, items))
    return plan


def spacing_marks():
    """Spacing versions of accents as components of the combining marks."""
    return [('grave', 0x60, 'gravecomb'), ('acute', 0xB4, 'acutecomb'), ('circumflex', 0x2C6, 'circumflexcomb'),
            ('tilde', 0x2DC, 'tildecomb'), ('macron', 0xAF, 'macroncomb'), ('breve', 0x2D8, 'brevecomb'),
            ('dotaccent', 0x2D9, 'dotaccentcomb'), ('dieresis', 0xA8, 'dieresiscomb'), ('ring', 0x2DA, 'ringcomb'),
            ('cedilla', 0xB8, 'cedillacomb'), ('ogonek', 0x2DB, 'ogonekcomb'), ('caron', 0x2C7, 'caroncomb'),
            ('hungarumlaut', 0x2DD, 'hungarumlautcomb')]


class Master:
    """All glyphs of one master. `outlines[name] = Drawing`, `components[name] = [(base, dx, dy)]`."""

    def __init__(self, d: Design):
        self.d = d; self.outlines = OrderedDict(); self.components = OrderedDict(); self.unicodes = {}; self.advances = {}
        self.order = []
        self._build()

    def add(self, name, g, uni=None):
        self.outlines[name] = g; self.advances[name] = round(g.advance); self.order.append(name)
        if uni:
            self.unicodes[name] = uni

    def _build(self):
        d = self.d
        # .notdef: a box with a counter
        nd = Drawing(d, 420, 40, 40); nd.left = 40; nd.right = 40; nd.w = 420; nd.advance = 500
        t = d.s * 0.6
        nd.rect(0, 0, 420, C); nd._emit((40 + t, t), [('L', (40 + 420 - t, t)), ('L', (40 + 420 - t, C - t)), ('L', (40 + t, C - t)), ('L', (40 + t, t))], clockwise=False)
        self.add('.notdef', nd)
        # letters and figures
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ıȷ':
            g = letters.build(ch, d); marks.add_base_anchors(ch, g, d)
            name = gname(ord(ch)) if ch not in 'ıȷ' else ('dotlessi' if ch == 'ı' else 'uni0237')
            self.add(name, g, ord(ch))
        for name, (uni, fn) in symbols.SYMBOLS.items():
            self.add(name, fn(d), uni)
        for name, (uni, fn) in special.SPECIAL.items():
            self.add(name, fn(d), uni)
        for name, (uni, fn) in marks.MARKS.items():
            self.add(name, fn(d), uni)
        # composites
        for name, cp, base, items in composite_plan():
            bname = gname(ord(base)) if base not in 'ıȷ' else ('dotlessi' if base == 'ı' else 'uni0237')
            bg = self.outlines[bname]; comps = [(bname, 0.0, 0.0)]
            for mn, anchor in items:
                mg = self.outlines[mn]
                if anchor == 'alt':
                    bb = symbols._bounds(bg); top = {'d': A, 'l': A, 't': 676, 'L': C}[base]
                    dx = bb[2] + 36 + d.s * 0.2; dy = top
                else:
                    ax, ay = bg.anchors[anchor]; mx, my = mg.anchors['_' + anchor]
                    dx, dy = ax - mx, ay - my
                comps.append((mn, dx, dy))
            self.components[name] = comps; self.advances[name] = round(bg.advance); self.unicodes[name] = cp; self.order.append(name)
        for name, cp, comb in spacing_marks():
            mg = self.outlines[comb]; bb = symbols._bounds(mg)
            adv = round(bb[2] - bb[0] + 2 * 60 + d.s * 0.2)
            dx = (adv / 2) - (bb[0] + bb[2]) / 2
            dy = 0 if comb in ('cedillacomb', 'ogonekcomb') else 0
            self.components[name] = [(comb, dx, dy)]; self.advances[name] = adv; self.unicodes[name] = cp; self.order.append(name)
        # Idotaccent etc. come from the plan (U+0130 decomposes to I + dot above).

    def all_names(self):
        return list(self.order)
