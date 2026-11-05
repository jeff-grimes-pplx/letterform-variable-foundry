"""Generate specimen/index.html for Apertide. Everything visible is set in Apertide itself:
text through @font-face (the compiled static instances and the variable font), the glyph map and
the construction figure through outlines read from app/data/apertide-data.json (the same
compatible master outlines the fonts were compiled from). Print with print.mjs."""
import json, os, html, datetime
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, 'app', 'data', 'apertide-data.json')))
VF = TTFont(os.path.join(ROOT, 'fonts', 'Apertide[wdth,wght].ttf'))
GLYPH_ORDER = VF.getGlyphOrder(); CMAP = VF.getBestCmap()
REV = {}
for cp, gn in CMAP.items(): REV.setdefault(gn, []).append(cp)
DEFAULT = DATA['masters'].index([400, 100])
VERSION = VF['name'].getDebugName(5)
TODAY = datetime.date(2026, 10, 15).strftime('%-d %B %Y')

def esc(s): return html.escape(s, quote=False)

import subprocess
VF_PATH = os.path.join(ROOT, 'fonts', 'Apertide[wdth,wght].ttf')
NAMECHECK_DATE = '14 October 2026'
_wcache = {}
def text_width_em(text, wght=400, wdth=100):
    """Advance width of `text` in em, measured with hb-shape on the compiled variable font (kerning on)."""
    key = (text, wght, wdth)
    if key not in _wcache:
        out = subprocess.run(['hb-shape', VF_PATH, f'--text={text}', f'--variations=wght={wght},wdth={wdth}', '--no-glyph-names', '--no-clusters'],
                             capture_output=True, text=True, check=True, env=dict(os.environ, LC_ALL='C.UTF-8')).stdout.strip()
        adv = 0
        for tok in out.strip('[]').split('|'):
            adv += int(tok.split('+')[-1].split(',')[0])
        _wcache[key] = adv / 1000
    return _wcache[key]

def fit_pt(lines, max_pt, width_mm, wght=400, wdth=100, tracking_em=0.0, slack=0.97):
    """Largest size (<= max_pt) at which every line fits in width_mm, measured from the font."""
    avail_pt = width_mm / 25.4 * 72 * slack
    widest = max(text_width_em(l, wght, wdth) + tracking_em * len(l) for l in lines)
    return round(min(max_pt, avail_pt / widest), 2)

def fits(text, pt, width_mm, wght=400, wdth=100, slack=0.97):
    return text_width_em(text, wght, wdth) * pt <= width_mm / 25.4 * 72 * slack

PAGE_W = 178.0   # mm, inside the 16 mm margins

def glyph_path(name, mi=DEFAULT, dx=0.0, dy=0.0):
    g = DATA['glyphs'][name]
    if 'cmds' in g:
        pts = g['pts'][mi]; out = []; i = 0
        for c in g['cmds']:
            if c == 'M' or c == 'L':
                out.append(f'{c}{pts[i]+dx:.1f} {pts[i+1]+dy:.1f}'); i += 2
            elif c == 'C':
                out.append('C' + ' '.join(f'{pts[i+k]+dx:.1f} {pts[i+k+1]+dy:.1f}' for k in (0, 2, 4))); i += 6
            else:
                out.append('Z')
        return ''.join(out)
    return ''.join(glyph_path(cn, mi, dx + off[mi][0], dy + off[mi][1]) for cn, off in g['components'])

def skeleton_paths(name, mi=DEFAULT):
    out = []
    for st in DATA['skeletons'].get(name, []):
        pts = st['pts'][mi]; d = []; i = 0
        for c in st['cmds']:
            if c in 'ML': d.append(f'{c}{pts[i]:.1f} {pts[i+1]:.1f}'); i += 2
            elif c == 'C': d.append('C' + ' '.join(f'{pts[i+k]:.1f} {pts[i+k+1]:.1f}' for k in (0, 2, 4))); i += 6
            else: d.append('Z')
        out.append((''.join(d), st['kind'], st['s'][mi]))
    return out

