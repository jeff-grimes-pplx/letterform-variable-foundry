#!/usr/bin/env python3
"""Collision receipt: shape test strings with HarfBuzz (uharfbuzz) at chosen variable-font locations,
rasterise every glyph's filled outline separately at 1 px per font unit (1000 px/em) and intersect the
masks of neighbouring glyphs.  Any shared pixel between two different glyphs is reported as a collision.
Overlapping contours are removed before rasterising (skia-pathops), so even-odd filling equals non-zero.

usage: python3 qa/pair_overlap.py [font.ttf] [--json out.json]
"""
import sys, json, itertools
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.basePen import BasePen
from fontTools.pens.recordingPen import RecordingPen
from PIL import Image, ImageDraw, ImageChops
import uharfbuzz as hb

LOCATIONS = [(200, 75), (200, 125), (400, 100), (600, 88), (700, 75), (800, 75), (800, 100), (800, 125)]
# strings cover the pairs that have ever touched or are typical collision risks (f before dotted/accented
# letters and ascenders with ligatures off, Czech/Slovak caron sequences, dieresis stacks, punctuation after f).
STRINGS = {
    'f-before (liga off)': 'fi fí fì fî fï fĩ fī fĭ fį fı fj fĵ fb fh fk fl fł ft f? f) f] f} f! f| f/ fä fö fü fë fÿ fâ fê fô fû fá fé fó fú fà fè fò fù fã fõ fñ fā fē fō fū få fů fč fě fň fř fš fž fť fď fľ fţ fş fț fș fğ fĝ fĥ fĵ fŵ fŷ fẃ fẁ fẅ fỳ fċ fġ fḃ fḋ fḟ fṁ fṗ fṡ fṫ',
    'ff-before (liga off)': 'ffi ffí ffï ffî ffj ffb ffh ffk ffl ff? ff) ffä ffé ffü ffö',
    'carons / accents in sequence': 'přiřídíl ří ře řá řé řó řú řů řy řt řl řk řb řh řd řť ďí ťí ľí ňí šť čí žíl iř íř ìř îř ïř ĩř īř ĭř lř jř kř hř bř dř tř úř ůř éř ýř ďi ťi ľi ďì ťì ľì ďî ťî ľî ďï ťï ľï ďú ťú ľú ďá ťá ľá ďó ťó ľó ďé ťé ľé ďü ťü ľü ďö ťö ľö ďä ťä ľä ďô ľô ťô ďô ľů ďů ťů ďý ťý ľý ďñ ďã ďõ ďâ ďê ďà ďè ďò ďù ďā ďē ďō ďū ďě ďň ďš ďž ďč ďř ďľ ďť ďď ťť ľľ ď? ď) ď! ť? ť) ľ) ď” ť’ ľ’',
    'dieresis / stacks': 'ïëÿ ÄÖÜ äöü ÿï ïï ëï üï öï äï ïë ÏË ÄË ÖÜ ÜÏ',
    'quotes & punctuation': "f' f\" f’ f” fʼ r’ r” v’ w’ y’ T’ V’ W’ Y’ P. P, F. F, T. T, V. V, Y. Y, r. r, v. v, w. w, y. y, 7. 7,",
    'kerned pairs': 'AV AW AY AT LT LV LY TA Ta Te To Tr Tu Ty VA Va Ve Vo WA Wa We Wo YA Ya Ye Yo PA Pa Pe Po FA Fa Fe Fo KO Ko RO Ro ro re rt ra rs vo va wo wa yo ya L’A f) f? ff',
    'narrow i-marks (1.102)': 'dîner Nîmes Hî Mî Vî Kï Yï Tî maître naïf fête île Îles îî ĩĭ ïĩ īī ĭĭ ïi iï iĭ íĭ Hawaïi',
    'Ľ Ŀ đ Æ Œ (1.102)': 'ĽV ĽY ĽT Ľ’ Ľ" ĽUDIA ĽW Ŀ’ ĿL đĩa đã đi đó đĵ ÆV ÆT ÆY Æ’ ŒV ŒT ŒY',
    'tails and arms (1.102)': 'Q, Q; Q‚ FAQ, K2 k2 R2 A2 SKY KYIV kv kx mił był kąpiel następny ąj ęj ďb ďh ďk ďl ďt ťb ťh ťk ťl ťt ľb ľh ľk ľl ľt',
}
FEATURES_BY_GROUP = {'f-before (liga off)': {'liga': False}, 'ff-before (liga off)': {'liga': False}}


class FlattenPen(BasePen):
    """Collect closed contours as point lists (curves flattened)."""
    def __init__(self, glyphSet, steps=12):
        super().__init__(glyphSet); self.contours = []; self.cur = []; self.steps = steps
    def _moveTo(self, p): self.cur = [p]
    def _lineTo(self, p): self.cur.append(p)
    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; mt = 1 - t
            self.cur.append((mt**3*p0[0] + 3*mt*mt*t*p1[0] + 3*mt*t*t*p2[0] + t**3*p3[0], mt**3*p0[1] + 3*mt*mt*t*p1[1] + 3*mt*t*t*p2[1] + t**3*p3[1]))
    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; mt = 1 - t
            self.cur.append((mt*mt*p0[0] + 2*mt*t*p1[0] + t*t*p2[0], mt*mt*p0[1] + 2*mt*t*p1[1] + t*t*p2[1]))
    def _closePath(self):
        if len(self.cur) > 2: self.contours.append(self.cur)
        self.cur = []
    def _endPath(self): self._closePath()


