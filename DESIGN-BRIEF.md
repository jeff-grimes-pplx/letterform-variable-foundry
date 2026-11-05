# Apertide — design brief

Apertide is an original upright, two-axis Latin typeface designed for this commission. The application is called Letterform. This brief was written before drawing glyphs.

## Drawing premise

Tension rather than perfect geometry: upright stems support broad, slightly squared curves; counters open decisively toward the right. Round forms use unequal corner tension rather than circles. Terminal cuts sit on a consistent shallow diagonal. The double-storey a, open-tailed single-storey g, low-bar A, folded R leg, clipped e aperture and squared dots are the identifying family members. This is a display-and-editorial face, not a claim to replace a screen-text workhorse at tiny sizes.

No existing font outlines, font-derived skeletons or traced letter images will enter the pipeline. Original numerical centerlines, independent glyph recipes and optical adjustments generate the outlines. Unicode names and decomposition data specify character semantics, not designs. Generic Bézier mathematics and open-source compilers are tools, not outline sources.

## Metrics and optical rules

1000 units per em. Cap height 700; x-height 520; ascenders 740; descenders −210. Rounded capitals overshoot by 12 units and lowercase by 10. Horizontal stroke weight is lighter than vertical stroke weight. Diagonals receive their own compensation. Width changes move the skeleton and change advance widths while preserving stem thickness, rather than applying an affine stretch to the finished font. Sidebearings are assigned by form and interpolated deliberately; kerning families inherit through accented characters.

Nine compatible masters are planned: weight 200/400/800 crossed with width 75/100/125. Default: 400/100. Registered axes: wght 200–800; wdth 75–125, in percent of the normal width coordinate. Light, Regular, Medium, Semibold and Bold at normal width, plus narrow/wide selections, will be exported as named static instances. Names and exact counts are finalized from compiled binaries, not estimates.

## Character and feature contract

Printable ASCII, Latin-1, Latin Extended-A, Latin Extended Additional, language-critical extra Latin letters, combining marks, typographic punctuation, common mathematical signs, currency, arrows and explicit alternate glyphs. The final machine-readable manifest defines the exact repertoire. English, French, German, Spanish, Portuguese, Italian, Dutch, Nordic languages, Icelandic, Irish, Welsh, Catalan, Maltese, Polish, Czech, Slovak, Slovenian, Croatian, Romanian, Hungarian and Turkish sample strings will be tested for missing glyphs, including decomposed accents.

Features: class kerning inherited across accents; fi/fl/ff/ffi/ffl ligatures; proportional and tabular figures; numerator/denominator forms and contextual fractions; mark positioning; case-sensitive punctuation where appropriate. Features must alter HarfBuzz output for their test strings. Count encoded characters separately from unencoded glyphs and alternate forms.

## Name check — 14 October 2026

Queries: “Apertide font typeface”, “Apertide typography font family”, “Apertide”, and “Apertide font” restricted to MyFonts, Adobe Fonts, Fonts In Use and Google Fonts. No returned result identified an existing font family called Apertide. Broad search did identify an unrelated Code-OSS application called Apertide on https://github.com/TheJhyeFactor and a historical word form at https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary/MED1931. Catalog entry points examined in search results: https://fonts.adobe.com/fonts, https://fonts.google.com/, https://fontsinuse.com/, https://www.myfonts.com/pages/whatthefont. This is a bounded obvious-font-name check, not trademark clearance or a guarantee of worldwide uniqueness. Jeff decides any release.

## Specimen and work surface

Ink, chalk-white and vermilion. A type workbench, not a landing page: large editable text, exposed axis sliders, a feature laboratory, a complete inspectable glyph map, and a drawing view that uses the actual source skeleton and compiled outlines. Secondary notes contain licenses, exact coverage and test evidence. No slogans, promotional counters, decorative branding or external image assets.

PDF: a restrained foundry specimen using embedded instances of Apertide itself. Show its voice at large scale, then alphabet, waterfall, weight/width matrix, multilingual passages, feature comparisons and every glyph. All pages will be rendered and inspected; all file claims derive from the compiled font.

## Private-review boundary

All generated font, app, specimen and films are for private review. No public or organization-wide publication is authorized. No third-party outline license is needed because no third-party font outlines are used. Tool licenses will be recorded separately. Machine validation and independent agent review are not human foundry certification, trademark clearance or cross-platform installation testing.