def glyph_svg(name, size_css, mi=DEFAULT, cls='g'):
    adv = DATA['glyphs'][name]['adv'][mi]; w = max(adv, 320) + 160
    return (f'<svg class="{cls}" viewBox="{-(w-adv)/2:.0f} -1000 {w:.0f} 1300" style="height:{size_css}" aria-label="{esc(name)}">'
            f'<g transform="scale(1,-1)"><path d="{glyph_path(name, mi)}"/></g></svg>')

def construction_figure(names=('a', 'g', 'R', 'ampersand'), mi=DEFAULT):
    cells = []
    for n in names:
        adv = DATA['glyphs'][n]['adv'][mi]; w = adv + 240
        sk = ''.join(
            (f'<circle cx="{d[1:].split(" ")[0]}" cy="{d[1:].split(" ")[1]}" r="{s/2:.1f}" class="sk-dot"/>' if kind == 'dot'
             else f'<path d="{d}" class="sk"/>') for d, kind, s in skeleton_paths(n, mi))
        nodes = ''.join(f'<circle cx="{x}" cy="{y}" r="7" class="node"/>' for x, y in skeleton_nodes(n, mi))
        cells.append(f'<svg viewBox="-120 -1000 {w} 1300" class="cons"><g transform="scale(1,-1)">'
                     f'<path d="{glyph_path(n, mi)}" class="outline"/>{sk}{nodes}</g></svg>')
    return ''.join(cells)

def skeleton_nodes(name, mi=DEFAULT):
    pts = []
    for d, kind, s in skeleton_paths(name, mi):
        if kind == 'dot': continue
        import re
        for m in re.finditer(r'([MLC])([^MLCZ]*)', d):
            nums = re.findall(r'-?\d+\.?\d*', m.group(2))
            if m.group(1) == 'C': pts.append((nums[4], nums[5]))
            else: pts.append((nums[0], nums[1]))
    return pts

# ------------------------------------------------------------------ content
INSTANCES = [('ExtraLight', 200, 100), ('Light', 300, 100), ('Regular', 400, 100), ('Medium', 500, 100), ('SemiBold', 600, 100),
             ('Bold', 700, 100), ('ExtraBold', 800, 100), ('Condensed ExtraLight', 200, 75), ('Condensed Regular', 400, 75),
             ('Condensed Bold', 700, 75), ('Condensed ExtraBold', 800, 75), ('Extended ExtraLight', 200, 125),
             ('Extended Regular', 400, 125), ('Extended Bold', 700, 125), ('Extended ExtraBold', 800, 125)]

LANGS = [
 ('Français', 'Voix ambiguë d’un cœur qui, au zéphyr, préfère les jattes de kiwis. À l’ombre du café, Noël paraît naïf; où est l’île?'),
 ('Deutsch', 'Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Die Große Straße führt über die Brücke zum Schloß.'),
 ('Español', 'El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío; añoraba a su querido cachorro. ¿Qué tal? ¡Vaya!'),
 ('Português', 'Luís argüia à Júlia que «brações, fé, chá, óxido, pôr, zângão» eram palavras do português. Ação e coração.'),
 ('Italiano', 'Pranzo d’acqua fa volti sghembi. Perché la città è più così: caffè, virtù, lunedì, però.'),
 ('Nederlands', 'Pa’s wijze lynx bezag vroom het fikse aquaduct. Het IJsselmeer ligt vlak bij de dijk.'),
 ('Dansk / Norsk', 'Høj bly gom vandt fræk sexquiz på wc. Smørrebrød med æble, ørred og blåbærsyltetøy.'),
 ('Svenska / Suomi', 'Flygande bäckasiner söka hwila på mjuka tuvor. Törkylempijävongahdus — ääliö, älä lyö, ööliä läikkyy.'),
 ('Íslenska', 'Kæmi ný öxi hér, ykist þjófum nú bæði víl og ádrepa. Þórður, Ægir, Ýr og Ðe.'),
 ('Polski', 'Pchnąć w tę łódź jeża lub ośm skrzyń fig. Zażółć gęślą jaźń — ĄĆĘŁŃÓŚŹŻ.'),
 ('Čeština / Slovenčina', 'Příliš žluťoučký kůň úpěl ďábelské ódy. Kŕdeľ šťastných ďatľov učí koňa obhrýzať kôru.'),
 ('Magyar', 'Árvíztűrő tükörfúrógép. Őszi ősz, űrhajó, hűvös tűz.'),
 ('Română', 'Muzicologă în bej vând whisky și tequila, preț fix. Ştiinţă, înţelegere, șoaptă.'),
 ('Türkçe', 'Pijamalı hasta yağız şoföre çabucak güvendi. İstanbul’da ılık bir akşam: Ğğ Şş Çç Öö Üü.'),
 ('Latviešu / Lietuvių', 'Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļu vākus. Įlinkdama fechtuotojo špaga pragręžė arbūzą.'),
 ('Gaeilge / Cymraeg', 'D’fhuascail Íosa Úrmhac na hÓighe Beannaithe pór Éava agus Ádhaimh. Dŵr a thân, ŵy a ŷd — Ḃ ḃ Ċ ċ Ḋ ḋ Ḟ ḟ Ṁ ṁ Ṗ ṗ Ṡ ṡ Ṫ ṫ.'),
 ('Català / Malti', 'Jove xef, porti whisky amb quinze glaçons d’hidrogen, coi! Il·lustre col·lecció. Ċ ċ Ġ ġ Ħ ħ Ż ż — għandi l-ħbieb.'),
 ('Hrvatski / Eesti', 'Gojazni đačić s biciklom drži hmelj i finu vatu u džepu nošnje. See väike mölder jõuab rongile hüpata.'),
]

