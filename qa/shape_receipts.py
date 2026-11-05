"""HarfBuzz shaping receipts for Apertide. Runs hb-shape (independent shaper) against the
compiled variable font and records raw output plus pass/fail for each expectation.
Usage: python3 qa/shape_receipts.py  (from builds/A4-letterform)"""
import json, os, subprocess, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
VF = os.path.join(ROOT, 'fonts', 'Apertide[wdth,wght].ttf')
ENV = dict(os.environ, LC_ALL='C.UTF-8')

def shape(text, *args):
    cmd = ['hb-shape', VF, f'--text={text}', *args]
    out = subprocess.run(cmd, capture_output=True, text=True, env=ENV, check=True).stdout.strip()
    return ' '.join(cmd[1:]).replace(ROOT + '/', ''), out

def glyphs(out):
    return [tok.split('=')[0].split('@')[0] for tok in out.strip('[]').split('|')]

def advances(out):
    res = []
    for tok in out.strip('[]').split('|'):
        name, rest = tok.split('=', 1)
        adv = rest.split('+')[-1]
        res.append(int(adv.split(',')[0]))
    return res

receipts = []
def rec(title, text, expect_fn, *args):
    cmd, out = shape(text, *args)
    ok = bool(expect_fn(out))
    receipts.append({'title': title, 'text': text, 'command': 'hb-shape ' + cmd, 'output': out, 'pass': ok})
    print(('PASS' if ok else 'FAIL'), title); 
    if not ok: print('   ', out)

# --- ligatures
rec('liga default on: fi fl ff ffi ffl', 'fi fl ff ffi ffl', lambda o: all(g in glyphs(o) for g in ('f_i','f_l','f_f','f_f_i','f_f_l')))
rec('liga off (-liga): no ligature glyphs', 'fi fl ff ffi ffl', lambda o: not any(g.startswith('f_') for g in glyphs(o)), '--features=-liga')
rec('liga in words: office affinity -> two ffi ligatures', 'office affinity', lambda o: glyphs(o).count('f_f_i') == 2)
rec('Turkish language: no fi ligature (dotted i)', 'fi', lambda o: glyphs(o) == ['f', 'i'], '--language=tr')
rec('Turkish language: fl still ligates', 'fl', lambda o: glyphs(o) == ['f_l'], '--language=tr')
# --- kerning
rec('kern on: AV tighter than default advance', 'AV', lambda o: advances(o)[0] < advances(shape('A')[1])[0])
rec('kern off (-kern): A keeps its default advance', 'AV', lambda o: advances(o)[0] == advances(shape('A')[1])[0], '--features=-kern')
rec('kern pairs: AVATAR WAVY To Ta Yo', 'AVATAR WAVY To Ta Yo', lambda o: sum(1 for a, b in zip(advances(o), advances(shape('AVATAR WAVY To Ta Yo', '--features=-kern')[1])) if a != b) >= 8)
rec('kern: quote pairs L\u2019A', 'L\u2019A', lambda o: advances(o) != advances(shape('L\u2019A', '--features=-kern')[1]))
rec('kern: r before round letters (rg ro ra) tighter than unkerned', 'rg ro ra', lambda o: all(a < b for a, b in zip(advances(o)[0::3], advances(shape('rg ro ra', '--features=-kern')[1])[0::3])))
rec('kern: F before lowercase (Fo Fa Fs) tighter than unkerned', 'Fo Fa Fs', lambda o: all(a < b for a, b in zip(advances(o)[0::3], advances(shape('Fo Fa Fs', '--features=-kern')[1])[0::3])))
rec('kern at heavy condensed (wght 800, wdth 75): Apertide pairs r-t kerned', 'Apertide', lambda o: advances(o)[3] < advances(shape('Apertide', '--features=-kern', '--variations=wght=800,wdth=75')[1])[3], '--variations=wght=800,wdth=75')
# --- figures
rec('default figures are proportional (unequal widths)', '0123456789', lambda o: len(set(advances(o))) > 1)
rec('tnum: all figures share one width', '0123456789', lambda o: len(set(advances(o))) == 1 and all(g.endswith('.tf') for g in glyphs(o)), '--features=tnum')
rec('pnum explicit: proportional glyphs', '0123456789', lambda o: not any(g.endswith('.tf') for g in glyphs(o)), '--features=pnum')
rec('zero: slashed zero', '0', lambda o: glyphs(o) == ['zero.zero'], '--features=zero')
rec('zero + tnum: tabular slashed zero', '10', lambda o: glyphs(o) == ['one.tf', 'zero.tf.zero'], '--features=zero,tnum')
# --- fractions
rec('frac: 1/2 3/4 7/8', '1/2 3/4 7/8', lambda o: glyphs(o)[:3] == ['one.numr', 'fraction', 'two.dnom'] and 'seven.numr' in glyphs(o) and 'eight.dnom' in glyphs(o), '--features=frac')
rec('frac: 3-digit numerator and denominator 125/1000', '125/1000', lambda o: glyphs(o) == ['one.numr','two.numr','five.numr','fraction','one.dnom','zero.dnom','zero.dnom','zero.dnom'], '--features=frac')
rec('frac off: plain figures and slash', '1/2', lambda o: glyphs(o) == ['one', 'slash', 'two'])
rec('frac: slash between letters stays a slash (a/b)', 'a/b', lambda o: glyphs(o) == ['a', 'slash', 'b'], '--features=frac')
rec('frac: trailing slash without denominator unchanged (1/)', '1/', lambda o: glyphs(o) == ['one', 'slash'], '--features=frac')
rec('frac + tnum compose: 1/2 from tabular figures', '1/2', lambda o: glyphs(o) == ['one.numr', 'fraction', 'two.dnom'], '--features=tnum,frac')
rec('frac: chained 12/34/56 shapes consistently', '12/34/56', lambda o: glyphs(o) == ['one.numr','two.numr','fraction','three.dnom','four.dnom','fraction','five.dnom','six.dnom'], '--features=frac')
rec('sups + tnum compose', '12', lambda o: glyphs(o) == ['onesuperior', 'twosuperior'], '--features=tnum,sups')
rec('ordn + tnum compose', '1a', lambda o: glyphs(o) == ['one.tf', 'ordfeminine'], '--features=tnum,ordn')
rec('numr / dnom explicit', '12', lambda o: glyphs(o) == ['one.numr', 'two.numr'], '--features=numr')
rec('sups: superior figures', '123', lambda o: glyphs(o) == ['onesuperior', 'twosuperior', 'threesuperior'], '--features=sups')
rec('subs: inferior figures', '123', lambda o: glyphs(o) == ['oneinferior', 'twoinferior', 'threeinferior'], '--features=subs')
rec('ordn: 1a 2o ordinals', '1a 2o', lambda o: 'ordfeminine' in glyphs(o) and 'ordmasculine' in glyphs(o), '--features=ordn')
# --- case
rec('case: punctuation shifts to cap variants', '(H)-[A]\u00a1\u00bf', lambda o: all(g.endswith('.case') for g in glyphs(o) if g not in ('H', 'A')), '--features=case')
rec('case off: default punctuation', '(H)-', lambda o: not any(g.endswith('.case') for g in glyphs(o)))
# --- marks
def mark_attached(o):
    gs = glyphs(o); toks = o.strip('[]').split('|')
    return 'acutecomb' in gs and '@' in toks[gs.index('acutecomb')] and advances(o)[gs.index('acutecomb')] == 0
