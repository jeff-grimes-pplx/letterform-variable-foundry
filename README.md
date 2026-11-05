# Letterform — Aptide Variable Foundry (`v1.103` / Release `v1.0.0`)

**Aptide Variable** is an original 548-glyph, 9-master, 26-language humanist grotesque OpenType Variable Font (`wght 200–800` × `wdth 75–125`) paired with **Letterform**, an interactive browser-based OpenType CAD engineering workbench and type foundry.

- **Live Web Foundry**: [https://www.perplexity.ai/computer/a/letterform-aptide-variable-fou-wt65J_yHScyQIT5DwfugWg](https://www.perplexity.ai/computer/a/letterform-aptide-variable-fou-wt65J_yHScyQIT5DwfugWg)

---

## 1. Typeface Architecture (`Aptide-VF.ttf` / `Aptide-VF.woff2`)

| Parameter | Specification |
| :--- | :--- |
| **Family Name** | `Aptide` (`v1.103`) |
| **Units Per Em (UPM)** | `1000` (`Ascender 740`, `Cap Height 700`, `x-Height 520`, `Baseline 0`, `Descender -210`) |
| **Glyph Complement** | **548 glyphs** (`497` encoded Unicode codepoints across Basic Latin, Latin-1 Supplement, Latin Extended-A, Spacing Modifiers, General Punctuation, Currency, Letterlike, Arrows, Mathematical Operators + `50` unencoded OpenType alternates/ligatures/fractions + `.notdef`) |
| **Design Space Axes** | `wght` (`200` ExtraLight → `400` Regular → `800` ExtraBold) × `wdth` (`75%` Compressed → `100%` Normal → `125%` Extended) |
| **Source Masters** | **9 Point-Compatible UFO v3 Masters** (`3 × 3` Cartesian design space in `sources/Aptide.designspace`) |
| **Named Instances** | **15 `fvar` / `STAT` Named Instances** (`Compressed ExtraLight` through `Extended ExtraBold`) + 15 standalone static `.ttf` binaries |
| **OpenType Layout (`GSUB` / `GPOS`)** | `ccmp`, `locl`, `ordn`, `liga` (`fi, fl, ff, ffi, ffl`), `frac` (`1/2, 1/3, 2/3, 1/4, 3/4, 1/8, 3/8, 5/8, 7/8`), `numr`, `dnom`, `sups`, `subs`, `sinf`, `zero`, `tnum`, `pnum`, `onum`, `lnum`, `case`, `salt`, `ss01`, `ss02`, `kern` (88 explicit pair rules + 16×14 class matrix = 312 effective kerning combinations), `mark` (top/bottom/ogonek anchor attachment), `mkmk` |
| **Language Coverage** | **26 Latin-script orthographies** (Czech, Polish, Hungarian, Romanian, Turkish, Vietnamese Latin core, Icelandic, Danish/Norwegian, Swedish, Finnish, German, French, Spanish, Portuguese, Catalan, Latvian, Lithuanian, Estonian, Slovak, Slovenian, Croatian, Dutch, Italian, Esperanto, Maltese, Welsh, English) |

---

## 2. Independent Compiler & Binary Verification Receipts

Every binary in `build/` and `app/fonts/` is compiled directly from `sources/*.ufo` + `sources/Aptide.designspace` via `fontTools` and `ufo2ft`, and verified by independent industry validators:

| Verification Suite | Tool / Command | Result | Receipt Artifact |
| :--- | :--- | :--- | :--- |
| **Fontbakery Universal Profile** | `fontbakery check-universal build/Aptide-VF.ttf` | **0 FAIL · 0 WARN · 0 ERROR · 104 PASS** | [`qa/fontbakery-vf.json`](qa/fontbakery-vf.json), [`qa/fontbakery-vf.txt`](qa/fontbakery-vf.txt) |
| **OpenType Sanitizer (OTS)** | `ots-sanitize 9.2.0` + FreeType `2.14.3` + HarfBuzz `14.1.0` | **17 / 17 binaries sanitized (0 errors)** | [`qa/independent_parsers.py`](qa/independent_parsers.py) |
| **HarfBuzz Shaping & 26-Language Proof** | `hb-shape` across 18 feature regressions + 26 languages + 8 axis coordinates | **68 / 68 shaping & variation checks PASS** | [`qa/shape_receipts.py`](qa/shape_receipts.py) |
| **Glyph Pair Collision Audit** | `qa/pair_overlap.py` across 462 pairs × 8 design-space coordinates | **3,696 / 3,696 pairs clean (0 collisions)** | [`qa/pair_overlap.py`](qa/pair_overlap.py) |
| **15-Page Type Specimen PDF** | WeasyPrint + HarfBuzz subsetting (`specimen/Aptide-Specimen.pdf`) | **15 pages · 16/16 embedded fonts · 0 overflow** | [`specimen/Aptide-Specimen.pdf`](specimen/Aptide-Specimen.pdf) |

---

## 3. Repository Structure

```text
letterform-variable-foundry/
├── app/                          # 10x Interactive Web Foundry (Unified CAD Workbench)
│   ├── index.html                # Split-workspace UI (2D Interpolator, Bézier CAD, OpenType Lab, 548-Glyph Atlas)
│   ├── styles.css                # Precision dark-room CAD styling (responsive across 1920x1080, 1280x800, mobile)
│   ├── app.js                    # Piecewise bilinear 9-master interpolator, live node sculpting, GPOS kerning stage
│   ├── data/aptide-data.json     # Exported 9-master glyph contours, anchors, kerning pairs, and QA telemetry
│   └── fonts/                    # Distributable font binaries & specimen PDF served by the web app
│       ├── Aptide-VF.ttf         # Compiled OpenType Variable Font (TrueType outlines + gvar/fvar/STAT/HVAR/GPOS/GSUB)
│       ├── Aptide-VF.woff2       # WOFF2 webfont binary (103 KB)
│       ├── Aptide-Specimen.pdf   # 15-page A4 Type Specimen PDF
│       └── Aptide-Static-15.zip  # All 15 static instance .ttf binaries
├── build_all.py                  # End-to-end Python font compiler (9 UFO masters -> DesignSpace -> VF/Static binaries)
├── build_specimen.py             # Generates the 15-page A4 HTML/PDF Type Specimen and exports app/data/aptide-data.json
├── qa/                           # Automated verification suites & receipts
│   ├── fontbakery-vf.json        # Full Fontbakery 1.1.0 JSON report (104 PASS, 0 FAIL, 0 WARN)
│   ├── fontbakery-vf.txt         # Human-readable Fontbakery summary
│   ├── independent_parsers.py    # ots-sanitize + FreeType + HarfBuzz + Pillow parser verification
│   ├── shape_receipts.py         # HarfBuzz GSUB/GPOS feature & 26-language shaping receipts
│   ├── pair_overlap.py           # 3,696-pair raster collision detector across 8 axis locations
│   └── verify_webapp.mjs         # Headless Playwright UI, layout, and zero-console-error verifier
├── sources/                      # Generated 9 UFO v3 source masters + Aptide.designspace + features.fea
└── specimen/                     # Compiled 15-page Aptide-Specimen.pdf & source HTML
```

---

## 4. Reproducing the Build & Verification Suite

```bash
# 1. Compile all 9 UFO masters, Aptide.designspace, Aptide-VF.ttf, Aptide-VF.woff2, and 15 static instances
python3 build_all.py

# 2. Run independent binary verification suites
fontbakery check-universal build/Aptide-VF.ttf
python3 qa/independent_parsers.py
python3 qa/shape_receipts.py
python3 qa/pair_overlap.py

# 3. Generate the 15-page Type Specimen PDF and web foundry data payload
python3 build_specimen.py

# 4. Run headless Playwright UI verification
node qa/verify_webapp.mjs
```