PANGRAMS = [
 (400, 100, 'Quiet forms, vivid voices.'),
 (300, 100, 'Sphinx of black quartz, judge my vow.'),
 (700, 100, 'Pack my box with five dozen liquor jugs.'),
 (200, 125, 'How vexingly quick daft zebras jump!'),
 (800, 75, 'The five boxing wizards jump quickly.'),
 (500, 100, 'Jackdaws love my big sphinx of quartz.'),
 (600, 75, 'Crazy Frederick bought many very exquisite opal jewels.'),
 (400, 125, 'Waltz, bad nymph, for quick jigs vex.'),
 (800, 100, 'Mr Jock, TV quiz PhD, bags few lynx.'),
 (200, 100, 'Grumpy wizards make toxic brew for the evil queen and jack.'),
 (700, 75, 'Few quips galvanized the mock jury box.'),
 (600, 125, 'Big fjords vex quick waltz nymph.'),
]

TEXT_A = ('A typeface is a set of decisions made once and repeated ten thousand times. Apertide starts from numerical '
          'centerlines rather than drawn contours: every stem, bowl and terminal is a stroke along a skeleton whose '
          'width, nib and terminal angle are parameters. The nine masters at the corners and midpoints of the weight '
          'and width axes are generated from the same recipes, so their points correspond and the variable font '
          'interpolates cleanly between them.')
TEXT_B = ('The curves are not circles. Round forms lean on unequal corner tension so that the counters open toward the '
          'right, and every terminal is cut on one shallow diagonal. Horizontal strokes are lighter than vertical ones, '
          'and diagonals are compensated separately so that A, V, W, X and Y hold the same colour as the stems '
          'around them. Marks follow the width axis and lighten as the weight grows.')
TEXT_C = ('Width is a change of skeleton, not a stretch. The condensed masters move stems closer together and shorten '
          'the arches while the stroke stays the same thickness; the extended masters widen the bowls and lengthen '
          'the crossbars. Advance widths and sidebearings follow the skeleton so that spacing stays even across the '
          'design space, and class kerning is inherited by accented letters.')

FEATURE_DEMOS = [
 ('Standard ligatures', 'liga', 'affinity office film flora', 'liga off', 'liga on (default)'),
 ('Kerning', 'kern', 'AVATAR WAVY To Ta Yo L’A', 'kern off', 'kern on (default)'),
 ('Contextual fractions', 'frac', '1/2 3/4 7/8 125/1000', 'frac off', 'frac on'),
 ('Case-sensitive forms', 'case', '(H)-[A]¡HOLA!¿QUÉ?', 'case off', 'case on'),
 ('Slashed zero', 'zero', '0.001 10 2026', 'zero off', 'zero on'),
]

