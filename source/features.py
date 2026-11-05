"""OpenType features and kerning for Apertide. Kerning is class based; accented
letters inherit their base's class. Values are for Regular/Normal and scale with the
width factor f per master."""
from glyphset import gname, composite_plan

FIGS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def fea_text():
    figs = ' '.join(FIGS)
    f = lambda suf: ' '.join(n + suf for n in FIGS)
    caps = ' '.join(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + ['AE', 'OE', 'Oslash', 'Thorn', 'Eth', 'Dcroat', 'Hbar', 'Lslash', 'Tbar', 'Eng', 'IJ', 'uni1E9E', 'uni03A9'])
    return f"""languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK;
languagesystem latn AZE;
languagesystem latn CRT;

@figs = [{figs}];
@figs_tf = [{f('.tf')}];
@figs_numr = [{f('.numr')}];
@figs_dnom = [{f('.dnom')}];
@figs_sups = [{f('superior')}];
@figs_subs = [{f('inferior')}];

@figs_any = [@figs @figs_tf];

lookup FRAC_numr {{
  sub @figs by @figs_numr;
  sub @figs_tf by @figs_numr;
}} FRAC_numr;

lookup FRAC_dnom {{
  sub @figs by @figs_dnom;
  sub @figs_tf by @figs_dnom;
}} FRAC_dnom;

lookup FRAC_slash {{
  sub slash by fraction;
}} FRAC_slash;

# a slash becomes the fraction bar only between figures (a/b stays a/b)
lookup FRAC_slash_ctx {{
  sub @figs_any slash' lookup FRAC_slash @figs_any;
}} FRAC_slash_ctx;

# capitals (and any decomposed sequence after a capital) take the flatter .case marks
@CAPS = [{caps}];
@MARKS_LC = [gravecomb acutecomb circumflexcomb tildecomb macroncomb brevecomb dotaccentcomb dieresiscomb ringcomb hungarumlautcomb caroncomb];
@MARKS_CASE = [gravecomb.case acutecomb.case circumflexcomb.case tildecomb.case macroncomb.case brevecomb.case dotaccentcomb.case dieresiscomb.case ringcomb.case hungarumlautcomb.case caroncomb.case];

feature ccmp {{
  sub @CAPS @MARKS_LC' by @MARKS_CASE;
}} ccmp;

lookup liga_fi {{
  sub f f i by f_f_i;
  sub f i by f_i;
}} liga_fi;

lookup liga_fl {{
  sub f f l by f_f_l;
  sub f f by f_f;
  sub f l by f_l;
}} liga_fl;

# Turkic languages keep ff/fl/ffl but never swallow the dotted i into a ligature
feature liga {{
  lookup liga_fi;
  lookup liga_fl;
  script latn;
  language dflt;
  lookup liga_fi;
  lookup liga_fl;
  language TRK exclude_dflt;
  lookup liga_fl;
  language AZE exclude_dflt;
  lookup liga_fl;
  language CRT exclude_dflt;
  lookup liga_fl;
}} liga;

feature tnum {{
  sub @figs by @figs_tf;
}} tnum;

feature pnum {{
  sub @figs_tf by @figs;
}} pnum;

feature zero {{
  sub zero by zero.zero;
  sub zero.tf by zero.tf.zero;
}} zero;

# Fractions only form between figures (a/b stays a/b); up to three figures on each side.
# Tabular figures take part as well, so tnum + frac compose.
feature frac {{
  lookup FRAC_slash_ctx;
  sub fraction @figs_any' lookup FRAC_dnom;
  sub @figs_dnom @figs_any' lookup FRAC_dnom;
  sub @figs_any' lookup FRAC_numr @figs_any @figs_any fraction;
  sub @figs_any' lookup FRAC_numr @figs_any fraction;
  sub @figs_any' lookup FRAC_numr fraction;
}} frac;

feature numr {{
  sub @figs by @figs_numr;
  sub @figs_tf by @figs_numr;
}} numr;

feature dnom {{
  sub @figs by @figs_dnom;
  sub @figs_tf by @figs_dnom;
}} dnom;

feature sups {{
  sub @figs by @figs_sups;
  sub @figs_tf by @figs_sups;
}} sups;

feature subs {{
  sub @figs by @figs_subs;
  sub @figs_tf by @figs_subs;
}} subs;

feature ordn {{
  sub @figs_any a' by ordfeminine;
  sub @figs_any o' by ordmasculine;
}} ordn;

feature case {{
  sub hyphen by hyphen.case;
  sub endash by endash.case;
  sub emdash by emdash.case;
  sub parenleft by parenleft.case;
  sub parenright by parenright.case;
  sub bracketleft by bracketleft.case;
  sub bracketright by bracketright.case;
  sub braceleft by braceleft.case;
  sub braceright by braceright.case;
  sub guillemotleft by guillemotleft.case;
  sub guillemotright by guillemotright.case;
  sub guilsinglleft by guilsinglleft.case;
  sub guilsinglright by guilsinglright.case;
  sub periodcentered by periodcentered.case;
  sub bullet by bullet.case;
  sub exclamdown by exclamdown.case;
  sub questiondown by questiondown.case;
}} case;
"""


