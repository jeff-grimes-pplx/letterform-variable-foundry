"""Fast single-master visual proof: recipes -> ufo2ft static TTF -> hb-view sheet."""
import sys, os, subprocess
import ufoLib2
from ufo2ft import compileTTF
from fontTools.pens.pointPen import SegmentToPointPen
from geometry import Design
import letters
from PIL import Image

wg = int(sys.argv[1]) if len(sys.argv) > 1 else 400
wd = int(sys.argv[2]) if len(sys.argv) > 2 else 100
texts = sys.argv[3:] or ['ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ', 'abcdefghijklm', 'nopqrstuvwxyz', '0123456789']
out = '/home/user/workspace/a4-scratch/preview'; os.makedirs(out, exist_ok=True)
d = Design(wg, wd)
ufo = ufoLib2.Font(); ufo.info.unitsPerEm = 1000; ufo.info.familyName = 'ApertidePreview'; ufo.info.styleName = 'R'
ufo.info.ascender = 940; ufo.info.descender = -260; ufo.info.xHeight = 520; ufo.info.capHeight = 700
names = {}
for ch in letters.WIDTHS:
    gd = letters.build(ch, d); name = 'uni%04X' % ord(ch); names[ch] = name
    gl = ufo.newGlyph(name); gl.width = round(gd.advance); gl.unicodes = [ord(ch)]
    gd.draw(SegmentToPointPen(gl.getPointPen()))
sp = ufo.newGlyph('space'); sp.width = 240; sp.unicodes = [32]
ttf = compileTTF(ufo, removeOverlaps=True)
path = os.path.join(out, f'prev-{wg}-{wd}.ttf'); ttf.save(path)
ims = []
for i, t in enumerate(texts):
    png = os.path.join(out, f'line{i}.png')
    subprocess.run(['hb-view', '--font-size=110', '--margin=16', '--output-file=' + png, path, t], check=True)
    ims.append(Image.open(png))
W = max(i.width for i in ims); H = sum(i.height for i in ims)
sheet = Image.new('RGB', (W, H), 'white'); y = 0
for im in ims:
    sheet.paste(im, (0, y)); y += im.height
sp = os.path.join(out, f'sheet-{wg}-{wd}.png'); sheet.save(sp); print(sp, sheet.size)
