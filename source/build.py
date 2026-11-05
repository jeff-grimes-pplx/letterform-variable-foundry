"""Build Apertide: 9 UFO masters -> designspace -> variable TTF + static instances.

    python3 build.py ufo            # write masters + designspace into ../build/
    python3 build.py quick WGHT WDTH # one master -> TTF with features (previews)
    python3 build.py fonts          # fontmake variable + statics into ../fonts/
    python3 build.py skeletons      # default-master skeleton JSON for the app
"""
import os, sys, json, subprocess, shutil
import ufoLib2
from fontTools.pens.pointPen import SegmentToPointPen
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, AxisLabelDescriptor
from geometry import Design
from glyphset import Master
import features
EXTRA_UNICODES = {'uni03A9': [0x2126]}   # Ohm sign shares the Omega glyph

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(ROOT, 'build'); FONTS = os.path.join(ROOT, 'fonts')
FAMILY = 'Apertide'
WGHTS = (200, 400, 800); WDTHS = (75, 100, 125)
VERSION = (1, 103)   # name ID 5 "Version 1.103", head.fontRevision 1.103
COPYRIGHT = 'Copyright 2026 Jeff Grimes. Private review build A4.'

WEIGHT_NAMES = {200: 'ExtraLight', 300: 'Light', 400: 'Regular', 500: 'Medium', 600: 'SemiBold', 700: 'Bold', 800: 'ExtraBold'}
WIDTH_NAMES = {75: 'Condensed', 100: '', 125: 'Extended'}
WIDTH_CLASS = {75: 3, 100: 5, 125: 7}


def style_name(wght, wdth):
    w = WEIGHT_NAMES[wght]; n = WIDTH_NAMES[wdth]
    return (n + ' ' + w).strip() if n else w


def make_ufo(wght, wdth):
    d = Design(wght, wdth); m = Master(d)
    ufo = ufoLib2.Font()
    info = ufo.info
    info.familyName = FAMILY; info.styleName = style_name(wght, wdth)
    info.unitsPerEm = 1000; info.ascender = 940; info.descender = -260; info.xHeight = 520; info.capHeight = 700
    info.italicAngle = 0
    info.versionMajor, info.versionMinor = VERSION
    info.copyright = COPYRIGHT
    info.openTypeNameDesigner = 'Jeff Grimes (programmatic design, Perplexity Computer build A4)'
    info.openTypeNameManufacturer = 'A4 Letterform'
    info.openTypeNameLicense = 'Private review build. All rights reserved. See LICENSE.txt in the build folder.'
    info.openTypeNameDescription = 'Apertide: an upright variable sans with blade terminals, drawn programmatically from skeletons.'
    info.openTypeOS2WeightClass = wght; info.openTypeOS2WidthClass = WIDTH_CLASS[wdth]
    info.openTypeOS2TypoAscender = 940; info.openTypeOS2TypoDescender = -260; info.openTypeOS2TypoLineGap = 0
    info.openTypeHheaAscender = 940; info.openTypeHheaDescender = -260; info.openTypeHheaLineGap = 0
    info.openTypeOS2WinAscent = 1000; info.openTypeOS2WinDescent = 400   # covers the lowest glyph (dot below y, -385)
    info.openTypeOS2Selection = [7, 8]   # USE_TYPO_METRICS, WWS
    info.openTypeOS2Type = []            # installable embedding
    info.openTypeOS2VendorID = 'A4LF'
    info.openTypeOS2Panose = [2, 11, 5, 3, 3, 4, 2, 2, 2, 4]
    info.openTypeOS2SubscriptXSize = 600; info.openTypeOS2SubscriptYSize = 600; info.openTypeOS2SubscriptYOffset = 130
    info.openTypeOS2SuperscriptXSize = 600; info.openTypeOS2SuperscriptYSize = 600; info.openTypeOS2SuperscriptYOffset = 320
    info.openTypeOS2StrikeoutSize = round(d.h * 0.9); info.openTypeOS2StrikeoutPosition = 290
    info.postscriptUnderlineThickness = 60; info.postscriptUnderlinePosition = -120   # constant across the family
    info.postscriptFontName = f'{FAMILY}-{style_name(wght, wdth).replace(" ", "")}'
    info.openTypeOS2CodePageRanges = [0, 1, 2]   # Latin 1, Latin 2, Cyrillic bit intentionally absent -> set below
    info.openTypeOS2CodePageRanges = [0, 1]      # Latin 1 (1252) + Latin 2 (1250)
    info.openTypeOS2UnicodeRanges = [0, 1, 2, 3, 29, 31]  # Basic Latin, Latin-1, Ext-A, Ext-B, Ext Additional, Punctuation

    for name in m.order:
        g = ufo.newGlyph(name); g.width = m.advances[name]
        g.lib['public.truetype.overlap'] = True   # VF keeps overlapping contours: set OVERLAP_SIMPLE/COMPOUND
        if name in m.unicodes:
            g.unicodes = [m.unicodes[name]] + EXTRA_UNICODES.get(name, [])
        if name in m.outlines:
            dr = m.outlines[name]; dr.draw(SegmentToPointPen(g.getPointPen()))
            for an, (ax, ay) in dr.anchors.items():
                g.appendAnchor({'name': an, 'x': round(ax), 'y': round(ay)})
        else:
            pen = g.getPen()
            for base, dx, dy in m.components[name]:
                pen.addComponent(base, (1, 0, 0, 1, round(dx), round(dy)))
    ufo.glyphOrder = list(m.order)
    ufo.lib['public.glyphOrder'] = list(m.order)
    def category(n):
        if n in ('f_i', 'f_l', 'f_f', 'f_f_i', 'f_f_l'):
            return 'ligature'
        if n in m.outlines and any(a.startswith('_') for a in m.outlines[n].anchors):
            return 'mark'
        return 'base'
    ufo.lib['public.openTypeCategories'] = {n: category(n) for n in m.order}
    groups = features.kern_groups(set(m.order))
    for k, v in groups.items():
        ufo.groups[k] = v
    for (a, b), v in features.kerning_for(d).items():
        if a.startswith('public.kern') or b.startswith('public.kern'):
            if groups.get(a) and groups.get(b):
                ufo.kerning[(a, b)] = v
        elif a in m.order and b in m.order:
            ufo.kerning[(a, b)] = v
    ufo.features.text = features.fea_text()
    return ufo, m


