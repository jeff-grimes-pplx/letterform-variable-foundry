# A4 · Letterform — handoff (Apertide 1.103, v4 films pass)

**548 glyphs · 477 encoded · 2 axes · 9 masters · 15 instances · 26 languages · fontbakery 0 FAIL** (variable font 0 FAIL / 0 WARN; statics 0 FAIL / 12 explained WARN) · hb-shape 68/68 · exhaustive two-glyph collision receipt: 211 137 pairs × 8 locations, every remaining contact listed and categorised, the six real-word residuals of 1.102 cleared · app QA 206/206 local and hosted · two 45 s films of the same 2,700 frames at exactly 60/1 (captioned release candidate + clean film), receipts in `films-v2.md` below.

Apertide is an original upright variable sans drawn from numerical skeletons: every stem, bowl and terminal is a stroke along a centerline whose width, nib and terminal angle are parameters, so the nine masters at the corners and midpoints of the weight and width axes come from the same recipes and interpolate cleanly. Terminals are cut on one shallow diagonal ("blade"); round forms lean on an unequal corner tension so counters open toward the right. Nothing is derived from an existing font (see `PROVENANCE.md`).

What changed in the v2 pass (parent mail "v2 pass for A4 Letterform", 15 Oct 2026): font 1.102 → 1.103 (six residual kerning contacts cleared, nothing else redrawn — `DESIGN-BRIEF.md` revision note), specimen re-rendered from 1.103 with the cover foot stating Glyphs 548 · Masters 9 · Languages 26, app Build 1.103 with a glyph-grid head that no longer wraps or clips, redeployed in place (bundle hash below), and one 45-second film replacing the 60 s and 30 s cuts (both kept as superseded assets). v2.1 (parent mail, 16 Oct 2026): burned-in subtitles are required and the captioned film is the release candidate — the 45 s film was re-shot (take 2) with every shot composed below a 300 px clear top band, eight captions in Inter SemiBold 64 px, and delivered as `letterform-45s-captioned.mp4` plus the clean `letterform-45s.mp4`; take 1 (`Letterform-45s.mp4`) is kept as a superseded asset.