# ----------------------------------------------------------------------- kerning
# Shape classes. Left side (kern1) describes the RIGHT edge of the first glyph;
# right side (kern2) describes the LEFT edge of the second glyph.
LEFT_SEEDS = {
    'A': 'A', 'L': 'L', 'T': 'T', 'V': 'V', 'W': 'W', 'Y': 'Y', 'P': 'P', 'F': 'F', 'K': 'K', 'R': 'R', 'O': 'OQ', 'D': 'D',
    'r': 'r', 'v': 'v', 'w': 'w', 'y': 'y', 'f': 'f', 'o': 'obp', 'e': 'e', 'quote': None, 'period': None, 'seven': None,
    'E': 'E', 'B': 'B',
}
RIGHT_SEEDS = {
    'A': 'A', 'T': 'T', 'V': 'V', 'W': 'W', 'Y': 'Y', 'O': 'OCGQ', 'J': 'J',
    'o': 'ocdeqg', 'a': 'a', 's': 's', 'u': 'u', 'v': 'v', 'w': 'w', 'y': 'y', 'x': 'x', 'z': 'z', 'r': 'rnmp', 't': 't',
    'i': 'ijl', 'f': 'f', 'b': 'bhk', 'quote': None, 'period': None, 'hyphen': None, 'colon': None,
}
EXTRA_LEFT = {'quote': ['quotesingle', 'quotedbl', 'quoteright', 'quotedblright', 'quoteleft', 'quotedblleft'], 'period': ['period', 'comma', 'ellipsis', 'quotesinglbase', 'quotedblbase'],
              'seven': ['seven']}
EXTRA_RIGHT = {'quote': ['quotesingle', 'quotedbl', 'quoteright', 'quotedblright', 'quoteleft', 'quotedblleft'], 'period': ['period', 'comma', 'ellipsis', 'quotesinglbase', 'quotedblbase'],
               'hyphen': ['hyphen', 'endash', 'emdash', 'uni00AD', 'uni2010', 'uni2011'], 'colon': ['colon', 'semicolon']}

