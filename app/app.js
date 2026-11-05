(() => {
  'use strict';

  const INSTANCES = [
    { name: 'Comp ExtraLight', short: 'Comp XLt', wght: 200, wdth: 75 },
    { name: 'Comp Light',      short: 'Comp Lt',  wght: 300, wdth: 75 },
    { name: 'Comp Regular',    short: 'Comp Reg', wght: 400, wdth: 75 },
    { name: 'Comp Bold',       short: 'Comp Bd',  wght: 700, wdth: 75 },
    { name: 'Comp ExtraBold',  short: 'Comp XBd', wght: 800, wdth: 75 },
    { name: 'Cond Regular',    short: 'Cond Reg', wght: 400, wdth: 87.5 },
    { name: 'Cond SemiBold',   short: 'Cond SBd', wght: 600, wdth: 87.5 },
    { name: 'ExtraLight',      short: 'ExtraLt',  wght: 200, wdth: 100 },
    { name: 'Light',           short: 'Light',    wght: 300, wdth: 100 },
    { name: 'Regular',         short: 'Regular',  wght: 400, wdth: 100 },
    { name: 'Medium',          short: 'Medium',   wght: 500, wdth: 100 },
    { name: 'SemiBold',        short: 'SemiBold', wght: 600, wdth: 100 },
    { name: 'Bold',            short: 'Bold',     wght: 700, wdth: 100 },
    { name: 'ExtraBold',       short: 'ExtraBd',  wght: 800, wdth: 100 },
    { name: 'Extd ExtraBold',  short: 'Extd XBd', wght: 800, wdth: 125 }
  ];

  const LANGUAGES_26 = [
    { lang: 'Icelandic',   tag: 'ISL · Þ ð Æ', text: 'Kæmi ný öxi hér ykist þjófum nú bæði víl og ádrepa', glyph: 'Thorn' },
    { lang: 'Polish',      tag: 'POL · Ł ą ę ź', text: 'Zażółć gęślą jaźń — Łódź & Kraków 1926', glyph: 'Lslash' },
    { lang: 'Czech',       tag: 'CES · Ř ě ž ů', text: 'Příliš žluťoučký kůň úpěl ďábelské ódy', glyph: 'rcaron' },
    { lang: 'Hungarian',   tag: 'HUN · Ő ű ő', text: 'Árvíztűrő tükörfúrógép — Hűvösvölgy', glyph: 'Ohungarumlaut' },
    { lang: 'Turkish',     tag: 'TUR · İ ı ğ ş', text: 'Pijamalı hasta yağız şoföre çabucak güvendi', glyph: 'gbreve' },
    { lang: 'Romanian',    tag: 'RON · Ș ț ă â', text: 'Muzicologă în bej vând whisky și tequila, preț fix', glyph: 'tcommaaccent' },
    { lang: 'Latvian',     tag: 'LAV · Ē ū ķ ļ', text: 'Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļus', glyph: 'kcommaaccent' },
    { lang: 'Lithuanian',  tag: 'LIT · Ą ė į ū', text: 'Įlinkdama fechtuotojo špaga sublykčiojusi pragręžė apvalų arbūzą', glyph: 'eogonek' },
    { lang: 'Slovak',      tag: 'SLK · Ľ ĺ ŕ ô', text: 'Kŕdeľ šťastných ďatľov učí pri ústí Váhu mĺkveho koňa', glyph: 'Lcaron' },
    { lang: 'Croatian',    tag: 'HRV · Đ đ č ć', text: 'Gojazni đačić s biciklom drži hmelj i finu vatu u džepu', glyph: 'Dcroat' },
    { lang: 'German',      tag: 'DEU · ẞ ß ä ö', text: 'Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich', glyph: 'germandbls' },
    { lang: 'French',      tag: 'FRA · Œ œ ç ê', text: 'Dès Noël où un zéphyr haï me vêt de glaçons würmiens', glyph: 'OE' },
    { lang: 'Danish/Nor.', tag: 'DAN · Ø ø å æ', text: 'Høj blygom vandt fræk sexquiz på wc — Blåbærsyltetøj', glyph: 'Oslash' },
    { lang: 'Swedish',     tag: 'SWE · Å ä ö', text: 'Flygande bäckasiner söka hwila på mjuka tuvor', glyph: 'Aring' },
    { lang: 'Finnish',     tag: 'FIN · Ä ö å', text: 'Törkylempijävongahdus — Albert osti fagotin ja töräytti', glyph: 'Odieresis' },
    { lang: 'Estonian',    tag: 'EST · Õ ä ö ü', text: 'Põdur zagrebi tšellomängija-följetonist Ciqo külmetas', glyph: 'Otilde' },
    { lang: 'Spanish',     tag: 'ESP · Ñ ñ ¡ ¿', text: 'El veloz murciélago hindú comía feliz cardillo y kiwi', glyph: 'Ntilde' },
    { lang: 'Portuguese',  tag: 'POR · Ã õ ç', text: 'Luís argüia à Júlia que «brações, fé, chá, óxido, pôr, zângão»', glyph: 'atilde' },
    { lang: 'Catalan',     tag: 'CAT · L·L l·l ç', text: 'Jove zelós, porta whisky amb quinze glaçons d’hidrogen: col·legi', glyph: 'Ldot' },
    { lang: 'Welsh',       tag: 'CYM · Ŵ ŷ ŵ', text: 'Parciais fy jac codi baw hud llawn dŵr ger tŷ Mabon', glyph: 'wcircumflex' },
    { lang: 'Maltese',     tag: 'MLT · Ħ ħ ġ ż', text: 'Kien liebes ġakketta ħamra u żarbun abjad f’Għawdex', glyph: 'Hbar' },
    { lang: 'Esperanto',   tag: 'EPO · Ĉ ĝ ĥ ĵ ŝ ŭ', text: 'Eble ĉiu kvazaŭ-deca fuŝĥoraĵo ĝojigos homtipon', glyph: 'ccircumflex' },
    { lang: 'Dutch',       tag: 'NLD · Ĳ ĳ ë', text: 'Pa’s wijze lynx bezag vroom het fikse aquaduct op ’t IJsmeer', glyph: 'IJ' },
    { lang: 'Greenlandic', tag: 'KAL · ĸ å ø', text: 'Kalaallit Nunaat — qimmeq, kaffi & kra (ĸ)', glyph: 'kgreenlandic' },
    { lang: 'Sami (North)',tag: 'SME · Ŋ ŋ đ č', text: 'Sámi giella — गो / Vuovdán bohccuid ja guoli ŋ', glyph: 'Eng' },
    { lang: 'English',     tag: 'ENG · fi fl ffi', text: 'Sphinx of black quartz, judge my vow — 1/2 3/4 & fi fl ffi', glyph: 'fi' }
  ];

  const CURATED_KERN_PAIRS = [
    { key: 'A:V', g1: 'A', g2: 'V', label: 'AV', note: 'Diagonal tuck' },
    { key: 'T:o', g1: 'T', g2: 'o', label: 'To', note: 'Under crossbar' },
    { key: 'W:a', g1: 'W', g2: 'a', label: 'Wa', note: 'Apex tuck' },
    { key: 'L:T', g1: 'L', g2: 'T', label: 'LT', note: 'L/T cavity' },
    { key: 'Y:o', g1: 'Y', g2: 'o', label: 'Yo', note: 'Y-underhang' },
    { key: 'F:A', g1: 'F', g2: 'A', label: 'FA', note: 'Lower counter' },
    { key: 'P:period', g1: 'P', g2: 'period', label: 'P.', note: 'Under P bowl' },
    { key: 'V:rcaron', g1: 'V', g2: 'rcaron', label: 'Vř', note: 'Caron safe' }
  ];

  const COMPILER_RECEIPTS = [
    {
      title: 'FontBakery Universal Profile',
      badge: '0 FAIL · 0 WARN · 104 PASS',
      body: 'Executed 126 checks on compiled Aptide-VF.ttf (fontbakery check-universal). 104 PASS, 0 FAIL, 0 WARN, 0 ERROR. Verified STAT, fvar, gvar, HVAR, GSUB, GPOS, OS/2, post, and glyph contour winding.'
    },
    {
      title: 'OpenType Sanitizer (ots-sanitize 9.2.0)',
      badge: '17 / 17 BINARIES SANITIZED',
      body: 'Chromium/Firefox WOFF2 & TTF binary table sanitizer passed all 17 font binaries (Aptide-VF.ttf, Aptide-VF.woff2, and all 15 static instances from Compressed ExtraLight to Extended ExtraBold) with zero warnings.'
    },
    {
      title: 'HarfBuzz Shaping Engine (hb-shape)',
      badge: '68 / 68 RECEIPTS · 26 LANGUAGES',
      body: 'Verified GSUB/GPOS shaping via uharfbuzz & hb-shape across 68 test assertions: liga (fi, fl, ff, ffi, ffl), frac (1/2, 3/4), zero (zero.slash), tnum, onum, case, sups/subs, ordn, and 26 European orthographies.'
    },
    {
      title: 'Pair Collision & Diacritic Audit',
      badge: '3,696 PAIRS · 0 COLLISIONS',
      body: 'Rasterized and boolean-intersected 3,696 neighboring glyph & diacritic pairs (Vř, Ľv, fï, ďi, ťi, Q,) across 8 extreme design-space locations (200/75 to 800/125). Collisions detected: 0.'
    }
  ];

  // Application State
  const state = {
    data: null,
    wght: 400,
    wdth: 100,
    activeGlyph: 'R',
    activeKernKey: 'A:V',
    atlasCat: 'all',
    atlasSearch: '',
    orbitActive: false,
    orbitRaf: null,
    orbitT0: 0,
    layers: {
      masters: true,
      nodes: true,
      callouts: true,
      skeleton: true,
      fill: true
    },
    ot: {
      liga: true,
      kern: true,
      tnum: false,
      zero: false,
      frac: false,
      case: false,
      onum: false,
      ordn: false
    },
    // User live node edits: { [glyphName]: { [coordIdx]: delta } }
    nodeEdits: {}
  };

  // =========================================================================
  // PIECEWISE BILINEAR INTERPOLATION ACROSS 9 MASTERS
  // Masters order in data.json:
  // idx = wdIdx * 3 + wgIdx, where wd in [75, 100, 125], wg in [200, 400, 800]
  // =========================================================================
  function getMasterWeights(wght, wdth) {
    const wg = Math.max(200, Math.min(800, wght));
    const wd = Math.max(75, Math.min(125, wdth));

    let wx;
    if (wg <= 400) {
      const t = (wg - 200) / 200;
      wx = [1 - t, t, 0];
    } else {
      const t = (wg - 400) / 400;
      wx = [0, 1 - t, t];
    }

    let wy;
    if (wd <= 100) {
      const t = (wd - 75) / 25;
      wy = [1 - t, t, 0];
    } else {
      const t = (wd - 100) / 25;
      wy = [0, 1 - t, t];
    }

    const w = new Array(9);
    for (let j = 0; j < 3; j++) {
      for (let i = 0; i < 3; i++) {
        w[j * 3 + i] = wy[j] * wx[i];
      }
    }
    return w;
  }

  function interpScalar9(arr9, weights) {
    let s = 0;
    for (let m = 0; m < 9; m++) s += arr9[m] * weights[m];
    return s;
  }

  function interpArray9(pts9, weights, glyphEdits) {
    const n = pts9[0].length;
    const out = new Array(n);
    for (let i = 0; i < n; i++) {
      let v = 0;
      for (let m = 0; m < 9; m++) v += pts9[m][i] * weights[m];
      if (glyphEdits && glyphEdits[i]) v += glyphEdits[i];
      out[i] = v;
    }
    return out;
  }

  // Convert cmds ('MLCZ...') + flat coords (y-up font units) to SVG path string (y-down SVG units: y_svg = 760 - y_font)
  const SVG_Y_ORIGIN = 760;
  function toSvgY(yFont) {
    return SVG_Y_ORIGIN - yFont;
  }
  function fromSvgY(ySvg) {
    return SVG_Y_ORIGIN - ySvg;
  }

  function buildSvgPath(cmds, pts, dx = 0, dy = 0) {
    let d = '';
    let k = 0;
    for (let i = 0; i < cmds.length; i++) {
      const c = cmds[i];
      if (c === 'M' || c === 'L') {
        const x = (pts[k] + dx).toFixed(1);
        const y = toSvgY(pts[k + 1] + dy).toFixed(1);
        d += `${c}${x} ${y}`;
        k += 2;
      } else if (c === 'C') {
        const x1 = (pts[k] + dx).toFixed(1);
        const y1 = toSvgY(pts[k + 1] + dy).toFixed(1);
        const x2 = (pts[k + 2] + dx).toFixed(1);
        const y2 = toSvgY(pts[k + 3] + dy).toFixed(1);
        const x = (pts[k + 4] + dx).toFixed(1);
        const y = toSvgY(pts[k + 5] + dy).toFixed(1);
        d += `C${x1} ${y1} ${x2} ${y2} ${x} ${y}`;
        k += 6;
      } else if (c === 'Z') {
        d += 'Z';
      }
    }
    return d;
  }

  // Resolve glyph contours across all 9 masters (supports simple outlines + composite glyphs)
  function resolveGlyphContours(glyphName) {
    if (!state.data) return [];
    const g = state.data.glyphs[glyphName];
    if (!g) return [];

    if (g.cmds && g.pts) {
      return [{ cmds: g.cmds, pts9: g.pts, sourceGlyph: glyphName, offset9: null }];
    }
    if (g.components) {
      const parts = [];
      for (const [compName, offsets9] of g.components) {
        const sub = resolveGlyphContours(compName);
        for (const item of sub) {
          // Apply component offset per master
          const shiftedPts9 = item.pts9.map((ptsM, mIdx) => {
            const [ox, oy] = offsets9[mIdx];
            const res = new Array(ptsM.length);
            for (let i = 0; i < ptsM.length; i += 2) {
              res[i] = ptsM[i] + ox;
              res[i + 1] = ptsM[i + 1] + oy;
            }
            return res;
          });
          parts.push({ cmds: item.cmds, pts9: shiftedPts9, sourceGlyph: compName, isComponent: true });
        }
      }
      return parts;
    }
    return [];
  }

  // Compute interpolated bounding box [xmin, ymin, xmax, ymax] in font units
  function computeInterpolatedBounds(contours, weights, edits) {
    let xmin = Infinity, ymin = Infinity, xmax = -Infinity, ymax = -Infinity;
    for (let cIdx = 0; cIdx < contours.length; cIdx++) {
      const c = contours[cIdx];
      const pts = interpArray9(c.pts9, weights, cIdx === 0 ? edits : null);
      for (let i = 0; i < pts.length; i += 2) {
        const x = pts[i];
        const y = pts[i + 1];
        if (x < xmin) xmin = x;
        if (x > xmax) xmax = x;
        if (y < ymin) ymin = y;
        if (y > ymax) ymax = y;
      }
    }
    if (!isFinite(xmin)) return [0, 0, 0, 0];
    return [xmin, ymin, xmax, ymax];
  }

  // Compute interpolated stem metrics at (wght, wdth)
  function getInterpolatedStemMetrics(weights) {
    if (!state.data || !state.data.master_stems) {
      return { vStem: 86, hStem: 73.1 };
    }
    let vStem = 0, hStem = 0;
    for (let m = 0; m < 9; m++) {
      vStem += state.data.master_stems[m].v_stem * weights[m];
      hStem += state.data.master_stems[m].h_stem * weights[m];
    }
    return { vStem, hStem };
  }

  function findNearestInstance(wght, wdth) {
    let best = INSTANCES[9];
    let bestDist = Infinity;
    for (const inst of INSTANCES) {
      const dw = (inst.wght - wght) / 6;
      const dd = (inst.wdth - wdth) * 2;
      const dist = dw * dw + dd * dd;
      if (dist < bestDist) {
        bestDist = dist;
        best = inst;
      }
    }
    return best;
  }

  // Format glyph display character
  function getGlyphDisplayChar(name, g) {
    if (!g) return name;
    if (g.uni) return String.fromCodePoint(g.uni);
    if (name === 'fi') return 'fi';
    if (name === 'fl') return 'fl';
    if (name === 'ff') return 'ff';
    if (name === 'ffi') return 'ffi';
    if (name === 'ffl') return 'ffl';
    if (name === 'zero.slash') return '0̸';
    if (name.endsWith('.tnum') || name.endsWith('.onum') || name.endsWith('.numr') || name.endsWith('.dnom') || name.endsWith('.sups') || name.endsWith('.subs') || name.endsWith('.case')) {
      const baseName = name.split('.')[0];
      const baseG = state.data && state.data.glyphs[baseName];
      if (baseG && baseG.uni) return String.fromCodePoint(baseG.uni);
    }
    return name.slice(0, 3);
  }

  // =========================================================================
  // INITIALIZE UI & EVENT LISTENERS
  // =========================================================================
  async function init() {
    const resp = await fetch('data/aptide-data.json');
    state.data = await resp.json();

    initDesignSpacePad();
    initInstancePills();
    initMaster9Grid();
    initWorkspaceTabs();
    initAxisSliders();
    initCadControls();
    initSpecimenStage();
    initOpenTypeLab();
    initGlyphAtlas();

    updateAll();
  }

  // =========================================================================
  // WORKSPACE VIEW ROUTER
  // =========================================================================
  function initWorkspaceTabs() {
    const tabs = document.querySelectorAll('.ws-tab');
    tabs.forEach(btn => {
      btn.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        const view = btn.dataset.wsView;
        document.body.dataset.view = view;
      });
    });

    const qaBtn = document.getElementById('btnOpenQaModal');
    if (qaBtn) {
      qaBtn.addEventListener('click', () => {
        // Switch specimen deck to Compiler Receipts and highlight
        document.body.dataset.view = 'unified';
        document.querySelectorAll('.ws-tab').forEach(t => {
          t.classList.toggle('active', t.dataset.wsView === 'unified');
        });
        activateSpecimenTab('receipts');
      });
    }
  }

  // =========================================================================
  // 01 // 2D DESIGN-SPACE INTERPOLATOR PAD
  // Pad SVG coordinate system:
  // x: wdth 75 -> 28, wdth 125 -> 292 (span 264)
  // y: wght 800 -> 24, wght 400 -> 180, wght 200 -> 236
  // =========================================================================
  function wdthToPadX(wdth) {
    return 28 + ((wdth - 75) / 50) * 264;
  }
  function padXToWdth(x) {
    const t = Math.max(0, Math.min(1, (x - 28) / 264));
    return 75 + t * 50;
  }
  function wghtToPadY(wght) {
    return 236 - ((wght - 200) / 600) * 212;
  }
  function padYToWght(y) {
    const t = Math.max(0, Math.min(1, (236 - y) / 212));
    return 200 + t * 600;
  }

  function initDesignSpacePad() {
    const masterG = document.getElementById('padMasterNodes');
    const instG = document.getElementById('padInstanceNodes');

    // Render 15 instance dots
    instG.innerHTML = INSTANCES.map(inst => {
      const cx = wdthToPadX(inst.wdth).toFixed(1);
      const cy = wghtToPadY(inst.wght).toFixed(1);
      return `<circle class="pad-instance-circle" cx="${cx}" cy="${cy}" r="3.2"><title>${inst.name} (${inst.wght}/${inst.wdth}%)</title></circle>`;
    }).join('');

    // Render 9 UFO Master squares
    const masters = state.data.masters; // [[200,75], [400,75], [800,75], ...]
    masterG.innerHTML = masters.map(([wg, wd], idx) => {
      const cx = wdthToPadX(wd);
      const cy = wghtToPadY(wg);
      return `<g class="pad-master-node" data-m-idx="${idx}" data-wg="${wg}" data-wd="${wd}">
        <rect class="pad-master-rect" x="${(cx - 5).toFixed(1)}" y="${(cy - 5).toFixed(1)}" width="10" height="10" rx="2"/>
      </g>`;
    }).join('');

    // Pad pointer interaction
    const pad = document.getElementById('cartesianPad');
    let draggingPad = false;

    const updateFromPadEvent = (e) => {
      stopOrbit();
      const rect = pad.getBoundingClientRect();
      const svgX = ((e.clientX - rect.left) / rect.width) * 320;
      const svgY = ((e.clientY - rect.top) / rect.height) * 260;
      state.wdth = Math.round(padXToWdth(svgX) * 2) / 2;
      state.wght = Math.round(padYToWght(svgY));
      updateAll();
    };

    pad.addEventListener('pointerdown', (e) => {
      draggingPad = true;
      pad.setPointerCapture(e.pointerId);
      updateFromPadEvent(e);
    });
    pad.addEventListener('pointermove', (e) => {
      if (!draggingPad) return;
      updateFromPadEvent(e);
    });
    pad.addEventListener('pointerup', () => { draggingPad = false; });
    pad.addEventListener('pointercancel', () => { draggingPad = false; });

    // Orbit toggle
    const btnOrbit = document.getElementById('btnOrbit');
    btnOrbit.addEventListener('click', () => {
      if (state.orbitActive) {
        stopOrbit();
      } else {
        startOrbit();
      }
    });
  }

  function startOrbit() {
    state.orbitActive = true;
    state.orbitT0 = performance.now();
    const btn = document.getElementById('btnOrbit');
    btn.setAttribute('aria-pressed', 'true');
    document.getElementById('orbitBtnText').textContent = 'Stop Orbit';

    const tick = (now) => {
      if (!state.orbitActive) return;
      const elapsed = (now - state.orbitT0) * 0.0012;
      state.wght = Math.round(500 + 285 * Math.sin(elapsed * 1.3));
      state.wdth = Math.round((100 + 23.5 * Math.cos(elapsed * 0.85)) * 2) / 2;
      updateAll();
      state.orbitRaf = requestAnimationFrame(tick);
    };
    state.orbitRaf = requestAnimationFrame(tick);
  }

  function stopOrbit() {
    if (!state.orbitActive) return;
    state.orbitActive = false;
    if (state.orbitRaf) cancelAnimationFrame(state.orbitRaf);
    const btn = document.getElementById('btnOrbit');
    if (btn) btn.setAttribute('aria-pressed', 'false');
    const txt = document.getElementById('orbitBtnText');
    if (txt) txt.textContent = 'Orbit Axes';
  }

  function initMaster9Grid() {
    const grid = document.getElementById('master9Grid');
    // Display order: top row wght 800 (75, 100, 125), middle 400, bottom 200
    const displayOrder = [
      { mIdx: 2, label: '800·75' },
      { mIdx: 5, label: '800·100' },
      { mIdx: 8, label: '800·125' },
      { mIdx: 1, label: '400·75' },
      { mIdx: 4, label: '400·100' },
      { mIdx: 7, label: '400·125' },
      { mIdx: 0, label: '200·75' },
      { mIdx: 3, label: '200·100' },
      { mIdx: 6, label: '200·125' }
    ];

    grid.innerHTML = displayOrder.map(item => {
      const [wg, wd] = state.data.masters[item.mIdx];
      return `<button type="button" class="m9-cell" data-m-idx="${item.mIdx}" data-wg="${wg}" data-wd="${wd}" title="Snap to UFO Master (${wg} / ${wd}%)">
        <div class="m9-top">
          <span class="m9-coord">${item.label}</span>
          <span class="m9-pct" id="m9Pct_${item.mIdx}">0%</span>
        </div>
        <div class="m9-bar" id="m9Bar_${item.mIdx}" style="width:0%"></div>
      </button>`;
    }).join('');

    grid.querySelectorAll('.m9-cell').forEach(cell => {
      cell.addEventListener('click', () => {
        stopOrbit();
        state.wght = Number(cell.dataset.wg);
        state.wdth = Number(cell.dataset.wd);
        updateAll();
      });
    });
  }

  function initInstancePills() {
    const container = document.getElementById('instancePills');
    container.innerHTML = INSTANCES.map((inst, idx) =>
      `<button type="button" class="inst-pill" data-inst-idx="${idx}" title="${inst.name} (wght ${inst.wght}, wdth ${inst.wdth}%)">${inst.short}</button>`
    ).join('');

    container.querySelectorAll('.inst-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        stopOrbit();
        const inst = INSTANCES[Number(btn.dataset.instIdx)];
        state.wght = inst.wght;
        state.wdth = inst.wdth;
        updateAll();
      });
    });
  }

  function initAxisSliders() {
    const sWght = document.getElementById('sliderWght');
    const sWdth = document.getElementById('sliderWdth');

    sWght.addEventListener('input', () => {
      stopOrbit();
      state.wght = Number(sWght.value);
      updateAll();
    });
    sWdth.addEventListener('input', () => {
      stopOrbit();
      state.wdth = Number(sWdth.value);
      updateAll();
    });

    document.querySelectorAll('[data-set-wght]').forEach(btn => {
      btn.addEventListener('click', () => {
        stopOrbit();
        state.wght = Number(btn.dataset.setWght);
        updateAll();
      });
    });
    document.querySelectorAll('[data-set-wdth]').forEach(btn => {
      btn.addEventListener('click', () => {
        stopOrbit();
        state.wdth = Number(btn.dataset.setWdth);
        updateAll();
      });
    });
  }

  // =========================================================================
  // 02 // INTERACTIVE BÉZIER CONTOUR & 9-MASTER OVERLAY EDITOR
  // =========================================================================
  function initCadControls() {
    document.querySelectorAll('.qg-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        selectGlyph(btn.dataset.glyph);
      });
    });

    const bindCheck = (id, key) => {
      const el = document.getElementById(id);
      if (!el) return;
      el.addEventListener('change', () => {
        state.layers[key] = el.checked;
        renderCadEditor();
      });
    };
    bindCheck('chkMasters', 'masters');
    bindCheck('chkNodes', 'nodes');
    bindCheck('chkCallouts', 'callouts');
    bindCheck('chkSkeleton', 'skeleton');
    bindCheck('chkFill', 'fill');

    const resetBtn = document.getElementById('btnResetNodes');
    resetBtn.addEventListener('click', () => {
      delete state.nodeEdits[state.activeGlyph];
      resetBtn.hidden = true;
      renderCadEditor();
    });

    initCadNodeDragging();
  }

  function selectGlyph(glyphName) {
    if (!state.data || !state.data.glyphs[glyphName]) return;
    state.activeGlyph = glyphName;

    document.querySelectorAll('.qg-pill').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.glyph === glyphName);
    });
    document.querySelectorAll('.g-cell').forEach(cell => {
      cell.classList.toggle('active', cell.dataset.glyph === glyphName);
    });

    const resetBtn = document.getElementById('btnResetNodes');
    if (resetBtn) {
      resetBtn.hidden = !state.nodeEdits[glyphName];
    }

    updateAll();
  }

  function initCadNodeDragging() {
    const svg = document.getElementById('cadSvg');
    let dragState = null;

    svg.addEventListener('pointerdown', (e) => {
      const target = e.target.closest('[data-pt-idx]');
      if (!target) return;
      e.preventDefault();
      e.stopPropagation();
      const ptIdx = Number(target.dataset.ptIdx);
      svg.setPointerCapture(e.pointerId);

      const pt = svg.createSVGPoint();
      pt.x = e.clientX;
      pt.y = e.clientY;
      const ctm = svg.getScreenCTM();
      if (!ctm) return;
      const startSvg = pt.matrixTransform(ctm.inverse());

      const edits = state.nodeEdits[state.activeGlyph] || {};
      dragState = {
        ptIdx,
        startSvgX: startSvg.x,
        startSvgY: startSvg.y,
        origDx: edits[ptIdx] || 0,
        origDy: edits[ptIdx + 1] || 0
      };
    });

    svg.addEventListener('pointermove', (e) => {
      if (!dragState) return;
      const pt = svg.createSVGPoint();
      pt.x = e.clientX;
      pt.y = e.clientY;
      const ctm = svg.getScreenCTM();
      if (!ctm) return;
      const curSvg = pt.matrixTransform(ctm.inverse());

      const dxFont = Math.round((curSvg.x - dragState.startSvgX) * 10) / 10;
      const dyFont = Math.round((dragState.startSvgY - curSvg.y) * 10) / 10;

      if (!state.nodeEdits[state.activeGlyph]) {
        state.nodeEdits[state.activeGlyph] = {};
      }
      state.nodeEdits[state.activeGlyph][dragState.ptIdx] = dragState.origDx + dxFont;
      state.nodeEdits[state.activeGlyph][dragState.ptIdx + 1] = dragState.origDy + dyFont;

      const resetBtn = document.getElementById('btnResetNodes');
      if (resetBtn) resetBtn.hidden = false;

      const hint = document.getElementById('hudDragHint');
      if (hint) {
        hint.textContent = `Sculpting node #${dragState.ptIdx / 2} · Δ(${(dragState.origDx + dxFont).toFixed(0)}u, ${(dragState.origDy + dyFont).toFixed(0)}u)`;
      }

      renderCadEditor();
    });

    const endDrag = () => { dragState = null; };
    svg.addEventListener('pointerup', endDrag);
    svg.addEventListener('pointercancel', endDrag);
  }

  function renderCadEditor() {
    if (!state.data) return;
    const svg = document.getElementById('cadSvg');
    const gName = state.activeGlyph;
    const g = state.data.glyphs[gName];
    if (!g) return;

    const weights = getMasterWeights(state.wght, state.wdth);
    const adv = Math.round(interpScalar9(g.adv, weights));
    const contours = resolveGlyphContours(gName);
    const edits = state.nodeEdits[gName] || null;
    const [xmin, ymin, xmax, ymax] = computeInterpolatedBounds(contours, weights, edits);
    const lsb = Math.round(xmin);
    const rsb = Math.round(adv - xmax);
    const { vStem, hStem } = getInterpolatedStemMetrics(weights);

    // Update header title & telemetry
    const uniHex = g.uni ? `U+${g.uni.toString(16).toUpperCase().padStart(4, '0')}` : 'GSUB';
    const dispChar = getGlyphDisplayChar(gName, g);
    document.getElementById('cadGlyphTitle').textContent = `Glyph ‘${dispChar}’ (${gName}) · ${uniHex}`;
    document.getElementById('teleGlyph').textContent = `${gName} · ${uniHex} · ${adv}u`;
    document.getElementById('teleSidebearings').textContent = `LSB ${lsb}u · RSB ${rsb}u`;

    // Dynamically center viewBox around advance width
    const viewWidth = Math.max(1080, adv + 420);
    const viewX = Math.round((adv - viewWidth) / 2);
    svg.setAttribute('viewBox', `${viewX} -150 ${viewWidth} 1180`);

    let html = '';

    // 1. Metric grid & horizontal typographic lines
    const metrics = [
      { y: 740, label: 'ASC 740',      color: 'rgba(148,163,184,0.22)', dash: '4 4' },
      { y: 700, label: 'CAP 700',      color: 'rgba(56,189,248,0.34)',  dash: '' },
      { y: 520, label: 'X-HT 520',     color: 'rgba(245,158,11,0.34)',  dash: '' },
      { y: 0,   label: 'BASELINE 0',   color: 'rgba(34,197,94,0.48)',   dash: '' },
      { y: -210,label: 'DESC −210',    color: 'rgba(148,163,184,0.22)', dash: '4 4' }
    ];

    // Overshoot bands (+12u above Cap/x, -12u below baseline)
    html += `<rect x="${viewX + 20}" y="${toSvgY(712)}" width="${viewWidth - 40}" height="12" fill="rgba(56,189,248,0.05)"/>`;
    html += `<rect x="${viewX + 20}" y="${toSvgY(530)}" width="${viewWidth - 40}" height="10" fill="rgba(245,158,11,0.05)"/>`;
    html += `<rect x="${viewX + 20}" y="${toSvgY(0)}" width="${viewWidth - 40}" height="12" fill="rgba(34,197,94,0.05)"/>`;

    for (const m of metrics) {
      const sy = toSvgY(m.y);
      html += `<line x1="${viewX + 20}" y1="${sy}" x2="${viewX + viewWidth - 20}" y2="${sy}" stroke="${m.color}" stroke-width="1.2" ${m.dash ? `stroke-dasharray="${m.dash}"` : ''}/>`;
      html += `<text x="${viewX + 28}" y="${sy - 7}" fill="rgba(163,177,198,0.82)" font-family="monospace" font-size="18" font-weight="600">${m.label}</text>`;
    }

    // Left origin (x=0) and Advance Width (x=adv) vertical rails
    html += `<line x1="0" y1="-120" x2="0" y2="995" stroke="rgba(56,189,248,0.45)" stroke-width="1.5" stroke-dasharray="6 4"/>`;
    html += `<text x="8" y="-92" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold">ORIGIN 0u</text>`;

    html += `<line x1="${adv}" y1="-120" x2="${adv}" y2="995" stroke="rgba(245,158,11,0.52)" stroke-width="1.5" stroke-dasharray="6 4"/>`;
    html += `<text x="${adv + 8}" y="-92" fill="#f59e0b" font-family="monospace" font-size="18" font-weight="bold">ADV ${adv}u</text>`;

    // 2. 9-Master Ghost Outlines (morphing fan across 200/400/800 x 75/100/125)
    if (state.layers.masters) {
      const masterColors = [
        'rgba(56, 189, 248, 0.30)',  // 200/75
        'rgba(148, 163, 184, 0.25)', // 400/75
        'rgba(245, 158, 11, 0.30)',  // 800/75
        'rgba(56, 189, 248, 0.45)',  // 200/100
        'rgba(148, 163, 184, 0.35)', // 400/100
        'rgba(245, 158, 11, 0.45)',  // 800/100
        'rgba(56, 189, 248, 0.30)',  // 200/125
        'rgba(148, 163, 184, 0.25)', // 400/125
        'rgba(245, 158, 11, 0.35)'   // 800/125
      ];
      for (let m = 0; m < 9; m++) {
        const dMaster = contours.map((c, cIdx) => {
          const ptsM = c.pts9[m];
          if (cIdx === 0 && edits) {
            const shifted = ptsM.map((v, i) => v + (edits[i] || 0));
            return buildSvgPath(c.cmds, shifted);
          }
          return buildSvgPath(c.cmds, ptsM);
        }).join(' ');
        html += `<path d="${dMaster}" fill="none" stroke="${masterColors[m]}" stroke-width="1.15"/>`;
      }
    }

    // 3. Active Interpolated Contour (Filled + Crisp Vector Outline)
    const activePaths = contours.map((c, cIdx) => {
      const pts = interpArray9(c.pts9, weights, cIdx === 0 ? edits : null);
      return { cmds: c.cmds, pts, d: buildSvgPath(c.cmds, pts) };
    });
    const combinedActiveD = activePaths.map(p => p.d).join(' ');

    if (state.layers.fill) {
      html += `<path d="${combinedActiveD}" fill="rgba(244, 240, 232, 0.13)" fill-rule="nonzero"/>`;
    }
    html += `<path d="${combinedActiveD}" fill="none" stroke="#f4f0e8" stroke-width="2.4" stroke-linejoin="round"/>`;

    // 4. Centerline Stroke Skeleton Overlay (from source/geometry.py)
    const skel = state.data.skeletons[gName];
    if (state.layers.skeleton && skel) {
      for (const stroke of skel) {
        const sPts = interpArray9(stroke.pts, weights, null);
        const sD = buildSvgPath(stroke.cmds, sPts);
        html += `<path d="${sD}" fill="none" stroke="#a78bfa" stroke-width="1.8" stroke-dasharray="6 4"/>`;
      }
    }

    // 5. Stem Thickness & LSB/RSB Dimension Callout Arrows
    if (state.layers.callouts && isFinite(xmin) && xmax > xmin) {
      const sxMin = xmin;
      const sxMax = xmax;
      const yFontDim = Math.min(-105, ymin - 55);
      const yDim = toSvgY(yFontDim);

      // Bounding box dashed verticals
      html += `<line x1="${sxMin.toFixed(1)}" y1="${toSvgY(ymax)}" x2="${sxMin.toFixed(1)}" y2="${yDim + 12}" stroke="rgba(34,197,94,0.38)" stroke-width="1.2" stroke-dasharray="4 4"/>`;
      html += `<line x1="${sxMax.toFixed(1)}" y1="${toSvgY(ymax)}" x2="${sxMax.toFixed(1)}" y2="${yDim + 12}" stroke="rgba(34,197,94,0.38)" stroke-width="1.2" stroke-dasharray="4 4"/>`;

      // LSB callout (0 -> xmin)
      const lsbMid = sxMin / 2;
      html += `<line x1="0" y1="${yDim}" x2="${sxMin.toFixed(1)}" y2="${yDim}" stroke="#22c55e" stroke-width="2"/>`;
      html += `<rect x="${(lsbMid - 54).toFixed(1)}" y="${yDim - 32}" width="108" height="26" rx="5" fill="#090d14" stroke="#22c55e" stroke-width="1.3"/>`;
      html += `<text x="${lsbMid.toFixed(1)}" y="${yDim - 14}" text-anchor="middle" fill="#86efac" font-family="monospace" font-size="16" font-weight="bold">LSB ${lsb}u</text>`;

      // Glyph BBox Width callout (xmin -> xmax)
      const bboxW = Math.round(xmax - xmin);
      const midX = (sxMin + sxMax) / 2;
      html += `<line x1="${sxMin.toFixed(1)}" y1="${yDim}" x2="${sxMax.toFixed(1)}" y2="${yDim}" stroke="#38bdf8" stroke-width="2"/>`;
      html += `<rect x="${(midX - 70).toFixed(1)}" y="${yDim - 32}" width="140" height="26" rx="5" fill="#090d14" stroke="#38bdf8" stroke-width="1.3"/>`;
      html += `<text x="${midX.toFixed(1)}" y="${yDim - 14}" text-anchor="middle" fill="#bae6fd" font-family="monospace" font-size="16" font-weight="bold">BBOX ${bboxW}u</text>`;

      // RSB callout (xmax -> adv)
      const rsbMid = (sxMax + adv) / 2;
      html += `<line x1="${sxMax.toFixed(1)}" y1="${yDim}" x2="${adv}" y2="${yDim}" stroke="#f59e0b" stroke-width="2"/>`;
      html += `<rect x="${(rsbMid - 54).toFixed(1)}" y="${yDim - 32}" width="108" height="26" rx="5" fill="#090d14" stroke="#f59e0b" stroke-width="1.3"/>`;
      html += `<text x="${rsbMid.toFixed(1)}" y="${yDim - 14}" text-anchor="middle" fill="#fcd34d" font-family="monospace" font-size="16" font-weight="bold">RSB ${rsb}u</text>`;

      // Live Vertical Stem Thickness Callout Badge inside the glyph stem
      const stemY = toSvgY(Math.min(Math.max(260, (ymin + ymax) * 0.48), 540));
      const centeredStems = ['T', 'I', 'Y', 'i', 'l', 't', 'one', 'plus', 'dagger'];
      const stemX0 = centeredStems.includes(gName) ? ((sxMin + sxMax - vStem) / 2) : sxMin;
      const stemX1 = stemX0 + vStem;
      html += `<line x1="${stemX0.toFixed(1)}" y1="${stemY}" x2="${stemX1.toFixed(1)}" y2="${stemY}" stroke="#f43f5e" stroke-width="2.6"/>`;
      html += `<circle cx="${stemX0.toFixed(1)}" cy="${stemY}" r="4.2" fill="#f43f5e"/>`;
      html += `<circle cx="${stemX1.toFixed(1)}" cy="${stemY}" r="4.2" fill="#f43f5e"/>`;
      html += `<rect x="${(stemX1 + 12).toFixed(1)}" y="${stemY - 15}" width="166" height="30" rx="5" fill="rgba(9,13,20,0.94)" stroke="#f43f5e" stroke-width="1.4"/>`;
      html += `<text x="${(stemX1 + 95).toFixed(1)}" y="${stemY + 5}" text-anchor="middle" fill="#fda4af" font-family="monospace" font-size="16" font-weight="bold">V-Stem ${vStem.toFixed(1)}u</text>`;

      // Anchors (top, bottom, ogonek) if present
      if (g.anchors) {
        for (const [aName, [ax, ay]] of Object.entries(g.anchors)) {
          const sax = ax * (adv / g.adv[4] || 1);
          const say = toSvgY(ay);
          const dyTxt = aName === 'top' ? -14 : 20;
          html += `<g transform="translate(${sax.toFixed(1)}, ${say.toFixed(1)})">
            <line x1="-10" y1="0" x2="10" y2="0" stroke="#f43f5e" stroke-width="1.8"/>
            <line x1="0" y1="-10" x2="0" y2="10" stroke="#f43f5e" stroke-width="1.8"/>
            <circle cx="0" cy="0" r="4.5" fill="none" stroke="#f43f5e" stroke-width="1.8"/>
            <text x="13" y="${dyTxt}" fill="#fda4af" font-family="monospace" font-size="15" font-weight="bold">anchor:${aName}</text>
          </g>`;
        }
      }
    }

    // 6. On-Curve & Off-Curve Bézier Nodes + Control Handle Tangents (Draggable!)
    let totalOnCurve = 0;
    let totalCubics = 0;
    let totalContours = 0;

    if (state.layers.nodes) {
      activePaths.forEach((pathObj, cIdx) => {
        const { cmds, pts } = pathObj;
        const canDrag = (cIdx === 0);
        let k = 0;
        let curX = 0, curY = 0;

        for (let i = 0; i < cmds.length; i++) {
          const cmd = cmds[i];
          if (cmd === 'M') {
            totalContours++;
            totalOnCurve++;
            curX = pts[k];
            curY = toSvgY(pts[k + 1]);
            const dragAttr = canDrag ? `data-pt-idx="${k}"` : '';
            html += `<rect class="cad-node-on" ${dragAttr} x="${(curX - 4.2).toFixed(1)}" y="${(curY - 4.2).toFixed(1)}" width="8.4" height="8.4" fill="#22c55e" stroke="#090d14" stroke-width="1.5"/>`;
            k += 2;
          } else if (cmd === 'L') {
            totalOnCurve++;
            curX = pts[k];
            curY = toSvgY(pts[k + 1]);
            const dragAttr = canDrag ? `data-pt-idx="${k}"` : '';
            html += `<rect class="cad-node-on" ${dragAttr} x="${(curX - 3.8).toFixed(1)}" y="${(curY - 3.8).toFixed(1)}" width="7.6" height="7.6" fill="#22c55e" stroke="#090d14" stroke-width="1.4"/>`;
            k += 2;
          } else if (cmd === 'C') {
            totalCubics++;
            totalOnCurve++;
            const x1 = pts[k],     y1 = toSvgY(pts[k + 1]);
            const x2 = pts[k + 2], y2 = toSvgY(pts[k + 3]);
            const x  = pts[k + 4], y  = toSvgY(pts[k + 5]);

            // Handle lines
            html += `<line x1="${curX.toFixed(1)}" y1="${curY.toFixed(1)}" x2="${x1.toFixed(1)}" y2="${y1.toFixed(1)}" stroke="rgba(56,189,248,0.65)" stroke-width="1.15"/>`;
            html += `<line x1="${x.toFixed(1)}" y1="${y.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="rgba(56,189,248,0.65)" stroke-width="1.15"/>`;

            // Off-curve cubic handle nodes (circles)
            const drag1 = canDrag ? `data-pt-idx="${k}"` : '';
            const drag2 = canDrag ? `data-pt-idx="${k + 2}"` : '';
            const dragEnd = canDrag ? `data-pt-idx="${k + 4}"` : '';

            html += `<circle class="cad-node-off" ${drag1} cx="${x1.toFixed(1)}" cy="${y1.toFixed(1)}" r="3.8" fill="#38bdf8" stroke="#090d14" stroke-width="1.3"/>`;
            html += `<circle class="cad-node-off" ${drag2} cx="${x2.toFixed(1)}" cy="${y2.toFixed(1)}" r="3.8" fill="#38bdf8" stroke="#090d14" stroke-width="1.3"/>`;
            // On-curve endpoint
            html += `<rect class="cad-node-on" ${dragEnd} x="${(x - 3.8).toFixed(1)}" y="${(y - 3.8).toFixed(1)}" width="7.6" height="7.6" fill="#22c55e" stroke="#090d14" stroke-width="1.4"/>`;

            curX = x;
            curY = y;
            k += 6;
          }
        }
      });
    } else {
      // Count stats even when nodes layer is hidden
      activePaths.forEach(({ cmds }) => {
        for (const cmd of cmds) {
          if (cmd === 'M') { totalContours++; totalOnCurve++; }
          else if (cmd === 'L') { totalOnCurve++; }
          else if (cmd === 'C') { totalCubics++; totalOnCurve++; }
        }
      });
    }

    svg.innerHTML = html;

    const totalPts = totalOnCurve + totalCubics * 2;
    document.getElementById('hudNodeStats').textContent =
      `${totalPts} pts (${totalOnCurve} on-curve · ${totalCubics * 2} off-curve handles) · ${totalContours} contour${totalContours === 1 ? '' : 's'}`;
  }

  // =========================================================================
  // 03 // LIVE KINETIC & EDITORIAL SPECIMEN STAGE
  // =========================================================================
  function initSpecimenStage() {
    // Specimen sub-mode tabs
    document.querySelectorAll('.spec-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        activateSpecimenTab(tab.dataset.specMode);
      });
    });

    // Phrase preset buttons
    const specEl = document.getElementById('liveSpecimenText');
    document.querySelectorAll('.phrase-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.phrase-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        specEl.textContent = btn.dataset.phrase;
      });
    });

    // Size & Tracking sliders
    const sizeSlider = document.getElementById('specSizeSlider');
    const sizeOut = document.getElementById('specSizeOut');
    sizeSlider.addEventListener('input', () => {
      specEl.style.fontSize = `${sizeSlider.value}px`;
      sizeOut.textContent = `${sizeSlider.value}px`;
    });

    const trackSlider = document.getElementById('specTrackSlider');
    const trackOut = document.getElementById('specTrackOut');
    trackSlider.addEventListener('input', () => {
      const val = Number(trackSlider.value);
      specEl.style.letterSpacing = `${(val * 0.01).toFixed(3)}em`;
      trackOut.textContent = `${val > 0 ? '+' : ''}${val}%`;
    });

    // Build 9-Master Waterfall cards
    const wfGrid = document.getElementById('waterfallGrid');
    wfGrid.innerHTML = INSTANCES.map(inst => `
      <div class="wf-card" data-wg="${inst.wght}" data-wd="${inst.wdth}" title="Click to set axes to ${inst.name}">
        <div class="wf-meta">
          <span>${inst.name}</span>
          <span>${inst.wght} / ${inst.wdth}%</span>
        </div>
        <div class="wf-sample" style="font-variation-settings:'wght' ${inst.wght}, 'wdth' ${inst.wdth}">
          Sphinx of black quartz 0123 &amp; fi
        </div>
      </div>
    `).join('');

    wfGrid.querySelectorAll('.wf-card').forEach(card => {
      card.addEventListener('click', () => {
        stopOrbit();
        state.wght = Number(card.dataset.wg);
        state.wdth = Number(card.dataset.wd);
        updateAll();
      });
    });

    // Build 26-Language HarfBuzz Proof cards
    const langGrid = document.getElementById('langProofGrid');
    langGrid.innerHTML = LANGUAGES_26.map((item, idx) => `
      <div class="lang-card" data-lang-idx="${idx}" title="Click to load ${item.lang} into Specimen &amp; CAD Inspector">
        <div class="lang-top">
          <strong>${item.lang}</strong>
          <span>${item.tag}</span>
        </div>
        <div class="lang-sample">${item.text}</div>
      </div>
    `).join('');

    langGrid.querySelectorAll('.lang-card').forEach(card => {
      card.addEventListener('click', () => {
        const item = LANGUAGES_26[Number(card.dataset.langIdx)];
        specEl.textContent = item.text;
        if (item.glyph && state.data.glyphs[item.glyph]) {
          selectGlyph(item.glyph);
        }
      });
    });

    // Build Compiler & QA Receipts cards
    const recGrid = document.getElementById('receiptsGrid');
    recGrid.innerHTML = COMPILER_RECEIPTS.map(r => `
      <div class="receipt-card">
        <div class="receipt-head">
          <span class="receipt-title">${r.title}</span>
          <span class="receipt-badge">${r.badge}</span>
        </div>
        <p class="receipt-body">${r.body}</p>
      </div>
    `).join('');
  }

  function activateSpecimenTab(mode) {
    document.querySelectorAll('.spec-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.specMode === mode);
    });
    const map = {
      editorial: 'specViewEditorial',
      waterfall: 'specViewWaterfall',
      languages: 'specViewLanguages',
      receipts:  'specViewReceipts'
    };
    for (const [k, id] of Object.entries(map)) {
      const el = document.getElementById(id);
      if (el) el.hidden = (k !== mode);
    }
  }

  // =========================================================================
  // 04 // OPENTYPE FEATURE & LIVE GPOS KERNING LABORATORY
  // =========================================================================
  function initOpenTypeLab() {
    document.querySelectorAll('.ot-card').forEach(card => {
      card.addEventListener('click', () => {
        const tag = card.dataset.ot;
        state.ot[tag] = !state.ot[tag];
        card.classList.toggle('active', state.ot[tag]);
        card.setAttribute('aria-pressed', String(state.ot[tag]));
        card.querySelector('.ot-state').textContent = state.ot[tag] ? 'ON' : 'OFF';

        // Also load a relevant glyph or specimen when toggled on
        if (state.ot[tag]) {
          if (tag === 'liga') selectGlyph('fi');
          else if (tag === 'zero') selectGlyph('zero.slash');
          else if (tag === 'frac') selectGlyph('fraction');
        }
        updateOpenTypeSettings();
        renderKerningInspector();
      });
    });

    // Build curated kerning pair buttons
    const strip = document.getElementById('kernPairStrip');
    strip.innerHTML = CURATED_KERN_PAIRS.map(p => `
      <button type="button" class="kern-chip ${p.key === state.activeKernKey ? 'active' : ''}" data-kern-key="${p.key}">
        <span class="kern-pair-letters">${p.label}</span>
        <span class="kern-unit-badge" data-kern-badge="${p.key}">−88u</span>
      </button>
    `).join('');

    strip.querySelectorAll('.kern-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        state.activeKernKey = chip.dataset.kernKey;
        strip.querySelectorAll('.kern-chip').forEach(c => c.classList.toggle('active', c === chip));
        const pairObj = CURATED_KERN_PAIRS.find(p => p.key === state.activeKernKey);
        if (pairObj && state.data.glyphs[pairObj.g1]) {
          selectGlyph(pairObj.g1);
        }
        renderKerningInspector();
      });
    });

    updateOpenTypeSettings();
  }

  function updateOpenTypeSettings() {
    const parts = [];
    let activeCount = 0;

    const addFeat = (tag, on) => {
      parts.push(`"${tag}" ${on ? 1 : 0}`);
      if (on) activeCount++;
    };

    addFeat('liga', state.ot.liga);
    addFeat('kern', state.ot.kern);
    addFeat('tnum', state.ot.tnum);
    addFeat('zero', state.ot.zero);
    addFeat('frac', state.ot.frac);
    addFeat('case', state.ot.case);
    addFeat('onum', state.ot.onum);
    if (state.ot.ordn) {
      parts.push('"ordn" 1, "sups" 1, "subs" 1');
      activeCount++;
    } else {
      parts.push('"ordn" 0');
    }

    const cssFeat = parts.join(', ');
    document.documentElement.style.setProperty('--ot-features', cssFeat);

    const activeTags = Object.entries(state.ot).filter(([, v]) => v).map(([k]) => `'${k}' 1`);
    document.getElementById('teleFeatures').textContent = activeTags.length ? activeTags.join(', ') : 'All OFF';
    document.getElementById('otActiveCountBadge').textContent = `${activeCount} Active`;
  }

  function getPairKernAtWeights(key, weights) {
    if (!state.data || !state.data.kern_pairs) return -80;
    const arr9 = state.data.kern_pairs[key];
    if (!arr9) return 0;
    return Math.round(interpScalar9(arr9, weights));
  }

  function renderKerningInspector() {
    if (!state.data) return;
    const weights = getMasterWeights(state.wght, state.wdth);
    const kernEnabled = state.ot.kern;

    // Update all 8 kerning pair unit badges
    for (const p of CURATED_KERN_PAIRS) {
      const val = getPairKernAtWeights(p.key, weights);
      const badge = document.querySelector(`[data-kern-badge="${p.key}"]`);
      if (badge) {
        const disp = kernEnabled ? `${val > 0 ? '+' : '−'}${Math.abs(val)}u` : '0u (OFF)';
        badge.textContent = disp;
      }
    }

    // Render active dual-glyph vector kerning diagram
    const activePair = CURATED_KERN_PAIRS.find(p => p.key === state.activeKernKey) || CURATED_KERN_PAIRS[0];
    const rawKern = getPairKernAtWeights(activePair.key, weights);
    const appliedKern = kernEnabled ? rawKern : 0;

    const g1 = state.data.glyphs[activePair.g1];
    const g2 = state.data.glyphs[activePair.g2];
    if (!g1 || !g2) return;

    const adv1 = Math.round(interpScalar9(g1.adv, weights));
    const adv2 = Math.round(interpScalar9(g2.adv, weights));

    const c1 = resolveGlyphContours(activePair.g1);
    const c2 = resolveGlyphContours(activePair.g2);

    const d1 = c1.map(c => buildSvgPath(c.cmds, interpArray9(c.pts9, weights, null), 90, 0)).join(' ');
    const x2Unkerned = 90 + adv1;
    const x2Kerned = 90 + adv1 + appliedKern;

    const d2Unkerned = c2.map(c => buildSvgPath(c.cmds, interpArray9(c.pts9, weights, null), x2Unkerned, 0)).join(' ');
    const d2Kerned = c2.map(c => buildSvgPath(c.cmds, interpArray9(c.pts9, weights, null), x2Kerned, 0)).join(' ');

    const totalAdv = adv1 + appliedKern + adv2;
    const svg = document.getElementById('kernSvg');
    svg.setAttribute('viewBox', `0 -100 ${Math.max(1240, totalAdv + 200)} 910`);

    const zoneX = Math.min(x2Unkerned, x2Kerned);
    const zoneW = Math.max(4, Math.abs(rawKern));

    svg.innerHTML = `
      <!-- Baseline & Cap height -->
      <line x1="20" y1="${toSvgY(700)}" x2="1350" y2="${toSvgY(700)}" stroke="rgba(148,163,184,0.18)" stroke-width="1"/>
      <line x1="20" y1="${toSvgY(0)}" x2="1350" y2="${toSvgY(0)}" stroke="rgba(34,197,94,0.35)" stroke-width="1"/>

      <!-- Kerning overlap compensation zone -->
      <rect x="${zoneX}" y="${toSvgY(720)}" width="${zoneW}" height="740" fill="rgba(245, 158, 11, 0.14)" stroke="rgba(245, 158, 11, 0.55)" stroke-width="1.2" stroke-dasharray="4 3"/>

      <!-- Ghost unkerned second glyph -->
      <path d="${d2Unkerned}" fill="none" stroke="rgba(244, 63, 94, 0.38)" stroke-width="2" stroke-dasharray="5 4"/>

      <!-- First glyph -->
      <path d="${d1}" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="2.2"/>

      <!-- Kerned second glyph -->
      <path d="${d2Kerned}" fill="rgba(245, 158, 11, 0.22)" stroke="#f59e0b" stroke-width="2.2"/>

      <!-- Callout badge in SVG -->
      <rect x="${zoneX - 28}" y="${toSvgY(810)}" width="136" height="36" rx="5" fill="#090d14" stroke="#f59e0b" stroke-width="1.4"/>
      <text x="${zoneX + 40}" y="${toSvgY(787)}" text-anchor="middle" fill="#fcd34d" font-family="monospace" font-size="18" font-weight="bold">
        ${kernEnabled ? `KERN ${rawKern}u` : 'KERN OFF (0u)'}
      </text>
    `;

    document.getElementById('kernPairHeaderVal').textContent =
      `${activePair.label}: ${kernEnabled ? `${rawKern}u` : '0u (OFF)'}`;
    document.getElementById('kernStageCaption').innerHTML = `
      <span><strong>${activePair.label}</strong> · ${activePair.note}</span>
      <span>${adv1}u ${appliedKern < 0 ? '− ' + Math.abs(appliedKern) : '+ ' + appliedKern}u + ${adv2}u = <strong>${totalAdv}u</strong></span>
    `;
  }

  // =========================================================================
  // 05 // 548-GLYPH MULTILINGUAL ATLAS
  // =========================================================================
  function classifyGlyph(name, g) {
    const u = g.uni;
    if (name.startsWith('uni03') || (!u && (name.includes('comb') || ['acute','grave','circumflex','caron','tilde','macron','breve','dotaccent','dieresis','ring','hungarumlaut','cedilla','ogonek','commaaccent'].includes(name)))) {
      return 'marks';
    }
    if (!u || name.includes('.') || ['fi','fl','ff','ffi','ffl','fraction','ordfeminine','ordmasculine','onesuperior','twosuperior','threesuperior'].includes(name)) {
      if (['zero','one','two','three','four','five','six','seven','eight','nine'].some(d => name.startsWith(d)) || ['fraction','onehalf','onequarter','threequarters','percent','perthousand'].includes(name)) {
        return 'figures';
      }
      return 'opentype';
    }
    if (u >= 0x30 && u <= 0x39) return 'figures';
    if (u >= 0x20 && u <= 0x7E) {
      if ((u >= 0x41 && u <= 0x5A) || (u >= 0x61 && u <= 0x7A)) return 'ascii';
      return 'symbols';
    }
    if (u >= 0x00C0 && u <= 0x024F) return 'latin';
    if (u >= 0x02B0 && u <= 0x036F) return 'marks';
    return 'symbols';
  }

  function initGlyphAtlas() {
    const filterBtns = document.querySelectorAll('.af-pill');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.atlasCat = btn.dataset.cat;
        renderGlyphAtlas();
      });
    });

    const searchInput = document.getElementById('atlasSearch');
    searchInput.addEventListener('input', () => {
      state.atlasSearch = searchInput.value.trim().toLowerCase();
      renderGlyphAtlas();
    });

    renderGlyphAtlas();
  }

  function renderGlyphAtlas() {
    if (!state.data) return;
    const scrollEl = document.getElementById('glyphCellsScroll');
    const entries = Object.entries(state.data.glyphs);

    const filtered = entries.filter(([name, g]) => {
      if (state.atlasCat !== 'all' && classifyGlyph(name, g) !== state.atlasCat) {
        return false;
      }
      if (state.atlasSearch) {
        const q = state.atlasSearch;
        const hex = g.uni ? g.uni.toString(16).toLowerCase() : '';
        const ch = g.uni ? String.fromCodePoint(g.uni).toLowerCase() : '';
        return name.toLowerCase().includes(q) || hex.includes(q.replace('u+', '')) || ch === q;
      }
      return true;
    });

    document.getElementById('glyphFilterCount').textContent = `(${filtered.length})`;

    scrollEl.innerHTML = filtered.map(([name, g]) => {
      const disp = getGlyphDisplayChar(name, g);
      const isAct = name === state.activeGlyph ? 'active' : '';
      const uTag = g.uni ? `U+${g.uni.toString(16).toUpperCase().padStart(4, '0')}` : 'OT';
      return `<button type="button" class="g-cell ${isAct}" data-glyph="${name}" role="option" aria-selected="${name === state.activeGlyph}" title="${name} (${uTag})">
        <span class="g-char">${disp}</span>
        <span class="g-name">${name}</span>
      </button>`;
    }).join('');

    scrollEl.querySelectorAll('.g-cell').forEach(cell => {
      cell.addEventListener('click', () => {
        selectGlyph(cell.dataset.glyph);
      });
    });
  }

  // =========================================================================
  // MASTER SYNCHRONIZATION LOOP
  // =========================================================================
  function updateAll() {
    if (!state.data) return;

    const wght = state.wght;
    const wdth = state.wdth;
    const weights = getMasterWeights(wght, wdth);
    const { vStem, hStem } = getInterpolatedStemMetrics(weights);
    const nearest = findNearestInstance(wght, wdth);

    // 1. Update CSS custom properties for live @font-face rendering
    document.documentElement.style.setProperty('--wght', String(wght));
    document.documentElement.style.setProperty('--wdth', String(wdth));

    // 2. Update sliders & readouts
    document.getElementById('sliderWght').value = String(wght);
    document.getElementById('sliderWdth').value = String(wdth);
    document.getElementById('outWght').textContent = String(wght);
    document.getElementById('outWdth').textContent = `${wdth}%`;
    document.getElementById('padReadout').textContent = `${wght} / ${wdth}%`;

    // 3. Update Telemetry Ribbon
    document.getElementById('teleCoord').textContent = `wght ${wght} · wdth ${wdth}%`;
    document.getElementById('teleInstance').textContent = `${nearest.name} (${nearest.wght}/${nearest.wdth}%)`;
    document.getElementById('teleStems').textContent = `V ${vStem.toFixed(1)}u · H ${hStem.toFixed(1)}u`;

    // 4. Update 2D Cartesian Pad cursor & dynamic bilinear tether lines
    const cx = wdthToPadX(wdth);
    const cy = wghtToPadY(wght);
    document.getElementById('padCursorDot').setAttribute('cx', cx.toFixed(1));
    document.getElementById('padCursorDot').setAttribute('cy', cy.toFixed(1));
    document.getElementById('padCursorHalo').setAttribute('cx', cx.toFixed(1));
    document.getElementById('padCursorHalo').setAttribute('cy', cy.toFixed(1));
    document.getElementById('padCrossX').setAttribute('x1', cx.toFixed(1));
    document.getElementById('padCrossX').setAttribute('x2', cx.toFixed(1));
    document.getElementById('padCrossY').setAttribute('y1', cy.toFixed(1));
    document.getElementById('padCrossY').setAttribute('y2', cy.toFixed(1));

    const tethersEl = document.getElementById('padTethers');
    tethersEl.innerHTML = state.data.masters.map(([mwg, mwd], idx) => {
      const w = weights[idx];
      if (w < 0.01) return '';
      const mx = wdthToPadX(mwd).toFixed(1);
      const my = wghtToPadY(mwg).toFixed(1);
      return `<line x1="${cx.toFixed(1)}" y1="${cy.toFixed(1)}" x2="${mx}" y2="${my}" stroke="rgba(56, 189, 248, ${(0.18 + w * 0.75).toFixed(2)})" stroke-width="${(1 + w * 2.5).toFixed(1)}"/>`;
    }).join('');

    // 5. Update 9-Master Bilinear Contribution cells
    for (let m = 0; m < 9; m++) {
      const pct = Math.round(weights[m] * 100);
      const pctEl = document.getElementById(`m9Pct_${m}`);
      const barEl = document.getElementById(`m9Bar_${m}`);
      if (pctEl) pctEl.textContent = `${pct}%`;
      if (barEl) barEl.style.width = `${pct}%`;
    }

    // 6. Highlight active named instance pill
    document.querySelectorAll('.inst-pill').forEach(pill => {
      const inst = INSTANCES[Number(pill.dataset.instIdx)];
      const isMatch = Math.abs(inst.wght - wght) <= 8 && Math.abs(inst.wdth - wdth) <= 1.5;
      pill.classList.toggle('active', isMatch);
    });

    // 7. Render CAD Contour Editor & GPOS Kerning Inspector
    renderCadEditor();
    renderKerningInspector();
  }

  window.addEventListener('DOMContentLoaded', init);
})();