rec('mark: x + combining acute (no precomposed form) positions with zero advance and an offset', 'x\u0301', mark_attached)
rec('mark: B + combining grave uses the .case grave', 'B\u0300', lambda o: 'gravecomb.case' in glyphs(o) and advances(o)[-1] == 0)
rec('mark: cap A + combining ring uses .case mark', 'A\u030a', lambda o: 'ringcomb.case' in glyphs(o) or 'Aring' in glyphs(o), '--features=ccmp')
rec('mark: O + combining ogonek attaches', 'O\u0328', lambda o: 'ogonekcomb' in glyphs(o) and advances(o)[-1] == 0)
rec('precomposed vs decomposed: \u00e9 == e + \u0301 width', 'e\u0301', lambda o: sum(advances(o)) == advances(shape('\u00e9')[1])[0])
# --- coverage: language corpus must not produce .notdef (gid 0)
LANGS = {
 'English': 'The quick brown fox jumps over the lazy dog.',
 'French': 'Voix ambiguë d\u2019un cœur qui, au zéphyr, préfère les jattes de kiwis. À l\u2019ombre du café. Ça va? Où? Noël, naïve, Æ, ÿ',
 'German': 'Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Große Straße. ẞ',
 'Spanish': 'El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío; añoraba a su querido cachorro. ¿Qué tal? ¡Hola!',
 'Italian': 'Pranzo d\u2019acqua fa volti sghembi. Perché città più così è',
 'Portuguese': 'Luís argüia à Júlia que «brações, fé, chá, óxido, pôr, zângão» eram palavras do português. Ação, coração',
 'Dutch': 'Pa\u2019s wijze lynx bezag vroom het fikse aquaduct. IJsselmeer ĳ',
 'Danish': 'Høj bly gom vandt fræk sexquiz på wc. Smørrebrød Æble Ørn Åse',
 'Norwegian': 'Vår sære Zulu fra badeøya spilte jo whist og quickstep i min taxi. Blåbærsyltetøy',
 'Swedish': 'Flygande bäckasiner söka hwila på mjuka tuvor. Åäö ÅÄÖ',
 'Finnish': 'Törkylempijävongahdus. Ääliö älä lyö, ööliä läikkyy. Šakki Žemaitija',
 'Icelandic': 'Kæmi ný öxi hér, ykist þjófum nú bæði víl og ádrepa. Þórður Ægir Ýr ð',
 'Polish': 'Pchnąć w tę łódź jeża lub ośm skrzyń fig. Zażółć gęślą jaźń. ĄĆĘŁŃÓŚŹŻ',
 'Czech': 'Příliš žluťoučký kůň úpěl ďábelské ódy. Ďábel ťuká Ľ ľ Ř ř Ě ě Ů ů',
 'Slovak': 'Kŕdeľ šťastných ďatľov učí pri ústí Váhu mĺkveho koňa obhrýzať kôru a žrať čerstvé mäso. Ĺ ĺ Ŕ ŕ Ô ô Ä ä',
 'Hungarian': 'Árvíztűrő tükörfúrógép. Ő ő Ű ű',
 'Romanian': 'Muzicologă în bej vând whisky și tequila, preț fix. Ă ă Â â Î î Ș ș Ț ț',
 'Turkish': 'Pijamalı hasta yağız şoföre çabucak güvendi. İstanbul ı Ğ ğ Ş ş Ç ç Ö ö Ü ü',
 'Latvian': 'Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļu vākus. Ā Č Ē Ģ Ī Ķ Ļ Ņ Š Ū Ž ģ ķ ļ ņ ŗ',
 'Lithuanian': 'Įlinkdama fechtuotojo špaga sublykčiojusi pragręžė apvalų arbūzą. Ą Č Ę Ė Į Š Ų Ū Ž ė ų ū',
 'Estonian': 'See väike mölder jõuab rongile hüpata. Õ õ Ä ä Ö ö Ü ü Š š Ž ž',
 'Catalan': 'Jove xef, porti whisky amb quinze glaçons d\u2019hidrogen, coi! Ŀ ŀ l·l Ç ç À è é í ï ò ó ú ü',
 'Welsh': 'Dŵr a thân. Ŵ ŵ Ŷ ŷ Â â Ê ê Î î Ô ô Û û Ẁ ẁ Ẃ ẃ Ẅ ẅ Ỳ ỳ',
 'Irish': 'D\u2019fhuascail Íosa Úrmhac na hÓighe Beannaithe pór Éava agus Ádhaimh. Ḃ ḃ Ċ ċ Ḋ ḋ Ḟ ḟ Ġ ġ Ṁ ṁ Ṗ ṗ Ṡ ṡ Ṫ ṫ',
 'Maltese': 'Ċ ċ Ġ ġ Ħ ħ Ż ż għandi l-ħbieb',
 'Croatian': 'Gojazni đačić s biciklom drži hmelj i finu vatu u džepu nošnje. Č č Ć ć Đ đ Š š Ž ž',
 'Punctuation & symbols': '«»‹›“”‘’„‚…–—•·©®™°§¶†‡ #%‰ $€£¥₹₽₺₩¢ +−×÷=≠<>≤≥±¬~≈ ∞∑∆√∂∏∫πΩµ◊ ←→↑↓ @&/\\|¦ ^`¨¯´¸˘˙˚˛˜˝ [](){}',
 'ASCII': ''.join(chr(c) for c in range(0x20, 0x7F)),
}
for lang, sample in LANGS.items():
    cmd, out = shape(sample, '--no-glyph-names')
    gids = [int(g.split('=')[0]) for g in out.strip('[]').split('|')]
    missing = sorted({sample[int(tok.split('=')[1].split('+')[0].split('@')[0])] for tok in out.strip('[]').split('|') if int(tok.split('=')[0]) == 0})
    ok = 0 not in gids
    receipts.append({'title': f'coverage: {lang} shapes without .notdef', 'text': sample, 'command': 'hb-shape ' + cmd,
                     'output': out if len(out) < 600 else out[:600] + ' …', 'pass': ok, 'missing': [f'U+{ord(c):04X} {unicodedata.name(c, "?")}' for c in missing]})
    print(('PASS' if ok else 'FAIL'), lang, '' if ok else missing)

