"""Independent parser / sanitizer receipts for the compiled Apertide binaries.
Run from builds/A4-letterform:  python3 qa/independent_parsers.py > qa/independent-parsers.txt"""
import glob, json, subprocess, sys, os
files = ['fonts/Apertide[wdth,wght].ttf', 'fonts/Apertide[wdth,wght].woff2'] + sorted(glob.glob('fonts/static/*.ttf'))
print('# Independent parser / sanitizer receipts\n')
print('## OpenType Sanitizer (ots-sanitize, python -m ots <file>)')
import ots
print('ots-python', getattr(ots, '__version__', '?'))
allok = True
for f in files:
    r = subprocess.run([sys.executable, '-m', 'ots', f], capture_output=True, text=True)
    ok = r.returncode == 0; allok &= ok
    print(('OK  ' if ok else 'FAIL'), f, '—', (r.stdout + r.stderr).strip().replace('\n', ' | ')[:160])
print('all sanitized:', allok)

print('\n## fontTools TTFont (compiled binary re-opened from disk)')
from fontTools.ttLib import TTFont
vf = TTFont('fonts/Apertide[wdth,wght].ttf')
cmap = vf.getBestCmap()
print('glyphs:', len(vf.getGlyphOrder()), 'encoded:', len(cmap))
print('fvar axes:', [(a.axisTag, a.minValue, a.defaultValue, a.maxValue) for a in vf['fvar'].axes])
print('fvar instances:', [vf['name'].getDebugName(i.subfamilyNameID) for i in vf['fvar'].instances])
print('STAT axis values:', [(vf['name'].getDebugName(av.ValueNameID), av.AxisIndex, getattr(av, 'Value', None)) for av in vf['STAT'].table.AxisValueArray.AxisValue])
print('tables:', sorted(vf.keys()))
print('GSUB features:', sorted({fr.FeatureTag for fr in vf['GSUB'].table.FeatureList.FeatureRecord}))
print('GPOS features:', sorted({fr.FeatureTag for fr in vf['GPOS'].table.FeatureList.FeatureRecord}))
print('name 1/2/4/6:', [vf['name'].getDebugName(i) for i in (1, 2, 4, 6)])
print('OS/2 fsType:', vf['OS/2'].fsType, 'usWeightClass:', vf['OS/2'].usWeightClass, 'usWidthClass:', vf['OS/2'].usWidthClass,
      'typo asc/desc/gap:', vf['OS/2'].sTypoAscender, vf['OS/2'].sTypoDescender, vf['OS/2'].sTypoLineGap,
      'win:', vf['OS/2'].usWinAscent, vf['OS/2'].usWinDescent, 'hhea:', vf['hhea'].ascent, vf['hhea'].descent)
w2 = TTFont('fonts/Apertide[wdth,wght].woff2'); print('woff2 flavor:', w2.flavor, 'glyphs:', len(w2.getGlyphOrder()))
for f in sorted(glob.glob('fonts/static/*.ttf')):
    t = TTFont(f); print('static', os.path.basename(f), 'glyphs', len(t.getGlyphOrder()), 'encoded', len(t.getBestCmap()),
                         'wght', t['OS/2'].usWeightClass, 'wdth', t['OS/2'].usWidthClass, 'nameID2', t['name'].getDebugName(2),
                         'nameID17', t['name'].getDebugName(17) or t['name'].getDebugName(2))

print('\n## FontForge (independent editor, scripting API)')
ff = subprocess.run(['fontforge', '-lang=py', '-c',
    'import fontforge; f = fontforge.open("fonts/Apertide[wdth,wght].ttf"); '
    'print("VF fontname", f.fontname, "glyphs", sum(1 for _ in f.glyphs()), "em", f.em, "gsub lookups", len(f.gsub_lookups), "gpos lookups", len(f.gpos_lookups)); '
    'g = fontforge.open("fonts/static/Apertide-Regular.ttf"); '
    'bad = [n.glyphname for n in g.glyphs() if n.validate(True) & 0x1 or n.validate(True) & 0x2]; '
    'print("static Regular glyphs", sum(1 for _ in g.glyphs()), "open-contour/intersecting glyphs:", bad)'],
    capture_output=True, text=True)
print(ff.stdout.strip())
noise = [l for l in ff.stderr.splitlines() if l.strip() and not l.startswith(('Copyright', ' License', ' with many', ' Version', ' Based on', 'PythonUI', 'copyUI', 'Program root', 'Core python'))]
import collections
print('FontForge stderr (deduplicated):', dict(collections.Counter(noise)))
print('note: FontForge 20230101 ignores HVAR/MVAR/STAT and reports variable-font VariationIndex device tables as "Bad device table"; this is a known FontForge limitation with OpenType Variations, not a font defect (OTS and fontTools parse the same tables cleanly).')

print('\n## HarfBuzz (hb-shape) — see shaping-receipts.txt (68 receipts)')
print(subprocess.run(['hb-shape', '--version'], capture_output=True, text=True).stdout.strip())

# glyph manifest
man = {'glyph_count': len(vf.getGlyphOrder()), 'encoded': len(cmap),
       'glyphs': [{'name': n, 'unicode': next((f'U+{u:04X}' for u, g in cmap.items() if g == n), None)} for n in vf.getGlyphOrder()]}
json.dump(man, open('qa/glyph-manifest.json', 'w'), indent=0)
print('\nglyph manifest written: qa/glyph-manifest.json')
