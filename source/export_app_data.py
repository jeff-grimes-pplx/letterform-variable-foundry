"""Export compatible master outlines + skeleton centerlines + GPOS kerning + stem metrics
for the Letterform — Aptide Variable Foundry workbench.
Output: app/data/aptide-data.json and app/data/apertide-data.json (coordinates in font units, y up)."""
import json, os, re, sys
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.boundsPen import BoundsPen
from geometry import Design
from glyphset import Master
import features

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTERS = [(wg, wd) for wd in (75, 100, 125) for wg in (200, 400, 800)]
NUM = re.compile(r'[-+]?\d*\.?\d+(?:e[-+]?\d+)?')

def parse_svg(d):
    """Return (cmd string, flat number list) for an M/L/C/Z path."""
    cmds = []; nums = []
    for tok in re.findall(r'[MLCZ][^MLCZ]*', d):
        cmds.append(tok[0]); nums.extend(float(v) for v in NUM.findall(tok[1:]))
    return ''.join(cmds), nums

def rec_outline(g):
    pen = RecordingPen(); g.draw(pen); cmds = []; nums = []
    for op, args in pen.value:
        if op == 'moveTo': cmds.append('M'); nums.extend(args[0])
        elif op == 'lineTo': cmds.append('L'); nums.extend(args[0])
        elif op == 'curveTo': cmds.append('C'); [nums.extend(p) for p in args]
        elif op == 'closePath': cmds.append('Z')
        else: raise ValueError(op)
    return ''.join(cmds), nums

designs = [Design(wg, wd) for wg, wd in MASTERS]
masters = [Master(d) for d in designs]
ref = masters[4]  # 400/100
from build import EXTRA_UNICODES

master_stems = [
    {
        'wght': wg,
        'wdth': wd,
        'v_stem': round(d.s, 1),
        'h_stem': round(d.h, 1),
        'width_factor': round(d.f, 3),
    }
    for (wg, wd), d in zip(MASTERS, designs)
]

# Build resolved kerning lookup across all 9 masters for key pairs + class pairs
groups = features.kern_groups(set(ref.order))
master_kerns = [features.kerning_for(d) for d in designs]

# Map glyph -> left class and right class
left_class_of = {}
right_class_of = {}
for k, members in groups.items():
    if k.startswith('public.kern1.'):
        for m in members:
            left_class_of[m] = k
    elif k.startswith('public.kern2.'):
        for m in members:
            right_class_of[m] = k

def pair_kern_9(g1, g2):
    vals = []
    c1 = left_class_of.get(g1)
    c2 = right_class_of.get(g2)
    for mk in master_kerns:
        if (g1, g2) in mk:
            vals.append(mk[(g1, g2)])
        elif c1 and c2 and (c1, c2) in mk:
            vals.append(mk[(c1, c2)])
        else:
            vals.append(0)
    return vals

# Export curated + common kerning pairs (glyph names -> 9-master values)
SHOWCASE_KERN_PAIRS = [
    ('A', 'V'), ('A', 'W'), ('A', 'Y'), ('A', 'T'), ('A', 'O'), ('A', 'v'), ('A', 'y'), ('A', 'quoteright'),
    ('T', 'o'), ('T', 'a'), ('T', 'e'), ('T', 's'), ('T', 'u'), ('T', 'r'), ('T', 'y'), ('T', 'A'), ('T', 'period'), ('T', 'hyphen'),
    ('V', 'A'), ('V', 'o'), ('V', 'a'), ('V', 'e'), ('V', 'period'), ('V', 'rcaron'),
    ('W', 'a'), ('W', 'o'), ('W', 'A'), ('W', 'e'), ('W', 'period'),
    ('Y', 'o'), ('Y', 'a'), ('Y', 'A'), ('Y', 'e'), ('Y', 'period'),
    ('L', 'T'), ('L', 'V'), ('L', 'W'), ('L', 'Y'), ('L', 'quoteright'), ('Lcaron', 'v'),
    ('P', 'A'), ('P', 'o'), ('P', 'a'), ('P', 'period'),
    ('F', 'A'), ('F', 'o'), ('F', 'a'), ('F', 'r'), ('F', 'period'),
    ('R', 'V'), ('R', 'Y'), ('R', 'T'), ('R', 'W'), ('R', 'O'),
    ('K', 'O'), ('K', 'o'), ('K', 'y'), ('K', 'v'),
    ('O', 'A'), ('O', 'V'), ('O', 'T'), ('O', 'Y'),
    ('r', 'o'), ('r', 'a'), ('r', 'e'), ('r', 'g'), ('r', 't'), ('r', 'period'),
    ('f', 'o'), ('f', 'e'), ('f', 'a'), ('f', 'i'), ('f', 'idieresis'), ('f', 'icircumflex'), ('f', 'question'), ('f', 'quoteright'),
    ('v', 'o'), ('v', 'a'), ('v', 'period'), ('w', 'o'), ('w', 'a'), ('y', 'o'), ('y', 'a'), ('y', 'period'),
    ('rcaron', 'iacute'), ('dcaron', 'i'), ('tcaron', 'i'), ('lcaron', 'i'), ('Q', 'comma'), ('aogonek', 'j')
]
kern_Export = {}
for g1, g2 in SHOWCASE_KERN_PAIRS:
    if g1 in ref.order and g2 in ref.order:
        vals = pair_kern_9(g1, g2)
        if any(vals):
            kern_Export[f"{g1}:{g2}"] = vals