# --- variations: shaping stable across the design space
for var in ('wght=200', 'wght=800,wdth=75', 'wght=600,wdth=125'):
    rec(f'liga+kern at {var}', 'office AVATAR', lambda o: 'f_f_i' in glyphs(o) and advances(o)[0] > 0, f'--variations={var}')

passed = sum(r['pass'] for r in receipts); total = len(receipts)
summary = {'font': os.path.basename(VF), 'hb_version': subprocess.run(['hb-shape', '--version'], capture_output=True, text=True).stdout.strip(),
           'passed': passed, 'total': total, 'receipts': receipts}
json.dump(summary, open(os.path.join(HERE, 'shaping-receipts.json'), 'w'), indent=1, ensure_ascii=False)
with open(os.path.join(HERE, 'shaping-receipts.txt'), 'w') as f:
    f.write(f"# Apertide shaping receipts — {summary['hb_version']} — {passed}/{total} passed\n\n")
    for r in receipts:
        f.write(f"## {'PASS' if r['pass'] else 'FAIL'} — {r['title']}\n$ {r['command']}\n{r['output']}\n")
        if r.get('missing'): f.write('missing: ' + ', '.join(r['missing']) + '\n')
        f.write('\n')
print(f'{passed}/{total} passed')
sys.exit(0 if passed == total else 1)