# Regular/Normal values (font units)
PAIRS = {
    ('A', 'T'): -82, ('A', 'V'): -88, ('A', 'W'): -58, ('A', 'Y'): -98, ('A', 'v'): -36, ('A', 'w'): -28, ('A', 'y'): -44, ('A', 'quote'): -110, ('A', 'O'): -18, ('A', 't'): -20,
    ('L', 'T'): -94, ('L', 'V'): -84, ('L', 'W'): -62, ('L', 'Y'): -102, ('L', 'y'): -40, ('L', 'quote'): -150, ('L', 'O'): -22, ('L', 'v'): -36, ('L', 'w'): -30,
    ('T', 'A'): -82, ('T', 'O'): -22, ('T', 'o'): -96, ('T', 'a'): -98, ('T', 's'): -84, ('T', 'u'): -72, ('T', 'r'): -66, ('T', 'y'): -62, ('T', 'w'): -62, ('T', 'v'): -62, ('T', 'z'): -60, ('T', 'x'): -56,
    ('T', 'period'): -104, ('T', 'hyphen'): -84, ('T', 'colon'): -64, ('T', 'J'): -60,
    ('V', 'A'): -88, ('V', 'a'): -64, ('V', 'o'): -62, ('V', 'u'): -40, ('V', 'r'): -40, ('V', 'y'): -24, ('V', 'period'): -112, ('V', 'hyphen'): -60, ('V', 'colon'): -40, ('V', 's'): -50,
    ('W', 'A'): -58, ('W', 'a'): -40, ('W', 'o'): -34, ('W', 'u'): -24, ('W', 'r'): -24, ('W', 'period'): -82, ('W', 'hyphen'): -40, ('W', 's'): -30,
    ('Y', 'A'): -98, ('Y', 'a'): -100, ('Y', 'o'): -94, ('Y', 'u'): -70, ('Y', 's'): -84, ('Y', 'r'): -66, ('Y', 'period'): -122, ('Y', 'hyphen'): -98, ('Y', 'colon'): -74, ('Y', 'v'): -46, ('Y', 'z'): -50, ('Y', 'x'): -50, ('Y', 'O'): -30,
    ('P', 'A'): -84, ('P', 'period'): -160, ('P', 'a'): -26, ('P', 'o'): -22, ('P', 'J'): -60,
    ('F', 'A'): -74, ('F', 'period'): -128, ('F', 'J'): -50,
    ('K', 'O'): -34, ('K', 'o'): -22, ('K', 'y'): -30, ('K', 'v'): -30, ('K', 'w'): -24,
    ('R', 'V'): -30, ('R', 'Y'): -42, ('R', 'T'): -30, ('R', 'W'): -20, ('R', 'O'): -14, ('R', 'y'): -14,
    ('O', 'A'): -20, ('O', 'V'): -30, ('O', 'T'): -24, ('O', 'Y'): -38, ('O', 'W'): -18, ('O', 'period'): -26, ('O', 'J'): -16,
    ('D', 'A'): -22, ('D', 'V'): -30, ('D', 'T'): -26, ('D', 'Y'): -40, ('D', 'W'): -18, ('D', 'period'): -28,
    # r: the hook leaves a hole under it, so round and open letters move in; stems do not
    ('r', 'period'): -84, ('r', 'a'): -34, ('r', 'o'): -40, ('r', 's'): -22, ('r', 'u'): -8, ('r', 'v'): -10, ('r', 'w'): -8, ('r', 'y'): -10,
    ('r', 't'): -22, ('r', 'z'): -12, ('r', 'x'): -8, ('r', 'hyphen'): -40, ('r', 'quote'): 16,
    # F and P: open below the bar / bowl
    ('F', 'o'): -38, ('F', 'a'): -42, ('F', 's'): -34, ('F', 'u'): -22, ('F', 'r'): -26, ('F', 'y'): -16, ('F', 'v'): -16, ('F', 'w'): -14, ('F', 'O'): -22, ('F', 'i'): -6,
    ('F', 'z'): -24, ('F', 'x'): -20, ('F', 'hyphen'): -30, ('F', 'colon'): -40,
    ('P', 's'): -16, ('P', 'u'): -8, ('P', 'y'): -8, ('P', 'hyphen'): -14, ('P', 'colon'): -40, ('P', 'O'): -10,
    ('E', 'o'): -8, ('E', 'J'): -14, ('B', 'J'): -10,
    ('T', 'i'): -8, ('V', 'i'): -6, ('W', 'i'): -4, ('Y', 'i'): -10,
    ('v', 'period'): -64, ('v', 'a'): -14, ('v', 'o'): -10, ('v', 'hyphen'): -14,
    ('w', 'period'): -54, ('w', 'o'): -8, ('w', 'a'): -10,
    ('y', 'period'): -72, ('y', 'o'): -10, ('y', 'a'): -14,
    ('f', 'period'): -24, ('f', 'quote'): 40, ('f', 'hyphen'): -20,
    ('o', 'v'): -12, ('o', 'w'): -8, ('o', 'y'): -12, ('o', 'x'): -14, ('o', 'period'): -12, ('o', 'quote'): -70,
    ('e', 'v'): -10, ('e', 'y'): -10, ('e', 'quote'): -50,
    ('quote', 'A'): -110, ('quote', 'o'): -70, ('quote', 'a'): -60, ('quote', 'J'): -40,
    ('period', 'quote'): -120, ('period', 'T'): -104, ('period', 'V'): -112, ('period', 'Y'): -122, ('period', 'W'): -82,
    ('seven', 'period'): -72, ('seven', 'hyphen'): -40,
}