# Also export class tables so the client can compute kerning for ANY pair of glyphs in the 548-glyph set!
class_kern_9 = {}
for (a, b) in features.PAIRS.keys():
    k1 = 'public.kern1.' + a
    k2 = 'public.kern2.' + b
    vals = [mk.get((k1, k2), 0) for mk in master_kerns]
    if any(vals):
        class_kern_9[f"{a}:{b}"] = vals

out = {
    'family': 'Aptide',
    'canonical_family': 'Apertide',
    'version': '1.103',
    'masters': MASTERS,
    'master_stems': master_stems,
    'default': [400, 100],
    'extra_unicodes': EXTRA_UNICODES,
    'metrics': {'upm': 1000, 'cap': 700, 'x': 520, 'asc': 740, 'desc': -210, 'overshoot_cap': 12, 'overshoot_x': 10},
    'kern_pairs': kern_Export,
    'kern_classes': {
        'left': {k.replace('public.kern1.', ''): v for k, v in groups.items() if k.startswith('public.kern1.')},
        'right': {k.replace('public.kern2.', ''): v for k, v in groups.items() if k.startswith('public.kern2.')},
        'values': class_kern_9,
    },
    'glyphs': {},
    'skeletons': {}
}

bad = []
for name in ref.order:
    g = {'uni': ref.unicodes.get(name), 'adv': [m.advances[name] for m in masters]}
    if name in ref.outlines:
        recs = [rec_outline(m.outlines[name]) for m in masters]
        if len({c for c, _ in recs}) != 1 or len({len(n) for _, n in recs}) != 1:
            bad.append(name); continue
        g['cmds'] = recs[0][0]
        g['pts'] = [[round(v, 1) for v in n] for _, n in recs]
        # Compute x-bounds [xmin, xmax] across the 9 masters from the recorded points
        bounds = []
        for _, flat_nums in recs:
            xs = flat_nums[0::2]
            ys = flat_nums[1::2]
            if xs and ys:
                bounds.append([round(min(xs), 1), round(min(ys), 1), round(max(xs), 1), round(max(ys), 1)])
            else:
                bounds.append([0, 0, 0, 0])
        g['bbox'] = bounds
        # Anchors on default master
        if ref.outlines[name].anchors:
            g['anchors'] = {an: [round(ax, 1), round(ay, 1)] for an, (ax, ay) in ref.outlines[name].anchors.items()}
        sks = [m.outlines[name].skeleton for m in masters]
        if len({len(s) for s in sks}) == 1:
            strokes = []
            ok = True
            for i in range(len(sks[0])):
                parsed = [parse_svg(s[i]['d']) for s in sks]
                if len({c for c, _ in parsed}) != 1 or len({len(n) for _, n in parsed}) != 1:
                    ok = False; break
                strokes.append({
                    'cmds': parsed[0][0],
                    'pts': [[round(v, 1) for v in n] for _, n in parsed],
                    's': [round(s[i]['s'], 1) for s in sks],
                    'h': [round(s[i]['h'], 1) for s in sks],
                    'kind': sks[0][i].get('kind', 'stroke'),
                    'closed': bool(sks[0][i].get('closed'))
                })
            if ok:
                out['skeletons'][name] = strokes
    else:
        g['components'] = [
            [c[0], [[round(m.components[name][j][1], 1), round(m.components[name][j][2], 1)] for m in masters]]
            for j, c in enumerate(ref.components[name])
        ]
    out['glyphs'][name] = g

os.makedirs(os.path.join(ROOT, 'app', 'data'), exist_ok=True)
for fname in ('aptide-data.json', 'apertide-data.json'):
    path = os.path.join(ROOT, 'app', 'data', fname)
    with open(path, 'w') as fh:
        json.dump(out, fh, separators=(',', ':'))
print('Exported', path, round(os.path.getsize(path) / 1e6, 2), 'MB', 'glyphs:', len(out['glyphs']), 'skeletons:', len(out['skeletons']), 'kern_pairs:', len(kern_Export), 'incompatible:', bad)