def feature_rows():
    rows = []
    for title, tag, sample, off_label, on_label in FEATURE_DEMOS:
        off = f"'{tag}' 0"
        on = f"'{tag}' 1"
        rows.append(f'''<div class="feat"><div class="feat-h">{esc(title)} <span class="tag">{tag}</span></div>
          <div class="feat-pair"><div><div class="lab">{esc(off_label)}</div><div class="feat-s" style="font-feature-settings:{off}">{esc(sample)}</div></div>
          <div><div class="lab">{esc(on_label)}</div><div class="feat-s" style="font-feature-settings:{on}">{esc(sample)}</div></div></div></div>''')
    return ''.join(rows)

def glyph_map_pages():
    cols, rows = 14, 14; per = cols * rows; pages = []   # 196 cells a page: 548 glyphs fill three pages
    names = GLYPH_ORDER
    for p in range(0, len(names), per):
        chunk = names[p:p+per]; cells = []
        for n in chunk:
            cps = REV.get(n, []); label = ' '.join(f'U+{cp:04X}' for cp in cps) if cps else '—'
            cu = 'cu cu2' if len(cps) > 1 else 'cu'   # Ω carries two codepoints: smaller label so both fit the cell
            stem = n.split('.')[0]; cn = 'cn long' if len(stem) > 13 else 'cn'   # break suffixed names at the dot, shrink the longest stems
            cells.append(f'<div class="cell">{glyph_svg(n, "8.2mm")}<div class="{cn}">{esc(n).replace(".", "<wbr>.").replace("comb", "<wbr>comb")}</div><div class="{cu}">{label}</div></div>')
        pages.append((chunk[0], chunk[-1], ''.join(cells)))
    return pages

def axis_grid():
    cells = []
    for wd in (75, 100, 125):
        for wg in (200, 400, 800):
            cells.append(f'<div class="ag"><div class="ag-g" style="font-variation-settings:\'wght\' {wg},\'wdth\' {wd}">Rg</div><div class="lab" style="white-space:nowrap">{wg} / {wd}</div></div>')
    return ''.join(cells)

def page(cls, body, folio):
    return f'<section class="page {cls}">{body}<div class="folio"><span>Apertide — type specimen</span><span>{folio}</span></div></section>\n'

ACC_UPPER = ['ÀÁÂÃÄÅĀĂĄÆÇĆĈĊČĎĐÈÉÊËĒĔĖĘĚ', 'ĜĞĠĢĤĦÌÍÎÏĨĪĬĮİĲĴĶĹĻĽĿŁÑŃŅŇŊ', 'ÒÓÔÕÖØŌŎŐŒŔŖŘŚŜŞŠȘŢŤŦȚÙÚÛÜ', 'ŨŪŬŮŰŲŴÝŶŸŹŻŽÞÐẞ']
ACC_LOWER = ['àáâãäåāăąæçćĉċčďđèéêëēĕėęě', 'ĝğġģĥħìíîïĩīĭįıĳĵķĸĺļľŀłñńņňŉŋ', 'òóôõöøōŏőœŕŗřśŝşšșţťŧțùúûü', 'ũūŭůűųŵýÿŷźżžþðßſ']