def _accents_of():
    """base letter -> list of composite glyph names whose base it is."""
    out = {}
    for name, cp, base, items in composite_plan():
        out.setdefault(base, []).append(name)
    return out


def kern_groups(all_names):
    acc = _accents_of(); groups = {}
    # left classes describe a glyph's RIGHT side: Æ and Œ end in an E, so they kern like E (not like A), while on
    # their left side (right classes) Æ behaves like A and Œ like O
    SPECIAL_LEFT = {'A': [], 'E': ['AE', 'OE'], 'O': ['Oslash'], 'D': ['Eth', 'Dcroat', 'Thorn'], 'L': ['Lslash', 'Ldot'], 'T': ['Tbar'], 'o': ['oslash', 'thorn'], 'e': ['ae', 'oe'], 'f': ['f_f', 'longs'], 'r': []}
    SPECIAL_RIGHT = {'A': ['AE'], 'O': ['Oslash', 'OE'], 'o': ['oslash', 'oe'], 'a': ['ae'], 'u': [], 'r': ['eng', 'napostrophe'], 't': ['tbar'],
                     'i': ['dotlessi', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'itilde', 'imacron', 'ibreve', 'ij', 'jcircumflex']}
    for key, seeds in LEFT_SEEDS.items():
        members = []
        if seeds:
            for ch in seeds:
                base = gname(ord(ch)); members.append(base); members.extend(acc.get(ch, []))
        members.extend(EXTRA_LEFT.get(key, [])); members.extend(SPECIAL_LEFT.get(key, []))
        groups['public.kern1.' + key] = [m for m in dict.fromkeys(members) if m in all_names]
    for key, seeds in RIGHT_SEEDS.items():
        members = []
        if seeds:
            for ch in seeds:
                base = gname(ord(ch)); members.append(base); members.extend(acc.get(ch, []))
        members.extend(EXTRA_RIGHT.get(key, [])); members.extend(SPECIAL_RIGHT.get(key, []))
        groups['public.kern2.' + key] = [m for m in dict.fromkeys(members) if m in all_names]
    return groups


# Pairs whose value GROWS with weight (the f hook and the marks get heavier): the f before dotted, accented and
# ascending letters and closing punctuation, with ligatures off or where no ligature exists.
GROW_PAIRS = {('f', 'i'): 30, ('f', 'b'): 14, ('f', 'quote'): 40}
# Glyph-to-glyph exceptions: accent sequences that would otherwise touch (Czech/Slovak ří; f before accented vowels, café).
# Positive values push the pair apart; they grow with weight because the marks get heavier.
GLYPH_PAIRS = {
    ('rcaron', 'iacute'): 36, ('rcaron', 'idieresis'): 30, ('rcaron', 'icircumflex'): 30, ('rcaron', 'itilde'): 24,
    ('rcaron', 'imacron'): 26, ('rcaron', 'ibreve'): 24, ('rcaron', 'igrave'): 16, ('rcaron', 'i'): 14,
    ('f', 'question'): 24, ('f', 'parenright'): 26, ('f', 'bracketright'): 26, ('f', 'braceright'): 26, ('f', 'exclam'): 16, ('f', 'bar'): 14,
}
for _v in ('a', 'e', 'o', 'u', 'y'):
    for _m, _k in (('dieresis', 22), ('circumflex', 22), ('acute', 16), ('grave', 10), ('tilde', 20), ('macron', 20), ('caron', 20), ('breve', 20), ('ring', 20)):
        GLYPH_PAIRS[('f', _v + _m)] = _k
        GLYPH_PAIRS[('f_f', _v + _m)] = _k
        GLYPH_PAIRS[('uni1E1F', _v + _m)] = _k   # ḟ (Irish lenited f) has the same hook
# f before the dotless-i composites (ï î í ì ĩ ī ĭ are built on dotlessi, so they are not reached through the i class),
# before ř and ĵ; values measured with qa/pair_overlap.py so that no outline touches at any of the nine masters.
for _g, _k in (('idieresis', 95), ('icircumflex', 80), ('iacute', 60), ('igrave', 60), ('itilde', 125), ('imacron', 100),
               ('ibreve', 125), ('dotlessi', 10), ('rcaron', 90), ('jcircumflex', 90), ('ij', 30), ('iogonek', 30)):
    GLYPH_PAIRS[('f', _g)] = _k
    GLYPH_PAIRS[('f_f', _g)] = _k
    GLYPH_PAIRS[('uni1E1F', _g)] = _k