def glyph_mask(glyphset, name, pad=4):
    """(mask image, origin offset) for a glyph at 1 px/unit; even-odd fill of its contours."""
    pen = FlattenPen(glyphset); glyphset[name].draw(pen)
    if not pen.contours: return None
    xs = [x for c in pen.contours for x, y in c]; ys = [y for c in pen.contours for x, y in c]
    x0, y0, x1, y1 = int(min(xs)) - pad, int(min(ys)) - pad, int(max(xs)) + pad + 1, int(max(ys)) + pad + 1
    w, h = x1 - x0, y1 - y0
    mask = Image.new('1', (w, h), 0)
    for c in pen.contours:
        m = Image.new('1', (w, h), 0)
        ImageDraw.Draw(m).polygon([(x - x0, y1 - 1 - y) for x, y in c], fill=1)   # flip y
        mask = ImageChops.logical_xor(mask, m)
    return mask, (x0, y0, x1, y1)


def shape(font_bytes, text, features):
    face = hb.Face(font_bytes); font = hb.Font(face); font.scale = (face.upem, face.upem)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, features)
    return [(i.codepoint, p.x_advance, p.x_offset, p.y_offset) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]


def check_location(vf_path, wght, wdth):
    vf = TTFont(vf_path)
    static = instancer.instantiateVariableFont(vf, {'wght': wght, 'wdth': wdth}, inplace=False, overlap=instancer.OverlapMode.REMOVE) if 'fvar' in vf else vf
    import io
    bio = io.BytesIO(); static.save(bio); font_bytes = bio.getvalue()
    gs = static.getGlyphSet(); order = static.getGlyphOrder(); masks = {}
    results = []
    for group, text in STRINGS.items():
        feats = FEATURES_BY_GROUP.get(group, {})
        for word in text.split(' '):
            run = shape(font_bytes, word, feats)
            x = 0; placed = []
            for gid, adv, xo, yo in run:
                name = order[gid]
                if name not in masks: masks[name] = glyph_mask(gs, name)
                placed.append((name, x + xo, yo, masks[name])); x += adv
            for (na, xa, ya, ma), (nb, xb, yb, mb) in zip(placed, placed[1:]):
                if ma is None or mb is None: continue
                (ax0, ay0, ax1, ay1) = ma[1]; (bx0, by0, bx1, by1) = mb[1]
                ix0, ix1 = max(xa + ax0, xb + bx0), min(xa + ax1, xb + bx1)
                iy0, iy1 = max(ya + ay0, yb + by0), min(ya + ay1, yb + by1)
                if ix1 <= ix0 or iy1 <= iy0: continue
                # crop both masks to the intersection box (image y is flipped: row 0 = top = y1-1)
                def crop(m, box, gx, gy):
                    (x0, y0, x1, y1) = box
                    left = int(ix0 - (gx + x0)); right = int(ix1 - (gx + x0))
                    top = int((gy + y1) - iy1); bottom = int((gy + y1) - iy0)
                    return m.crop((left, top, right, bottom))
                ca = crop(ma[0], ma[1], xa, ya); cb = crop(mb[0], mb[1], xb, yb)
                inter = ImageChops.logical_and(ca, cb)
                n = int(sum(inter.convert('L').point(lambda v: 1 if v else 0).getdata()))
                if n:
                    bbox = inter.getbbox()
                    results.append({'group': group, 'word': word, 'pair': f'{na} {nb}', 'overlap_px': n,
                                    'x': [int(ix0 + bbox[0]), int(ix0 + bbox[2])], 'y': [int(iy1 - bbox[3]), int(iy1 - bbox[1])]})
    return results


def main():
    out_json = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
    args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith('--') and sys.argv[i - 1] != '--json']
    vf_path = args[0] if args else 'fonts/Apertide[wdth,wght].ttf'
    report = {}; total = 0
    locations = LOCATIONS if 'fvar' in TTFont(vf_path) else [('static', '')]
    for wght, wdth in locations:
        res = check_location(vf_path, wght, wdth); report[f'{wght}/{wdth}'] = res; total += len(res)
        print(f'{wght}/{wdth}: {len(res)} colliding pair(s)' + (' — ' + '; '.join(f"{r['word']} [{r['pair']}] {r['overlap_px']}px" for r in res) if res else ''))
    npairs = sum(len(w) - 1 for t in STRINGS.values() for w in t.split(' ')) * len(locations)
    print(f'\n{npairs} neighbouring glyph pairs tested over {len(locations)} locations; collisions: {total}')
    if out_json: json.dump({'font': vf_path, 'locations': LOCATIONS, 'strings': STRINGS, 'collisions': report, 'pairs_tested': npairs}, open(out_json, 'w'), indent=1, ensure_ascii=False)
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