## Revision note — 15 October 2026, build 1.100

Written after the independent review of build 1.001; the brief above is kept as written before drawing.

- Repertoire, stated precisely from the compiled cmap: printable ASCII, Latin-1 Supplement and Latin Extended-A are complete; Latin Extended-B is covered by 5 letters and Latin Extended Additional by 65 letters (the ones the tested languages need: Ș ș Ț ț, Welsh Ŵ Ŷ and their accented forms, Irish dotted consonants, dot-below letters), not the full blocks. The numero sign (U+2116), the double arrows (↔ ↕) and Vietnamese stacked accents are out of scope. The exact list is `qa/glyph-manifest.json`.
- Review findings addressed in 1.100: § ¶ ₹ redrawn; f-ligatures run the arch straight into the raised stem; r and F/P spacing (RSB + kerning classes) so "Apertide" no longer breaks after r; marks follow the width axis and lighten with weight, dieresis narrowed; heavy-corner counters opened (e bar, a, s/S terminals, A bar, z/Z/7 joins, &); g tail lengthened; `frac` limited to figure contexts and composable with `tnum` (also sups/subs/ordn/numr/dnom); OVERLAP flags set in the variable font; specimen layout and copy corrected; reduced motion honoured in the app; PROVENANCE.md added.
- Wording: the face is described as upright with tension (as above), not "humanist-geometric"; the specimen headline and the font's description string were aligned to this.

## Revision note — 15 October 2026, build 1.101

After the fresh regression review of 1.100:

- `f_i` and `f_f_i` keep the i's dot: the f's hook is trimmed to end clear of the dot and the pair is fitted, not fused, so fi is no longer read as fl. `f_l` / `f_f_l` keep the arch-into-stem join.
- Marks: stroke factor 1 − 0.30·kb (was 0.18), widths narrow 8 % per unit of boldness, dieresis dots smaller with a wider gap (no fusing at 700–800 / 75), caron and circumflex 6 % narrower, the r's top anchor moved toward its stem, and glyph-pair kerning for ř + í ì î ï ĩ ī ĭ i so Czech/Slovak "ří" does not touch.
- Ampersand stroke 1.0 − 0.16·kb (was 0.94 − 0.30·kb): it now matches the weight of the letters beside it while both counters stay open at 800.
- f spacing with ligatures off (or where no ligature exists): new weight-growing kerning (`GROW_PAIRS`, scaled by 1 + 0.35·kb) for f before the i/j/l class, the b/h/k class and quotes, plus glyph pairs for f and f_f before accented vowels (café, fünf, naïf) and before ? ) ] } ! | — in the tested pairs and locations (`qa/pair-overlaps.txt`: 2744 neighbouring pairs at eight locations, 0 outline collisions) the hook no longer runs into dots, marks, ascenders or closing punctuation. With `liga` on, f_i / f_f_i / f_l / f_f_l / f_f take over as before.
- Specimen: cover stack and info row sized to the page; seven alphabet blocks spread over the page; the axes page gained a width-axis text comparison and the design-space matrix fills its column; feature samples at 20 pt; the hero construction diagrams are no longer repeated at one size. No "№" (it was the only glyph outside the font).
- Films: the 30 s cut opens in an empty tester and types at once (scene `type30`); the FontForge finale carries a pointer circuit round the outline; the hold after the drawn letter is shorter.

## Revision note — 15 October 2026, build 1.101 final

After the independent verification of 1.101 and the coordination parent's review of the deployed app:

- The i-accent composites (í ì î ï ĩ ī ĭ, built on dotlessi), ij and ĵ now belong to the i kern class, so the weight-growing f kerning applies to them; explicit pairs for f / f_f before í ì î ï ĩ ī ĭ ĵ ř; ď ť ľ (apostrophe-shaped caron) before the i-family, j, l, b h k, f, ř, other carons, closing punctuation and quotes; the i-family before ř; ïï. Receipt: `qa/pair-overlaps.txt` — 2744 neighbouring pairs at 200/75, 200/125, 400/100, 600/88, 700/75, 800/75, 800/100 and 800/125, 0 shared pixels. Earlier wording that f "never touches at any master" is withdrawn in favour of this tested scope.
- App Drawing view: skeleton and stroke expansion are interpolated at the current wght/wdth (the header names position and instance), and a "Compiled font overlay" traces the real font over the drawing; QA measures the two as equal in advance (±1.5 units at four positions) and overlapping with IoU 0.997 at wght 555 / wdth 93.
- Films re-shot: Drawing hero, pad drag with reflow, pointer-led zooms on text beats, one specimen spread, FontForge finale with the full pointer circuit; all composited elements disclosed in `films/README.md`.
- Not changed: j/y tails, ß, ₹ at 200, § at 800, Condensed ExtraBold f/t hook weight, s balance (recorded taste items).

