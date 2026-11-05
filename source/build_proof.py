"""Proof build: UFO masters -> designspace -> variable TTF (fontmake)."""
import os, sys, json, subprocess
import ufoLib2
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor
from fontTools.pens.pointPen import SegmentToPointPen
from geometry import Design
from recipes import recipe, WIDTHS

OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/workspace/a4-scratch/proof'
os.makedirs(OUT, exist_ok=True)
MASTERS = [(wg, wd) for wg in (200, 400, 800) for wd in (75, 100, 125)]
GLYPHS = ['space', 'H', 'O', 'A', 'V', 'R', 'a', 'e', 'n', 'g', 'f', 'i', 'f_i']
UNI = {'space': 0x20, 'H': 0x48, 'O': 0x4F, 'A': 0x41, 'V': 0x56, 'R': 0x52, 'a': 0x61, 'e': 0x65, 'n': 0x6E, 'g': 0x67, 'f': 0x66, 'i': 0x69}
skeletons = {}
for wg, wd in MASTERS:
    d = Design(wg, wd)
    ufo = ufoLib2.Font()
    ufo.info.familyName = 'Apertide'; ufo.info.styleName = f'W{wg} D{wd}'
    ufo.info.unitsPerEm = 1000; ufo.info.ascender = 940; ufo.info.descender = -260
    ufo.info.xHeight = 520; ufo.info.capHeight = 700
    ufo.info.openTypeOS2TypoAscender = 940; ufo.info.openTypeOS2TypoDescender = -260; ufo.info.openTypeOS2TypoLineGap = 0
    ufo.info.openTypeHheaAscender = 940; ufo.info.openTypeHheaDescender = -260; ufo.info.openTypeHheaLineGap = 0
    ufo.info.openTypeOS2WinAscent = 1000; ufo.info.openTypeOS2WinDescent = 300
    ufo.info.openTypeOS2WeightClass = wg; ufo.info.openTypeOS2WidthClass = {75: 3, 100: 5, 125: 7}[wd]
    ufo.info.versionMajor = 1; ufo.info.versionMinor = 0
    ufo.info.copyright = 'Copyright 2026 Jeff Grimes. Private review build A4.'
    ufo.lib['public.glyphOrder'] = GLYPHS
    for name in GLYPHS:
        gd = recipe(name, d)
        gl = ufo.newGlyph(name)
        gl.width = round(gd.advance)
        if name in UNI:
            gl.unicodes = [UNI[name]]
        gd.draw(SegmentToPointPen(gl.getPointPen()))
        if (wg, wd) == (400, 100):
            skeletons[name] = {'advance': gl.width, 'strokes': gd.skeleton}
    ufo.features.text = 'feature liga { sub f i by f_i; } liga;\nfeature kern { pos A V -70; pos V A -70; pos R V -20; } kern;\n'
    ufo.save(os.path.join(OUT, f'Apertide-W{wg}D{wd}.ufo'), overwrite=True)
json.dump(skeletons, open(os.path.join(OUT, 'skeletons.json'), 'w'))
ds = DesignSpaceDocument()
ds.addAxis(AxisDescriptor(tag='wght', name='Weight', minimum=200, default=400, maximum=800))
ds.addAxis(AxisDescriptor(tag='wdth', name='Width', minimum=75, default=100, maximum=125))
for wg, wd in MASTERS:
    ds.addSource(SourceDescriptor(path=os.path.join(OUT, f'Apertide-W{wg}D{wd}.ufo'), familyName='Apertide', styleName=f'W{wg} D{wd}', location={'Weight': wg, 'Width': wd}))
ds.addInstance(InstanceDescriptor(familyName='Apertide', styleName='Regular', location={'Weight': 400, 'Width': 100}))
ds.write(os.path.join(OUT, 'Apertide.designspace'))
cmd = ['fontmake', '-m', os.path.join(OUT, 'Apertide.designspace'), '-o', 'variable', '--output-path', os.path.join(OUT, 'Apertide-VF.ttf')]
print(' '.join(cmd)); subprocess.run(cmd, check=True)
print('OK')