for _g, _k in (('question', 24), ('parenright', 26), ('bracketright', 26), ('braceright', 26), ('exclam', 16), ('bar', 14)):
    GLYPH_PAIRS[('uni1E1F', _g)] = _k
# ď ť ľ carry their caron as a tick that overhangs the right side bearing; before tall or marked narrow letters,
# carons and closing punctuation the tick must be kerned clear.
for _l in ('dcaron', 'tcaron', 'lcaron'):
    for _g, _k in (('i', 75), ('iacute', 90), ('igrave', 75), ('icircumflex', 140), ('idieresis', 130), ('itilde', 150),
                   ('imacron', 110), ('ibreve', 130), ('iogonek', 75), ('dotlessi', 30), ('uni1ECB', 75), ('j', 40), ('jcircumflex', 110), ('ij', 75),
                   ('l', 30), ('lacute', 50), ('lcaron', 80), ('lslash', 30), ('uni013C', 30), ('uni1E37', 30),
                   ('b', 26), ('h', 26), ('k', 26), ('f', 36), ('dcaron', 40), ('tcaron', 40),
                   ('rcaron', 120), ('ecaron', 40), ('scaron', 50), ('zcaron', 60), ('ccaron', 50), ('ncaron', 40),
                   ('parenright', 70), ('bracketright', 70), ('braceright', 70), ('quoteright', 60), ('quotedblright', 60),
                   ('quoteleft', 60), ('quotedblleft', 60), ('quotesingle', 60), ('quotedbl', 60), ('question', 50),
                   ('exclam', 50), ('bar', 50), ('slash', 50), ('backslash', 30), ('asterisk', 40), ('dagger', 40)):
        GLYPH_PAIRS[(_l, _g)] = _k
    for _v in ('a', 'e', 'o', 'u', 'y'):
        for _m in ('dieresis', 'circumflex', 'acute', 'grave', 'tilde', 'macron', 'caron', 'breve', 'ring'):
            GLYPH_PAIRS[(_l, _v + _m)] = 16
# narrow dotted/marked letters before ř (its caron hangs over the r's left side), and two dieresis in a row
for _g, _k in (('i', 30), ('iacute', 70), ('igrave', 45), ('icircumflex', 90), ('idieresis', 95), ('itilde', 135), ('imacron', 110), ('ibreve', 125), ('j', 20), ('l', 24)):
    GLYPH_PAIRS[(_g, 'rcaron')] = _k
GLYPH_PAIRS[('idieresis', 'idieresis')] = 100
GLYPH_PAIRS[('idieresis', 'icircumflex')] = 40
GLYPH_PAIRS[('icircumflex', 'idieresis')] = 40
# two marked narrow letters in a row (îî, ĩĭ, ïĩ …): even the narrow i-marks are wider than the i advance, so the
# marks would meet; measured with qa/pair_exhaustive.py at 800/75 (widest overlap 71 units) plus clearance.
_WIDE_I = ('icircumflex', 'itilde', 'imacron', 'ibreve', 'idieresis', 'jcircumflex')
for _a in _WIDE_I:
    for _b in _WIDE_I:
        _k = 90
        if 'imacron' in (_a, _b): _k = 60
        if _a == _b == 'imacron': _k = 40
        GLYPH_PAIRS[(_a, _b)] = max(_k, GLYPH_PAIRS.get((_a, _b), 0))
for _g in ('i', 'iogonek', 'ij', 'uni1ECB', 'j'):   # ï before a dotted i (Hawaïi) and after one
    GLYPH_PAIRS[('idieresis', _g)] = 40; GLYPH_PAIRS[(_g, 'idieresis')] = 40
# đ: its bar overhangs the right side bearing at mark height (đĩa)
for _g, _k in (('itilde', 110), ('icircumflex', 95), ('idieresis', 80), ('ibreve', 85), ('imacron', 90), ('jcircumflex', 85), ('iacute', 50), ('igrave', 35)):
    GLYPH_PAIRS[('dcroat', _g)] = _k
for _v in ('a', 'e', 'o', 'u', 'y'):   # đã, đẽ: the bar meets a wide lowercase mark at the light condensed end
    for _m in ('dieresis', 'circumflex', 'acute', 'grave', 'tilde', 'macron', 'caron', 'breve', 'ring'):
        GLYPH_PAIRS[('dcroat', _v + _m)] = 24