What changed in the v3 pass (parent mail “Caption treatment v3”, 20 Oct 2026; Jeff: the band captions “just don't look that professional”, use the bottom-block treatment of the reference film): the eight approved v2.1 caption texts are re-set in the reference treatment — Lato Bold 60 px white on one opaque #1b262b rounded block per caption, bottom-centre at (960, 1009), hard in/out, burned in with libass from the kit's `captions_v3.py` output — and every shot is re-framed full-frame 1920×1080 (the v2.1 300 px top matte is gone) so the action stays ≥ 24 px clear of the block. Footage otherwise frozen: the captured frames are the v2.1 take 2b captures; the tester scene (frames 822–1259) is byte-identical to v2.1; frames 0–821 and 1260–2699 are new crops of the same captures. Font, specimen, app and bundle hash are unchanged. v2.1 films kept under `films/v21/`. Take 4 (the delivered pair) follows three independent review passes (`qa/film45v3/review-v3.md` on take 1, FIX FIRST; `qa/film45v3/review-v3-take2.md` on take 2, FIX FIRST small; `qa/film45v3/review-v3-take3.md` on take 3, FIX FIRST one item): shots were re-framed so that nothing a caption names sits in or within 24 px of the block — specimen shot moved from the page 3 alphabet (its digits row fell inside the block band) to the page 6 waterfall, glyph cluster replaced by a bounded 7 × 3 crop that ends 46 px above the block, readout close-up re-targeted with no partial column, features sample band given headroom, footer centred without the page number, the glyph-grid push re-pathed so that its frame edges move monotonically — and the receipt's drag press/release frames corrected to f450/f750. Receipts: section “films-v3.md” below, `qa/film-check45v3.txt`, independent reviews `qa/film45v3/review-v3.md` (take 1), `qa/film45v3/review-v3-take2.md` (take 2), `qa/film45v3/review-v3-take3.md` (take 3) and `qa/film45v3/review-v3-take4.md` (take 4).

What changed in the v4 pass (parent mail "A4 Letterform — v4", 21 Oct 2026; Jeff: set the scene with a zoomed-out view first, stay wide enough that the viewer can see what is going on, captions at the bottom, plain wording): a new 60-second film pair replaces the 45 s v3 pair (kept, superseded). New capture (Playwright, CSS 1280×720 at 3× supersampling = 1.5 film px per CSS px at camera 1.0×), 5.0 s opener at 1.0× on the populated Glyphs workspace, four push-ins and one wide click (max 1.8×, 87.4 % of frames wide), every view re-established wide before a push-in, twelve v4-voice captions in the v3 bottom block (kit v4.1 `captions_v4.py`, `caption_lint.py` exit 0, `camera_budget.py` exit 0, kit v2.2 verifier exit 0), two three-page specimen spreads at 100 % for the close. Five takes: take 5 is delivered, after independent reviews of take 2 (`films/logs60v4/review-v4-take2.md`: a progress thumb 4 px above the caption block, an Alphabet click framed so the first letters drew out of frame, ligature and kerning changes off-frame, two captions without an on-screen receipt), take 3 (`films/logs60v4/review-v4-take3.md`: the re-framed Alphabet push-in put the transport row inside the caption block and held no action; stale capture logs in the build folder) and take 4 (`films/logs60v4/review-v4-take4.md`: the 1.44× Alphabet box excluded the letter rows, so the consequence began off-frame for 0.47 s after the click; no camera box can hold both the transport row clear of the block and the first row in frame). The app got a legibility-only pass (body 13 → 14 px, readouts 16 px, Alphabet-view node and hairline scale), after the take-2 review 24 px more space under the Drawing view's transport row, and after the take-4 review 19 px transport buttons (28.5 px em at camera 1.0×, so the Alphabet click is shot wide with no push-in and the whole consequence stays in frame; Play keeps the Pause width so the row no longer shifts); it was redeployed in place each time (current bundle hash `8408de75…`); no new features. Full receipts: `films/films-v4.md` (also embedded below). The Project rule asks for `user:app-build-rules` before UI edits; the skill was not loadable in this session (`load_skill` → unknown), so its stated principles were applied directly and are listed in `films/films-v4.md`.

## Deliverables

| What | Where |
| --- | --- |
| Design brief, name check, revision notes (1.100 → 1.103) | `DESIGN-BRIEF.md` |
| Variable font | `fonts/Apertide[wdth,wght].ttf` (325 KB), `fonts/Apertide[wdth,wght].woff2` (103 KB) |
| 15 static instances | `fonts/static/Apertide-*.ttf` (ExtraLight → ExtraBold; Condensed and Extended ExtraLight/Regular/Bold/ExtraBold); zipped with the license as `app/fonts/Apertide-static.zip`; everything together as `fonts/Apertide-fonts-1.103.zip` |
| Source | `source/` (Python recipe engine → UFO masters → designspace → fontmake); `python3 source/build.py all` rebuilds everything in ~25 s |
| Specimen PDF | `specimen/Apertide-Specimen.pdf` — 15 pages A4: cover, construction, character set, seven alphabet blocks, named instances, waterfall, axis sweeps + nine masters + design-space matrix + width-axis text, pangrams, 18 language blocks (26 languages), features, text settings, glyph map (3 pages, 14 × 14), colophon |
| Tester app (private, deployed in place) | [Letterform](https://www.perplexity.ai/computer/a/letterform-DFI51AvrQb2HEl5kaRMwug) — source `app/`; Build 1.103; deployed bundle hash `8408de759805386a5fc93e881b7cd4ff955289a1bccb6a059f89df7e7de0f8e6` (v4d, 21 Oct 2026 10:52 UTC: legibility pass + Drawing transport spacing + 19 px transport buttons; `qa/app-bundle-hashes.txt`; hosted files equal `app/` byte for byte; hosted QA 206/206 `qa/app-qa-hosted.txt`). Earlier bundles: `95d028a2…6e70` (v4c), `3c10c6db…58fd` (v4b), `8489e4b2…` (v4a), `d61dce3f…c396` (v3), `807b6994…e698` (v1). |
| Films (v4) | `films/letterform-60s-captioned.mp4` (release candidate, burned-in v4 captions) and `films/letterform-60s.mp4` (clean), both 3,600 frames / 60.000 s / 60/1 / 1920×1080 / yuv420p BT.709 / silent; master `films/master/letterform-60s-v4-master.mp4` (CRF 10 yuv444p). Capture `films/capture60v4.mjs`, renderer `films/render60v4.py`, assembly `films/assemble60v4.sh`, captions `films/captions-v4/`, receipts `films/films-v4.md`, `films/logs60v4/` (capture log, camera, ffprobe, verify, budget, lint, contact sheet, native frames, the five review reports), checker `qa/film_check60v4.py`. |
| v3 films (kept, superseded by v4) | `films/letterform-45s-captioned.mp4` (release candidate, burned-in v3 captions) and `films/letterform-45s.mp4` (clean), both 2,700 frames / 45.000 s / 60/1 / 1920×1080 full frame; masters `films/master/letterform-45s-captioned-master.mp4`, `films/master/letterform-45s-master.mp4` (CRF 10, 4:4:4); caption kit `films/captions-v3/` (`captions_v3.py`, `verify_captions_v3.py`, `cues.json`, `fonts/Lato-Bold.ttf` + OFL, `build/Captions.ass`, `build/caption-geometry.json`); renderer `films/render45v3.py`, assembly `films/assemble45v3.sh`; pipeline and disclosures `films/README.md`; receipts `qa/film-check45v3.txt` (+ `qa/film45v3/`), reviews `qa/film45v3/review-v3.md` (take 1), `qa/film45v3/review-v3-take2.md` (take 2), `qa/film45v3/review-v3-take3.md` (take 3), `qa/film45v3/review-v3-take4.md` (take 4) |
| v2.1 films (kept, superseded) | `films/v21/letterform-45s-captioned.mp4`, `films/v21/letterform-45s.mp4`, masters in `films/v21/master/`; caption font `films/captions/Inter-SemiBold.ttf`; receipts `qa/film-check45.txt`, `qa/film45/`, review `qa/film45/review-v21.md` |
| Superseded films (kept) | `films/Letterform-45s.mp4` (take 1, v2), `films/Letterform-60s.mp4`, `films/Letterform-30s.mp4`, their masters, `qa/film-check.txt` |
| Checker and receipts | `qa/` (see below) |
| License / provenance | `LICENSE.txt` (private review; Jeff decides any release), `PROVENANCE.md` |

## Font facts

- 548 glyphs, 477 encoded characters. Printable ASCII, Latin-1 Supplement and Latin Extended-A complete; 5 Latin Extended-B and 65 Latin Extended Additional letters (Ș ș Ț ț, Welsh circumflexes and graves, Irish dotted consonants, dot-below letters); combining marks with case variants and narrow i/j variants; typographic punctuation; currency € £ ¥ ₹ ₺ ₽ ₩ ¢ $ ¤; mathematical signs; four arrows; f-ligatures; tabular/numerator/denominator/superior/inferior figures; slashed zero; case-sensitive punctuation. Full list: `qa/glyph-manifest.json`.
- Axes: `wght` 200–800 (default 400), `wdth` 75–125 (default 100). Nine masters at 200/400/800 × 75/100/125. STAT names seven weights × three widths; Regular is elidable and linked to Bold. 15 named instances in `fvar`.
- Metrics: 1000 UPM, cap 700, x-height 520, ascender 740, descender −210; typo metrics 940/−260/0 with USE_TYPO_METRICS; hhea 940/−260.
- OpenType: GSUB `ccmp liga tnum pnum zero frac numr dnom sups subs ordn case`; GPOS class kerning plus glyph-pair exceptions (`kern`) and mark attachment (`mark`). `frac` only converts a slash between figures and composes with `tnum`/`sups`/`subs`/`ordn`. Turkish/Azeri/Crimean Tatar exclude the f-ligatures over dotted i via the language system.
- Languages: the 26 languages typeset on the specimen's language pages (18 blocks) shape with no `.notdef` (receipts below).
- Name/version: family "Apertide", version 1.103, copyright "Copyright 2026 Jeff Grimes. Private review build A4."

## Checks (all in `qa/`)

- fontbakery 1.1.0 universal, variable font: **0 FAIL, 0 WARN**, 3 INFO, 19 SKIP, 104 PASS (`fontbakery-vf.txt/.html/.json`).
- fontbakery universal, 15 statics: **0 FAIL**, 12 WARN — all `contour_count` on one glyph, ₩ (`uni20A9`), whose two bars enclose fewer counters in the heavier/narrower instances by design (`fontbakery-static.*`, parsed and explained in `CHECKER-SUMMARY.md`).
- Honest exclusions: `fontdata_namecheck` passed once (14 Oct) then hit the service's HTTP 429 rate limit, so it is excluded from the saved reports; `shape_languages` is skipped because shaperglot is not installed — language coverage is proven instead by hb-shape (27 corpora, no `.notdef`).
- HarfBuzz 12.3.2 shaping receipts: **68/68** (`shaping-receipts.txt/.json`, script `shape_receipts.py`): kerning pairs (AV, To, Ta, Yo, r/F/P pairs, "Apertide" at 800/75), f-ligatures on/off and the Turkish exclusion, tabular vs proportional advances, fractions (incl. negative tests: a/b and "1/" stay slashes), figure features composing with `tnum`, ordinals, case forms, mark attachment, 27 language corpora. The film's own consequences at wght 800 / wdth 125: "AVATAR, Tokyo" advances 8 990 units with `kern` off, 8 501 on; "Official waffle" 8 088 with `liga` off, 7 747 on.
- Outline collisions, curated (`pair-overlaps.txt/.json`, script `pair_overlap.py`): test strings shaped with uharfbuzz at 8 locations (200/75, 200/125, 400/100, 600/88, 700/75, 800/75, 800/100, 800/125), every glyph rasterised separately at 1000 px/em and neighbouring masks intersected — **3696 pairs, 0 shared pixels**.
- Outline collisions, exhaustive (`pair-exhaustive.txt/.json`, script `pair_exhaustive.py`): every ordered pair of the 459 encoded characters that can stand next to each other, `kern` on, `liga` off plus every f-pair with `liga` on, minus pairs that ligate or decompose — **211 137 two-glyph pairs at the same 8 locations, 1 689 096 tests**. 4 403 pair/location contacts remain and every one is listed by category: fraction bar (negative side bearings by design), slash/backslash overhang (by design), lowercase letter before a capital, symbol/superior/punctuation pairs, capital before lowercase, cross-language lowercase sequences (ďħ ťħ đħ ďŉ ľħ ïħ ďỹ ďſ ąȷ ḋĥ ſř æł įy), stacks of two marked capital I's plus ĽX. The six real-word residuals of 1.102 (Vř, Ľv, ą) Ę) ų) —ł) are gone in 1.103 — exactly the 16 targeted pair/location hits disappeared and nothing new appeared. Scope of the claim: the 8 locations, not every point of the design space.
- Independent parsers (`independent-parsers.txt`): OpenType Sanitizer 9.2.0 passes all 17 binaries; FontForge 20230101 opens the VF and statics (548 glyphs); fontTools re-reads every table. `font-checksums.txt` ties `fonts/` to the copies served by the app.
- Specimen (`specimen-check.txt`): qpdf clean; only Apertide embedded (static text as CID TrueType, variable-font settings as Skia Type 3 glyph procedures — disclosed in the colophon); Chromium print-layout receipt `specimen/overflow_check.mjs` → 0 issues; every one of the 15 pages inspected as an image after the 1.103 build.
- App (`app-qa.txt`, `app-qa-hosted.txt`, `app-shots/`, `label-wrap.txt`): **206/206** checks locally and on the deployed copy (hosted woff2 sha256 `5cc200d3…` matches `fonts/`) — axis sliders and pad drive the real `font-variation-settings`; feature toggles change shaping; glyph grid has all 548 cells with filter and detail; Drawing view follows the design-space position (header names the instance) and its "Compiled font overlay" — the real font via `@font-face` drawn through the same transform — matches the drawn outline (advance equal ±1.5 units at four positions; rasterised IoU 0.997 at wght 555 / wdth 93); the design-space pad keeps its position for every instance label; the glyph-grid head keeps its count on one line and the filter on its own row at ≤ 900 px (0 wrap/clip findings at 1440×900, 1280×720, 390×844); reduced motion honoured; keyboard access; empty/long/unsupported text; downloads match the font checksums; no console errors.

## Films (v4) — what they show

Same 3,600 frames in both films, full frame 1920×1080, 60.000 s. Camera 1.0× = 1.5 film px per CSS px of the 1280×720 app viewport. Captions sit in one opaque block at the bottom centre; the pointer, every click target, the typed lines, the Drawing view's transport row at the Alphabet push-in and its moving progress thumb stay ≥ 24 px clear of it (measurements in `films/films-v4.md` §5).

| s | frames | shot | caption |
| --- | --- | --- | --- |
| 0–5.0 | 0–299 | Opener at 1.0×: the whole Glyphs workspace, populated (grid of 548 glyph cells with the `a` selected, detail panel with the `a` outline over its skeleton, rail with Weight 400 / Width 100 / Size 76 px, design-space pad, Features list). Static until the pointer enters from the bottom edge at f280 | 1 · This is a brand new typeface, drawn from scratch. |
| 5.0–9.5 | 300–571 | Pointer reaches the grid (f360); wheel scroll of 3,398 CSS px (f372–551, eased) brings the accented rows (Ccedilla…) into view, wide | 2 · The grid holds every letter in the font, including the accented ones. |
| 9.5–14.5 | 572–869 | Push-in 1.0 → 1.8× (f582–642) onto the glyph-count readout "548 glyphs · 477 encoded…" above the accented rows (readout 37.8 px em), hold, pull back (f750–810), wide to the cut | 3 · The count at the top of the grid says 548 glyphs. |
| 14.5–18.0 | 870–1079 | Cut to the Drawing view at 1.0× (no push-in in this view): the `a` over its red skeleton with nodes and metric guides, Play / Replay / Alphabet (19 px, 28.5 px em), picker; pointer to Alphabet (f900–960), hover state, 2.0 s dwell | 4 · Red dots mark the skeleton each letter is built on. |
| 18.0–27.3 | 1080–1639 | Click Alphabet wide (f1080); Play reads Pause, the progress thumb starts, and the 52 letters grow from skeleton strokes to outlines over 7 s (to f1500) with every row in frame from the first stroke; hold | 5 · Press Alphabet, and every skeleton grows into its shape. |
| 27.3–30.7 | 1640–1843 | Cut to the Tester at 1.0× (re-establish 2.0 s): "Sphinx of black quartz, judge my vow." at 76 px, rail and pad; pointer to the Regular dot (f1650–1760); push-in 1.5× onto rail and pad (f1760–1820) | 6 · The tester sets live text in the new font. |
| 30.7–37.4 | 1844–2243 | Grab the Regular dot (f1844) and drag 400/100 → 200/75 → 700/125 (release f2082, ≤ 236 px/s); pull back during the drag (f1851–1923) so the sample re-sets wide, readouts follow (Extended Bold, wght 700 · wdth 125) | 7 · Drag the weight and width, and the letters change live. |
| 37.4–41.4 | 2244–2485 | Click into the sample (f2244), Ctrl+A, type "Official waffle AVATAR, Toronto" (31 keystrokes, f2296–2458, 11.1 cps mean, seeded rhythm), I-beam parked below the lines; wide throughout (the sample is 114 px em) | 8 · Any text typed here sets in the new font right away. |
| 41.4–48.5 | 2486–2911 | Pointer to Ligatures (f2486–2546); push-in 1.8× onto the lower rail (f2540–2600); click Ligatures (f2624); pull back from the click (f2626–2686): "Official" re-sets with the ffi ligature, "waffle" with ffl, wide; pointer steps down to Kerning (f2756–2796); push-in 1.8× (f2826–2886) | 9 · With ligatures on, pairs like ffi merge into one glyph. |
| 48.5–52.0 | 2912–3119 | Click Kerning (f2912); pull back from the click (f2914–2974): AV 124.4 → 108.9 CSS px, To 109.1 → 100.6, wide hold | 10 · Kerning pulls pairs like AV and To closer together. |
| 52.0–55.5 | 3120–3329 | Cut to specimen spread A at 100 %: pages 1 (cover, waterfall, foot "548 · 477 · 15 · 9 · 26"), 6 (waterfall) and 8 (pangrams across the weights) | 11 · These pages are all set in the finished font. |
| 55.5–60 | 3330–3599 | Spread B: pages 3 (character set), 4 (alphabets) and 5 (the fifteen named instances, ExtraLight to Extended ExtraBold) | 12 · The font comes in fifteen styles, ExtraLight to Extended ExtraBold. |

Receipts for every number in the captions: 548 glyphs is on screen at f641 (readout) and f3120 (cover foot) and in `qa/` (`fontbakery-vf.txt`); ffi/AV/To pair widths are in `films/logs60v4/capture60v4.json` (`geometry.pairsOff/pairsLiga/pairsKern`); fifteen styles: `fvar` (`qa/font-checksums.txt`) and specimen page 5 on screen from f3330; "set in the finished font": `qa/specimen-check.txt` (only Apertide embedded). Two baseline captions were reworded after the take-2 review because their claims were not on screen: "26 languages" (only a 6 px label on the cover) and "It installs like any other font" (no installation is shown).

## films-v4.md — 60 s film receipts (v4, 21 Oct 2026)

Deliverables: `films/letterform-60s-captioned.mp4` and `films/letterform-60s.mp4` (clean), 3,600 frames, 60.000 s, 60/1, 1920×1080, yuv420p BT.709, one silent video stream each; master `films/master/letterform-60s-v4-master.mp4` (libx264 CRF 10, yuv444p, 60000 timescale). The two delivered films are frame-identical outside the caption blocks (kit v2.2 verifier `diff_outside_block` below).

Length reason: 60 s because the 5.0 s opener at 1.0×, four re-established views (Glyphs, Drawing, Tester, specimen) and the wide consequence beats after the four push-ins (count, pad, Ligatures, Kerning) and the wide Alphabet click (7 s of drawing) do not fit the 45 s default without cutting the ligature or kerning beat.

### How the film was made (disclosure)

- Frame-stepped capture, not a real-time recording: Playwright headless Chromium (`--hide-scrollbars --disable-smooth-scrolling --font-render-hinting=none`) at a CSS viewport of 1280×720 with deviceScaleFactor 3; the page clock (`performance.now`, `requestAnimationFrame`, timers) is stepped by `__filmStep(1000 + g·1000/60)` one frame at a time, and every frame is a full-page screenshot (3840×2160 PNG). `render60v4.py` crops each PNG to the camera box of that frame and Lanczos-resamples it to 1920×1080. At camera 1.0× that is an exact 2:1 downscale of the 3× capture, i.e. the same pixel size as a 1280×720 capture at deviceScaleFactor 1.5 (1.5 film px per CSS px), which is the v4 §3.1 requirement.
- The pointer (arrow, hand, I-beam, grab) and the text caret are composited by the capture program from the logged pointer path, not recorded from the OS; every pointer position, click, key and wheel step is in `films/logs60v4/capture60v4.json` (per-frame `pointer`, `cursor`, `down`; `actions[]`). Pointer paths are minimum-jerk eased; the capture program throws if a move exceeds 1,200 film px/s (600 while dragging), if a click has less than 0.3 s of dwell, or if typing leaves 10–14 characters per second.
- The camera (`camera.json`, `camera-frames.json`) is exported by the same program from its SEGMENTS table and applied by the renderer; zoom is eased in log space (in-out cubic), the box is a homothety of the full frame (monotonic edges), and nothing in the browser changes with the camera. The camera and pointer timelines are deterministic; take 5 of the capture is the delivered one. Take 1 was re-shot after the clearance check (the pointer entered under the caption block, the glyph-count push-in was 1.6×, the Kerning click had no push-in). Take 2 was re-shot after the first independent review (`films/logs60v4/review-v4-take2.md`): the Drawing view's progress thumb travelled 4 px above the caption block during the alphabet animation, the Alphabet click sat inside a bottom-anchored 1.5× box so the first letters drew out of frame, the Ligatures and Kerning changes happened off-frame before the pull-backs, two captions had no on-screen receipt and two specimen pages were body copy. Take 3 was re-shot after the second independent review (`films/logs60v4/review-v4-take3.md`): its 1.35× Alphabet push-in put the transport row (progress thumb, Speed) inside the caption block and held no action (the click was at 1.0×, where the label is 21 px em), and the build folder's camera/capture logs were stale take-2 copies. Take 4 moved the Alphabet push-in to a 1.44× box with the transport row 32 px above the block and the click inside it; the third independent review (`films/logs60v4/review-v4-take4.md`) found that this box excludes the Alphabet rows, so the consequence began off-frame for 0.47 s after the click (f1117–1144), and showed that no camera box at ≥ 1.26× can hold both the transport row clear of the block and the first letter row in frame. Take 5: the Drawing view is shot at 1.0× throughout; the product's transport buttons are 19 px (28.5 px em at 1.0×, bundle `8408de75…`), so the click is wide and legible without a push-in and all 52 letters draw in frame from the first frame; the assembly script copies the capture's own logs into `films/logs60v4/`. The fourth independent review (`films/logs60v4/review-v4-take5.md`) passed the footage and asked for two caption changes; one was made: cue 4 now reads "Red dots mark the skeleton each letter is built on." (the finished-outline skeleton line is drawn at 18 % opacity by design, so at camera 1.0× what reads in red is the eight 8 px node dots; the old wording named a red stroke), and the captions were re-burned on the same clean film (byte-identical, SHA-256 `649155a1…801e`). The other request, replacing the parent's prescribed caption 1 with one that names the tool, was not made: the parent's v4 mail sets caption 1 verbatim; the objection is reported to the parent. A fifth independent confirmation review of the re-burned pair (`films/logs60v4/review-v4.md`) verified the clean film unchanged, the eleven other cues within 1 px of the geometry file, cue 4's receipt (eight red 8 px dots) and its timing floors, and returned POST. Nothing was retouched between capture and film.
- The two in-app view changes (Glyphs → Drawing at f870, Drawing → Tester at f1640) are `letterform.setView` calls between two frames, i.e. hard cuts, and the specimen (f3120–3599) is two static three-page spreads composited from the shipped `specimen/Apertide-Specimen.pdf` (pages rendered at 600 dpi, placed at 1.0 px per pt on a chalk ground), not a browser capture.
- Nothing here is a measurement of real-time GPU performance; frame-to-frame motion in the film is whatever the app drew for that stepped clock value.
- `user:app-build-rules` (required by the Project rule before UI edits) was not loadable in this session (`load_skill` → unknown skill); its stated principles (proportional, no new features, no badges or marketing chrome, redeploy in place, record the bundle hash) were applied directly and are listed under "App changes".

### Kit versions

- Captions: `captions_v4.py` from kit v4.1 (MAX_CHARS 40, 1,120 px width binding, quantity-aware line split; forced splits honoured) → `films/captions-v4/build/Captions.ass` and `caption-geometry.json`. Burned with kit v4.1.
- `caption_lint.py` (v4), `camera_budget.py` (v4), `verify_captions_v3.py` (kit v2.2) — copies in `films/captions-v4/`.
- Caption font: `/usr/share/fonts/truetype/lato/Lato-Bold.ttf`, 657,188 B, SHA-256 `bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b` (the only font passed as `--font` and the only Lato Bold in `fontsdir`; libass `fontselect: (Lato, 700, 0) -> Lato-Bold`).
- Burn-in (v3 §7.5, unchanged): `ffmpeg -i letterform-60s.mp4 -vf "ass=films/captions-v4/build/Captions.ass:fontsdir=/usr/share/fonts/truetype/lato" -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart letterform-60s-captioned.mp4`, after the kit's `-c copy -video_track_timescale 60000` remux of the clean film (`films/assemble60v4.sh`).

### App changes for v4 (Build 1.103, bundle hash `8408de759805386a5fc93e881b7cd4ff955289a1bccb6a059f89df7e7de0f8e6`)

Legibility only, proportional, no new features, no badges, labels or marketing chrome; redeployed in place as the same asset ([Letterform](https://www.perplexity.ai/computer/a/letterform-DFI51AvrQb2HEl5kaRMwug), asset `0c5239d4-0beb-41bd-8712-5e64691330ba`); hosted files equal the local `app/` byte for byte (`qa/app-bundle-hashes.txt`), hosted QA 206/206 (`qa/app-qa-hosted.txt`).

- `style.css`: body 13 → 14 px (so the smallest essential UI text is 21 px em at camera 1.0×); `.readout` and `.ctl-head output` 16 px (primary readouts 24 px em); `.pad .pad-label` 11 px; `.cell .nm` 11 px; `--rail-w` 328 px; `.detail .big` 240 px; `.draw-svg .guide-label` 32 (SVG units); new `.draw-svg.is-abc .node { stroke-width: 12 }` so skeleton nodes stay visible in the 52-letter Alphabet view.
- `app.js`: the Drawing view opens on the finished outline (`draw.t` = 1) with `a` selected on load; the Alphabet view gets 520 units of headroom in its viewBox and three-times hairline and node widths while it runs (`is-abc`).
- `index.html`: `#draw-scrub` starts at 1000 and the stage label reads "outline · final" to match.
- `style.css` (v4c, after the take-2 review): `.draw-controls` grid gap 10 → 34 px, so the Drawing view's transport row (Play, Replay, Alphabet, progress, Speed, overlays) sits 20 px higher and its moving progress thumb stays ≥ 24 px above the caption block at camera 1.0× (measured 33 px); the glyph picker stays at the bottom. Spacing only.
- `style.css` (v4d, after the take-4 review): `.transport .btn { font-size: 19px; line-height: 1.25; padding: 6px 14px }` and `#draw-play { min-width: 5em }`. The Drawing view's three primary controls (Play, Replay, Alphabet) read at 28.5 px em at camera 1.0×, so the Alphabet click needs no push-in (standard v4 section 3.2: a push-in is optional when the control already reads at ≥ 28 px em) and the whole 52-letter consequence is in frame from its first frame; the Play button keeps the width of "Pause", so the row no longer shifts when the animation runs. The row stays one line at 1280 px (last control ends at CSS x 932 of 952); its bottom edge stays at CSS y 576 (the picker is bottom-anchored). Type size and one min-width only.
- Previous deployed bundle hashes: `95d028a2…6e70` (v4c, transport-row spacing), `3c10c6db…58fd` (v4b, legibility pass), `8489e4b2…` (v4a), `d61dce3f…c396` (v3), `807b6994…e698`.

### Kit v2.2 verifier (`verify_captions_v3.py captioned --clean clean`): exit 0, fails []

Per-cue maxima over the first and last frame of each cue (the verifier samples both):

| cue | frames sampled | ring adjacent luma diff | ring adjacent rgb diff | ring outer rgb diff | diff outside block | fill (min) | ink height (expected) |
|---|---|---|---|---|---|---|---|
| 1 | 0, 299 | 2.11 | 4.92 | 1.75 | 0.072 | 0.9999 | 98 (97) |
| 2 | 300, 571 | 1.78 | 4.16 | 1.42 | 0.19 | 0.9997 | 106 (106) |
| 3 | 572, 869 | 1.23 | 3.81 | 1.32 | 0.357 | 0.9998 | 106 (106) |
| 4 | 870, 1079 | 1.05 | 5.13 | 1.06 | 0.132 | 0.9998 | 98 (97) |
| 5 | 1080, 1639 | 2.73 | 3.77 | 2.11 | 0.045 | 0.9996 | 106 (106) |
| 6 | 1640, 1843 | 1.84 | 4.26 | 0.93 | 0.124 | 0.9996 | 98 (97) |
| 7 | 1844, 2243 | 4.7 | 6.79 | 1.58 | 0.122 | 0.9997 | 106 (106) |
| 8 | 2244, 2485 | 1.42 | 2.87 | 1.13 | 0.1 | 0.9997 | 106 (106) |
| 9 | 2486, 2911 | 1.73 | 3.4 | 1.62 | 0.117 | 0.9998 | 106 (106) |
| 10 | 2912, 3119 | 1.8 | 3.38 | 1.77 | 0.118 | 0.9995 | 106 (106) |
| 11 | 3120, 3329 | 1.75 | 3.78 | 1.0 | 0.041 | 1.0 | 98 (97) |
| 12 | 3330, 3599 | 2.0 | 5.16 | 1.5 | 0.061 | 1.0 | 106 (106) |

Overall maxima: ring_adjacent_luma_diff 4.7, ring_adjacent_rgb_diff 6.79, ring_outer_rgb_diff 2.11, diff_outside_block 0.357 (mean absolute RGB difference between the captioned and clean frames outside the block).

### captions_v4.py (kit v4.1)

```
font /usr/share/fonts/truetype/lato/Lato-Bold.ttf
  sha256 bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b
  unitsPerEm 2000, usWinAscent 1974, usWinDescent 426 -> libass em 50.0 px at Fontsize 60
{
  "cues": 12,
  "ass": "/home/user/workspace/projects/computer-use-cases-59DkbY5.QouRVj3hdp4Q8g/files/builds/A4-letterform/films/captions-v4/build/Captions.ass",
  "problems": []
}
```

### camera_budget.py (`camera.json --frames 3600`)

```
{
 "frames": 3600,
 "wide_share": 0.8736,
 "wide_threshold": 1.25,
 "max_zoom": 1.8,
 "longest_zoomed_run_frames": 174,
 "zoomed_runs": [
  [
   609,
   782,
   1.8
  ],
  [
   1791,
   1885,
   1.5
  ],
  [
   2567,
   2658,
   1.8
  ],
  [
   2853,
   2946,
   1.8
  ]
 ],
 "opener_frames_at_1x": 3600,
 "fails": [],
 "notes": []
}
camera_budget exit 0
```

### caption_lint.py (`cues.json`)

```
ok    1 This is a brand new typeface, drawn from scratch.
ok    2 The grid holds every letter in the font, including the accented ones.
ok    3 The count at the top of the grid says 548 glyphs.
ok    4 Red dots mark the skeleton each letter is built on.
ok    5 Press Alphabet, and every skeleton grows into its shape.
ok    6 The tester sets live text in the new font.
ok    7 Drag the weight and width, and the letters change live.
ok    8 Any text typed here sets in the new font right away.
ok    9 With ligatures on, pairs like ffi merge into one glyph.
ok   10 Kerning pulls pairs like AV and To closer together.
ok   11 These pages are all set in the finished font.
ok   12 The font comes in fifteen styles, ExtraLight to Extended ExtraBold.
0 fails, 0 advisories
caption_lint exit 0
```

### Measured receipts (`qa/film_check60v4.py`, on the decoded delivered films)

#### 1. ffprobe and hashes

| file | codec | size | frames | rate | time base | pix_fmt | colour | streams | duration | SHA-256 | bytes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| films/master/letterform-60s-v4-master.mp4 | h264 | 1920x1080 | 3600 | 60/1 / 60/1 | 1/60000 | yuv444p | bt709/bt709/bt709/tv | 1 | 60.000 s | `9771dbe05d30ae8af8c6924044ad598b6f37048c416b48cdb49c06ab4e80529b` | 16,905,561 |
| films/letterform-60s.mp4 | h264 | 1920x1080 | 3600 | 60/1 / 60/1 | 1/60000 | yuv420p | bt709/bt709/bt709/tv | 1 | 60.000 s | `649155a1ebddfbec1d51b9f9673e8d1103637a8d8acaccff232d43ce8a801f3e` | 8,934,009 |
| films/letterform-60s-captioned.mp4 | h264 | 1920x1080 | 3600 | 60/1 / 60/1 | 1/15360 | yuv420p | bt709/bt709/bt709/tv | 1 | 60.000 s | `43c92efbab4dd43e90951099a4f36604d26dcf00492d349d5add084866fc7edd` | 9,112,875 |

- letterform-60s.mp4: PASS (3,600 frames, 60/1, 1920x1080, yuv420p, one video stream, no audio)
- letterform-60s-captioned.mp4: PASS (3,600 frames, 60/1, 1920x1080, yuv420p, one video stream, no audio)

#### 2. Capture

- Method: real application in headless Chromium; real mouse, wheel and keyboard events; composited pointer whose shape follows the product CSS cursor; static caret; camera boxes from cameraAt() rendered verbatim by render60v4.py; views changed by cuts (letterform.setView)
- Clock: one rAF flush at 1000 + g*1000/60 ms per frame g; CSS viewport 1280x720, deviceScaleFactor 3 (3840x2160 source PNG per frame), film scale at 1.0x = 1.5 film px per CSS px (an exact 2:1 Lanczos downscale of the capture, equal to a 1280x720 capture at deviceScaleFactor 1.5); pointer overlay scale 0.75 of the v3 shape.
- App frames: 3120 (f0-3119); specimen composite frames: 480 (f3120-3599); page errors: 0
- Pre-roll (logged before frame 0): axes 400/100, liga and kern off, size 76 px, sample text and Centre set before frame 0; the Glyphs view opens with a selected (product default since v4); state at f0: {"view": "glyphs", "selected": "a", "axes": [400, 100], "size": 76, "features": {"liga": false, "kern": false, "tnum": false, "zero": false, "frac": false, "case": false, "sups": false, "subs": false, "ordn": false}, "draw": {"glyph": "a", "t": 1, "alphabet": false}, "scrollTop": 0, "centre": true}
- Typed text: 'Official waffle AVATAR, Toronto'; sample before: 'Sphinx of black quartz, judge my vow.'; final state: {"features": {"liga": true, "kern": true, "tnum": false, "zero": false, "frac": false, "case": false, "sups": false, "subs": false, "ordn": false}, "axes": [700, 125], "text": "Official waffle AVATAR, Toronto", "liga": true, "kern": true}
- Grid scroll: {"pitch": 87.125, "target": 3398, "max": 5441, "first": "Ccedilla", "perRow": 8}

#### 3. Beat list (film frame = capture frame; input beats from the capture log)

| frame | time | action | detail | zoom |
|---|---|---|---|---|
| 280 | 4.67 s | move-start | {"from": [160, 716], "to": [560, 330], "frames": 80, "duration": 1.3333333333333333, "easing": "cubic smoothstep", "peakCssPxPerS": 625.4, "peakFilmPxPerSAt1x": 938, "drag": false, "label": "pointer enters from the bottom edge, well left of the caption block,  | 1.000 |
| 360 | 6.00 s | move-end | {"at": [560, 330], "label": "pointer enters from the bottom edge, well left of the caption block, to the glyph grid (from f280, inside the last 1.5 s of the opener; arrives f360)"} | 1.000 |
| 372 | 6.20 s | wheel-start | {"totalPx": 3398, "frames": 180, "easing": "cubic smoothstep displacement", "at": [560, 330]} | 1.000 |
| 552 | 9.20 s | wheel-end | {"scrollTop": 3398, "expected": 3398} | 1.000 |
| 870 | 14.50 s | cut | {"view": "drawing", "method": "letterform.setView between two frames (an edit cut; no tab click is shown)"} | 1.000 |
| 900 | 15.00 s | move-start | {"from": [560, 330], "to": [276.9, 557.1], "frames": 60, "duration": 1, "easing": "cubic smoothstep", "peakCssPxPerS": 544.4, "peakFilmPxPerSAt1x": 816.6, "drag": false, "label": "to the Alphabet button"} | 1.000 |
| 960 | 16.00 s | move-end | {"at": [276.9, 557.1], "label": "to the Alphabet button"} | 1.000 |
| 1080 | 18.00 s | pointerdown | {"at": [276.9, 557.1], "label": "Alphabet"} | 1.000 |
| 1081 | 18.02 s | pointerup | {"at": [276.9, 557.1], "label": "Alphabet"} | 1.000 |
| 1640 | 27.33 s | cut | {"view": "tester", "method": "letterform.setView between two frames (an edit cut; no tab click is shown)"} | 1.000 |
| 1650 | 27.50 s | move-start | {"from": [276.9, 557.1], "to": [1084.1, 396.8], "frames": 110, "duration": 1.8333333333333333, "easing": "cubic smoothstep", "peakCssPxPerS": 673.3, "peakFilmPxPerSAt1x": 1010, "drag": false, "label": "to the Regular dot on the design-space pad"} | 1.000 |
| 1760 | 29.33 s | move-end | {"at": [1084.1, 396.8], "label": "to the Regular dot on the design-space pad"} | 1.000 |
| 1844 | 30.73 s | pointerdown | {"at": [1084.1, 396.8], "label": "grab the Regular instance"} | 1.500 |
| 1844 | 30.73 s | move-start | {"from": [1084.1, 396.8], "to": [1001.7, 444.3], "frames": 72, "duration": 1.2, "easing": "cubic smoothstep", "peakCssPxPerS": 118.9, "peakFilmPxPerSAt1x": 178.3, "drag": true, "label": "weight 400->200, width 100->75"} | 1.500 |
| 1916 | 31.93 s | move-end | {"at": [1001.7, 444.3], "label": "weight 400->200, width 100->75"} | 1.001 |
| 1916 | 31.93 s | move-start | {"from": [1001.7, 444.3], "to": [1207.8, 349.4], "frames": 130, "duration": 2.1666666666666665, "easing": "cubic smoothstep", "peakCssPxPerS": 157.1, "peakFilmPxPerSAt1x": 235.6, "drag": true, "label": "weight 200->700, width 75->125 (Extended Bold)"} | 1.001 |
| 2046 | 34.10 s | move-end | {"at": [1207.8, 349.4], "label": "weight 200->700, width 75->125 (Extended Bold)"} | 1.000 |
| 2082 | 34.70 s | pointerup | {"at": [1207.8, 349.4], "label": "drop at 700/125"} | 1.000 |
| 2136 | 35.60 s | move-start | {"from": [1207.8, 349.4], "to": [476, 240], "frames": 90, "duration": 1.5, "easing": "cubic smoothstep", "peakCssPxPerS": 739.9, "peakFilmPxPerSAt1x": 1109.8, "drag": false, "label": "to the sample text"} | 1.000 |
| 2226 | 37.10 s | move-end | {"at": [476, 240], "label": "to the sample text"} | 1.000 |
| 2244 | 37.40 s | pointerdown | {"at": [476, 240], "label": "focus the sample"} | 1.000 |
| 2245 | 37.42 s | pointerup | {"at": [476, 240], "label": "focus the sample"} | 1.000 |
| 2248 | 37.47 s | key | {"key": "Control+A", "label": "select the sample text"} | 1.000 |
| 2252 | 37.53 s | move-start | {"from": [476, 240], "to": [476, 560], "frames": 40, "duration": 0.6666666666666666, "easing": "cubic smoothstep", "peakCssPxPerS": 720, "peakFilmPxPerSAt1x": 1080, "drag": false, "label": "park below the text"} | 1.000 |
| 2292 | 38.20 s | move-end | {"at": [476, 560], "label": "park below the text"} | 1.000 |
| 2486 | 41.43 s | move-start | {"from": [476, 560], "to": [980, 517.359375], "frames": 60, "duration": 1, "easing": "cubic smoothstep", "peakCssPxPerS": 758.7, "peakFilmPxPerSAt1x": 1138.1, "drag": false, "label": "to the Ligatures checkbox"} | 1.000 |
| 2546 | 42.43 s | move-end | {"at": [980, 517.359375], "label": "to the Ligatures checkbox"} | 1.002 |
| 2624 | 43.73 s | pointerdown | {"at": [980, 517.359375], "label": "Ligatures on"} | 1.800 |
| 2625 | 43.75 s | pointerup | {"at": [980, 517.359375], "label": "Ligatures on"} | 1.800 |
| 2756 | 45.93 s | move-start | {"from": [980, 517.359375], "to": [980, 539.953125], "frames": 40, "duration": 0.6666666666666666, "easing": "cubic smoothstep", "peakCssPxPerS": 50.8, "peakFilmPxPerSAt1x": 76.3, "drag": false, "label": "down to the Kerning checkbox"} | 1.000 |
| 2796 | 46.60 s | move-end | {"at": [980, 539.953125], "label": "down to the Kerning checkbox"} | 1.000 |
| 2912 | 48.53 s | pointerdown | {"at": [980, 539.953125], "label": "Kerning on"} | 1.800 |
| 2913 | 48.55 s | pointerup | {"at": [980, 539.953125], "label": "Kerning on"} | 1.800 |
| 2296-2458 | 38.27-40.97 s | typing | 31 characters, seeded rhythm (mulberry32 seed 1113): intervals [6, 6, 5, 4, 5, 4, 4, 5, 9, 5, 4, 5, 5, 4, 5, 10, 4, 6, 6, 4, 5, 5, 7, 10, 6, 6, 4, 4, 4, 5] frames, 11.1 chars/s mean | 1.000 |
| 870 / 1640 / 3120 / 3330 | 14.50 / 27.33 / 52.00 / 55.50 s | cut | Glyphs -> Drawing, Drawing -> Tester (both letterform.setView between two frames), Tester -> specimen spread A, spread A -> spread B | 1.000 |

##### Camera segments (camera.json, as executed by render60v4.py)

| from | to | frames | zoom | view | subject |
|---|---|---|---|---|---|
| 0 | 582 | 582 | 1.000 | glyphs | whole workspace: glyph grid, glyph detail with skeleton, axis rail (opener f0-371), then the wheel scroll (f372-551) |
| 582 | 642 | 60 | 1.000 -> 1.800 (cubic) | glyphs | push to the glyph-count readout |
| 642 | 750 | 108 | 1.800 | glyphs | glyph-count readout (548 glyphs) over the accented rows |
| 750 | 810 | 60 | 1.800 -> 1.000 (cubic) | glyphs | pull back to the whole workspace |
| 810 | 870 | 60 | 1.000 | glyphs | whole workspace, accented rows |
| 870 | 1640 | 770 | 1.000 | drawing | Drawing view wide throughout: re-establish (letter a with skeleton nodes and metric guides), pointer to Alphabet, click Alphabet at f1080 (label 19 px CSS = 28.5 px em, no push-in), the 52 letters grow from skeleton to outline (to f1500), then hold |
| 1640 | 1760 | 120 | 1.000 | tester | re-establish: Tester view, sample text, axis rail |
| 1760 | 1820 | 60 | 1.000 -> 1.500 (cubic) | tester | push to the design-space pad and its readouts |
| 1820 | 1851 | 31 | 1.500 | tester | pad: dwell and grab (f1844) |
| 1851 | 1923 | 72 | 1.500 -> 1.000 (cubic) | tester | pull back during the drag so the sample changes wide |
| 1923 | 2540 | 617 | 1.000 | tester | whole view: the drag lands on Extended Bold, the sample is retyped, the pointer goes to the Features list |
| 2540 | 2600 | 60 | 1.000 -> 1.800 (cubic) | tester | push to the Ligatures toggle |
| 2600 | 2626 | 26 | 1.800 | tester | Ligatures toggle: dwell and click (f2624) |
| 2626 | 2686 | 60 | 1.800 -> 1.000 (cubic) | tester | pull back from the click: the ffi and ffl ligatures show in the sample |
| 2686 | 2826 | 140 | 1.000 | tester | whole view: ligatures on, the ffi and ffl pairs are single glyphs; the pointer steps down to Kerning |
| 2826 | 2886 | 60 | 1.000 -> 1.800 (cubic) | tester | push to the Kerning toggle |
| 2886 | 2914 | 28 | 1.800 | tester | Kerning toggle: dwell and click (f2912) |
| 2914 | 2974 | 60 | 1.800 -> 1.000 (cubic) | tester | pull back from the click: AV and To sit closer in the sample |
| 2974 | 3120 | 146 | 1.000 | tester | whole view: kerning on, the finished sample holds |
| 3120 | 3330 | 210 | 1.000 | specimen-a | specimen pages 1, 6 and 8 at 1.0 px per pt (100 %) |
| 3330 | 3600 | 270 | 1.000 | specimen-b | specimen pages 3, 4 and 5 at 1.0 px per pt (100 %) |

Settle between consecutive camera moves (must be >= 24 frames = 0.4 s): f642-f750 = 108, f810-f1760 = 950, f1820-f1851 = 31, f1923-f2540 = 617, f2600-f2626 = 26, f2686-f2826 = 140, f2886-f2914 = 28
Camera move durations (push-ins and pull-backs must be 0.8-1.5 s): 1.00 s, 1.00 s, 1.00 s, 1.20 s, 1.00 s, 1.00 s, 1.00 s, 1.00 s

#### 4. Native beat frames (decoded from the clean film) and measured text

##### Smallest essential text and primary readouts at 1.0x (frame 60, the opener)

- f60 (1.00 s, zoom 1.000): rail label "Weight" (smallest essential UI text, 14 CSS px): 'Weight400' em 21.0 px, measured ink height 22 px (box 429 px wide) at film (1460,105)-(1890,139)
- f60 (1.00 s, zoom 1.000): weight readout (primary readout, 16 CSS px): '400' em 24.0 px, measured ink height 19 px (box 39 px wide) at film (1536,105)-(1890,139)
- f60 (1.00 s, zoom 1.000): glyph-count readout (14 CSS px): '548 glyphs · 477 encoded · live at the current ins' em 21.0 px, measured ink height 20 px (box 486 px wide) at film (30,106)-(518,136)
- f60 (1.00 s, zoom 1.000): tab label: 'Tester' em 21.0 px, measured ink height 15 px (box 55 px wide) at film (1491,13)-(1584,63)
- f60 (1.00 s, zoom 1.000): detail heading: 'a' em 27.0 px, measured ink height 16 px (box 13 px wide) at film (980,105)-(1398,143)

##### Push-in beats (clicked control label >= 28 px em, readout numbers >= 32 px em), and the one wide click (section 3.2: a push-in is optional when the control already reads at >= 28 px em)

- f641 (10.68 s, zoom 1.800): glyph-count readout at the push-in: '548 glyphs · 477 encoded · live at the current ins' em 37.8 px, measured ink height 36 px (box 875 px wide) at film (54,51)-(932,104)
- f1079 (17.98 s, zoom 1.000): Alphabet button label at the dwell before the click (camera 1.0x, 19 CSS px): 'Alphabet' em 28.5 px, measured ink height 58 px (box 157 px wide) at film (337,807)-(493,864)
- f1080 (18.00 s, zoom 1.000): Alphabet button label at the click (camera 1.0x, no push-in): 'Alphabet' em 28.5 px, measured ink height 58 px (box 157 px wide) at film (337,807)-(493,864)
- f1844 (30.73 s, zoom 1.500): rail label at the grab: 'Weight400' em 31.5 px, measured ink height 33 px (box 644 px wide) at film (1229,40)-(1875,91)
- f1844 (30.73 s, zoom 1.500): weight readout at the grab: '400' em 36.0 px, measured ink height 27 px (box 59 px wide) at film (1345,40)-(1875,91)
- f1844 (30.73 s, zoom 1.500): pad heading at the grab: 'Design spaceRegular' em 31.5 px, measured ink height 35 px (box 642 px wide) at film (1229,580)-(1875,631)
- f2624 (43.73 s, zoom 1.800): Ligatures toggle label at the click: 'Ligaturesfi fl' em 37.8 px, measured ink height 48 px (box 773 px wide) at film (1091,560)-(1866,613)
- f2912 (48.53 s, zoom 1.800): Kerning toggle label at the click: 'KerningAV To' em 37.8 px, measured ink height 47 px (box 773 px wide) at film (1091,621)-(1866,674)

##### Sample text (the consequence shown wide)

- f1640: sample line boxes (CSS) [[104.5, 100.2, 742.9, 91], [847.5, 100.2, 18.3, 91], [242.7, 185.3, 466.6, 91]]; first line at film y 150, line height 136 px, font size 76 CSS px = 114 px em
- f2082: sample line boxes (CSS) [[155.4, 100.2, 641.1, 91], [796.6, 100.2, 23.5, 91], [126.5, 185.3, 698.9, 91], [825.5, 185.3, 23.5, 91], [381.1, 270.4, 189.9, 91]]; first line at film y 150, line height 136 px, font size 76 CSS px = 114 px em
- f2459: sample line boxes (CSS) [[180.7, 100.2, 590.7, 91], [771.3, 100.2, 23.5, 91], [101, 185.3, 750, 91]]; first line at film y 150, line height 136 px, font size 76 CSS px = 114 px em
- f2685: sample line boxes (CSS) [[180.7, 100.2, 590.7, 91], [771.3, 100.2, 23.5, 91], [101, 185.3, 750, 91]]; first line at film y 150, line height 136 px, font size 76 CSS px = 114 px em
- f2973: sample line boxes (CSS) [[180.7, 100.2, 590.7, 91], [771.3, 100.2, 23.5, 91], [101, 185.3, 750, 91]]; first line at film y 150, line height 136 px, font size 76 CSS px = 114 px em
- pair boxes (CSS px) with ligatures and kerning off: {"Offi": [180.7, 100.2, 146.5, 91], "ffi": [243.7, 100.2, 83.5, 91], "ffl": [621.5, 100.2, 96.8, 91], "AV": [101, 185.3, 124.4, 91], "VA": [166.2, 185.3, 124.4, 91], "AT": [225.4, 185.3, 121.2, 91], "To": [512.3, 185.3, 109.1, 91], "Toronto": [512.3, 185.3, 338.7, 91]}
- after Ligatures on: {"Offi": [189.8, 100.2, 138.2, 91], "ffl": [622.3, 100.2, 86.8, 91], "AV": [101, 185.3, 124.4, 91], "VA": [166.2, 185.3, 124.4, 91], "AT": [225.4, 185.3, 121.2, 91], "To": [512.3, 185.3, 109.1, 91], "Toronto": [512.3, 185.3, 338.7, 91]}
- after Kerning on: {"Offi": [190.2, 100.2, 138.2, 91], "ffl": [621.9, 100.2, 86.8, 91], "AV": [122, 185.3, 108.9, 91], "VA": [179.4, 185.3, 109.4, 91], "AT": [230.8, 185.3, 106.8, 91], "To": [503.3, 185.3, 100.6, 91], "Toronto": [503.3, 185.3, 326.7, 91]}
- receipts: 'Offi' width 146.5 -> 138.2 CSS px with ligatures (ffi becomes one glyph); 'AV' width 124.4 -> 108.9 and 'To' width 109.1 -> 100.6 CSS px with kerning

#### 5. Clearance: pointer, click targets and typed text vs the caption block (>= 24 px)

- minimum distance between the pointer glyph and the active caption block over all pointer-visible frames: 27 px at f314 (cursor pointer, hotspot at film (484, 838), block (521, 891, 1397, 1018))
- f1080 Alphabet: hotspot 206 px from the block
- f1081 Alphabet: hotspot 206 px from the block
- f1844 grab the Regular instance: hotspot 231 px from the block
- f2082 drop at 700/125: hotspot 647 px from the block
- f2244 focus the sample: hotspot 531 px from the block
- f2245 focus the sample: hotspot 531 px from the block
- f2624 Ligatures on: hotspot 304 px from the block
- f2625 Ligatures on: hotspot 304 px from the block
- f2912 Kerning on: hotspot 243 px from the block
- f2913 Kerning on: hotspot 243 px from the block
- f2459 typed text line film box (271,150)-(1157,287): 604 px above the block top 891
- f2459 typed text line film box (1157,150)-(1192,287): 604 px above the block top 891
- f2459 typed text line film box (152,278)-(1276,414): 477 px above the block top 891
- f1000 transport row bottom (the Alphabet button's bottom edge, CSS y 576.0) at film y 864; 27 px above the block top 891 (camera 1.00x)
- f1079 transport row bottom (the Alphabet button's bottom edge, CSS y 576.0) at film y 864; 27 px above the block top 891 (camera 1.00x)
- f1080 transport row bottom (the Alphabet button's bottom edge, CSS y 576.0) at film y 864; 27 px above the block top 891 (camera 1.00x)
- f1081 transport row bottom (the Alphabet button's bottom edge, CSS y 576.0) at film y 864; 27 px above the block top 891 (camera 1.00x)
- f1081 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- f1100 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- f1200 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- f1300 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- f1400 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- f1500 progress-slider ink (thumb ring and track) spans CSS y 548.0-566.0 = film y 822-849 at 1.0x; 42 px above the block top 891
- caption blocks: cue 1 x 621-1298 y 891-1009; cue 2 x 521-1397 y 891-1018; cue 3 x 641-1279 y 891-1018; cue 4 x 641-1280 y 891-1009; cue 5 x 614-1305 y 891-1018; cue 6 x 716-1203 y 891-1009; cue 7 x 643-1279 y 891-1018; cue 8 x 645-1275 y 891-1018; cue 9 x 639-1280 y 891-1018; cue 10 x 654-1270 y 891-1018; cue 11 x 693-1228 y 891-1009; cue 12 x 567-1355 y 891-1018

#### 6. Motion profile (decoded clean film, 1920x1080 luma)

- decoded frames: 3600; frame-to-frame mean |dY| computed for 3599 pairs
- still pairs (mean |dY| < 0.05): 2404 (66.8 %); moving pairs: 1195
- hard cuts (mean |dY| > 20): at frames [3120, 3330] (the specimen cuts; the in-app view switches at 870 and 1640 keep the same chrome: dY 15.08 and 18.79)
- per-second table (mean |dY| over the 60 frame pairs of each second, zoom at the start of the second):

| s | mean dY | max dY | zoom |
|---|---|---|---|
| 0 | 0.00 | 0.00 | 1.00 |
| 1 | 0.00 | 0.00 | 1.00 |
| 2 | 0.00 | 0.00 | 1.00 |
| 3 | 0.00 | 0.00 | 1.00 |
| 4 | 0.01 | 0.24 | 1.00 |
| 5 | 0.06 | 0.12 | 1.00 |
| 6 | 2.89 | 4.17 | 1.00 |
| 7 | 5.26 | 5.95 | 1.00 |
| 8 | 4.69 | 5.39 | 1.00 |
| 9 | 2.23 | 9.70 | 1.00 |
| 10 | 6.67 | 14.29 | 1.07 |
| 11 | 0.01 | 0.01 | 1.80 |
| 12 | 4.07 | 14.36 | 1.80 |
| 13 | 4.15 | 13.65 | 1.32 |
| 14 | 0.25 | 15.08 | 1.00 |
| 15 | 0.04 | 0.08 | 1.00 |
| 16 | 0.00 | 0.19 | 1.00 |
| 17 | 0.00 | 0.00 | 1.00 |
| 18 | 0.14 | 6.52 | 1.00 |
| 19 | 0.08 | 0.19 | 1.00 |
| 20 | 0.11 | 0.26 | 1.00 |
| 21 | 0.10 | 0.19 | 1.00 |
| 22 | 0.09 | 0.20 | 1.00 |
| 23 | 0.08 | 0.17 | 1.00 |
| 24 | 0.04 | 0.15 | 1.00 |
| 25 | 0.02 | 0.82 | 1.00 |
| 26 | 0.00 | 0.00 | 1.00 |
| 27 | 0.32 | 18.79 | 1.00 |
| 28 | 0.02 | 0.05 | 1.00 |
| 29 | 4.86 | 11.26 | 1.00 |
| 30 | 1.47 | 10.06 | 1.42 |
| 31 | 5.95 | 9.61 | 1.50 |
| 32 | 0.94 | 5.48 | 1.00 |
| 33 | 1.20 | 8.54 | 1.00 |
| 34 | 0.00 | 0.03 | 1.00 |
| 35 | 0.01 | 0.04 | 1.00 |
| 36 | 0.03 | 0.05 | 1.00 |
| 37 | 0.08 | 4.18 | 1.00 |
| 38 | 0.39 | 11.32 | 1.00 |
| 39 | 0.68 | 6.36 | 1.00 |
| 40 | 0.61 | 4.71 | 1.00 |
| 41 | 0.01 | 0.13 | 1.00 |
| 42 | 5.28 | 14.83 | 1.00 |
| 43 | 1.13 | 3.75 | 1.66 |
| 44 | 5.68 | 14.74 | 1.74 |
| 45 | 0.00 | 0.19 | 1.00 |
| 46 | 0.00 | 0.03 | 1.00 |
| 47 | 5.97 | 14.74 | 1.00 |
| 48 | 1.27 | 7.07 | 1.80 |
| 49 | 4.81 | 14.64 | 1.47 |
| 50 | 0.00 | 0.20 | 1.00 |
| 51 | 0.00 | 0.00 | 1.00 |
| 52 | 0.47 | 27.89 | 1.00 |
| 53 | 0.00 | 0.00 | 1.00 |
| 54 | 0.00 | 0.00 | 1.00 |
| 55 | 0.35 | 21.28 | 1.00 |
| 56 | 0.00 | 0.00 | 1.00 |
| 57 | 0.00 | 0.00 | 1.00 |
| 58 | 0.00 | 0.00 | 1.00 |
| 59 | 0.01 | 0.30 | 1.00 |

- frames inside camera moves whose luma equals the previous frame (would indicate a dropped/padded frame): 26 of 492
- frames inside the Alphabet animation (f1081-1500) whose whole-frame mean |dY| to the previous frame is below 0.05 (identical or a sub-threshold change such as one thin stroke growing): 98 of 420
- the same frames on the capture PNGs (stage region, exact comparison): 2 of 420 identical to the previous frame (at f1496, f1498: the last letter's outline reveal at the end of the 7 s run); smallest change 92 px at f1086

#### 7. Caption table (caption-geometry.json, kit v4.1 captions_v4.py)

| # | text | lines | chars | in | out | duration | beat |
|---|---|---|---|---|---|---|---|
| 1 | This is a brand new typeface, drawn from scratch. | This is a brand new typeface, / drawn from scratch. | 49 (29/19) | 0 | 300 | 5.00 s | opener: the whole Glyphs workspace at 1.0x, populated; the pointer enters from the bottom edge at f280 and reaches the grid at f360 |
| 2 | The grid holds every letter in the font, including the accented ones. | The grid holds every letter in the font, / including the accented ones. | 69 (40/28) | 300 | 572 | 4.53 s | wheel scroll through the glyph grid (f372-551), wide |
| 3 | The count at the top of the grid says 548 glyphs. | The count at the top / of the grid says 548 glyphs. | 49 (20/28) | 572 | 870 | 4.97 s | push-in to the glyph-count readout (f582-642, 1.8x), hold, pull back (f750-810) |
| 4 | Red dots mark the skeleton each letter is built on. | Red dots mark the skeleton / each letter is built on. | 51 (26/24) | 870 | 1080 | 3.50 s | cut to the Drawing view at 1.0x: the letter a over its skeleton, its nodes as red dots; pointer to the Alphabet button (f900-960), dwell |
| 5 | Press Alphabet, and every skeleton grows into its shape. | Press Alphabet, and every / skeleton grows into its shape. | 56 (25/30) | 1080 | 1640 | 9.33 s | click Alphabet wide (f1080; label 19 px CSS = 28.5 px em, no push-in); the 52 letters draw from skeleton to outline (to f1500), hold |
| 6 | The tester sets live text in the new font. | The tester sets live / text in the new font. | 42 (20/21) | 1640 | 1844 | 3.40 s | cut to the Tester view; pointer to the design-space pad; push-in (f1760-1820) |
| 7 | Drag the weight and width, and the letters change live. | Drag the weight and width, / and the letters change live. | 55 (26/28) | 1844 | 2244 | 6.67 s | grab the Regular dot (f1844), drag 400/100 -> 200/75 -> 700/125, pull back during the drag (f1851-1923), release f2082 |
| 8 | Any text typed here sets in the new font right away. | Any text typed here sets / in the new font right away. | 52 (24/27) | 2244 | 2486 | 4.03 s | click into the sample (f2244), select all, type Official waffle AVATAR, Toronto (f2296-2459), wide |
| 9 | With ligatures on, pairs like ffi merge into one glyph. | With ligatures on, pairs like / ffi merge into one glyph. | 55 (29/25) | 2486 | 2912 | 7.10 s | pointer to Ligatures; push-in (f2540-2600); click f2624; pull back from the click (f2626-2686): ffi and ffl join; pointer to Kerning |
| 10 | Kerning pulls pairs like AV and To closer together. | Kerning pulls pairs like AV / and To closer together. | 51 (27/23) | 2912 | 3120 | 3.47 s | push-in (f2826-2886); click Kerning f2912; pull back from the click (f2914-2974); wide hold |
| 11 | These pages are all set in the finished font. | These pages are all set / in the finished font. | 45 (23/21) | 3120 | 3330 | 3.50 s | cut to specimen spread A: pages 1, 6 and 8 at 100 % |
| 12 | The font comes in fifteen styles, ExtraLight to Extended ExtraBold. | The font comes in fifteen styles, / ExtraLight to Extended ExtraBold. | 67 (33/33) | 3330 | 3600 | 4.50 s | specimen spread B: pages 3, 4 and 5 (the fifteen named instances) at 100 % |

- font Lato-Bold.ttf sha256 bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b, libass em 50.0 px; treatment: v3 bottom block: Lato Bold 60 px white, opaque #1b262b block r=7 fitted to rendered ink with 18/10 px padding, anchor (960,1009), hard in/out
- geometry problems: []

#### 8. Stills

- contact sheet (one frame per second, from the clean film): films/logs60v4/contact-sheet-1fps.png
- native-1x-frame-0060.png (clean film, f60, zoom 1.000)
- final-frame-3599.png (clean film, f3599, zoom 1.000)
- captioned-frame-0060.png, captioned-final-frame-3599.png (captioned film)
- native beat frames (clean film): films/logs60v4/beats/c-NNNN.png for frames [0, 60, 299, 300, 372, 551, 641, 870, 1000, 1079, 1080, 1081, 1090, 1100, 1200, 1300, 1400, 1500, 1639, 1640, 1844, 1845, 1950, 2082, 2244, 2245, 2248, 2296, 2350, 2459, 2600, 2624, 2625, 2640, 2685, 2756, 2886, 2912, 2913, 2930, 2973, 3119, 3120, 3330, 3599]

## Films (v3) — what they show (superseded by v4, kept)

Same 2,700 frames in both films, full frame 1920×1080. Captions sit in one opaque block at the bottom centre; every shot is composed so the pointer, click target, typed text, dragged pad and every value a caption names stay ≥ 24 px clear of the block (measured per frame, receipt §7). Frame numbers are film frames at 60 fps.

| s | frames | shot | caption (captioned film) |
| --- | --- | --- | --- |
| 0–5.7 | 0–341 | Drawing view at 1.42× centred on (810, 500): the `a` built from skeleton to outline (app animation on the stepped clock, finished at f231; picture beat); baseline at y 838, the descender guide runs under the block | 1 · A new typeface, / built from scratch. |
| 5.7–13.7 | 342–821 | Design-space pad close-up 5.0→5.3×: approach, dwell, press on the 200/75 node (f450); one eased pull to a 3.6× coframe (two-line sample beside the Weight/Width readouts and the pad on a 533×300 board, native crops of the same frame; the pad grid ends at y 763); 2.0 s drag to 800/125 with sample, readouts and instance name recomputing on 98 of 120 frames; release (f750) on “800 · 125 · Extended ExtraBold” | 2 · Drag to change weight / and width, live. |
| 13.7–21 | 822–1259 | Tester field 2.2→2.6× (frames byte-identical to v2.1): approach, dwell, click (f948), pointer parks below the lines, Ctrl+A, “Official waffle AVATAR, Tokyo” typed at 11.0 cps (29 keystrokes, intervals 4–10 frames, f1034–1187), typed result held 1.2 s | 3 · Type any text to test it. |
| 21–28 | 1260–1679 | One continuous shot: sample band 2.2→2.6× (y 0–440; the two lines keep 42 px above and below) above the Features rows 3.2→3.9× (centred in y 440–870; native crops of the same frame); Ligatures clicked (f1386: ffi and ffl ligate in the sample, fi fl in the row), pointer moves down, Kerning clicked (f1530: AVATAR, Tokyo tightens) | 4 · Ligatures: ffi and ffl / each become one glyph. → 5 · Kerning: AV and To close up. (change inside the post-click hold, f1464) |
| 28–35 | 1680–2099 | Glyphs view at 1× (picture beat): 110 arrow keys move the instance 200/75 → 800/125 and all 548 cells redraw; 1.0 s push to 3.77× on the page's top-left corner (the visible box's edges are tweened with the smoothstep, so the page's left edge stays on the frame's left edge throughout): the readout “Extended ExtraBold · wght 800 · wdth 125 / 548 glyphs · 477 encoded” with two complete glyph rows and no partial column (the second row's name labels and cell bottoms pass behind the block, its glyphs end 60 px above it; the third row's cell tops show at the frame bottom); cut to the Latin Extended cluster around the selected Ď: a bounded native crop of 7 complete columns × 3 complete rows at 3.5× (Ď in the centre cell, half-gutter paper margins, pasted centred at y 45–905 on the same paper; 46 px of paper between the grid and the block, nothing under or within 24 px of it) | 6 · 548 glyphs cover 26 languages. |
| 35–39.2 | 2100–2351 | Specimen page 6 waterfall: “Quiet forms” at 56, 64 and 72 pt set in the compiled font, top edge pinned at 489.5 pt, slow push 2.64→2.72×; paper only in the block band (the 72 pt line ends 31 px above the block), folio out of frame | 7 · The specimen is set / in the compiled font. |
| 39.2–45 | 2352–2699 | Specimen page 1 footer: GLYPHS 548 · CHARACTERS 477 · INSTANCES 15 · MASTERS 9 · LANGUAGES 26 centred (347.75 pt), push 3.8→3.95×, held 4.0 s; the FAMILY column and the page number stay outside the frame, the rule spans the full width | 8 · 548 glyphs, 9 masters, / 26 languages. Version 1.103. |

Captions (v3 treatment): Lato Bold 60 px (`films/captions-v3/fonts/Lato-Bold.ttf`, version 2.015, sha256 `bf1b8130…574a7b`, the reference film's own copy, OFL), white, no outline or shadow; one opaque `#1b262b` block per caption, corner radius 7, fitted to the rendered glyph pixels with 18 px side and 10 px top/bottom padding; anchor bottom-centre (960, 1009), lines 60 px apart; one-line blocks 66–67 px tall, two-line 118–127 px, block bottom y 1016–1017; no motion, hard in/out on one frame, caption 1 from frame 0, caption 8 to frame 2,699, no gaps; changes at the cuts, plus C4→C5 inside the post-click hold (f1464); none during a camera move. Words are the approved v2.1 texts unchanged (their rewrites from the parent's script are explained in `qa/film45/review-v21.md` and the v2.1 handoff history). Generated by the kit: `captions_v3.py cues.json --fps 60 --frames 2700 --font Lato-Bold.ttf --out build/` → `Captions.ass` + `caption-geometry.json` (problems: none); burned in with `ffmpeg … -vf "ass=build/Captions.ass:fontsdir=fonts"` from the clean master (log shows `fontselect: (Lato, 700, 0) -> Lato-Bold`); `verify_captions_v3.py captioned.mp4 build/caption-geometry.json --clean clean.mp4` exits 0 with no fails.

Disclosures: frame-stepped capture (page clock advanced exactly 1/60 s per frame — not measured real-time GPU performance); pointer composited at the real input position in the product's own CSS cursor shape (arrow flickers shorter than 6 frames suppressed in the 3 px row gap, f1476–1505); non-blinking caret at the real selection position; editorial composites built from native crops of the same captured frame (drag coframe, tester padding, features band + rows, glyphs readout and cluster, one PDF crop at a time); the caption block covers footage by design — under it lie only inert parts (letter: the descender guide line; drag: board colour; tester: paper; features: chalk; glyphs: at 1× the live grid's cells as in any grid viewport, in the readout close-up the second row's name labels Odieresis / Ugrave / Uacute with the bottoms of their cells — no label is cut by a block edge — and in the cluster nothing but paper; specimen: paper only; measured per segment in the receipt's pixel census); colour: the PNG→YUV conversion now uses the BT.709 matrix and the streams are tagged bt709 (v2.1 was converted with swscale's default BT.601 matrix and untagged — the difference is a slight hue shift on saturated colours, none of which the film has); the Glyphs keyboard change is a picture beat at 1× whose readout is read at 3.78×; between keystrokes the field is static by construction; the camera pushes settle 0–0.2 s before the pointer approaches begin (the §3 settle rule is applied between camera moves).

## films-v3.md — 45 s film receipts (v3, superseded, kept)

<!-- films-v3 -->
### 1. ffprobe
letterform-45s-captioned.mp4: h264 (High) 1920x1080 r_frame_rate=60/1 avg_frame_rate=60/1 nb_frames=2700 duration=45.000 nb_streams=1 pix_fmt=yuv420p colour=bt709/bt709/bt709 moov_before_mdat=True
letterform-45s-captioned-master.mp4: h264 (High 4:4:4 Predictive) 1920x1080 r_frame_rate=60/1 avg_frame_rate=60/1 nb_frames=2700 duration=45.000 nb_streams=1 pix_fmt=yuv444p colour=bt709/bt709/bt709 moov_before_mdat=False
letterform-45s.mp4: h264 (High) 1920x1080 r_frame_rate=60/1 avg_frame_rate=60/1 nb_frames=2700 duration=45.000 nb_streams=1 pix_fmt=yuv420p colour=bt709/bt709/bt709 moov_before_mdat=True
letterform-45s-master.mp4: h264 (High 4:4:4 Predictive) 1920x1080 r_frame_rate=60/1 avg_frame_rate=60/1 nb_frames=2700 duration=45.000 nb_streams=1 pix_fmt=yuv444p colour=bt709/bt709/bt709 moov_before_mdat=False
letterform-45s-captioned.mp4 conforms to section 1 (1920x1080, 60/1 constant, 2700 frames, 45.000 s, one stream, no audio, H.264 yuv420p, +faststart): PASS
letterform-45s.mp4 conforms to section 1 (1920x1080, 60/1 constant, 2700 frames, 45.000 s, one stream, no audio, H.264 yuv420p, +faststart): PASS
Encode settings (films/assemble45v3.sh): clean master = PNG sequence -> libx264 -preset slow -crf 10 -pix_fmt yuv444p (BT.709 matrix via scale=out_color_matrix=bt709, tagged bt709); clean
delivery = the same PNG sequence -> -crf 14 -pix_fmt yuv420p -movflags +faststart; captioned delivery = clean master -> ass=Captions.ass:fontsdir=<Lato> -> -crf 14 yuv420p +faststart (the v3
kit command with CRF 14 instead of 17); captioned master = clean master -> ass -> -crf 10 yuv444p. All -an -r 60. Nothing is spliced, re-timed or padded.

### 2. SHA-256 and size
films/letterform-45s-captioned.mp4  6836417 bytes  sha256 2405cb081c35248c1cfaa57df91c7914d3fe0812978e457b423f06069db81090
films/master/letterform-45s-captioned-master.mp4  9492614 bytes  sha256 ff1a83a1be5984c3cfeec6c136d6634b43baf8fe091a72b8ce0b75ea9d098f1a
films/letterform-45s.mp4  6703871 bytes  sha256 533216b5251083eb276ffac7b2a8b2d9727aad7f9dbf7b78285d355979965999
films/master/letterform-45s-master.mp4  9411423 bytes  sha256 1fff232965f0efbd2a9f37dc67dc694163c452ffeae125543dd8780dda10d5de
films/captions-v3/fonts/Lato-Bold.ttf  657188 bytes  sha256 bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b
films/captions-v3/fonts/OFL.txt  4407 bytes  sha256 74ba064d03f1f1c4a952da936c3eb71866c34404916734de3cae73b34357e59e
films/captions-v3/cues.json  614 bytes  sha256 8075c775fe21ede45eae7c67b801d7ecbdd3751fd558a840be2a862bc97d5e2a
films/captions-v3/build/Captions.ass  3039 bytes  sha256 2d91e9b9d1772201d8e6c2272d7ff9d98a8c3ceca47acf816e629f6a478f5b07
films/captions-v3/build/caption-geometry.json  4409 bytes  sha256 47ebc0dc464ad77b90e72bd7dd6c1eb81f025ed27d68fe300adccfb7f753d00a
films/captions-v3/captions_v3.py  11903 bytes  sha256 5f955a4ab09b6970a9a63c762848f14737caef0a9800c2180d6b82b52c83aa4f
films/captions-v3/verify_captions_v3.py  11753 bytes  sha256 183ec4446cf0e531110822fee8238b46c8745777871dd33fe036c7875c97a014

### 3. Beat list (frame = film frame at 60 fps; every frame number below is read from the capture logs or the renderer camera tables)
| start s | end s | frames | subject | camera | pointer / input | cursor |
|---|---|---|---|---|---|---|
| 0.00 | 5.70 | 0–341 | Drawing view: the a built from skeleton to outline (app animation on the stepped clock; captured 360 frames, the first 342 cut in); caption 1 from frame 0 | 1.42x static | none (picture beat) | none; Play pre-rolled |
| 5.70 | 5.90 | 342–353 | Design-space pad close-up (native rail crop), crosshair parked; caption 2 from f342 (hard in) | 5.00x hold | parked | crosshair |
| 5.90 | 6.70 | 354–401 | Push onto the pad | 5.00→5.30x, smoothstep (3t²−2t³) in log zoom, 0.8 s | parked | crosshair |
| 6.70 | 7.10 | 402–425 | Approach the 200/75 node | 5.30x hold | move 0.4 s, planned peak 270 px/s at 1x | crosshair |
| 7.10 | 7.50 | 426–449 | Dwell on the node | 5.30x hold | dwell 0.4 s | crosshair |
| 7.50 | 8.10 | 450–485 | Press: grab the instance | 5.30x hold 0.6 s after the press | pointerdown at 7.50 s (f450) | grabbing |
| 8.10 | 9.10 | 486–545 | Pull to the coframe: two-line sample, Weight/Width readouts and the pad (native crops of the same frame) | 5.30→3.60x, smoothstep (3t²−2t³) in log zoom, 1.0 s | still (button held) | grabbing |
| 9.10 | 9.50 | 546–569 | Coframe settles | 3.60x hold 0.4 s | still | grabbing |
| 9.50 | 11.50 | 570–689 | Drag 200/75→800/125: sample, Weight, Width and instance name recompute every frame | 3.60x hold | drag 2.0 s, planned peak 179 px/s at 1x | grabbing |
| 11.50 | 12.50 | 690–749 | Dragged instance held | 3.60x hold 1.0 s | still (button held) | grabbing |
| 12.50 | 13.70 | 750–821 | Release at 800/125: Weight 800 · Width 125 · Extended ExtraBold; caption 2 to f821 | 3.60x hold 1.2 s | pointerup at 12.50 s (f750) | crosshair |
| 13.70 | 13.90 | 822–833 | Tester sample field; caption 3 from f822 (hard in) | 2.20x hold | parked | text |
| 13.90 | 14.90 | 834–893 | Push onto the field | 2.20→2.60x, smoothstep (3t²−2t³) in log zoom, 1.0 s | parked | text |
| 14.90 | 15.40 | 894–923 | Approach the field | 2.60x hold | move 0.5 s, planned peak 663 px/s at 1x | text |
| 15.40 | 15.80 | 924–947 | Dwell | 2.60x hold | dwell 0.4 s | text |
| 15.80 | 16.93 | 948–1015 | Click into the field (caret at the click); pointer parks below the lines | 2.60x hold | click at 15.80 s (f948); park move f950–1015, planned peak 731 px/s at 1x | text |
| 16.93 | 17.23 | 1016–1033 | Select all: both lines highlighted | 2.60x hold 0.3 s | Ctrl+A at f1016 | text |
| 17.23 | 19.80 | 1034–1187 | Typing “Official waffle AVATAR, Tokyo” replaces the selection | 2.60x hold | 29 characters f1034–1187 (intervals in section 6), caret visible | text |
| 19.80 | 21.00 | 1188–1259 | Typed result; caption 3 to f1259 | 2.60x hold 1.20 s | none | text |
| 21.00 | 21.20 | 1260–1271 | Features: sample band above, Features rows below (two native crops of the same frame; one continuous shot to f1679); caption 4 from f1260 (hard in) | sample 2.20x, controls 3.2x hold | parked right of the Ligatures row | pointer |
| 21.20 | 22.00 | 1272–1319 | Push | 2.20→2.60x, controls 3.2→3.9x, smoothstep (3t²−2t³) in log zoom, 0.8 s | parked | pointer |
| 22.00 | 22.20 | 1320–1331 | Settle | controls 3.9x hold 0.2 s | still | pointer |
| 22.20 | 22.70 | 1332–1361 | Approach the Ligatures label | hold | move 0.5 s, planned peak 330 px/s at 1x | pointer |
| 22.70 | 23.10 | 1362–1385 | Dwell | hold | dwell 0.4 s | pointer |
| 23.10 | 24.60 | 1386–1475 | Ligatures on: ffi and ffl ligate in the sample, fi fl in the row; caption 4→5 change at f1464 inside this hold | hold 1.5 s | click at 23.10 s (f1386) | pointer |
| 24.60 | 25.10 | 1476–1505 | Down to the Kerning label (no cut) | hold | move 0.5 s, planned peak 66 px/s at 1x | pointer (shape held across the 3 px row gap) |
| 25.10 | 25.50 | 1506–1529 | Dwell | hold | dwell 0.4 s | pointer |
| 25.50 | 28.00 | 1530–1679 | Kerning on: AVATAR, Tokyo tightens; caption 5 to f1679 | hold 2.5 s | click at 25.50 s (f1530) | pointer |
| 28.00 | 28.60 | 1680–1715 | Glyphs view at 1x, first rows Agrave…, Ď selected; caption 6 from f1680 (hard in) | 1x hold (picture beat) | none | crosshair resting on the pad |
| 28.60 | 29.60 | 1716–1775 | Instance moves 200/75→800/125 from the keyboard; all 548 cells redraw | 1x hold | 110 key events on the focused pad (f1716–1775) | resting |
| 29.60 | 30.20 | 1776–1811 | Whole grid at the new instance | 1x hold 0.6 s | none | resting |
| 30.20 | 31.20 | 1812–1871 | Push into the readout: Extended ExtraBold · wght 800 · wdth 125; 548 glyphs · 477 encoded | 1.00→3.77x, smoothstep (3t²−2t³) on the visible box's edges (left 0→0, top 0→3.9, width 1920→509.3 CSS; every frame edge moves monotonically — takes 1–3 tweened centre + log zoom, which let the left edge drift to CSS 114 at f1840 and return), 1.0 s | none | out of frame |
| 31.20 | 32.60 | 1872–1955 | Readout hold | 3.77x hold 1.4 s | none | none |
| 32.60 | 35.00 | 1956–2099 | Cut: Latin Extended cluster around the selected Ď (a bounded native crop of 7 complete columns × 3 complete rows, Ď in the centre cell, centred between the frame top and the caption block with paper margins; nothing but paper under or within 24 px of the block); caption 6 to f2099 | 3.50x hold 2.4 s | none | none |
| 35.00 | 36.00 | 2100–2159 | Specimen page 6: the waterfall, “Quiet forms” at 56, 64 and 72 pt set in the compiled font (take 2; take 1 used the page 3 alphabet, whose digits row fell inside the block band); caption 7 from f2100 (hard in) | 2.64x hold 1.0 s | none (document) | none |
| 36.00 | 37.20 | 2160–2231 | Slow push on the waterfall (top edge pinned at 489.5 pt) | 2.64→2.72x, smoothstep (3t²−2t³) in log zoom, 1.2 s | none | none |
| 37.20 | 39.20 | 2232–2351 | Waterfall hold; caption 7 to f2351 | 2.72x hold 2.0 s | none | none |
| 39.20 | 40.00 | 2352–2399 | Cut: page 1 footer metadata row (one crop, top edge at 701 pt); caption 8 from f2352 (hard in) | 3.80x hold 0.8 s | none | none |
| 40.00 | 41.00 | 2400–2459 | Footer push | 3.80→3.95x, smoothstep (3t²−2t³) in log zoom, 1.0 s | none | none |
| 41.00 | 45.00 | 2460–2699 | Payoff hold: GLYPHS 548 · CHARACTERS 477 · INSTANCES 15 · MASTERS 9 · LANGUAGES 26; caption 8 holds to the end | 3.95x hold 4.0 s | none | none |
cuts (first frame of a new shot): [342, 822, 1260, 1680, 1956, 2100, 2352]; camera moves: [(354, 402), (486, 546), (834, 894), (1272, 1320), (1812, 1872), (2160, 2232), (2400, 2460)]; pointer moves: [(402, 426), (570, 690), (894, 924), (950, 1016), (1332, 1362), (1476, 1506)]; typing (1034, 1188); keyboard (1716, 1776)
camera-move durations: [0.8, 1.0, 1.0, 0.8, 1.0, 1.2, 1.0] s (0.8–1.5 required); settle between successive moves in one shot: [1.4, 2.8] s (≥ 0.4 required)

### 4. Native beat frames and measured text heights (ink bounds on decoded delivery frames of the captioned film, px)
| frame | item | film region (x0,y0,x1,y1) | ink box h | per-letter heights (min = x-height where lowercase present, max = cap/ascender) |
|---|---|---|---|---|
| 449 | pad close-up 5.3x: heading “Design space” (13 px UI) | (31, 25, 457, 134) | 65 | min 36 / max 51 (11 segments) |
| 449 | pad close-up 5.3x: instance readout “Condensed ExtraLight” | (455, 25, 1416, 134) | 65 | min 36 / max 53 (19 segments) |
| 449 | pad close-up 5.3x: pad x-axis tick labels (8.5 px UI, inside the pad element) | (157, 674, 1418, 759) | 68 | min 31 / max 68 (13 segments) |
| 570 | coframe 3.6x: sample line 1 “Quiet” (48 px) | (195, 188, 718, 405) | 141 | min 92 / max 141 (5 segments) |
| 570 | coframe 3.6x: rail label “Weight” (13 px UI) | (926, 40, 1111, 118) | 44 | min 32 / max 35 (5 segments) |
| 570 | coframe 3.6x: Weight readout “200” (changing readout) | (1642, 40, 1870, 118) | 34 | min 34 / max 34 (3 segments) |
| 570 | coframe 3.6x: Width readout “75” | (1642, 148, 1870, 226) | 34 | min 34 / max 34 (2 segments) |
| 630 | mid-drag 3.6x: Weight readout | (1642, 40, 1870, 118) | 34 | min 34 / max 34 (3 segments) |
| 630 | mid-drag 3.6x: Width readout | (1642, 148, 1870, 226) | 34 | min 33 / max 34 (3 segments) |
| 630 | mid-drag 3.6x: instance readout | (1214, 268, 1870, 345) | 36 | min 24 / max 36 (6 segments) |
| 750 | release 3.6x: Weight readout “800” | (1642, 40, 1870, 118) | 34 | min 34 / max 34 (3 segments) |
| 750 | release 3.6x: Width readout “125” | (1642, 148, 1870, 226) | 34 | min 33 / max 34 (3 segments) |
| 750 | release 3.6x: instance readout “Extended ExtraBold” | (1214, 268, 1870, 345) | 36 | min 24 / max 36 (16 segments) |
| 750 | release 3.6x: heading “Design space” | (926, 268, 1219, 345) | 45 | min 24 / max 35 (11 segments) |
| 750 | release 3.6x: pad x-axis tick labels 200…800 (8.5 px UI) | (1010, 707, 1872, 770) | 43 | min 21 / max 43 (13 segments) |
| 1042 | typing starts 2.6x: line 1 (64 px; the tallest segment is the caret) | (132, 302, 1475, 514) | 200 | min 120 / max 200 (2 segments) |
| 1111 | typing 2.6x: line 1 so far | (132, 302, 1475, 514) | 132 | min 87 / max 132 (12 segments) |
| 1259 | typed 2.6x: line 1 “Official waffle” | (132, 302, 1475, 514) | 132 | min 87 / max 132 (12 segments) |
| 1259 | typed 2.6x: line 2 “AVATAR, Tokyo” | (132, 488, 1640, 701) | 200 | min 52 / max 200 (10 segments) |
| 1386 | features sample 2.6x: “Official waffle” before ligatures | (132, 11, 1433, 223) | 133 | min 87 / max 132 (12 segments) |
| 1387 | features sample 2.6x: “Official waffle” with ffi/ffl | (132, 11, 1433, 223) | 133 | min 87 / max 132 (10 segments) |
| 1387 | features controls 3.9x: “Features” heading (13 px UI) | (450, 493, 735, 576) | 37 | min 27 / max 36 (7 segments) |
| 1387 | features controls 3.9x: label “Ligatures” | (532, 587, 747, 670) | 47 | min 26 / max 37 (9 segments) |
| 1531 | features controls 3.9x: label “Kerning” | (532, 670, 711, 753) | 47 | min 27 / max 38 (6 segments) |
| 1531 | features controls 3.9x: row sample “fi fl” (ligated) | (1289, 587, 1472, 670) | 40 | min 40 / max 40 (2 segments) |
| 1531 | features sample 2.6x: “AVATAR, Tokyo” kerned | (132, 197, 1559, 409) | 163 | min 52 / max 127 (8 segments) |
| 1955 | readout close-up 3.77x: instance “Extended ExtraBold” (13 px UI) | (808, 44, 1235, 113) | 38 | min 27 / max 38 (17 segments) |
| 1955 | readout close-up 3.77x: wght “800” (changing readout) | (1372, 44, 1469, 113) | 36 | min 36 / max 36 (3 segments) |
| 1955 | readout close-up 3.77x: wdth “125” | (1606, 44, 1702, 113) | 36 | min 34 / max 36 (3 segments) |
| 1955 | readout close-up 3.77x: “548” of the glyph count | (69, 246, 194, 327) | 45 | min 35 / max 36 (4 segments) |
| 1955 | readout close-up 3.77x: glyph count line “548 glyphs · 477 encoded · live at the current instance” (min = the · separator) | (69, 246, 1219, 327) | 47 | min 4 / max 37 (45 segments) |
| 2099 | cluster 3.50x: cell name “Dcaron” (9 px UI; the label alone, inset from the selected cell's outline) | (866, 540, 1052, 594) | 21 | min 16 / max 21 (2 segments) |
| 2099 | cluster 3.50x: Ď glyph | (840, 336, 1078, 564) | 220 | min 220 / max 220 (1 segments) |
| 2232 | specimen waterfall 2.72x: “Quiet forms” 56 pt line (smallest line in the shot) | (335, 48, 1673, 279) | 173 | min 104 / max 159 (10 segments) |
| 2232 | specimen waterfall 2.72x: “Quiet forms” 72 pt line | (335, 606, 1673, 897) | 258 | min 133 / max 258 (6 segments) |
| 2232 | specimen waterfall 2.72x: size label “72” (7 pt, document) | (265, 728, 347, 897) | 17 | min 17 / max 17 (2 segments) |
| 2352 | footer 3.8x: label “GLYPHS” (7 pt caps) | (77, 252, 240, 308) | 24 | min 23 / max 24 (6 segments) |
| 2352 | footer 3.8x: number “548” (20 pt) | (77, 325, 275, 425) | 71 | min 68 / max 70 (3 segments) |
| 2699 | payoff 4.0x: label “GLYPHS” (7 pt caps) | (43, 262, 212, 320) | 25 | min 25 / max 25 (6 segments) |
| 2699 | payoff 4.0x: labels row | (2, 262, 1920, 320) | 25 | min 25 / max 25 (41 segments) |
| 2699 | payoff 4.0x: number “548” (20 pt) | (43, 338, 247, 441) | 74 | min 72 / max 74 (3 segments) |
| 2699 | payoff 4.0x: numbers row 548 · 477 · 15 · 9 · 26 | (2, 338, 1920, 441) | 74 | min 70 / max 74 (11 segments) |
Section 3 thresholds: UI text ≥ 28 px em with x-height ≥ 14 px; readout numbers ≥ 32 px; payoff ≥ 48 px. Regions are projected from the capture-log element rectangles through the
renderer camera (films/render45v3.py cam_state), then measured on the decoded frame; em = CSS font size × zoom. Picture beats (not reading beats): the Drawing view at 1.42x and the Glyphs view at 1x
during the keyboard change (its readouts are read in the 3.77x close-up). All beat frames: qa/film45v3/beats/c-NNNN.png (captioned) and g-NNNN.png (clean).

### 5. Motion profile
Two duplicate measures. (a) Identical frames: MD5 of consecutive source PNGs (the exact frames encoded) — a pair counts only when byte-identical; given for the clean sequence; for the
captioned sequence a pair is identical iff the clean pair is identical and no caption change falls between the two frames (v3 captions are static blocks with hard in/out, verified in section 7).
(b) The literal section-3 figure on the decoded captioned film: mean |delta| < 0.02 (0–1 scale, = 5.1/255) on a 160x90 area-averaged grey downscale; (b) also counts slow eased camera motion
on flat UI and small-pointer motion as "near-static" although the frames are distinct, so (a) is the duplicate count and (b) is reported alongside.

| second | identical source pairs, clean (a) | identical source pairs, captioned (a) | near-static pairs, captioned (b) | max mean delta captioned (x255) | max mean delta clean (x255) | content |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 60 | 0.01 | 0.01 | app motion |
| 1 | 1 | 1 | 60 | 0.31 | 0.31 | app motion |
| 2 | 1 | 1 | 60 | 0.38 | 0.38 | app motion |
| 3 | 9 | 9 | 60 | 0.31 | 0.31 | app motion |
| 4 | 60 | 60 | 60 | 0.03 | 0.02 | hold |
| 5 | 53 | 53 | 59 | 0.15 | 0.16 | camera move 6 f, caption change (one frame) |
| 6 | 0 | 0 | 60 | 0.59 | 0.59 | camera move 42 f, pointer motion |
| 7 | 54 | 54 | 60 | 0.64 | 0.64 | pointer motion |
| 8 | 6 | 6 | 58 | 5.15 | 5.16 | camera move 54 f |
| 9 | 22 | 22 | 60 | 2.24 | 2.24 | camera move 6 f, pointer motion |
| 10 | 0 | 0 | 60 | 1.07 | 1.06 | pointer motion |
| 11 | 31 | 31 | 60 | 1.08 | 1.08 | pointer motion |
| 12 | 59 | 59 | 60 | 0.29 | 0.29 | hold |
| 13 | 53 | 53 | 59 | 0.19 | 0.19 | camera move 6 f, caption change (one frame) |
| 14 | 0 | 0 | 60 | 0.69 | 0.69 | camera move 54 f, pointer motion |
| 15 | 25 | 25 | 60 | 0.11 | 0.11 | pointer motion |
| 16 | 4 | 4 | 60 | 2.70 | 2.67 | pointer motion |
| 17 | 51 | 51 | 59 | 7.35 | 7.31 | typing (discrete keystrokes) |
| 18 | 48 | 48 | 60 | 4.54 | 4.52 | typing (discrete keystrokes) |
| 19 | 52 | 52 | 60 | 1.01 | 1.00 | typing (discrete keystrokes) |
| 20 | 59 | 59 | 59 | 0.00 | 0.00 | caption change (one frame) |
| 21 | 12 | 12 | 60 | 1.85 | 1.85 | camera move 48 f |
| 22 | 30 | 30 | 60 | 0.36 | 0.36 | pointer motion |
| 23 | 58 | 58 | 59 | 5.90 | 5.90 | hold |
| 24 | 35 | 34 | 60 | 3.81 | 0.12 | pointer motion, caption change (one frame) |
| 25 | 53 | 53 | 59 | 8.51 | 8.50 | pointer motion |
| 26 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 27 | 59 | 59 | 59 | 0.00 | 0.00 | caption change (one frame) |
| 28 | 34 | 34 | 60 | 0.20 | 0.20 | app motion |
| 29 | 22 | 22 | 60 | 0.15 | 0.15 | app motion |
| 30 | 9 | 9 | 17 | 16.96 | 17.15 | camera move 48 f |
| 31 | 48 | 48 | 49 | 14.36 | 14.57 | camera move 12 f |
| 32 | 59 | 59 | 59 | 0.11 | 0.00 | hold |
| 33 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 34 | 59 | 59 | 59 | 0.00 | 0.00 | caption change (one frame) |
| 35 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 36 | 0 | 0 | 60 | 0.46 | 0.44 | camera move 60 f |
| 37 | 48 | 48 | 60 | 0.25 | 0.24 | camera move 12 f |
| 38 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 39 | 59 | 59 | 59 | 0.12 | 0.05 | caption change (one frame) |
| 40 | 0 | 0 | 60 | 0.18 | 0.18 | camera move 60 f |
| 41 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 42 | 60 | 60 | 60 | 0.00 | 0.00 | hold |
| 43 | 60 | 60 | 60 | 0.04 | 0.02 | hold |
| 44 | 59 | 59 | 59 | 0.00 | 0.00 | hold |

Moving windows (identical-pair rule < 2 %, no 2:2 / 3:2 / 5:5 cadence), clean source pairs; the captioned sequence has the same or fewer identical pairs:
| window | frames | identical pairs clean (a) | % | cadence | identical pairs captioned (a) | near-static pairs (b) | verdict |
|---|---|---|---|---|---|---|---|
| camera moves (7) | 408 | 0  | 0.00 (clean) | none | 0  | 352 | PASS |
| pointer moves incl. drag | 300 | 5 [(425, 425), (689, 689), (923, 923), (1361, 1361), (1505, 1505)] | 1.67 (clean) | none | 5  | 300 | PASS |
| drag 570–690 alone | 120 | 1 [(689, 689)] | 0.83 (clean) | none | 1  | 120 | PASS |
| letter animation 0–231 (app clock) | 231 | 2 [(85, 85), (161, 161)] | 0.87 (clean) | none | 2  | 231 | PASS |
| keyboard axis change 1716–1776 | 60 | 1 [(1775, 1775)] | 1.67 (clean) | none | 1  | 60 | PASS |
| typing 1034–1188 (discrete input) | 154 | 126 | 81.82 | keystroke intervals 4–10 f, irregular | 126 | 154 | reported, see note |
Typing note: the field is static between keystrokes (the product has no animation there; the pointer is parked), so consecutive frames between two keystrokes are identical by
construction. Intervals are [4, 5, 6, 7, 9, 10] frames (mean 5.46 f = 11.0 cps, sd 1.68 f, CV 0.31; seeded continuous draws with longer pauses after spaces
and the comma), and every keystroke frame changes the content (one new character + caret advance); it is not a padded capture — section 6 lists each keystroke frame.
identical source pairs over the whole clean sequence: 1652 of 2699, runs = [(85, 85), (161, 161), (231, 340), (342, 353), (425, 448), (450, 485), (547, 568), (689, 748), (750, 820), (822, 833), (923, 946), (948, 948), (1016, 1032), (1034, 1038), (1040, 1044), (1046, 1049), (1051, 1053), (1055, 1058), (1060, 1062), (1064, 1066), (1068, 1071), (1073, 1080), (1082, 1085), (1087, 1089), (1091, 1094), (1096, 1099), (1101, 1103), (1105, 1108), (1110, 1118), (1120, 1122), (1124, 1128), (1130, 1134), (1136, 1138), (1140, 1143), (1145, 1148), (1150, 1155), (1157, 1165), (1167, 1171), (1173, 1177), (1179, 1181), (1183, 1185), (1187, 1258), (1260, 1271), (1320, 1330), (1361, 1384), (1387, 1474), (1505, 1528), (1531, 1678), (1681, 1714), (1775, 1778), (1781, 1798), (1801, 1801), (1804, 1811), (1872, 1954), (1956, 2098), (2100, 2159), (2232, 2350), (2352, 2399), (2460, 2698)]; captioned sequence: 1651 (the 7 caption-change pairs differ)
near-static pairs (b) inside camera moves: 352 of 408; every one of them is a distinct frame by (a)
captioned: single-frame pops (frame differs from both neighbours by > 8/255 while the neighbours agree), cuts excluded: none; every pair outside cuts with mean |delta| > 8/255: [(1530, 8.51), (1821, 8.57), (1822, 9.46), (1823, 9.99), (1824, 10.5), (1825, 11.02), (1826, 11.28), (1827, 11.52), (1828, 12.18), (1829, 12.86), (1830, 13.11), (1831, 13.8), (1832, 14.04), (1833, 14.68), (1834, 15.14), (1835, 15.3), (1836, 15.16), (1837, 15.0), (1838, 16.01), (1839, 16.26), (1840, 15.96), (1841, 15.78), (1842, 16.36), (1843, 16.85), (1844, 16.36), (1845, 15.72), (1846, 16.17), (1847, 16.88), (1848, 16.96), (1849, 16.07), (1850, 15.84), (1851, 16.27), (1852, 16.63), (1853, 15.83), (1854, 14.95), (1855, 15.15), (1856, 15.2), (1857, 15.38), (1858, 15.01), (1859, 14.04), (1860, 14.36), (1861, 14.15), (1862, 13.47), (1863, 13.51), (1864, 13.89), (1865, 13.77), (1866, 12.86), (1867, 10.92), (1868, 9.91), (1869, 8.44)]; largest mean delta outside cuts 16.96/255; cut pairs [341, 821, 1259, 1679, 1955, 2099, 2351] deltas [28.4, 20.0, 33.4, 22.4, 20.8, 34.0, 22.2]
clean: single-frame pops (frame differs from both neighbours by > 8/255 while the neighbours agree), cuts excluded: none; every pair outside cuts with mean |delta| > 8/255: [(1530, 8.5), (1820, 8.19), (1821, 8.86), (1822, 9.7), (1823, 10.27), (1824, 10.92), (1825, 11.51), (1826, 11.83), (1827, 12.03), (1828, 12.52), (1829, 13.13), (1830, 13.58), (1831, 14.36), (1832, 14.54), (1833, 15.02), (1834, 15.37), (1835, 15.73), (1836, 15.72), (1837, 15.44), (1838, 16.27), (1839, 16.54), (1840, 16.6), (1841, 16.62), (1842, 16.89), (1843, 17.07), (1844, 16.68), (1845, 16.21), (1846, 16.6), (1847, 17.14), (1848, 17.15), (1849, 16.66), (1850, 16.86), (1851, 16.93), (1852, 16.83), (1853, 16.05), (1854, 15.41), (1855, 16.05), (1856, 15.98), (1857, 15.71), (1858, 15.2), (1859, 14.22), (1860, 14.5), (1861, 14.57), (1862, 14.18), (1863, 14.13), (1864, 14.17), (1865, 13.86), (1866, 12.97), (1867, 11.08), (1868, 10.11), (1869, 8.65)]; largest mean delta outside cuts 17.15/255; cut pairs [341, 821, 1259, 1679, 1955, 2099, 2351] deltas [25.6, 16.4, 29.8, 21.4, 20.8, 30.3, 19.1]
PSNR captioned delivery vs its master: mean 57.99 dB, min 45.39 dB at frame 1843; at cut frames: f342: 58.45, f822: 62.74, f1260: 59.11, f1680: 57.13, f1956: 55.87, f2100: 59.20, f2352: 58.80
PSNR clean delivery vs its master: mean 55.97 dB, min 45.50 dB at frame 1821; at cut frames: f342: 60.35, f822: 55.48, f1260: 57.19, f1680: 56.47, f1956: 56.45, f2100: 60.12, f2352: 61.77

### 6. Pointer and input log (from the capture logs; positions in CSS px of the capture viewport = 1x scale; film position via the renderer camera)
letter: planned peak speeds []; measured peak 0 px/s at 1x; peak while button down 0 px/s; dwell before clicks [] s; cursor shapes ['hidden']; errors []; highest pointer hotspot in the film (min y) = None px (band is y < 240)
drag: planned peak speeds [('approach the 200/75 instance', 270), ('weight 200→800; width 75→125', 179)]; measured peak 270 px/s at 1x; peak while button down 179 px/s; dwell before clicks [0.42] s; cursor shapes ['crosshair', 'grabbing']; errors []; highest pointer hotspot in the film (min y) = 397 px (band is y < 240)
  live recompute receipt: during the drag (f570–689) the (Weight, Width) readouts change on 98 of 120 frames; 200/75 → 800/125; per-frame values in pointer-log.csv
type: planned peak speeds [('sample field', 663), ('park below the typed lines', 731)]; measured peak 731 px/s at 1x; peak while button down 0 px/s; dwell before clicks [0.42] s; cursor shapes ['text']; errors []; highest pointer hotspot in the film (min y) = 420 px (band is y < 240)
  typing: 29 characters f1034–f1187, intervals [6, 6, 5, 4, 5, 4, 4, 5, 9, 5, 4, 5, 5, 4, 5, 10, 4, 6, 6, 4, 5, 5, 7, 10, 6, 6, 4, 4] frames (mean 5.46 f = 11.0 cps, sd 1.68 f, CV 0.31), last character held 1.22 s
  select-all (Ctrl+A) at f1016, 18 frames before the first replacement character; the pointer parks at f1016
feat: planned peak speeds [('approach the Ligatures label', 330), ('down to the Kerning label', 66)]; measured peak 330 px/s at 1x; peak while button down 0 px/s; dwell before clicks [0.42, 0.42] s; cursor shapes ['pointer']; errors []; highest pointer hotspot in the film (min y) = 629 px (band is y < 240)
grid: planned peak speeds []; measured peak 0 px/s at 1x; peak while button down 0 px/s; dwell before clicks [] s; cursor shapes ['crosshair']; errors []; highest pointer hotspot in the film (min y) = 417 px (band is y < 240)
  keyboard: 110 key events f1716–f1775 (['ArrowRight', 'ArrowUp']); pad scrollTop and first visible row in grid.json
full per-frame log: qa/film45/pointer-log.csv (2118 rows)
Capture method (full disclosure): real application in headless Chromium (Playwright), real mouse/keyboard events; the page clock is frame-stepped at exactly 1/60 s (one rAF flush per
frame), so this is frame-stepped rendering, not measured real-time GPU performance. The pointer is composited from the real input log at the real input position, with the shape the
product requests via CSS cursor under it (arrow, text, crosshair, grabbing, pointer); arrow transitions shorter than 6 frames are suppressed so the hand does not flicker while crossing
the 3 px gap between toggle rows (f1476–1505; the raw cssCursor is kept in the log). The text caret is drawn at the selection position and does not blink.
Editorial composites, all built from native crops of the SAME captured frame, full frame 1920x1080 (v3; the v2.1 300 px top margin is gone): (1) drag 6–14 s: the two-line sample (app
x0–236, y52–352) beside two rail crops (x1636–1912: y66–90 Weight, y141–165 Width, y288–434 Design space + pad) on a 533x300 board in the rail chalk colour; the Size row and slider tracks
are omitted; (2) tester 14–21 s: paper-colour padding beyond the top/left edge of the viewport (frames reused from v2.1); (3) features 21–28 s: sample band (y0–440) and Features-rows crop
(centred in y440–870) in chalk; (4) glyphs 28–35 s: 1x viewport, then a 1.0 s push whose visible box edges are tweened with the smoothstep (monotonic edges; take 4) into a readout close-up at 3.77x (frame = the page's top-left corner, CSS x 0–509.3, y 3.9–290.4: header, glyph-count line, two complete glyph rows and no partial column; the second row's name labels and cell bottoms inside the block band, the third row's cell tops at the frame bottom), then a bounded cluster crop at 3.5x (7 complete columns × 3 complete rows around Ď, 1723×860 px with half-gutter paper margins on all four edges, pasted centred at x 98–1821, y 45–905 on the same paper colour; 46 px of paper between the grid and the block);
(5) specimen 35–45 s: one crop of a PDF page at a time; the footer crop extends below the page into white padding. (6) captions: libass renders Captions.ass (Lato Bold 60 px, opaque
#1b262b block) onto the decoded clean master during the captioned encode; the clean film has no caption pixels (section 7).
No layout, text, label, number or state was altered or added.

### 7. Captions (v3 bottom block, burned in with libass; kit section 7 of October 20, 2026)
Font: films/captions-v3/fonts/Lato-Bold.ttf = Lato Bold, name table version “Version 2.015; 2015-08-06; http://www.latofonts.com/”, 657188 bytes, sha256 bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b; the same bytes as the approved file /usr/share/fonts/truetype/lato/Lato-Bold.ttf (sha256 bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b, identical); OS/2 winAscent/winDescent 1974/426, typo 1610/-390, unitsPerEm 2000 → libass em 50.0 px at Fontsize 60 (kit v2 requires 50.0); licence films/captions-v3/fonts/OFL.txt.
The Google Fonts copy first named in the 08:29Z kit (656,544 B, sha256 8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1) carries winAscent/winDescent 2233/599 → libass em 42.4 px, 15 % small (one-line block
60 px tall, bottom edge 1014); it was tried, rejected by measurement here before the parent’s 11:30Z amendment (kit v2, asset 2eb49efc-fd60-4d1d-b81e-9ac1124b75e0) withdrew it, and never burned into a delivered film.
Kit v2: films/captions-v3/captions_v3.py and verify_captions_v3.py are the v2 scripts (v1 kept in films/captions-v3/kit-v1/); build/ was regenerated with kit v2 and --font /usr/share/fonts/truetype/lato/Lato-Bold.ttf —
Captions.ass and every cue rectangle came out byte/value-identical to the kit-v1 build that was burned (kept as films/captions-v3/build-kit-v1/), so the burned films already carry the approved treatment and were not re-burned.
Geometry build: films/captions-v3/build/caption-geometry.json: treatment “v3 bottom block: Lato Bold 60 px white, opaque #1b262b block r=7 fitted to rendered ink with 18/10 px padding, anchor (960,1009), hard in/out”, font sha256 in the build bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b (matches the file), font_libass_em_px 50.0, problems none
| # | text (line split = /) | chars (per line) | in | out | duration s | minimum s = max(3.0, 0.065 × chars) | ink x0,y0–x1,y1 | block x,y,w,h | beat |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A new typeface, / built from scratch. | 35 (15+19) | 0 | 341 | 5.70 | 3.00 | 760,901–1160,999 | 742,891,436,118 | letter: skeleton to outline |
| 2 | Drag to change weight / and width, live. | 38 (21+16) | 342 | 821 | 8.00 | 3.00 | 712,901–1212,1006 | 694,891,536,125 | drag: design-space pad, readouts recompute per frame |
| 3 | Type any text to test it. | 25 (25) | 822 | 1259 | 7.30 | 3.00 | 701,961–1217,1007 | 683,951,552,66 | type: click, select all, type |
| 4 | Ligatures: ffi and ffl / each become one glyph. | 45 (22+22) | 1260 | 1463 | 3.40 | 3.00 | 694,901–1225,1008 | 676,891,567,127 | feat: Ligatures toggle |
| 5 | Kerning: AV and To close up. | 28 (28) | 1464 | 1679 | 3.60 | 3.00 | 643,961–1279,1008 | 625,951,672,67 | feat: Kerning toggle (change inside the post-click hold) |
| 6 | 548 glyphs cover 26 languages. | 30 (30) | 1680 | 2099 | 7.00 | 3.00 | 615,961–1306,1008 | 597,951,727,67 | grid: 1x picture, instance readout, diacritic cluster |
| 7 | The specimen is set / in the compiled font. | 41 (19+21) | 2100 | 2351 | 4.20 | 3.00 | 732,901–1188,1007 | 714,891,492,126 | pdf: specimen page 6 waterfall |
| 8 | 548 glyphs, 9 masters, / 26 languages. Version 1.103. | 51 (22+28) | 2352 | 2699 | 5.80 | 3.31 | 642,901–1278,1008 | 624,891,672,127 | pdf: specimen page 1 footer payoff |
Timing rules (each ≥ 3.0 s and ≥ 0.065 s/char; ≤ 2 lines; ≤ 34 chars per line): PASS; caption 1 from frame 0: True; last caption holds to frame 2699: True; continuous (every frame captioned, no gaps): True; longest caption 51 characters (≤ 68 total rule of v2.1 §7.4 applies per caption)
Caption changes [342, 822, 1260, 1464, 1680, 2100, 2352] vs camera moves [(354, 402), (486, 546), (834, 894), (1272, 1320), (1812, 1872), (2160, 2232), (2400, 2460)]: changes inside a move: none; cuts [342, 822, 1260, 1680, 1956, 2100, 2352] — changes at cuts: [342, 822, 1260, 1680, 2100, 2352]; changes inside holds: [1464]
Lines never break after a stop word (a, an, the, and, of, to, by, for, with, in, on, at, from, as, is, are): True

caption-geometry.json (verbatim):
```json
{
 "treatment": "v3 bottom block: Lato Bold 60 px white, opaque #1b262b block r=7 fitted to rendered ink with 18/10 px padding, anchor (960,1009), hard in/out",
 "font_file": "Lato-Bold.ttf",
 "font_sha256": "bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b",
 "font_libass_em_px": 50.0,
 "fps": 60.0,
 "cues": [
  {
   "id": 1,
   "text": "A new typeface,\nbuilt from scratch.",
   "lines": [
    "A new typeface,",
    "built from scratch."
   ],
   "chars": 35,
   "in": 0,
   "out": 342,
   "duration_s": 5.7,
   "ink": {
    "left": 760,
    "top": 901,
    "right": 1160,
    "bottom": 999
   },
   "box": {
    "x": 742,
    "y": 891,
    "width": 436,
    "height": 118,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 2,
   "text": "Drag to change weight\nand width, live.",
   "lines": [
    "Drag to change weight",
    "and width, live."
   ],
   "chars": 38,
   "in": 342,
   "out": 822,
   "duration_s": 8.0,
   "ink": {
    "left": 712,
    "top": 901,
    "right": 1212,
    "bottom": 1006
   },
   "box": {
    "x": 694,
    "y": 891,
    "width": 536,
    "height": 125,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 3,
   "text": "Type any text to test it.",
   "lines": [
    "Type any text to test it."
   ],
   "chars": 25,
   "in": 822,
   "out": 1260,
   "duration_s": 7.3,
   "ink": {
    "left": 701,
    "top": 961,
    "right": 1217,
    "bottom": 1007
   },
   "box": {
    "x": 683,
    "y": 951,
    "width": 552,
    "height": 66,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 4,
   "text": "Ligatures: ffi and ffl\neach become one glyph.",
   "lines": [
    "Ligatures: ffi and ffl",
    "each become one glyph."
   ],
   "chars": 45,
   "in": 1260,
   "out": 1464,
   "duration_s": 3.4,
   "ink": {
    "left": 694,
    "top": 901,
    "right": 1225,
    "bottom": 1008
   },
   "box": {
    "x": 676,
    "y": 891,
    "width": 567,
    "height": 127,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 5,
   "text": "Kerning: AV and To close up.",
   "lines": [
    "Kerning: AV and To close up."
   ],
   "chars": 28,
   "in": 1464,
   "out": 1680,
   "duration_s": 3.6,
   "ink": {
    "left": 643,
    "top": 961,
    "right": 1279,
    "bottom": 1008
   },
   "box": {
    "x": 625,
    "y": 951,
    "width": 672,
    "height": 67,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 6,
   "text": "548 glyphs cover 26 languages.",
   "lines": [
    "548 glyphs cover 26 languages."
   ],
   "chars": 30,
   "in": 1680,
   "out": 2100,
   "duration_s": 7.0,
   "ink": {
    "left": 615,
    "top": 961,
    "right": 1306,
    "bottom": 1008
   },
   "box": {
    "x": 597,
    "y": 951,
    "width": 727,
    "height": 67,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 7,
   "text": "The specimen is set\nin the compiled font.",
   "lines": [
    "The specimen is set",
    "in the compiled font."
   ],
   "chars": 41,
   "in": 2100,
   "out": 2352,
   "duration_s": 4.2,
   "ink": {
    "left": 732,
    "top": 901,
    "right": 1188,
    "bottom": 1007
   },
   "box": {
    "x": 714,
    "y": 891,
    "width": 492,
    "height": 126,
    "radius": 7,
    "color": "#1b262b"
   }
  },
  {
   "id": 8,
   "text": "548 glyphs, 9 masters,\n26 languages. Version 1.103.",
   "lines": [
    "548 glyphs, 9 masters,",
    "26 languages. Version 1.103."
   ],
   "chars": 51,
   "in": 2352,
   "out": 2700,
   "duration_s": 5.8,
   "ink": {
    "left": 642,
    "top": 901,
    "right": 1278,
    "bottom": 1008
   },
   "box": {
    "x": 624,
    "y": 891,
    "width": 672,
    "height": 127,
    "radius": 7,
    "color": "#1b262b"
   }
  }
 ],
 "problems": []
}
```

verify_captions_v3.py (kit v2.2 of the parent's kit note of Oct 20: v2.1 plus the --clean edge test in luma for the 1-px line touching the block, RGB for the 2-px ring at 2–3 px, whole-frame comparison outside a 3-px margin) exit code 0; fails: []; rows checked: 16 (first and last frame of every caption); ink height vs expected: [(46, 45), (46, 46), (97, 96), (104, 105), (106, 105), (106, 106)]; full output in qa/film45v3/verify-captions.txt

Per-cue maxima of the v2.2 edge figures (over the first and last frame of each caption; limits: adjacent luma ≤ 6, outer RGB ≤ 6, frame-outside-margin ≤ 2.0; adjacent RGB is information only):

| cue | ring_adjacent_luma_diff (≤ 6) | ring_adjacent_rgb_diff (info) | ring_outer_rgb_diff (≤ 6) | frame diff outside the 3-px margin (≤ 2.0) |
|---|---|---|---|---|
| 1 | 1.37 | 3.49 | 2.15 | 0.68 |
| 2 | 0.77 | 2.83 | 1.06 | 0.39 |
| 3 | 1.30 | 4.50 | 1.32 | 0.70 |
| 4 | 1.31 | 3.02 | 1.14 | 0.38 |
| 5 | 1.35 | 2.76 | 1.26 | 0.37 |
| 6 | 1.07 | 4.47 | 1.77 | 0.45 |
| 7 | 3.96 | 3.58 | 0.35 | 0.21 |
| 8 | 3.79 | 3.26 | 0.37 | 0.04 |
| all | 3.96 | 4.50 | 2.15 | 0.705 |
verify output (verbatim):
```json
{
 "film": "/home/user/workspace/projects/computer-use-cases-59DkbY5.QouRVj3hdp4Q8g/files/builds/A4-letterform/films/letterform-45s-captioned.mp4",
 "cues": 8,
 "fails": [],
 "rows": [
  {
   "cue": 1,
   "frame": 0,
   "which": "in",
   "fill": 1.0,
   "ink": [
    761,
    902,
    1160,
    999
   ],
   "edge_rows_mean_rgb": [
    [
     30,
     34,
     36
    ],
    [
     34,
     34,
     31
    ]
   ],
   "ink_height": 97,
   "expected_ink_height": 96,
   "padding": {
    "left": 19,
    "top": 11,
    "right": 18,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 1.37,
   "ring_adjacent_rgb_diff": 3.49,
   "ring_outer_rgb_diff": 1.76,
   "diff_outside_block": 0.68
  },
  {
   "cue": 1,
   "frame": 341,
   "which": "last",
   "fill": 1.0,
   "ink": [
    761,
    902,
    1160,
    999
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     34,
     34
    ],
    [
     34,
     36,
     36
    ]
   ],
   "ink_height": 97,
   "expected_ink_height": 96,
   "padding": {
    "left": 19,
    "top": 11,
    "right": 18,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 1.05,
   "ring_adjacent_rgb_diff": 3.29,
   "ring_outer_rgb_diff": 2.15,
   "diff_outside_block": 0.675
  },
  {
   "cue": 2,
   "frame": 342,
   "which": "in",
   "fill": 1.0,
   "ink": [
    713,
    901,
    1211,
    1005
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     37,
     36
    ],
    [
     25,
     35,
     40
    ]
   ],
   "ink_height": 104,
   "expected_ink_height": 105,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 0.77,
   "ring_adjacent_rgb_diff": 2.83,
   "ring_outer_rgb_diff": 1.06,
   "diff_outside_block": 0.097
  },
  {
   "cue": 2,
   "frame": 821,
   "which": "last",
   "fill": 1.0,
   "ink": [
    713,
    901,
    1211,
    1005
   ],
   "edge_rows_mean_rgb": [
    [
     33,
     35,
     33
    ],
    [
     25,
     35,
     41
    ]
   ],
   "ink_height": 104,
   "expected_ink_height": 105,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 0.63,
   "ring_adjacent_rgb_diff": 2.12,
   "ring_outer_rgb_diff": 1.06,
   "diff_outside_block": 0.388
  },
  {
   "cue": 3,
   "frame": 822,
   "which": "in",
   "fill": 1.0,
   "ink": [
    702,
    961,
    1216,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     36,
     38
    ],
    [
     32,
     34,
     34
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 45,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 1.3,
   "ring_adjacent_rgb_diff": 4.31,
   "ring_outer_rgb_diff": 1.32,
   "diff_outside_block": 0.674
  },
  {
   "cue": 3,
   "frame": 1259,
   "which": "last",
   "fill": 1.0,
   "ink": [
    702,
    961,
    1216,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     34,
     35
    ],
    [
     30,
     34,
     36
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 45,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 0.99,
   "ring_adjacent_rgb_diff": 4.5,
   "ring_outer_rgb_diff": 1.13,
   "diff_outside_block": 0.705
  },
  {
   "cue": 4,
   "frame": 1260,
   "which": "in",
   "fill": 1.0,
   "ink": [
    695,
    901,
    1224,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     34,
     31
    ],
    [
     26,
     35,
     40
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 106,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 1.31,
   "ring_adjacent_rgb_diff": 3.02,
   "ring_outer_rgb_diff": 1.14,
   "diff_outside_block": 0.335
  },
  {
   "cue": 4,
   "frame": 1463,
   "which": "last",
   "fill": 1.0,
   "ink": [
    695,
    901,
    1224,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     34,
     31
    ],
    [
     27,
     35,
     40
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 106,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 1.28,
   "ring_adjacent_rgb_diff": 2.88,
   "ring_outer_rgb_diff": 0.77,
   "diff_outside_block": 0.376
  },
  {
   "cue": 5,
   "frame": 1464,
   "which": "in",
   "fill": 0.9999,
   "ink": [
    644,
    961,
    1278,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     37,
     35,
     36
    ],
    [
     27,
     35,
     40
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 46,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 0.6,
   "ring_adjacent_rgb_diff": 2.52,
   "ring_outer_rgb_diff": 1.26,
   "diff_outside_block": 0.373
  },
  {
   "cue": 5,
   "frame": 1679,
   "which": "last",
   "fill": 1.0,
   "ink": [
    644,
    961,
    1278,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     34,
     32
    ],
    [
     30,
     36,
     42
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 46,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 1.35,
   "ring_adjacent_rgb_diff": 2.76,
   "ring_outer_rgb_diff": 0.86,
   "diff_outside_block": 0.35
  },
  {
   "cue": 6,
   "frame": 1680,
   "which": "in",
   "fill": 1.0,
   "ink": [
    615,
    961,
    1305,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     33,
     35,
     34
    ],
    [
     27,
     35,
     41
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 46,
   "padding": {
    "left": 18,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 1.04,
   "ring_adjacent_rgb_diff": 3.22,
   "ring_outer_rgb_diff": 1.13,
   "diff_outside_block": 0.323
  },
  {
   "cue": 6,
   "frame": 2099,
   "which": "last",
   "fill": 1.0,
   "ink": [
    615,
    961,
    1305,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     36,
     41
    ],
    [
     28,
     38,
     41
    ]
   ],
   "ink_height": 46,
   "expected_ink_height": 46,
   "padding": {
    "left": 18,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 1.07,
   "ring_adjacent_rgb_diff": 4.47,
   "ring_outer_rgb_diff": 1.77,
   "diff_outside_block": 0.445
  },
  {
   "cue": 7,
   "frame": 2100,
   "which": "in",
   "fill": 1.0,
   "ink": [
    733,
    901,
    1187,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     28,
     34,
     38
    ],
    [
     32,
     36,
     40
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 105,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 2.63,
   "ring_adjacent_rgb_diff": 2.79,
   "ring_outer_rgb_diff": 0.29,
   "diff_outside_block": 0.106
  },
  {
   "cue": 7,
   "frame": 2351,
   "which": "last",
   "fill": 0.9998,
   "ink": [
    733,
    901,
    1187,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     33,
     37,
     41
    ],
    [
     33,
     37,
     41
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 105,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 10
   },
   "ring_adjacent_luma_diff": 3.96,
   "ring_adjacent_rgb_diff": 3.58,
   "ring_outer_rgb_diff": 0.35,
   "diff_outside_block": 0.21
  },
  {
   "cue": 8,
   "frame": 2352,
   "which": "in",
   "fill": 1.0,
   "ink": [
    643,
    901,
    1277,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     36,
     40
    ],
    [
     31,
     37,
     43
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 106,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 3.79,
   "ring_adjacent_rgb_diff": 3.26,
   "ring_outer_rgb_diff": 0.37,
   "diff_outside_block": 0.04
  },
  {
   "cue": 8,
   "frame": 2699,
   "which": "last",
   "fill": 1.0,
   "ink": [
    643,
    901,
    1277,
    1007
   ],
   "edge_rows_mean_rgb": [
    [
     32,
     36,
     40
    ],
    [
     26,
     35,
     40
    ]
   ],
   "ink_height": 106,
   "expected_ink_height": 106,
   "padding": {
    "left": 19,
    "top": 10,
    "right": 19,
    "bottom": 11
   },
   "ring_adjacent_luma_diff": 2.92,
   "ring_adjacent_rgb_diff": 2.63,
   "ring_outer_rgb_diff": 0.09,
   "diff_outside_block": 0.04
  }
 ]
}
```

Clearance (kit §7.2): on every frame of every caption, the pointer sprite, the click target, the typed field, the dragged object and every value or label the caption refers to must stay ≥ 24 px
outside the block rectangle. Subjects are projected from the capture-log rectangles (CSS px) or the PDF page (pt) through the v3 renderer camera; the pointer sprite box is the composited
cursor artwork (arrow 26x34 hotspot 3,2; text 14x30 hotspot 7,15; crosshair 30x30 hotspot 15,15; pointer 26x30 hotspot 10,1; grabbing 26x26 hotspot 13,13; CSS px × zoom). Distance is the
rectangle-to-rectangle gap (0 when overlapping). Subjects that project outside the frame on a given frame are skipped (noted).
| # | frames checked | subject | min distance to block px | at frame | subject box at that frame | skipped frames (subject off-frame) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 0–341 (342) | glyph drawing with its guide labels (ascender label to baseline, CSS 544..1076 x 160..712) | 49.7 | 0 | (582, 57, 1338, 841) | 0 | PASS |
| 2 | 342–821 (480) | pointer sprite (crosshair) | 364.1 | 409 | (331, 430, 490, 589) | 0 | PASS |
| 2 | 342–821 (480) | design-space pad (click target / dragged handle) | 127.4 | 527 | (774, 323, 1796, 764) | 0 | PASS |
| 2 | 342–821 (480) | readout row Design | 551.5 | 546 | (932, 274, 1865, 340) | 0 | PASS |
| 2 | 342–821 (480) | pointer sprite (grabbing) | 138.7 | 535 | (925, 655, 1022, 752) | 0 | PASS |
| 2 | 342–821 (480) | readout row Width7 | 670.7 | 546 | (932, 155, 1865, 220) | 159 | PASS |
| 2 | 342–821 (480) | readout row Weight | 778.7 | 546 | (932, 47, 1865, 112) | 178 | PASS |
| 3 | 822–1259 (438) | pointer sprite (text) | 107.9 | 995 | (1280, 775, 1316, 853) | 0 | PASS |
| 3 | 822–1259 (438) | typed line 1 (field content incl. caret) | 437.4 | 822 | (265, 344, 1391, 514) | 0 | PASS |
| 3 | 822–1259 (438) | typed line 2 (field content incl. caret) | 464.3 | 822 | (1391, 344, 1435, 514) | 0 | PASS |
| 3 | 822–1259 (438) | typed line 3 (field content incl. caret) | 255.9 | 894 | (138, 495, 1634, 695) | 0 | PASS |
| 4 | 1260–1463 (204) | pointer sprite (pointer) | 148.9 | 1320 | (1155, 625, 1257, 742) | 0 | PASS |
| 4 | 1260–1463 (204) | Ligatures row (click target) | 226.2 | 1314 | (380, 594, 1540, 665) | 0 | PASS |
| 4 | 1260–1463 (204) | Kerning row (click target) | 143.9 | 1320 | (375, 676, 1545, 747) | 0 | PASS |
| 4 | 1260–1463 (204) | sample line 1 “Official waffle” (referenced: ffi/ffl) | 673.2 | 1260 | (265, 48, 1356, 218) | 0 | PASS |
| 4 | 1260–1463 (204) | sample line 3 “AVATAR, Tokyo” (referenced: AV, To) | 487.3 | 1320 | (138, 204, 1553, 404) | 0 | PASS |
| 5 | 1464–1679 (216) | pointer sprite (pointer) | 126.3 | 1505 | (705, 708, 806, 825) | 0 | PASS |
| 5 | 1464–1679 (216) | Ligatures row (click target) | 286.5 | 1464 | (375, 594, 1545, 664) | 0 | PASS |
| 5 | 1464–1679 (216) | Kerning row (click target) | 203.9 | 1464 | (375, 676, 1545, 747) | 0 | PASS |
| 5 | 1464–1679 (216) | sample line 1 “Official waffle” (referenced: ffi/ffl) | 733.6 | 1464 | (138, 17, 1428, 217) | 0 | PASS |
| 5 | 1464–1679 (216) | sample line 3 “AVATAR, Tokyo” (referenced: AV, To) | 547.3 | 1464 | (138, 204, 1553, 404) | 0 | PASS |
| 6 | 1680–2099 (420) | pointer sprite (crosshair) | 614.5 | 1680 | (1653, 402, 1683, 432) | 271 | PASS |
| 6 | 1680–2099 (420) | glyph count line “548 glyphs · 477 encoded …” (referenced value) | 629.5 | 1872 | (75, 253, 1214, 322) | 0 | PASS |
| 6 | 1680–2099 (420) | readout ro-inst | 843.5 | 1872 | (814, 51, 1229, 107) | 0 | PASS |
| 6 | 1680–2099 (420) | readout ro-wght | 845.3 | 1872 | (1379, 51, 1463, 107) | 0 | PASS |
| 6 | 1680–2099 (420) | readout ro-wdth | 860.1 | 1863 | (1380, 44, 1452, 93) | 0 | PASS |
| 6 | 1680–2099 (420) | design-space pad (keyboard target) | 608.3 | 1680 | (1641, 320, 1900, 432) | 126 | PASS |
| 6 | 1680–2099 (420) | cluster: the whole 7 × 3 crop around Ď (cells, glyphs and name labels) | 46.0 | 1956 | (98, 45, 1821, 905) | 0 | PASS |
| 6 | 1680–2099 (420) | Ď cell | 343.2 | 1956 | (847, 342, 1072, 608) | 0 | PASS |
| 7 | 2100–2351 (252) | waterfall: the three “Quiet forms” lines with their size labels (page 6, 45.6..428.8 x 511.1..736.1 pt) | 30.6 | 2232 | (291, 75, 1629, 860) | 0 | PASS |
| 8 | 2352–2699 (348) | footer labels row (pt 45.4..524.8 x 756.2..761.2) | 586.0 | 2460 | (-572, 280, 1857, 305) | 0 | PASS |
| 8 | 2352–2699 (348) | footer numbers 548 · 477 · 15 · 9 · 26 (referenced values) | 444.1 | 2460 | (-571, 351, 1752, 447) | 0 | PASS |
Clearance ≥ 24 px for every subject on every captioned frame: PASS (per-frame distances in qa/film45v3/clearance.csv, 8896 rows)

Pixel census under and around each block (clean source frames; every 3rd frame of each segment plus its first and last; a segment is a run between cuts and camera moves inside the caption; "ink" =
pixels darker than 170/255 grey, i.e. text, glyph and outline pixels; cell backgrounds, borders and guide lines are lighter and do not count). "halo" = the 24 px band around the block rectangle.
| # | segment | ink px inside the block (max, frame) | ink px in the 24 px halo (max, frame, y range, x range) | what it is |
|---|---|---|---|---|
| 1 | 0–341 | 0 | 26 (f0, y 1031–1032, x 742–775) | nothing under the block; in the halo only the descender guide label tick (drawing-view chrome, y 1031–1032); the glyph and its labelled guides end 44 px above the block |
| 2 | 342–353 | 0 | 0 | nothing: the coframe board (sample, Weight/Width readouts, pad) ends above the block; chalk under it |
| 2 | 354–401 | 0 | 0 | 〃 |
| 2 | 402–485 | 0 | 0 | 〃 |
| 2 | 486–545 | 0 | 0 | 〃 |
| 2 | 546–821 | 0 | 0 | 〃 |
| 3 | 822–833 | 0 | 0 | nothing: paper under the block (typed lines end above it) |
| 3 | 834–893 | 0 | 0 | 〃 |
| 3 | 894–1259 | 0 | 0 | 〃 |
| 4 | 1260–1271 | 0 | 0 | nothing: chalk under the block (Features rows end above it) |
| 4 | 1272–1319 | 0 | 0 | 〃 |
| 4 | 1320–1463 | 0 | 0 | 〃 |
| 5 | 1464–1679 | 0 | 0 | nothing: chalk under the block |
| 6 | 1680–1811 | 3127 (f1776) | 642 (f1776, y 947–1041, x 605–1256) | 1680–1811 (1x viewport): parts of the live glyph grid (cells, glyphs and name labels) lie under and around the block, as in every 1x view of a scrolling grid; 1812–1871: the same grid moving during the push; 1872–1955 (readout close-up): the second glyph row's name labels Odieresis / Ugrave / Uacute and the bottoms of their cells inside the block band (its glyphs end 60 px above the block, Otilde and Ucircumflex stay >= 94 px outside the block edges, no partial column at the right edge); 1956–2099 (cluster): nothing — the bounded 7 × 3 crop ends 46 px above the block (its lowest ink, the third row's name labels, 81 px above it); paper under and around the block |
| 6 | 1812–1871 | 5664 (f1851) | 3913 (f1839, y 927–1041, x 573–1320) | 〃 |
| 6 | 1872–1955 | 1970 (f1872) | 0 | 〃 |
| 6 | 1956–2099 | 0 | 0 | 〃 |
| 7 | 2100–2159 | 0 | 0 | nothing: paper under the block; the 72 pt line ends 31 px above it after the push |
| 7 | 2160–2231 | 0 | 0 | 〃 |
| 7 | 2232–2351 | 0 | 0 | 〃 |
| 8 | 2352–2399 | 0 | 0 | nothing: paper under the block; the numbers row ends 464 px above it |
| 8 | 2400–2459 | 0 | 0 | 〃 |
| 8 | 2460–2699 | 0 | 0 | 〃 |
Reading: captions 1–5, 7 and 8 have no footage ink under the block or within 24 px of it (the caption-1 tick excepted). Caption 6 is the glyph grid: at 1x and during the push the live grid
passes under the block as in any grid viewport; the readout close-up is composed so that only the second row's name labels (and the bottoms of their cells) pass behind the block, with the glyphs
they name complete 60 px above it; the cluster is a bounded crop that ends 46 px above the block, so nothing lies under or within 24 px of it.

Note on the typed field: the contenteditable element itself spans CSS 44..756 x 96..1036 (its invisible box extends below the frame at 2.6x); the rule is applied to its visible content, the
typed lines and caret, which end at the bottom of line 2. Pixel check: on every frame of the type scene no non-background pixel of the clean frame lies inside the block rectangle + 24 px
(max |pixel − paper| inside that rectangle over frames 822–1259: 0; 0 = nothing there).

Decoded clean vs captioned, y 0–890 (above every block): PSNR mean 54.49 dB, min 43.89 dB at frame 1843 (codec noise only; the captioned film is the clean master plus the libass render)
Decoded clean vs captioned, y 891–1080, x 0–596 (left of every block): PSNR mean 74.19 dB, min 42.66 dB at frame 1838 (codec noise only; the captioned film is the clean master plus the libass render)
Decoded clean vs captioned, y 891–1080, x 1324–1919 (right of every block): PSNR mean 80.27 dB, min 41.77 dB at frame 1851 (codec noise only; the captioned film is the clean master plus the libass render)
Frames changed versus the frozen v2.1 take 2b (MD5 of the source PNGs): [(0, 821), (1260, 2699)] (2262 frames re-framed full-frame); byte-identical to v2.1: [(822, 1259)] (438 frames: the type scene)
Caption facts: C4 — hb-shape receipt in qa/shaping-receipts.txt (“Official waffle” +liga → O f_f_i c i a l · w a f_f_l e); C5 — kerning receipt (A→V advance 626→538, T→o 577→481 units);
C6/C8 — 548 glyphs and 26 languages are the specimen footer and HANDOFF.md receipts, 9 masters the design-space matrix; Version 1.103 is the font name table (nameID 5), the specimen colophon
and the app build label; C7 — pdffonts lists the embedded Apertide fonts in specimen/Apertide-Specimen.pdf (qa/specimen-check.txt). C2/C3 describe the filmed interactions. Words unchanged from v2.1.

### 8. Contact sheets and final frames
qa/film45v3/contact-45-captioned.png and contact-45.png (one frame per second, 0–44 s, 384x216 each, row-major); final-1x-captioned.png and final-1x.png (frame 2699 at native 1920x1080)

v2.1 receipts (superseded, kept): `qa/film-check45.txt`, `qa/film45/`.
<!-- /films-v3 -->

## Where the binaries are · SHA-256

The project repo is at its 5 GiB cap (the A4 commits carry only text: handoff, status, scripts, receipts); binaries are thread assets of this session, identified by these hashes. v4 assets (21 Oct 2026, private): captioned film `f8d03a09-71b2-4408-ab42-81669d994a9f`, clean film `7b8e7bd8-f971-4d1c-9d3f-7caf47a6e61a`, receipt `films/films-v4.md` `f7a0f312-4656-452a-ba4f-67d36171933d`, this handoff and the source zip `A4-letterform-source-1.103-v4.zip` (IDs in `STATUS.md` and `REPO-NOTE.md`). v3 assets (kept): captioned `1b0a3285-abb6-4829-9832-1f919aae101c`, clean `2ce1f3d1-8526-4436-bf0c-3a3f127736e0`, handoff `4e843a5f-0e54-4a57-90ea-48737f9180a3`, receipt `4aa84c2b-2c82-47a0-a4d4-7d82c9528c96`, zip `5b2e48ae-2211-4f0c-b47a-8a9bd43cfc65`.

<!-- hashes -->
| File | SHA-256 | Bytes |
| --- | --- | --- |
| `films/letterform-60s-captioned.mp4` — v4 captioned film, take 5 (the release candidate; cue 4 re-burned after the fourth review) | `43c92efbab4dd43e90951099a4f36604d26dcf00492d349d5add084866fc7edd` | 9 112 875 |
| `films/letterform-60s.mp4` — v4 clean film, take 5 (remuxed to 1/60000 before burn-in) | `649155a1ebddfbec1d51b9f9673e8d1103637a8d8acaccff232d43ce8a801f3e` | 8 934 009 |
| `films/master/letterform-60s-v4-master.mp4` — v4 clean master, CRF 10 yuv444p | `9771dbe05d30ae8af8c6924044ad598b6f37048c416b48cdb49c06ab4e80529b` | 16 905 561 |
| `films/captions-v4/cues.json` — the twelve v4 cues | `7ae5b61ac38e1f70799c3e23c71ac28751caf16416c91b7319d9d20249800251` | 2 682 |
| `films/captions-v4/build/Captions.ass` — burned-in subtitle track (kit v4.1 `captions_v4.py`) | `cb3e2703418356c3b0c9b93a0d10027f7e105ecfb197061c977892657beb2339` | 4 462 |
| `films/captions-v4/build/caption-geometry.json` — measured block geometry per caption, with `lines[]` | `2004b2a4eadebf5a620c765d01a58ba81b0b4e562276d2154e45f506b98415cf` | 6 898 |
| `films/logs60v4/camera.json` — camera segments as executed (take 5) | `fa2aeeb7a8beb55437c1d7fda4dbfd7ec153495a7fed461b256fffb244531012` | 3 451 |
| `films/logs60v4/capture60v4.json` — per-frame pointer/action log of the take-5 capture | `2103b6ebc5ccc53fba5355aac423389b62ae4287105c6bb955ef253b48861d3d` | 1 258 209 |
| `films/films-v4.md` — v4 receipt (take 5) | `ab3803db1024f8091b3ae23ed631b04f9fd34267648bd98c78b54c5614ea7f38` | 38 050 |
| `films/letterform-45s-captioned.mp4` — v3 captioned film, take 4 (the release candidate) | `2405cb081c35248c1cfaa57df91c7914d3fe0812978e457b423f06069db81090` | 6 836 417 |
| `films/letterform-45s.mp4` — v3 clean film, take 4 | `533216b5251083eb276ffac7b2a8b2d9727aad7f9dbf7b78285d355979965999` | 6 703 871 |
| `films/master/letterform-45s-captioned-master.mp4` — v3 captioned master, CRF 10 yuv444p | `ff1a83a1be5984c3cfeec6c136d6634b43baf8fe091a72b8ce0b75ea9d098f1a` | 9 492 614 |
| `films/master/letterform-45s-master.mp4` — v3 clean master, CRF 10 yuv444p | `1fff232965f0efbd2a9f37dc67dc694163c452ffeae125543dd8780dda10d5de` | 9 411 423 |
| `films/captions-v3/fonts/Lato-Bold.ttf` — Lato Bold 2.015, OFL (v3 caption font; the same bytes as /usr/share/fonts/truetype/lato/Lato-Bold.ttf) | `bf1b8130069b44b9148eeece35e5423bedac49777ba746615b826b8276574a7b` | 657 188 |
| `films/captions-v3/build/Captions.ass` — burned-in subtitle track (unchanged between the v3 takes) | `2d91e9b9d1772201d8e6c2272d7ff9d98a8c3ceca47acf816e629f6a478f5b07` | 3 039 |
| `films/captions-v3/build/caption-geometry.json` — measured block geometry per caption | `47ebc0dc464ad77b90e72bd7dd6c1eb81f025ed27d68fe300adccfb7f753d00a` | 4 409 |
| `films/captions-v3/verify_captions_v3.py` — kit v2.2 verifier (parent asset 0886a3d4-0ff0-4ebd-be56-915dcdc59f81) | `183ec4446cf0e531110822fee8238b46c8745777871dd33fe036c7875c97a014` | 11 753 |
| `films/captions-v3/captions_v3.py` — kit v2 caption builder (parent asset 2eb49efc-fd60-4d1d-b81e-9ac1124b75e0) | `5f955a4ab09b6970a9a63c762848f14737caef0a9800c2180d6b82b52c83aa4f` | 11 903 |
| `qa/film-check45v3.txt` — v3 receipt (take 4) | `0a16a62786bdef4709f165f846baafb9dd1b36812ad96c819a98bd21caa843f6` | 56 678 |
| `films/v21/letterform-45s-captioned.mp4` — v2.1 captioned film (superseded, kept) | `e9b0b099106584780e6a570260c13ecf46bc402a2d43c75e2c60c0f26eacf338` | 6 290 568 |
| `films/v21/letterform-45s.mp4` — v2.1 clean film (kept) | `08d74cef31130daa5e63e3aaae2b5bc259d656d340b26212dd44ec33e0cddb7c` | 5 597 994 |
| `films/v21/master/letterform-45s-captioned-master.mp4` — v2.1 captioned master (kept) | `7dc19c0dc47b1ee6d8ca9296c820280813e3419413764d61b85d2101cf519272` | 8 717 660 |
| `films/v21/master/letterform-45s-master.mp4` — v2.1 clean master (kept) | `a0665aee5c7133ba59f37054b392b96e7c37b8b9a7f57b621d84793ced1257a2` | 7 782 758 |
| `films/captions/Inter-SemiBold.ttf` — Inter 4.1 SemiBold, OFL (v2.1 caption font) | `78a843fade9d4612a5567302fb595b56976eb5fcebf4fea5a5912d638bafcde3` | 419 744 |
| `qa/film-check45.txt` — v2.1 receipt | `19c0ad2cac373d376e2c2996575ea5e026f4bd1b5b5de6180942a98f9af31656` | 30 613 |
| `fonts/Apertide-fonts-1.103.zip` — VF ttf + woff2 + 15 statics + license + checksums | `b8cf9f46326f37694876dce851002a9472d4a5d7a06b81ccd296bbfc5f474223` | 677 240 |
| `fonts/Apertide[wdth,wght].ttf` | `aa26824aa283fbd459967aec81663ecfb64bdd7127c40b25390b51737187e556` | 324 936 |
| `fonts/Apertide[wdth,wght].woff2` — also the copy the app serves | `5cc200d3699890ab81dc1e0e2299c13c37523f892701eab4696641ede1380ae1` | 103 316 |
| `specimen/Apertide-Specimen.pdf` | `3f383b61df552edc32119cbec6025157746d690e413c802832158ee464e9b2ad` | 889 132 |
| `films/Letterform-45s.mp4` — superseded take 1 (v2), kept | `4d62c1e8111f5ab7394666503ba3bfabca38cc765fe3247d784851811c00226a` | 7 912 032 |
| `films/Letterform-60s.mp4` — superseded, kept | `201ba0e14149c7a11130ba435840bf0908946f17f61febc3d8b09441070a7f70` | 17 478 334 |
| `films/Letterform-30s.mp4` — superseded, kept | `e2c76fe654479a9254874098273fc673cd11a70bb6cedf3c5f815a1aa6d86d23` | 8 061 859 |
<!-- /hashes -->

Per-file hashes of all 17 font binaries: `qa/font-checksums.txt`. Deployed app bundle: `qa/app-bundle-hashes.txt`.

## Review history

- Independent review of 1.001 (`a4-review/REVIEW.md`, outside the repo): accept with fixes → 1.100 (§ ¶ ₹ redrawn; f-ligature joins; r and F/P spacing; mark fit; heavy-corner counters; g tail; `frac` scope and `tnum` interplay; specimen clipping, copy, labels, Type 3 disclosure; OVERLAP flags; reduced motion; PROVENANCE.md).
- Fresh regression review of 1.100 (`a4-review/REVIEW-2.md`): "not yet acceptable" — fi read as fl; dieresis fusing and mark touches at 700–800/75; light ampersand; blank lower thirds on specimen pages; thin film arcs. Addressed in 1.101.
- Independent verification of 1.101 (`a4-review/r3/`): heavy fï / fî still collided, a 6-pixel iř contact at 800/75, overstated wording, FontForge finale cut short. Fixed in 1.101 final.
- Coordination-parent review of the deployed app: the Drawing view ignored the design-space position. Fixed (interpolated skeleton and stroke expansion, header names the position, "Compiled font overlay" with IoU 0.997 receipt).
- Final independent review of 1.101 final (`a4-review/REVIEW-4.md`): **not acceptable** — seven findings, all fixed in 1.102 (pointer overlay on pointer events; different default pangram; narrow i-marks and class fixes with the exhaustive 211 137-pair receipt; single-line instance label; feature zooms on the joins; outline-following FontForge circuit; wording).
- Fresh independent review of 1.102 (`a4-review/REVIEW-5.md`): **acceptable as a freeze**; three LOW wording items applied. Parent verdict READY; frozen.
- v2 pass: 1.103 kerning residuals; artifact fixes; 45 s film take 1 produced → every beat inspected on native frames → fixed → independent §3 review (`qa/film45/review-v2.md`): 4 FAIL (cursor flicker in the row gap, Kerning jump cut, metronomic typing, unreadable readouts during the drag at 1.5×) + judgement items (1× keyboard change without a readable readout, two-crop composites) → all addressed in take 2 (one continuous features shot, seeded typing rhythm, 3.6× drag coframe with 34 px readouts, 3.78× readout close-up, composites disclosed shot by shot).
- v2.1 pass: take 2 re-composed below a 300 px clear band, eight captions, two films; own checker (`qa/film-check45.txt`) PASS on §1, §3 and §7; independent review of the captioned film against §3 + §7 (`qa/film45/review-v21.md`): no hard break, ten findings F-1…F-10 → take 2b: C1/C4/C5 reworded (caption-before-click contradiction, “drawn”), the typed-result hold lengthened 0.92 → 1.20 s by re-capturing `type` with 438 frames and cutting `letter` at 342 (the 420 frames shared with take 2 rendered MD5-identical; feat/grid/pdf frame numbers unchanged), easing named correctly (smoothstep, not cubic in-out) in the receipts, `qa/specimen-check.txt` regenerated for 1.103 by the new `qa/specimen_check.sh`; checker re-run PASS. Left as documented judgement items: ink-height reading of small UI labels (F-3), the 1× keyboard beat (F-4), band luminance 0.250 at the PDF beats (F-5: 0.75 scrim on white gives 64/255 = 0.251 in 8-bit, the rule's own value), the instance reset and pointer jump across the cuts at f1259/f1680 (F-6), C6 baseline 1 px (F-8); the reviewer's taste note that the heavy letterforms look unfinished concerns the frozen 1.102/1.103 design and is passed to the parent.
- v3 pass (20 Oct 2026, caption treatment only, footage frozen): take 1 re-set the eight v2.1 captions in the reference bottom-block treatment and re-framed every shot full-frame; own checker PASS, kit v2.1 verifier exit 0; independent review of the captioned film against §3 + §7 (`qa/film45v3/review-v3.md`): **FIX FIRST** — High: the page 3 digits row sat inside the caption-7 block, sliced at both block edges; Medium: glyph cells and name labels under the caption-6 block with “Jcircumflex” cut at the block edge and the 5th cluster row cut by the frame bottom, the 1× keyboard beat; Low–Medium: caption-1 block 118 px tall with its bottom at y 1008 (kit output for a last line without descenders; the 11:30Z amendment's two-line range is 118–127 px); Low: typing 6–15 cps instantaneous, imperative captions 2–3 (the parent's script); plus judgement items (continuity reset at the Glyphs cut, hand cursor over the dragged node, 23 px headroom above the features sample, page number at the payoff's right edge, captions 4/5 up before their clicks, pushes 0.2 s after cuts) and a receipt error (drag press/release listed as f468/f768 from the capture clock; the film and pointer log say f450/f750). Take 2 fixed what the v3 scope allows (composition and receipts; the captured footage, the caption words and the in/out frames are frozen by the parent): specimen shot moved to the page 6 waterfall with paper only in the block band; cluster re-cropped to 7 complete columns at 3.07× with no label touching a block edge and the previous row out of frame; readout close-up re-targeted so only name labels pass behind the block; features sample band 440 px (42 px headroom); footer centred without the page number; receipt frames corrected and a per-segment pixel census of what lies under and around every block added. Not changed, documented for Jeff: the 1× keyboard beat and the instance reset at the Glyphs cut (footage), the composited cursor sprite, caption-1 block height (kit), captions 2–3 wording and captions 4/5 lead time (parent's script and frozen timing), typing rhythm (accepted v2.1 frames), the 5th cluster row's cell tops at the frame bottom (a 4-row crop cannot clear both frame edges without the block touching the 4th row's glyphs). Take-2 independent re-review (`qa/film45v3/review-v3-take2.md`): **FIX FIRST (small, in scope)** — Medium: cluster comma-below marks of Ļ/ļ 17 px above the block (< 24) with 20 label components behind it and the 5th row's glyph tops cut by the frame; readout: a 10 px sliver of an 8th column at the right edge; Low: waterfall size labels 17 px; everything outside the re-framed ranges confirmed identical, caption geometry and change frames unchanged, 0 duplicates / no pops. Take 3 (frames 1813–2099 only): the cluster became a bounded native crop of 7 × 3 complete cells around Ď at 3.5× (1723 × 860 px, half-gutter margins on all four edges, pasted centred between the frame top and the block: paper 45 px above, grid y 45–905, 46 px of paper to the block, 0 ink px under or within 24 px of it), and the readout push became a zoom on the page's top-left corner at 3.77× (page padding as the left margin, right edge in the gutter after the 7th column; labels and cell bottoms of the second row inside the block band, glyphs 60 px above). The waterfall's 7 pt size labels (17 px) are document furniture beside 133–204 px lines and stay. Take-3 independent re-review (`qa/film45v3/review-v3-take3.md`): **FIX FIRST (one in-scope item)** — the 1812–1872 push tweened centre and log zoom, so the visible left/top edge drifted to CSS 114/66 at f1840 and returned (the first glyph column and the header's left part left the frame and re-entered; present in takes 1–3, newly found); cluster, readout right edge, block/halo census, frame-lock and duplicates all confirmed. Take 4 (frames 1813–1871 only): the push tweens the visible box's edges (left 0→0, top 0→3.9 CSS, width 1920→509.3) with the same smoothstep over 60 frames; the first ink column on the clean frames is x 23 / 31 / 53 / 78 at f1826 / 1840 / 1856 / 1871 (never out of frame). The other pushes keep their paths (drag 486–546: monotonic edges, ≤ 4.1 CSS from the linear box path; pdf: pinned-top zooms; type: reused v2.1 footage). Take-4 independent re-review (`qa/film45v3/review-v3-take4.md`): **READY from the maker's side** — push path monotonic (camera log and decoded frames: header row 9→56, first column never leaves the frame), 0 duplicates, no pops, block constant; changed frames exactly 1813–1871 vs take 3; no §3/§7 break remains inside the maker's scope. The reviewer's remaining reasons not to post are the parent-frozen footage items (continuity reset at 1679→1680 with the invisible keyboard change, the hand hiding the node at 450–750 and the pasted coframe, captions 4/5 leading their clicks, pushes 12 frames after cuts, the empty payoff, the k/ķ construction on the hero line) and the two accepted compromises (second-row labels under the block in the readout, 17 px size labels beside the waterfall lines).
- v4 pass (21 Oct 2026, new 60 s footage under standard v4): take 1 discarded on the clearance check (pointer entered under the block, 1.6× count push-in with a sliver of the detail glyph, no Kerning push-in); take 2 passed every kit check and went to an independent reviewer (`films/logs60v4/review-v4-take2.md`): **FIX FIRST** — the Drawing view's progress thumb 4 px above the caption block during the alphabet animation (f1292–1489), "26 languages" and "installs" captions with no on-screen receipt, the Alphabet click inside a bottom-anchored 1.5× box so the first letters drew out of frame, Ligatures and Kerning changes off-frame before the pull-backs, specimen pages 2 and 7 mostly unreadable body copy; advisories: drag overshoot, k/y join artifacts at Extended Bold, fast wheel scroll, tester push-in cutting the sample mid-word. Stranger test: second 1 ("a font-making program"). Fixes in take 3: 24 px more room under the transport row in the product (bundle `95d028a2…`, thumb now 27 px clear at 1.0×), captions 3 and 12 reworded to what is on screen (548 glyphs; fifteen styles from specimen page 5), Alphabet push-in then back to 1.0× before the click, pull-backs starting at the click frame, drag without overshoot, "Toronto" instead of "Kyoto", spreads 1/6/8 and 3/4/5. Take 3 went to a second fresh reviewer (`films/logs60v4/review-v4-take3.md`): **FIX FIRST** — the 1.35× Alphabet push-in put the transport row (progress thumb, Speed select) inside the caption block for 2.2 s (f1014–1145) and contained no action (the click was at 1.0×, label 21 px em, under the 28 px threshold that makes a push-in mandatory); the build folder's `camera.json`, `camera-frames.json` and `capture60v4.json` were stale take-2 copies; advisories: specimen label sizes, the 1.8× toggle beats (empty chalk, change off-frame before the pull-back), the Tester push-in cutting the sample mid-word, cue 1 naming the typeface rather than the tool, the Extended Bold ffi/ffl joins. Stranger test: second 0 ("a font-making program: a grid of every letter, one letter blown up with its construction lines, sliders for weight and width"). Fixes in take 4: 1.44× Alphabet box with the transport row 32 px above the block and the click inside the push-in, pull-back from the click; the assembly script copies the capture logs itself. Take 4 went to a third fresh reviewer (`films/logs60v4/review-v4-take4.md`): **FIX FIRST** — one hard break: the 1.44× Alphabet box excludes the letter rows (CSS y 121–297), so after the click the stage in frame held zero ink at f1117 and the letters' feet slid in from the frame's top edge during the pull-back (f1118–1144, 0.47 s) under "every skeleton grows into its shape"; the reviewer showed that at any zoom ≥ 1.26× the transport-row clearance and the first letter row are mutually exclusive, and offered two fixes: a layout change in the product, or dropping the push-in with 19 px transport labels so section 3.2's optional clause applies. Confirmed fixed from take 3: click inside the push-in (30.2 px em), transport row 32–38 px clear, logs byte-identical to the work dir. Advisories: the 1.8× toggle beats (change off-frame, half the frame empty panel), specimen label sizes, cue 1 naming the typeface, the faint skeleton hairline at 1.0× (18 % opacity by design at the finished state), the Tester push-in cutting the sample mid-word, picker row 2 skimming the block at 1.44×, 28 s without a product change, grid scroll 2,610 px/s, typing window at 9 cps. Stranger test: second 0 ("a font-making program"). Fixes in take 5: the second route — transport buttons 19 px in the product (bundle `8408de75…`; Play keeps the Pause width), the Drawing view shot at 1.0× throughout, the Alphabet click wide at f1080 (label 28.5 px em) with all 52 letters drawing in frame from f1081; the picker-row and transport-row items disappear with the push-in. Take 5 went to a fourth fresh reviewer (`films/logs60v4/review-v4-take5.md`): **FIX FIRST, captions only** — the footage passed every measured rule (opener, budget 87.4 % wide, the wide Alphabet click at 28.5 px em with the whole consequence in frame, transport row 35–44 px clear, no layout shift, motion, caption mechanics, clearance ≥ 29.6 px, logs are this film's). Two caption items: cue 4 named a "red skeleton stroke" that at 1.0× is a 2 px line at 1.3:1 contrast (what reads is the nine red nodes), and cue 1 names the typeface rather than the tool. Fixed: cue 4 reworded to "Red dots mark the skeleton each letter is built on." and re-burned on the byte-identical clean film (lint exit 0, verifier exit 0, film check exit 0). Not changed: cue 1 is the parent's prescribed text; reported to the parent as a decision. Advisories (kept, each needs a re-capture or a product change): the 1.8× toggle beats with the change off-frame, the specimen label sizes, the Tester push-in cutting the sample mid-word, the 19 px transport buttons being the largest control labels in the app (made without `user:app-build-rules`, which is not loadable in this session), the Drawing beat's 2.0 s hover and 2.3 s tail, the hand parked on the clicked label, the hairline first second of the alphabet animation. Stranger test: second 0 ("a font-design program"). The re-burned pair went to a fifth fresh reviewer for confirmation (`films/logs60v4/review-v4.md`): **POST** — clean film byte-identical (SHA-256 verified), block geometry within 1 px of the geometry file on all twelve cues with hard in/out at the eleven boundaries, captioned frames differ from the clean ones only inside the block, cue 4 receipted at 1.0× (eight red 8 px node dots, ring 2.2–2.8:1 on the black fill with a bright core; the skeleton line itself ~1.2:1 stays advisory), 51 chars / 3.5 s / 0.0686 s per char, caption change on the pointerdown frame with the camera static, pointer ≥ 34 px from the block over all 2,840 pointer frames. Remaining items: cue 1 (parent decision, reported) and the carried footage advisories.
- Left by design / taste notes: the ₩ contour-count WARN; short j/y tails, the β-like ß, the small ₹ bowl at 200, the § counter that nearly closes at 800, the parent's optional note that Condensed ExtraBold f/t hooks look heavy and the s slightly top-heavy; at the heavy end the blade-cut terminals of bowls and bars leave thin openings where they meet the stems (p e r t d in the ExtraBold word of the film's finale) — present in the reviewed 1.102 outlines, unchanged in 1.103, a design decision for Jeff if he wants the joins closed.

## Not done / decisions for Jeff

- No release, publication or social copy; the app is private and unpublished. Trademark clearance is not represented (bounded name check only).
- Hinting: unhinted by design (gasp/prep smart-dropout only).
- Vietnamese stacked accents, the numero sign and double arrows are out of scope.
- `user:app-build-rules` (Project rule for UI edits) was not loadable in this session; the v4 legibility pass and the transport-row spacing were made with its stated principles applied directly (proportional, no new features, redeployed in place, bundle hash recorded). Jeff may want the skill owner to confirm.
- Font notes surfaced by the v4 film review, not changed in 1.103: the k and y joins show small artifacts at Extended Bold (wght 700 · wdth 125) in the tester; the specimen's body-copy pages (2 and 7) are set small for a 1080p frame (fine in the PDF). Both are design decisions for Jeff.
- Caption 12 departs from the parent's v4 baseline ("It installs like any other font, in fifteen styles") because no installation is shown in the film; it now reads "The font comes in fifteen styles, ExtraLight to Extended ExtraBold", receipted by specimen page 5 on screen.
