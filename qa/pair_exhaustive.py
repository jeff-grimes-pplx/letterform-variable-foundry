#!/usr/bin/env python3
"""Exhaustive two-glyph collision receipt.

Every ordered pair of encoded characters (all 477 codepoints of the font except controls, spaces and
soft hyphen) is shaped with HarfBuzz (uharfbuzz) at each design-space location with `liga` off, plus
every pair starting with f with `liga` on; each glyph's filled outline is rasterised separately at
1 px per font unit (overlaps removed first, skia-pathops), and the two masks are intersected.  Any
shared pixel is a collision.  Unlike `pair_overlap.py` (curated strings), this covers nonsense pairs
too, so the report lists every colliding pair and the review decides which ones matter.

usage: python3 qa/pair_exhaustive.py [font.ttf] [--json out.json] [--locations 800/75,400/100]
"""
import sys, io, json, itertools, time
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageDraw
import uharfbuzz as hb
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from pair_overlap import FlattenPen

LOCATIONS = [(200, 75), (200, 125), (400, 100), (600, 88), (700, 75), (800, 75), (800, 100), (800, 125)]


def char_list(font):
    cmap = font.getBestCmap()
    # combining marks (U+0300–036F) attach to the preceding base by design, so they are not neighbours
    return [chr(cp) for cp in sorted(cmap) if cp > 0x20 and cp not in (0x7F, 0xA0, 0xAD) and not (0x80 <= cp < 0xA0) and not (0x300 <= cp <= 0x36F)]


def masks_for(static):
    gs = static.getGlyphSet(); out = {}
    for name in static.getGlyphOrder():
        pen = FlattenPen(gs); gs[name].draw(pen)
        if not pen.contours:
            out[name] = None; continue
        xs = [x for c in pen.contours for x, y in c]; ys = [y for c in pen.contours for x, y in c]
        x0, y0, x1, y1 = int(np.floor(min(xs))) - 1, int(np.floor(min(ys))) - 1, int(np.ceil(max(xs))) + 2, int(np.ceil(max(ys))) + 2
        w, h = x1 - x0, y1 - y0
        m = np.zeros((h, w), bool)
        for c in pen.contours:
            im = Image.new('1', (w, h), 0)
            ImageDraw.Draw(im).polygon([(x - x0, y1 - 1 - y) for x, y in c], fill=1)   # even-odd via xor; y flipped
            m ^= np.array(im, bool)
        out[name] = (m, (x0, y0, x1, y1))
    return out


def intersect(ma, xa, ya, mb, xb, yb):
    """shared pixel count of mask a placed at (xa, ya) and mask b at (xb, yb); None if boxes are disjoint."""
    A, (ax0, ay0, ax1, ay1) = ma; B, (bx0, by0, bx1, by1) = mb
    ix0, ix1 = max(xa + ax0, xb + bx0), min(xa + ax1, xb + bx1)
    iy0, iy1 = max(ya + ay0, yb + by0), min(ya + ay1, yb + by1)
    if ix1 <= ix0 or iy1 <= iy0:
        return 0, None
    # rows: image row 0 is the top (y = y1 - 1)
    def crop(M, box, gx, gy):
        x0, y0, x1, y1 = box
        left = int(ix0 - (gx + x0)); right = int(ix1 - (gx + x0))
        top = int((gy + y1) - iy1); bottom = int((gy + y1) - iy0)
        return M[top:bottom, left:right]
    inter = crop(A, (ax0, ay0, ax1, ay1), xa, ya) & crop(B, (bx0, by0, bx1, by1), xb, yb)
    n = int(inter.sum())
    if not n:
        return 0, None
    ys, xs = np.nonzero(inter)
    return n, [int(ix0 + xs.min()), int(iy1 - 1 - ys.max()), int(ix0 + xs.max() + 1), int(iy1 - ys.min())]