def write_masters():
    os.makedirs(BUILD, exist_ok=True)
    ds = DesignSpaceDocument()
    wlabels = [AxisLabelDescriptor(name=n, userValue=v, elidable=(v == 400), linkedUserValue=(700 if v == 400 else None))
               for v, n in WEIGHT_NAMES.items()]
    ds.addAxis(AxisDescriptor(tag='wght', name='Weight', minimum=200, default=400, maximum=800, axisLabels=wlabels))
    dlabels = [AxisLabelDescriptor(name='Condensed', userValue=75), AxisLabelDescriptor(name='Normal', userValue=100, elidable=True),
               AxisLabelDescriptor(name='Extended', userValue=125)]
    ds.addAxis(AxisDescriptor(tag='wdth', name='Width', minimum=75, default=100, maximum=125, axisLabels=dlabels))
    masters = {}
    for wght in WGHTS:
        for wdth in WDTHS:
            ufo, m = make_ufo(wght, wdth); masters[(wght, wdth)] = m
            path = os.path.join(BUILD, f'Apertide-{wght}-{wdth}.ufo')
            if os.path.exists(path):
                shutil.rmtree(path)
            ufo.save(path, overwrite=True)
            src = SourceDescriptor(path=path, name=f'Apertide {wght} {wdth}', familyName=FAMILY, styleName=style_name(wght, wdth),
                                   location={'Weight': wght, 'Width': wdth})
            if (wght, wdth) == (400, 100):
                src.copyLib = src.copyInfo = src.copyGroups = src.copyFeatures = True
            ds.addSource(src)
            print('master', wght, wdth, len(m.order), 'glyphs')
    # named instances
    for wdth, wn in ((100, ''), (75, 'Condensed'), (125, 'Extended')):
        for wght, sn in WEIGHT_NAMES.items():
            if wdth != 100 and wght in (300, 500, 600):
                continue
            style = (wn + ' ' + sn).strip()
            i = InstanceDescriptor(familyName=FAMILY, styleName=style, location={'Weight': wght, 'Width': wdth},
                                   postScriptFontName=f'{FAMILY}-{style.replace(" ", "")}')
            # RIBBI style mapping: Regular/Bold in the plain family, everything else its own WWS family
            if wdth == 100 and wght in (400, 700):
                i.styleMapFamilyName = FAMILY; i.styleMapStyleName = 'bold' if wght == 700 else 'regular'
            else:
                i.styleMapFamilyName = f'{FAMILY} {style}'; i.styleMapStyleName = 'regular'
            ds.addInstance(i)
    dspath = os.path.join(BUILD, 'Apertide.designspace'); ds.write(dspath)
    print('designspace', dspath, len(ds.instances), 'instances')
    return dspath, masters


def quick(wght, wdth, out):
    from ufo2ft import compileTTF
    ufo, m = make_ufo(wght, wdth)
    compileTTF(ufo, removeOverlaps=True).save(out); print(out, len(m.order))