# Ľ: the tick sits where the L class kerning pulls V W Y T and quotes into the L's open corner; the class values are
# replaced by small positive ones for Ľ, and the narrow marked letters are pushed clear of the tick.
for _g in ('V', 'W', 'Wcircumflex', 'Wgrave', 'Wacute', 'Wdieresis', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'Ygrave', 'uni1E8E', 'uni1EF4', 'uni1EF8',
           'T', 'Tcaron', 'uni0162', 'uni021A', 'uni1E6A', 'uni1E6C', 'Tbar', 'quotesingle', 'quotedbl', 'quoteleft', 'quoteright', 'quotedblleft', 'quotedblright',
           'asterisk', 'dagger', 'daggerdbl', 'trademark', 'degree', 'ordfeminine', 'ordmasculine'):
    GLYPH_PAIRS[('Lcaron', _g)] = 10
for _g, _k in (('icircumflex', 80), ('itilde', 80), ('imacron', 70), ('ibreve', 80), ('idieresis', 80), ('jcircumflex', 60), ('iacute', 50), ('igrave', 40), ('i', 20), ('j', 20)):
    GLYPH_PAIRS[('Lcaron', _g)] = _k
# 1.103 residuals (qa/pair-exhaustive 1.102): V before ř — the caron top met the V's right arm at Regular and at the heavy
# condensed end (Vřídlo), so the V–r class tuck (−40) is replaced by a shallower one; Ľ before v — the tick met the v at 200/125.
GLYPH_PAIRS[('V', 'rcaron')] = -16
GLYPH_PAIRS[('Lcaron', 'v')] = -20
# 1.103 residuals that only touch at the light end: the thin ) ] } ends reach under an ogonek tail (ą) Ę) ų) at 200/75) and
# the ł stroke meets a preceding em dash (—ł). Scaled by `lscale` in kerning_for, so they fade as the weight grows, where
# the clearance already exists (measured 30–60 units at the 800 masters).
LIGHT_PAIRS = {('emdash', 'lslash'): 30}
for _g in ('aogonek', 'Eogonek', 'uogonek'):
    for _b in ('parenright', 'bracketright', 'braceright'):
        LIGHT_PAIRS[(_g, _b)] = 40
# ď ť ľ before every letter whose left stem rises to the ascender (b h k l þ ŀ and their marked forms), not only the plain ones
_acc = _accents_of()
for _l in ('dcaron', 'tcaron', 'lcaron'):
    for _base in 'bhklt':
        for _g in [gname(ord(_base))] + _acc.get(_base, []):
            GLYPH_PAIRS[(_l, _g)] = max(40, GLYPH_PAIRS.get((_l, _g), 0))
    for _g in ('thorn', 'ldot', 'lslash'):
        GLYPH_PAIRS[(_l, _g)] = max(40, GLYPH_PAIRS.get((_l, _g), 0))
# a dotted i before a marked i (iĭ): the dot meets the left end of the mark at the heavy end
for _g in ('i', 'iogonek', 'ij', 'uni1ECB'):
    for _m, _k in (('ibreve', 45), ('itilde', 25), ('icircumflex', 25), ('imacron', 20)):
        GLYPH_PAIRS[(_g, _m)] = max(_k, GLYPH_PAIRS.get((_g, _m), 0))
# a marked narrow letter before or after a plain/acute/grave one (ĭi, íĭ, ïì): the mark meets the dot or the acute
_NARROW_I = ('i', 'iogonek', 'ij', 'uni1ECB', 'igrave', 'iacute')
for _a in _WIDE_I:
    for _b in _NARROW_I:
        GLYPH_PAIRS[(_a, _b)] = max(50, GLYPH_PAIRS.get((_a, _b), 0)); GLYPH_PAIRS[(_b, _a)] = max(50, GLYPH_PAIRS.get((_b, _a), 0))
# đ bar before ascender stems and quotes at the light condensed end
for _base in 'bhklt':
    for _g in [gname(ord(_base))] + _acc.get(_base, []):
        GLYPH_PAIRS.setdefault(('dcroat', _g), 20)
