# Checker summary (fontbakery 1.1.0, universal profile) — build 1.103

## Variable font `fonts/Apertide[wdth,wght].ttf`
`fontbakery check-universal --succinct -l WARN -x fontdata_namecheck` → **0 FAIL, 0 WARN**, 3 INFO, 19 SKIP, 104 PASS.
Reports: `fontbakery-vf.txt`, `fontbakery-vf.html`, `fontbakery-vf.json`.
INFO items: `superfamily/list` (no superfamily given), `hinting_impact` (unhinted by design; gasp/prep smart-dropout only),
`required_tables` (lists the optional tables present). `fontdata_namecheck` PASSED in an earlier full run of the same family name ("Font familyname seems to be unique."); later runs hit the namecheck.fontdata.com rate limit (HTTP 429), so the check is excluded from the saved reports and the name check is additionally documented in DESIGN-BRIEF.md.

## 15 static instances `fonts/static/*.ttf`
`fontbakery check-universal --succinct -l WARN -x fontdata_namecheck` → **0 FAIL**, 12 WARN, 45 INFO, 566 SKIP, 1099 PASS.
Reports: `fontbakery-static.txt`, `fontbakery-static.html`, `fontbakery-static.json`.

The 12 WARNs are all one check, `contour_count`, for one glyph, `uni20A9` (₩): 6 contours (5 in
CondensedExtraBold) where the reference statistic expects 1, 3, 4 or 7. Cause: ₩ is W plus two bars; in
the twelve heavier/narrower instances the W's middle apex merges the two inner diagonals above the upper
bar, so the bars enclose fewer counters. The three ExtraLight instances report 7, which the check accepts.
This is the intended design, so it is left as-is and disclosed here rather than redesigned to please a
statistic. (Builds 1.100–1.103: the earlier 1.001 build warned on 11 instances; the stronger condensed nib
reduction added one.)

`fontdata_namecheck` was excluded from the static run only because the namecheck.fontdata.com service
returned HTTP 429 (rate limit) on repeated calls; the same check passed on the variable font
(same family name) in the VF report above.

`shape_languages` (googlefonts glyphset check) is not loaded because `shaperglot` is not installed in
this environment; language coverage is instead verified directly with hb-shape in `shaping-receipts.txt`
(27 language/symbol corpora, no .notdef; 68 receipts in total).

## Other independent checks
- OpenType Sanitizer 9.2.0: all 17 binaries (VF .ttf, VF .woff2, 15 statics) "sanitized successfully" — `independent-parsers.txt`.
- fontTools 4.67.0 re-open of the compiled binaries: 548 glyphs, 477 encoded codepoints, fvar/STAT/GSUB/GPOS as listed — `independent-parsers.txt`.
- FontForge 20230101: opens the VF and the static Regular (548 glyphs each); no open or self-intersecting contours in the Regular — `independent-parsers.txt`.
- HarfBuzz 12.3.2 `hb-shape`: 68/68 feature, kerning, mark, fraction/figure-interaction and coverage receipts — `shaping-receipts.txt` / `.json` (script: `shape_receipts.py`).
- Curated outline-collision receipt (`pair_overlap.py` → `pair-overlaps.txt` / `.json`): test strings shaped with uharfbuzz 0.56.3 at 8 design-space locations, each glyph rasterised separately at 1000 px/em after overlap removal (skia-pathops 0.9.2), neighbouring masks intersected — 3696 pairs, 0 shared pixels. Scope: f/ff before dotted and accented i, j, ascenders, closing punctuation and accented vowels (liga off); Czech/Slovak ď ť ľ ř sequences; dieresis stacks; quotes after f r v w y T V W Y; kerned capitals; and the 1.102 additions (narrow i-marks in words and stacks, Ľ Ŀ đ Æ Œ pairs, Q tails, K/A/R before 2, ogonek before j/p, ď ť ľ before ascender stems).
- Exhaustive pair receipt (`pair_exhaustive.py` → `pair-exhaustive.txt` / `.json`): every ordered pair of the 459 encoded characters that can stand next to each other (the cmap minus controls, space, no-break space, soft hyphen and the combining marks U+0300–036F) shaped with uharfbuzz with `kern` on and `liga` off, plus every pair beginning with f shaped with `liga` on, minus the pairs that ligate or decompose into a single glyph — 211 137 two-glyph pairs rasterised at the same 8 locations, 1 689 096 pair/location tests. 4 403 hits remain (1.103; 4 419 in 1.102), every one listed by category in the report: fraction bar 342 distinct pairs (negative side bearings by design), slash/backslash 104 (overhang by design), lowercase before a capital 277, symbol/superior/punctuation 200, capital before lowercase 73, two lowercase letters 47, two capitals 24. The 47 lowercase pairs are all cross-language sequences (ď ť ľ đ ï î ī before Maltese ħ, Afrikaans ŉ, long s, Vietnamese ỹ, dotless j, Irish ḟ, Sami ŧ; į before y) and the 24 capital pairs are stacks of two marked capital I's plus ĽX. The 1.102 residual contacts a covered language can write — Vř (Czech) at 400/100, 600/88, 700/75, 800/75; Ľv (Slovak) at 200/125; ogonek or ł-bar under a closing parenthesis or dash at 200/75 (ą) Ę) ų) —ł) — are gone in 1.103 through targeted kern pairs (`source/features.py`: V–rcaron −16, Lcaron–v −20, emdash–lslash 30, ogonek letters before closing brackets 40, fading at the 800 masters); exactly those 16 pair/location hits disappeared and nothing new appeared. Everything else is a by-design overhang or a sequence no covered language writes. A measured statement about those 8 locations, not about every point of the design space.