## Revision note — 15 October 2026, build 1.102

After the final independent review (REVIEW-4), which tested every two-glyph pair rather than curated strings:

- Narrow i-marks. The circumflex, tilde, macron, breve and dieresis over i and j were the full-width marks, wider than the letter's advance, so î ĩ ī ĭ ï collided with a following d, N, H, M, V, K or Y in ordinary words (dîner, Nîmes, Hî, Kï, Yï) and with each other (îî, ïĩ). Five dedicated marks (`circumflexcomb.i`, `tildecomb.i`, `macroncomb.i`, `brevecomb.i`, `dieresiscomb.i`) are now drawn narrower, scaled to the i's advance at every master, and the composites are rebuilt on them — 548 glyphs (+5 unencoded marks), encoded count unchanged at 477.
- Kerning: wide-mark i before another i-mark; đ before marked i (đĩa) and marked vowels (đã) at the light condensed end; Ľ and Ŀ no longer inherit the L class pulls into V W Y T and quotes (the Slovak tick and the Catalan dot were being driven under them); Æ and Œ kern on their right side like E, not like A (ÆV, ÆT, Æ’ were tightened as if the A's leg were there); ď ť ľ before every ascender-stem letter including the marked ones; Q before low punctuation (FAQ,); K/k before Y, Æ and the figure 2; ogonek tails before j and p; ḟ treated like f.
- Exhaustive receipt replaces the curated claim: `qa/pair_exhaustive.py` rasterises all 211 137 encoded-glyph pairs at 8 design-space locations and lists every pair that shares a pixel, by category (`qa/pair-exhaustive.txt`). What remains is by design (the fraction bar, slash and backslash overhang) or is a sequence no covered language produces (a lowercase letter before a capital or superior, ď/ť/ľ/đ/ï before Maltese ħ, Afrikaans ŉ, long s or Vietnamese ỹ, marked capital I stacks, Y/V/K before a marked lowercase i).
- App: the default sample is a real pangram (“Sphinx of black quartz, judge my vow.”) so typing in the film replaces it instead of retyping it; the design-space header names the nearest instance on one line so the pad never shifts under a pressed pointer.
- Not changed: j/y tails, ß, ₹ at 200, § at 800, Condensed ExtraBold f/t hook weight, s balance (recorded taste items).

## Revision note — 15 October 2026, build 1.103

The v2 pass clears the six real-word residual contacts that 1.102 had left and changes nothing else in the drawings:

- Kerning (`source/features.py`): glyph pairs V–ř −16 and Ľ–v −20; light-end pairs —ł +30 and ą/Ę/ų before ) ] } +40, fading to zero at the 800 masters (`LIGHT_PAIRS` with `lscale`). The exhaustive receipt (`qa/pair_exhaustive.py`, 211 137 pairs × 8 locations) loses exactly the 16 targeted pair/location hits (the six named pairs and the ] } siblings of the ogonek pairs) and gains none.
- fontbakery unchanged (VF 0 FAIL / 0 WARN; statics 0 FAIL / 12 ₩ `contour_count` WARN); hb-shape 68/68; OTS, FontForge and fontTools re-read all 17 binaries.
- Specimen re-rendered from 1.103 (cover foot states Glyphs 548 · Masters 9 · Languages 26; 15 pages; Chromium layout receipt 0 issues). App: fonts, zip and Build line → 1.103; the glyph-grid head no longer wraps or clips (`#grid-count` on one line, filter input flexes to its own row at ≤ 900 px; receipt `qa/label-wrap.txt`); data file byte-identical to 1.102.
- Not changed: everything listed under 1.102 "Not changed".
