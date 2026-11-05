"""Quick single-master font from every available recipe (letters + symbols [+ more]); renders text lines."""
import sys, os, subprocess
import ufoLib2
from ufo2ft import compileTTF
from fontTools.pens.pointPen import SegmentToPointPen
from geometry import Design
import letters, symbols
from PIL import Image

def make_font(d, path):
    ufo = ufoLib2.Font(); ufo.info.unitsPerEm = 1000; ufo.info.familyName = 'ApertidePreview'; ufo.info.styleName = 'R'
    ufo.info.ascender = 940; ufo.info.descender = -260; ufo.info.xHeight = 520; ufo.info.capHeight = 700
    for ch in letters.WIDTHS:
        gd = letters.build(ch, d); gl = ufo.newGlyph('uni%04X' % ord(ch)); gl.width = round(gd.advance); gl.unicodes = [ord(ch)]
        gd.draw(SegmentToPointPen(gl.getPointPen()))
    for name, (uni, fn) in symbols.SYMBOLS.items():
        gd = fn(d); gl = ufo.newGlyph(name); gl.width = round(gd.advance)
        if uni: gl.unicodes = [uni]
        gd.draw(SegmentToPointPen(gl.getPointPen()))
    compileTTF(ufo, removeOverlaps=True).save(path)

if __name__ == '__main__':
    wg = int(sys.argv[1]); wd = int(sys.argv[2]); texts = sys.argv[3:]
    out = '/home/user/workspace/a4-scratch/preview'; os.makedirs(out, exist_ok=True)
    path = os.path.join(out, f'all-{wg}-{wd}.ttf'); make_font(Design(wg, wd), path)
    ims = []
    for i, t in enumerate(texts):
        png = os.path.join(out, f'aline{i}.png')
        subprocess.run(['hb-view', '--font-size=96', '--margin=12', '--output-file=' + png, '--text=' + t, path], check=True)
        ims.append(Image.open(png))
    W = max(i.width for i in ims); H = sum(i.height for i in ims)
    sheet = Image.new('RGB', (W, H), 'white'); y = 0
    for im in ims:
        sheet.paste(im, (0, y)); y += im.height
    sp = os.path.join(out, f'all-{wg}-{wd}.png'); sheet.save(sp); print(sp, sheet.size)