def build():
    enc = len(CMAP); total = len(GLYPH_ORDER)
    pages = []
    acc_pt = fit_pt(ACC_UPPER + ACC_LOWER, 18.5, PAGE_W, tracking_em=0.03)
    # 1 cover. Languages = English (the text pages) + the languages named on the language-coverage page; a block
    # that pairs two languages ("Dansk / Norsk") counts both. All of them shape without .notdef (qa/shaping-receipts.txt).
    n_langs = 1 + sum(1 + l.count('/') for l, _ in LANGS)
    cover_lines = ''.join(f'<div class="cover-line" style="font-variation-settings:\'wght\' {w},\'wdth\' 100">Apertide</div>' for w in (200, 300, 400, 500, 600, 700, 800))
    pages.append(page('cover', f'''
      <div class="cover-top"><span>Type specimen</span><span>Variable · wght 200–800 · wdth 75–125</span><span>{TODAY}</span></div>
      <div class="cover-lines">{cover_lines}</div>
      <div class="cover-foot">
        <div><div class="lab">Family</div><div class="big">Apertide</div></div>
        <div><div class="lab">Glyphs</div><div class="big">{total}</div></div>
        <div><div class="lab">Characters</div><div class="big">{enc}</div></div>
        <div><div class="lab">Instances</div><div class="big">{len(INSTANCES)}</div></div>
        <div><div class="lab">Masters</div><div class="big">{len(DATA['masters'])}</div></div>
        <div><div class="lab">Languages</div><div class="big">{n_langs}</div></div>
      </div>''', '1'))
    # 2 concept + construction
    pages.append(page('concept', f'''
      <h1>An upright sans drawn from skeletons</h1>
      <div class="cols2"><p>{esc(TEXT_A)}</p><p>{esc(TEXT_B)}</p><p>{esc(TEXT_C)}</p>
      <p>The identifying forms are the double-storey a, the open-tailed single-storey g, the low-bar A, the folded leg of R, the clipped aperture of e and the squared dots. Apertide is a display and editorial face; text sizes are shown on page 11 for judgement.</p></div>
      <div class="cons-row">{construction_figure()}</div>
      <div class="caption"><span class="sw sk-c"></span> source skeleton (centerline and stroke nodes) &nbsp; <span class="sw ol-c"></span> compiled outline — Regular 400 / 100</div>
      <div class="cons-row cons-row2">{construction_figure(mi=DATA['masters'].index([800, 75]))}</div>
      <div class="caption">The same four recipes at the Condensed ExtraBold master, 800 / 75: the skeleton moves and the nib changes while the point structure stays compatible.</div>''', '2'))
    # 3 character set regular
    pages.append(page('charset', f'''
      <div class="lab">Regular · 400 / 100</div>
      <div class="alpha">ABCDEFGHIJKLM<br>NOPQRSTUVWXYZ</div>
      <div class="alpha">abcdefghijklm<br>nopqrstuvwxyz</div>
      <div class="alpha figs"><span class="figrow">0123456789<span class="lab">proportional</span></span> <span class="figrow" style="font-feature-settings:'tnum' 1">0123456789<span class="lab">tabular</span></span></div>
      <div class="punct">! ¡ ? ¿ . , : ; … · • ' " ‘ ’ “ ” „ ‚ « » ‹ › - – — _ ( ) [ ] {{ }} / &#92; | ¦ @ &amp; § ¶ † ‡ * # % ‰ ° ^ ~ © ® ™</div>
      <div class="punct">$ ¢ £ ¥ € ₹ ₺ ₽ ₩ ¤ + − × ÷ = ≠ &lt; &gt; ≤ ≥ ± ¬ √ ∞ ∑ ∆ ∂ ∏ ∫ π Ω µ ◊ ← ↑ → ↓ ¼ ½ ¾ ¹ ² ³ ª º</div>
      <div class="punct accents" style="font-size:{acc_pt}pt">{"<br>".join(ACC_UPPER)}</div>
      <div class="punct accents" style="font-size:{acc_pt}pt">{"<br>".join(ACC_LOWER)}</div>
''', '3'))
    # 4 alphabets in seven instances, distributed over the page
    alphas = ''
    ALPHA_LINES = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789 &?!§@']
    for name, wg, wd in (('ExtraLight', 200, 100), ('Regular', 400, 100), ('Medium', 500, 100), ('Bold', 700, 100), ('Condensed Regular', 400, 75), ('Condensed ExtraBold', 800, 75), ('Extended ExtraLight', 200, 125)):
        pt = fit_pt(ALPHA_LINES, 26, PAGE_W, wght=wg, wdth=wd)
        alphas += f'''<div class="alpha-block"><div class="lab">{name} · {wg} / {wd}</div>
          <div class="alpha-s" style="font-weight:{wg};font-stretch:{wd}%;font-size:{pt}pt">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 &amp;?!§@</div></div>'''
    pages.append(page('alphas', alphas, '4'))
    # 5 instances
    inst = ''.join(f'<div class="inst"><span style="font-weight:{wg};font-stretch:{wd}%">Apertide {name}</span><span class="lab">wght {wg} · wdth {wd}</span></div>' for name, wg, wd in INSTANCES)
    pages.append(page('instances', f'<div class="lab">Fifteen named instances, each set in its own static font</div>{inst}', '5'))
    # 6 waterfall
    def wf_text(sz):
        for t in ('Quiet forms, vivid voices — Sphinx of black quartz, judge my vow', 'Quiet forms, vivid voices — judge my vow',
                  'Quiet forms, vivid voices.', 'Quiet forms'):
            if fits(t, sz, PAGE_W - 9): return t
        return 'Quiet'
    wf = ''.join(f'<div class="wf" style="font-size:{s}pt"><span class="lab">{s}</span>{wf_text(s)}</div>' for s in (7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 28, 34, 40, 48, 56, 64, 72))
    pages.append(page('waterfall', f'<div class="lab">Waterfall · Regular</div>{wf}', '6'))
    # 7 axes
    col_w = (PAGE_W - 10) / 2 - 9   # two columns, 10 mm gap, 9 mm label gutter
    sw_pt = min(fit_pt(['Hamburgefonstiv'], 27, col_w, 800, 100), fit_pt(['Hamburgefonstiv'], 27, col_w, 400, 125))
    wsweep = ''.join(f'<div class="sweep" style="font-size:{sw_pt}pt;font-variation-settings:\'wght\' {w},\'wdth\' 100"><span class="lab">{w}</span>Hamburgefonstiv</div>' for w in (200, 275, 350, 425, 500, 575, 650, 725, 800))
    dsweep = ''.join(f'<div class="sweep" style="font-size:{sw_pt}pt;font-variation-settings:\'wght\' 400,\'wdth\' {d}"><span class="lab">{d}</span>Hamburgefonstiv</div>' for d in (75, 87.5, 100, 112.5, 125))
    WPAR = ('Width is a change of skeleton, not a stretch: the condensed masters move stems closer together and shorten '
            'the arches while the stroke keeps its thickness; the extended masters widen the bowls and lengthen the crossbars.')
    wtext = ''.join(f'<div><div class="lab">wdth {wd}</div><p style="font-variation-settings:\'wght\' 400,\'wdth\' {wd}">{esc(WPAR)}</p></div>' for wd in (75, 100, 125))
    WG = (200, 300, 400, 500, 600, 700, 800); WD = (75, 87.5, 100, 112.5, 125)
    mx_pt = fit_pt(['Quartz'], 30, (PAGE_W - 14 - 7 * 1.5) / 7 - 1.5, 800, 125)
    matrix = '<div class="mx-lab"></div>' + ''.join(f'<div class="mx-lab">wght {wg}</div>' for wg in WG)
    for wd in WD:
        matrix += f'<div class="mx-lab">wdth {wd:g}</div>' + ''.join(f'<div class="mx" style="font-size:{mx_pt}pt;font-variation-settings:\'wght\' {wg},\'wdth\' {wd}">Quartz</div>' for wg in WG)
    pages.append(page('axes', f'''
      <div class="two"><div><div class="lab">Weight axis · wght 200 → 800 at wdth 100 (variable font)</div>{wsweep}</div>
      <div><div class="lab">Width axis · wdth 75 → 125 at wght 400</div>{dsweep}<div class="lab" style="margin-top:6mm">Nine masters</div><div class="agrid">{axis_grid()}</div></div></div>
      <div class="lab" style="margin-top:8mm">Design space · seven weights × five widths, variable font instances (rows wdth, columns wght)</div><div class="matrix">{matrix}</div>
      <div class="lab" style="margin-top:7mm">Width axis in text · the same paragraph at wdth 75, 100 and 125 (Regular 9.5 / 13)</div>
      <div class="wtext">{wtext}</div>''', '7'))
    # 8 pangrams
    pg = ''.join(f'<div class="pang" style="font-weight:{wg};font-stretch:{wd}%">{esc(t)}<span class="lab">{wg} / {wd}</span></div>' for wg, wd, t in PANGRAMS)
    pages.append(page('pangrams', f'<div class="lab">Pangrams across the design space</div>{pg}', '8'))
    # 9 multilingual
    ml = ''.join(f'<div class="ml"><div class="lab">{esc(l)}</div><p>{esc(t)}</p></div>' for l, t in LANGS)
    pages.append(page('multi', f'<div class="lab">Language coverage · Regular 11 / 15 — every string below shaped without a missing glyph (HarfBuzz receipts)</div><div class="cols2 ml-cols">{ml}</div>', '9'))
    # 10 features
    figs = '<table class="figs-t"><tr><th class="lab">proportional (default)</th><th class="lab">tabular · tnum</th><th class="lab">tabular + zero</th></tr>' + ''.join(
        f'<tr><td>{r}</td><td style="font-feature-settings:\'tnum\' 1">{r}</td><td style="font-feature-settings:\'tnum\' 1,\'zero\' 1">{r}</td></tr>' for r in ('1,024.00', '7,110.35', '0,998.10', '2,026.07')) + '</table>'
    extras = f'''<div class="feat"><div class="feat-h">Figure sets <span class="tag">pnum tnum zero</span></div>{figs}</div>
      <div class="feat"><div class="feat-h">Superiors, inferiors, ordinals <span class="tag">sups subs ordn numr dnom</span></div>
      <div class="feat-s">x<span style="font-feature-settings:'sups' 1">2</span> + y<span style="font-feature-settings:'sups' 1">3</span> &nbsp; H<span style="font-feature-settings:'subs' 1">2</span>O &nbsp; CO<span style="font-feature-settings:'subs' 1">2</span> &nbsp; <span style="font-feature-settings:'ordn' 1">1a 2o 3a</span> &nbsp; <span style="font-feature-settings:'numr' 1">12</span>⁄<span style="font-feature-settings:'dnom' 1">34</span></div></div>
      <div class="feat"><div class="feat-h">Mark positioning and Turkic ligature rules <span class="tag">mark ccmp liga (language system)</span></div>
      <div class="feat-s">x&#x301; q&#x323; B&#x300; N&#x30C; w&#x308; &nbsp; a&#x301; = á &nbsp; <span lang="tr">fi fl ffi (Türkçe)</span> &nbsp; <span lang="en">fi fl ffi (English)</span></div></div>'''
    pages.append(page('features', f'<div class="lab">OpenType features · Regular 400 / 100 unless noted</div>{feature_rows()}{extras}', '10'))
    # 11 text settings
    pages.append(page('text', f'''
      <div class="lab">Text settings</div>
      <div class="txt3">
        <div><div class="lab">Light 9 / 12.5</div><p style="font-weight:300;font-size:9pt;line-height:12.5pt">{esc(TEXT_A)} {esc(TEXT_B)}</p></div>
        <div><div class="lab">Regular 10.5 / 14</div><p style="font-weight:400;font-size:10.5pt;line-height:14pt">{esc(TEXT_B)} {esc(TEXT_C)}</p></div>
        <div><div class="lab">Medium 12 / 16</div><p style="font-weight:500;font-size:12pt;line-height:16pt">{esc(TEXT_C)}</p></div>
      </div>
      <div class="head-demo" style="font-weight:800;font-stretch:75%">Condensed ExtraBold headlines</div>
      <div class="quote" style="font-weight:200;font-stretch:125%">“Extended ExtraLight at twenty points.”</div>
      <div class="txt3">
        <div><div class="lab">Condensed Regular 9.5 / 12.5</div><p style="font-weight:400;font-stretch:75%;font-size:9.5pt;line-height:12.5pt">{esc(TEXT_A)}</p></div>
        <div><div class="lab">Extended Regular 9 / 13</div><p style="font-weight:400;font-stretch:125%;font-size:9pt;line-height:13pt">{esc(TEXT_B)}</p></div>
        <div><div class="lab">Bold 9.5 / 13</div><p style="font-weight:700;font-size:9.5pt;line-height:13pt">{esc(TEXT_C)}</p></div>
      </div>''', '11'))
    # 12.. glyph map
    gm = glyph_map_pages(); folio = 12
    for i, (first, last, cells) in enumerate(gm):
        pages.append(page('glyphmap', f'<div class="lab">Glyph map {i+1} of {len(gm)} · {esc(first)} → {esc(last)} · outlines from the compiled master set, Regular 400 / 100</div><div class="grid">{cells}</div>', str(folio))); folio += 1
    # colophon
    inst_rows = ''.join(f'<tr><td>Apertide {n}</td><td>{wg}</td><td>{wd}</td><td class="mono">Apertide-{n.replace(" ", "")}.ttf</td></tr>' for n, wg, wd in INSTANCES)
    ext_b = sum(1 for cp in CMAP if 0x0180 <= cp <= 0x024F); ext_add = sum(1 for cp in CMAP if 0x1E00 <= cp <= 0x1EFF)
    pages.append(page('colophon', f'''
      <h1>Colophon</h1>
      <div class="cols2 colo">
        <div>
          <div class="lab">Metrics</div>
          <p>1000 units per em. Cap height 700, x-height 520, ascender 740, descender −210; round overshoot 12 (capitals) and 10 (lowercase). Typographic ascender 940, descender −260, line gap 0 (USE_TYPO_METRICS set); hhea 940 / −260; Windows ascent 1000, descent 400. Underline position −120, thickness 60.</p>
          <div class="lab">Axes</div>
          <p>wght 200 → 800 (default 400), wdth 75 → 125 (default 100). Nine compatible masters at weight 200 / 400 / 800 × width 75 / 100 / 125; the variable font interpolates bilinearly between them. STAT table names seven weights and three widths; Regular is elidable and linked to Bold.</p>
          <div class="lab">Repertoire</div>
          <p>{total} glyphs, {enc} encoded characters: printable ASCII, Latin-1 Supplement and Latin Extended-A complete; {ext_b} Latin Extended-B and {ext_add} Latin Extended Additional letters (those Welsh, Irish, Maltese, Romanian, Turkish and the other tested languages need, not the full blocks); combining marks with case variants and narrow forms over i and j, typographic punctuation, currency, common mathematical signs, four arrows, f-ligatures, tabular, numerator, denominator, superior and inferior figures, slashed zeros and case-sensitive punctuation. Soft hyphen is intentionally unencoded; Vietnamese stacked accents, the numero sign (U+2116) and the double arrows are out of scope for this build.</p>
          <div class="lab">Features</div>
          <p>GSUB: ccmp, liga (with Turkic exclusions for fi/ffi), tnum, pnum, zero, frac, numr, dnom, sups, subs, ordn, case. GPOS: class kerning, mark attachment. Verified with HarfBuzz 12.3.2 (68 shaping receipts), fontbakery 1.1.0 universal profile (variable font 0 FAIL / 0 WARN; statics 0 FAIL, 12 WARN on one ₩ contour-count statistic), OpenType Sanitizer 9.2.0 and FontForge 20230101.</p>
        </div>
        <div>
          <div class="lab">Named instances</div>
          <table class="inst-t"><tr><th>Instance</th><th>wght</th><th>wdth</th><th>File</th></tr>{inst_rows}</table>
          <div class="lab">Build</div>
          <p>{esc(VERSION)}. Outlines generated programmatically from original numerical skeletons (Python), compiled with fontmake 3.12.2 / ufo2ft 3.9.1 / fontTools 4.67.0; no third-party font outlines were read or traced. Specimen typeset in Apertide through its static instances and variable font, printed from Chromium; glyph map drawn from the same master outlines.</p>
          <div class="lab">Rendering note</div>
          <p>Text set through the static instances is embedded as subsetted TrueType (CID) fonts. Text set through the variable font with font-variation-settings (cover, axis sweeps, design-space matrix) is written by Chromium's PDF backend as Type 3 glyph procedures: exact outlines from the font, searchable through ToUnicode, but not an embedded copy of the font program.</p>
          <div class="lab">Status</div>
          <p>Private review build A4 for Jeff Grimes, {TODAY}. Not released; see LICENSE.txt. Family name checked against public catalogues and the fontdata name check on {NAMECHECK_DATE}; this is not trademark clearance.</p>
        </div>
      </div>''', str(folio)))
    return ''.join(pages)

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specimen.css')).read()
HTML = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Apertide — type specimen</title><style>{CSS}</style></head><body>{build()}</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'), 'w').write(HTML)
print('index.html written', len(HTML) // 1000, 'KB')