def check_location(vf_path, wght, wdth, chars=None):
    vf = TTFont(vf_path)
    static = instancer.instantiateVariableFont(vf, {'wght': wght, 'wdth': wdth}, inplace=False, overlap=instancer.OverlapMode.REMOVE) if 'fvar' in vf else vf   # a static (e.g. a quick master build) is tested as is
    bio = io.BytesIO(); static.save(bio); fb = bio.getvalue()
    order = static.getGlyphOrder(); masks = masks_for(static)
    face = hb.Face(fb); font = hb.Font(face); font.scale = (face.upem, face.upem)
    chars = chars or char_list(static)
    hits = []; tested = 0
    for feats in ({'liga': False}, {'liga': True}):
        for a, b in itertools.product(chars, chars):
            if feats['liga'] and a != 'f':
                continue
            buf = hb.Buffer(); buf.add_str(a + b); buf.guess_segment_properties(); hb.shape(font, buf, feats)
            infos = buf.glyph_infos; pos = buf.glyph_positions
            if len(infos) != 2:
                continue   # ligated or decomposed: not a two-glyph pair
            tested += 1
            na, nb = order[infos[0].codepoint], order[infos[1].codepoint]
            ma, mb = masks[na], masks[nb]
            if ma is None or mb is None:
                continue
            xa, ya = pos[0].x_offset, pos[0].y_offset
            xb, yb = pos[0].x_advance + pos[1].x_offset, pos[1].y_offset
            n, box = intersect(ma, xa, ya, mb, xb, yb)
            if n:
                hits.append({'pair': a + b, 'glyphs': f'{na} {nb}', 'px': n, 'box': box, 'liga': feats['liga']})
    return tested, hits


def category(h):
    """Reading category for the report: which kinds of text a colliding pair can occur in."""
    a, b = h['pair'][0], h['pair'][1]; ga, gb = h['glyphs'].split()
    if 'fraction' in (ga, gb):
        return 'fraction bar (negative side bearings by design: numerators and denominators tuck under it)'
    if ga in ('slash', 'backslash') or gb in ('slash', 'backslash'):
        return 'slash or backslash (overhang by design)'
    if a.isalpha() and b.isalpha():
        if a.islower() and b.isupper():
            return 'lowercase letter followed by a capital'
        if a.isupper() and b.islower():
            return 'capital followed by a lowercase letter'
        if a.isupper() and b.isupper():
            return 'two capitals'
        return 'two lowercase letters'
    return 'symbol, figure, superior or punctuation pair'


def main():
    argv = sys.argv[1:]
    skip = {argv[i + 1] for i, a in enumerate(argv) if a in ('--json', '--locations') and i + 1 < len(argv)}
    args = [a for a in argv if not a.startswith('--') and a not in skip]
    vf_path = args[0] if args else 'fonts/Apertide[wdth,wght].ttf'
    out_json = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
    locs = LOCATIONS
    if '--locations' in sys.argv:
        locs = [tuple(int(v) for v in s.split('/')) for s in sys.argv[sys.argv.index('--locations') + 1].split(',')]
    report = {}; total = 0; tested_total = 0
    for wght, wdth in locs:
        t0 = time.time(); tested, hits = check_location(vf_path, wght, wdth)
        report[f'{wght}/{wdth}'] = {'pairs_tested': tested, 'collisions': hits}; total += len(hits); tested_total += tested
        print(f'{wght}/{wdth}: {tested} pairs tested, {len(hits)} colliding ({time.time() - t0:.0f} s)')
        for h in sorted(hits, key=lambda h: -h['px']):
            print(f"   {h['pair']}  [{h['glyphs']}]  {h['px']} px" + ('  (liga on)' if h['liga'] else ''))
    print(f'\n{tested_total} two-glyph pairs tested over {len(locs)} locations; colliding pairs: {total}')
    # category summary across locations, with every distinct pair listed
    cats = {}
    for loc, r in report.items():
        for h in r['collisions']:
            c = category(h); cats.setdefault(c, {})
            cats[c].setdefault(h['pair'], []).append((loc, h['px']))
    print('\nby category (distinct pairs; locations where they collide):')
    for c, pairs in sorted(cats.items(), key=lambda kv: -len(kv[1])):
        n = sum(len(v) for v in pairs.values())
        print(f'\n  {c}: {len(pairs)} distinct pairs, {n} pair/location hits')
        for pr, locs_ in sorted(pairs.items(), key=lambda kv: -max(px for _, px in kv[1])):
            print(f'    {pr}  ' + ', '.join(f'{l} ({px} px)' for l, px in locs_))
    if out_json:
        json.dump({'font': vf_path, 'locations': locs, 'method': __doc__, 'results': report}, open(out_json, 'w'), indent=1, ensure_ascii=False)
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