def clean_degenerate(f):
    """Static instances: overlap removal + integer rounding leaves zero-length or sub-unit
    segments (e.g. B<<236,609>-<237,610>-<236,609>>). Rebuild each simple glyph without them."""
    from fontTools.pens.recordingPen import RecordingPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    glyf = f['glyf']; gs = f.getGlyphSet(); changed = 0

    def near(a, b):
        return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

    for name in f.getGlyphOrder():
        g = glyf[name]
        if g.isComposite() or g.numberOfContours == 0:
            continue
        rec = RecordingPen(); gs[name].draw(rec)
        pen = TTGlyphPen(gs); cur = None; start = None; buf = []; dirty = False
        for op, args in rec.value:
            if op == 'moveTo':
                cur = start = args[0]; buf = [('moveTo', args)]
            elif op == 'lineTo':
                if near(cur, args[0]):
                    dirty = True; continue
                buf.append((op, args)); cur = args[0]
            elif op == 'qCurveTo':
                end = args[-1]; offs = [p for p in args[:-1] if p is not None]
                if end is None:   # all-off-curve contour (rare); keep verbatim
                    buf.append((op, args)); continue
                if near(cur, end) and all(near(cur, p) for p in offs):
                    dirty = True; continue
                offs2 = [p for p in offs if not (near(p, cur) and near(p, end))]
                if len(offs2) != len(offs):
                    dirty = True
                if not offs2:
                    buf.append(('lineTo', (end,)))
                else:
                    buf.append((op, tuple(offs2) + (end,)))
                cur = end
            elif op == 'closePath':
                # drop a closing lineTo that returns to the start
                if len(buf) > 1 and buf[-1][0] == 'lineTo' and near(buf[-1][1][0], start):
                    buf.pop(); dirty = True
                pts = [q for bop, bargs in buf for q in bargs if q is not None]
                tiny = pts and (max(q[0] for q in pts) - min(q[0] for q in pts) < 8) and (max(q[1] for q in pts) - min(q[1] for q in pts) < 8)
                if len(buf) >= 3 and not tiny:
                    for bop, bargs in buf:
                        getattr(pen, bop)(*bargs)
                    pen.closePath()
                else:
                    dirty = True   # degenerate sliver contour (< 3 segments, or a sub-8-unit hole left by overlap removal)
                buf = []
        if dirty:
            new = pen.glyph(); new.recalcBounds(glyf); glyf[name] = new; changed += 1
    return changed


def finish(path, variable):
    """Post-compile fixes: gasp + smart-dropout prep for unhinted TrueType, identity avar,
    degenerate-segment cleanup for statics, then a WOFF2 copy for the browser tester."""
    from fontTools.ttLib import TTFont, newTable
    from gftools.fix import fix_unhinted_font
    f = TTFont(path)
    fix_unhinted_font(f)
    if not variable:
        n = clean_degenerate(f)
        if n:
            print('  cleaned degenerate segments in', n, 'glyphs of', os.path.basename(path))
    if variable and 'avar' not in f:
        avar = newTable('avar'); avar.segments = {}
        for axis in f['fvar'].axes:
            avar.segments[axis.axisTag] = {-1.0: -1.0, 0.0: 0.0, 1.0: 1.0}
        f['avar'] = avar
    f.save(path)
    if variable:
        f = TTFont(path); f.flavor = 'woff2'; f.save(path[:-4] + '.woff2')


def fonts(dspath):
    os.makedirs(FONTS, exist_ok=True)
    env = dict(os.environ); env['PATH'] = os.path.expanduser('~/.local/bin') + ':' + env['PATH']
    vf = os.path.join(FONTS, 'Apertide[wdth,wght].ttf')
    subprocess.run(['fontmake', '-m', dspath, '-o', 'variable', '--output-path', vf, '--verbose', 'WARNING'], check=True, env=env)
    finish(vf, True)
    static = os.path.join(FONTS, 'static')
    if os.path.exists(static):
        shutil.rmtree(static)
    # statics: decompose composites (so attached marks such as ogoneks merge with their base
    # during overlap removal) and remove overlaps; the variable font keeps components + overlaps
    ogonek = [n for n in Master(Design(400, 100)).components if 'ogonek' in n.lower() or n in ('Aogonek', 'aogonek')]
    subprocess.run(['fontmake', '-m', dspath, '-o', 'ttf', '-i', '--output-dir', static, '--verbose', 'WARNING',
                    '--filter', f'DecomposeComponentsFilter(pre=True, include={ogonek!r})'], check=True, env=env)
    for fn in os.listdir(static):
        clean = fn.replace(' ', '')
        os.rename(os.path.join(static, fn), os.path.join(static, clean)); finish(os.path.join(static, clean), False)
    print(sorted(os.listdir(FONTS)), sorted(os.listdir(static)))


def skeletons():
    d = Design(400, 100); m = Master(d)
    out = {}
    for name in m.order:
        if name in m.outlines:
            g = m.outlines[name]
            out[name] = {'adv': m.advances[name], 'uni': m.unicodes.get(name), 'strokes': g.skeleton}
        else:
            out[name] = {'adv': m.advances[name], 'uni': m.unicodes.get(name), 'components': m.components[name]}
    path = os.path.join(BUILD, 'skeletons.json')
    os.makedirs(BUILD, exist_ok=True)
    with open(path, 'w') as fh:
        json.dump(out, fh)
    print(path, len(out))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'ufo':
        write_masters()
    elif cmd == 'quick':
        quick(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif cmd == 'fonts':
        fonts(os.path.join(BUILD, 'Apertide.designspace'))
    elif cmd == 'skeletons':
        skeletons()
    elif cmd == 'all':
        dspath, _ = write_masters(); fonts(dspath); skeletons()