for _g in ('quotesingle', 'quotedbl', 'quoteleft', 'quoteright', 'quotedblleft', 'quotedblright', 'thorn', 'ldot', 'lslash'):
    GLYPH_PAIRS.setdefault(('dcroat', _g), 30)
# Ŀ (Catalan L with middle dot) inherits the L class: the dot must not be pulled under quotes or V W Y T
for _g in ('quotesingle', 'quotedbl', 'quoteleft', 'quoteright', 'quotedblleft', 'quotedblright', 'V', 'W', 'Y', 'T', 'Yacute', 'Ycircumflex', 'Ydieresis', 'Ygrave', 'Wcircumflex', 'Wgrave', 'Wacute', 'Wdieresis'):
    GLYPH_PAIRS[('Ldot', _g)] = 4
# Q tail before low punctuation (FAQ, …) and K/k arms before the figure 2 at the heavy extended end
for _g, _k in (('comma', 40), ('quotesinglbase', 40), ('quotedblbase', 40), ('semicolon', 30)):
    GLYPH_PAIRS[('Q', _g)] = _k
for _base in 'Kk':
    for _g in [gname(ord(_base))] + _acc.get(_base, []) + (['kgreenlandic'] if _base == 'k' else []):
        GLYPH_PAIRS[(_g, 'two')] = 30
# ogonek tails before the j descender (ąj) and before p-like descenders (kąpiel, następny)
for _g, _k in (('aogonek', 56), ('eogonek', 56), ('uogonek', 50), ('iogonek', 50), ('Aogonek', 56), ('Eogonek', 56), ('Uogonek', 50), ('Iogonek', 50)):
    for _j in ('j', 'jcircumflex'):
        GLYPH_PAIRS[(_g, _j)] = _k
for _g in ('aogonek', 'eogonek', 'uogonek'):
    for _d in ('p', 'thorn', 'uni1E57', 'mu'):
        GLYPH_PAIRS[(_g, _d)] = 20
# the ł stroke reaches left under a preceding i dot at the heavy condensed end (mił, był); k leg before v w x y
for _g in ('i', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'itilde', 'imacron', 'ibreve', 'iogonek', 'dotlessi', 'uni1ECB', 'ij'):
    GLYPH_PAIRS[(_g, 'lslash')] = 10
for _g in [gname(ord('k'))] + _acc.get('k', []) + ['kgreenlandic']:
    for _d in ('v', 'w', 'x', 'y'):
        GLYPH_PAIRS[(_g, _d)] = 10
# capitals whose arm reaches the right edge at cap height before a marked narrow letter (Kï), K before Y and Æ, A and R before 2
_CAPS_ARM = [gname(ord(c)) for c in 'KVWXY'] + sum((_acc.get(c, []) for c in 'KVWXY'), [])
for _g in _CAPS_ARM:
    for _m, _k in (('idieresis', 45), ('ibreve', 40), ('itilde', 35), ('icircumflex', 30), ('imacron', 20)):
        GLYPH_PAIRS[(_g, _m)] = max(_k, GLYPH_PAIRS.get((_g, _m), 0))
for _g in [gname(ord('K'))] + _acc.get('K', []):
    for _y in [gname(ord('Y'))] + _acc.get('Y', []) + ['AE']:
        GLYPH_PAIRS[(_g, _y)] = 16
for _base in 'AR':
    for _g in [gname(ord(_base))] + _acc.get(_base, []):
        GLYPH_PAIRS[(_g, 'two')] = 16


def kerning_for(d):
    scale = d.f * (1 - 0.08 * d.kb)
    gscale = d.f * (1 + 0.35 * d.kb)
    lscale = d.f * max(0.0, 1 - 0.8 * d.kb)   # light-end pairs: 0.78 at 200/75, 1.0 at Regular, 0.2–0.33 at the 800 masters
    out = {('public.kern1.' + a, 'public.kern2.' + b): round(v * scale) for (a, b), v in PAIRS.items() if (a, b) not in GROW_PAIRS}
    out.update({('public.kern1.' + a, 'public.kern2.' + b): round(v * gscale) for (a, b), v in GROW_PAIRS.items()})
    out.update({(a, b): round(v * gscale) for (a, b), v in GLYPH_PAIRS.items()})
    out.update({(a, b): max(1, round(v * lscale)) for (a, b), v in LIGHT_PAIRS.items()})
    return out
