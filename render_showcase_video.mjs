import { chromium } from 'playwright';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';

const APP_DIR = '/home/user/workspace/letterform-variable-foundry/app';
const VIDEO_DIR = '/home/user/workspace/letterform-variable-foundry/video';
const MANIFEST_PATH = path.join(VIDEO_DIR, 'scenes_manifest.json');
const AUDIO_PATH = path.join(VIDEO_DIR, 'master_audio.wav');
const OUT_MP4 = '/home/user/workspace/letterform-variable-foundry/Letterform-Aptide-Variable-Foundry-Showcase.mp4';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.pdf': 'application/pdf',
  '.zip': 'application/zip'
};

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      const cleanUrl = req.url.split('?')[0];
      const relPath = cleanUrl === '/' ? '/index.html' : cleanUrl;
      const fullPath = path.join(APP_DIR, relPath);
      if (!fs.existsSync(fullPath) || fs.statSync(fullPath).isDirectory()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = path.extname(fullPath);
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      fs.createReadStream(fullPath).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => {
      resolve({ server, port: server.address().port });
    });
  });
}

function easeInOutCubic(x) {
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

async function main() {
  const manifestData = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  const scenes = manifestData.scenes;
  const totalDur = manifestData.total_duration;

  // Override camera coordinates for s10, s11, s12 so x=384..1920 shows 100% of Center + Right columns with zero text clipping
  const camOverrides = {
    s01: { zoom: 1.0,  cx: 960,  cy: 506 },
    s02: { zoom: 1.0,  cx: 960,  cy: 506 },
    s03: { zoom: 1.30, cx: 738,  cy: 390 },
    s04: { zoom: 1.30, cx: 738,  cy: 615 },
    s05: { zoom: 1.35, cx: 924,  cy: 375 },
    s06: { zoom: 1.35, cx: 924,  cy: 375 },
    s07: { zoom: 1.35, cx: 924,  cy: 375 },
    s08: { zoom: 1.0,  cx: 960,  cy: 506 },
    s09: { zoom: 1.30, cx: 924,  cy: 620 },
    s10: { zoom: 1.25, cx: 1152, cy: 420 },
    s11: { zoom: 1.25, cx: 1152, cy: 455 },
    s12: { zoom: 1.25, cx: 1152, cy: 615 },
    s13: { zoom: 1.0,  cx: 960,  cy: 506 },
    s14: { zoom: 1.0,  cx: 960,  cy: 506 },
    s15: { zoom: 1.0,  cx: 960,  cy: 506 },
    s16: { zoom: 1.0,  cx: 960,  cy: 506 }
  };
  for (const sc of scenes) {
    if (camOverrides[sc.id]) {
      sc.zoom = camOverrides[sc.id].zoom;
      sc.cx = camOverrides[sc.id].cx;
      sc.cy = camOverrides[sc.id].cy;
    }
  }

  const { server, port } = await startServer();
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForSelector('#cadSvg .cad-node-on');
  await page.waitForTimeout(400);

  // Inject camera wrapper, bottom caption bar, and custom high-contrast cursor
  await page.evaluate(() => {
    const stage = document.createElement('div');
    stage.id = 'cameraStage';
    stage.style.cssText = `
      width: 1920px;
      height: 1012px;
      position: fixed;
      top: 0;
      left: 0;
      overflow: hidden;
      transform-origin: 0 0;
      display: flex;
      flex-direction: column;
      background: #07090d;
    `;
    while (document.body.firstChild) {
      stage.appendChild(document.body.firstChild);
    }
    document.body.appendChild(stage);
    document.body.style.cssText = `
      margin: 0;
      padding: 0;
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #05070b;
    `;

    // Adjust foundry-grid inside cameraStage so it fits 1012px height cleanly
    const styleEl = document.createElement('style');
    styleEl.textContent = `
      #cameraStage .foundry-grid {
        height: calc(1012px - 82px) !important;
      }
      #showcaseBottomBar {
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        height: 68px;
        background: #05070b;
        border-top: 1px solid rgba(56, 189, 248, 0.22);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
        padding: 0 32px;
      }
      #showcaseCaptionPill {
        display: inline-flex;
        align-items: center;
        gap: 14px;
        background: rgba(11, 16, 26, 0.96);
        border: 1.5px solid rgba(56, 189, 248, 0.42);
        border-radius: 999px;
        padding: 9px 26px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.65);
        max-width: 1760px;
      }
      #showcaseSceneTag {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 12px;
        font-weight: 600;
        color: #38bdf8;
        background: rgba(56, 189, 248, 0.14);
        border: 1px solid rgba(56, 189, 248, 0.35);
        padding: 3px 10px;
        border-radius: 999px;
        letter-spacing: 0.04em;
        white-space: nowrap;
      }
      #showcaseCaptionText {
        font-family: 'AptideVariable', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 21.5px;
        font-weight: 500;
        color: #f8fafc;
        letter-spacing: 0.01em;
        line-height: 1.25;
        white-space: nowrap;
      }
      #showcaseCursor {
        position: fixed;
        left: 960px;
        top: 500px;
        width: 28px;
        height: 28px;
        pointer-events: none;
        z-index: 999990;
        transform: translate(-4px, -4px);
      }
      #showcaseCursorRipple {
        position: absolute;
        left: 4px;
        top: 4px;
        width: 34px;
        height: 34px;
        border-radius: 50%;
        border: 2.5px solid #38bdf8;
        background: rgba(56, 189, 248, 0.22);
        transform: translate(-50%, -50%) scale(0);
        opacity: 0;
      }
    `;
    document.head.appendChild(styleEl);

    const bottomBar = document.createElement('div');
    bottomBar.id = 'showcaseBottomBar';
    bottomBar.innerHTML = `
      <div id="showcaseCaptionPill">
        <span id="showcaseSceneTag">01 / 16</span>
        <span id="showcaseCaptionText"></span>
      </div>
    `;
    document.body.appendChild(bottomBar);

    const cursor = document.createElement('div');
    cursor.id = 'showcaseCursor';
    cursor.innerHTML = `
      <div id="showcaseCursorRipple"></div>
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
        <path d="M4 3L12.5 24L15.8 15.8L24 12.5L4 3Z" fill="#38bdf8" stroke="#07090d" stroke-width="2.2" stroke-linejoin="round"/>
      </svg>
    `;
    document.body.appendChild(cursor);

    window.__setShowcaseFrame = function({ zoom, cx, cy, sceneIdx, caption, cursorX, cursorY, rippleProgress }) {
      const W = 1920, H = 1012;
      const viewW = W / zoom;
      const viewH = H / zoom;
      let x0 = cx - viewW / 2;
      let y0 = cy - viewH / 2;
      x0 = Math.max(0, Math.min(W - viewW, x0));
      y0 = Math.max(0, Math.min(H - viewH, y0));
      stage.style.transform = `scale(${zoom.toFixed(4)}) translate(${(-x0).toFixed(2)}px, ${(-y0).toFixed(2)}px)`;

      // Convert stage-space cursor (cursorX, cursorY) into screen-space
      const screenX = (cursorX - x0) * zoom;
      const screenY = (cursorY - y0) * zoom;
      cursor.style.left = `${screenX.toFixed(1)}px`;
      cursor.style.top = `${screenY.toFixed(1)}px`;

      const ripple = document.getElementById('showcaseCursorRipple');
      if (rippleProgress > 0 && rippleProgress < 1) {
        const s = 0.3 + rippleProgress * 1.35;
        const op = 1 - rippleProgress;
        ripple.style.transform = `translate(-50%, -50%) scale(${s.toFixed(2)})`;
        ripple.style.opacity = op.toFixed(2);
      } else {
        ripple.style.opacity = '0';
      }

      document.getElementById('showcaseSceneTag').textContent = `${String(sceneIdx).padStart(2, '0')} / 16`;
      document.getElementById('showcaseCaptionText').textContent = caption;
    };
  });

  // Helper to get center of any selector in stage-space (when zoom=1)
  async function getBoxCenter(selector) {
    return await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      if (!el) return { x: 960, y: 500 };
      const r = el.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }, selector);
  }

  // Query key UI coordinates at 1x before starting
  const coords = {
    center: { x: 960, y: 480 },
    qaBadge: await getBoxCenter('#btnOpenQaModal'),
    padSvg: await getBoxCenter('#designSpacePad'),
    instCompXLt: await getBoxCenter('.inst-pill[data-inst-idx="0"]'),
    instCondSBd: await getBoxCenter('.inst-pill[data-inst-idx="6"]'),
    instExtraBd: await getBoxCenter('.inst-pill[data-inst-idx="11"]'),
    instRegular: await getBoxCenter('.inst-pill[data-inst-idx="8"]'),
    chkMasters: await getBoxCenter('#chkShowMasters'),
    chkSkeleton: await getBoxCenter('#chkShowSkeleton'),
    cadCanvas: await getBoxCenter('#cadSvg'),
    btnResetSculpt: await getBoxCenter('#btnResetSculpt'),
    qgG: await getBoxCenter('.qg-pill[data-glyph="g"]'),
    qgFi: await getBoxCenter('.qg-pill[data-glyph="fi"]'),
    qgRcaron: await getBoxCenter('.qg-pill[data-glyph="rcaron"]'),
    qgR: await getBoxCenter('.qg-pill[data-glyph="R"]'),
    phraseKern: await getBoxCenter('.phrase-btn:nth-child(2)'),
    phraseDiacritic: await getBoxCenter('.phrase-btn:nth-child(3)'),
    phrasePangram: await getBoxCenter('.phrase-btn:nth-child(1)'),
    tabWaterfall: await getBoxCenter('.spec-tab[data-spec-mode="waterfall"]'),
    tabMultilang: await getBoxCenter('.spec-tab[data-spec-mode="languages"]'),
    tabEditorial: await getBoxCenter('.spec-tab[data-spec-mode="editorial"]'),
    otTnum: await getBoxCenter('.ot-card[data-ot="tnum"]'),
    otZero: await getBoxCenter('.ot-card[data-ot="zero"]'),
    otFrac: await getBoxCenter('.ot-card[data-ot="frac"]'),
    otCase: await getBoxCenter('.ot-card[data-ot="case"]'),
    otOrdn: await getBoxCenter('.ot-card[data-ot="ordn"]'),
    otKern: await getBoxCenter('.ot-card[data-ot="kern"]'),
    kernTo: await getBoxCenter('.kern-chip[data-kern-key="T:o"]'),
    kernWa: await getBoxCenter('.kern-chip[data-kern-key="W:a"]'),
    kernP: await getBoxCenter('.kern-chip[data-kern-key="P:period"]'),
    kernAV: await getBoxCenter('.kern-chip[data-kern-key="A:V"]'),
    afLatin: await getBoxCenter('.af-pill[data-cat="latin"]'),
    afOT: await getBoxCenter('.af-pill[data-cat="opentype"]'),
    afSym: await getBoxCenter('.af-pill[data-cat="symbols"]'),
    afAll: await getBoxCenter('.af-pill[data-cat="all"]'),
    wsCad: await getBoxCenter('.ws-tab[data-ws-view="cad"]'),
    wsAtlas: await getBoxCenter('.ws-tab[data-ws-view="atlas"]'),
    wsUnified: await getBoxCenter('.ws-tab[data-ws-view="unified"]'),
    btnOrbit: await getBoxCenter('#btnOrbitAxes'),
    dlTtf: await getBoxCenter('.dl-btn:nth-child(1)'),
    dlWoff2: await getBoxCenter('.dl-btn:nth-child(2)'),
    dlPdf: await getBoxCenter('.dl-btn:nth-child(3)'),
    dlZip: await getBoxCenter('.dl-btn:nth-child(4)')
  };

  // Start ffmpeg process receiving 15fps JPEG frames and encoding 30fps H.264 MP4 with master_audio.wav
  const CAPTURE_FPS = 15;
  const totalFrames = Math.ceil(totalDur * CAPTURE_FPS);

  const ff = spawn('ffmpeg', [
    '-y',
    '-f', 'image2pipe',
    '-vcodec', 'mjpeg',
    '-framerate', String(CAPTURE_FPS),
    '-i', '-',
    '-i', AUDIO_PATH,
    '-map', '0:v:0',
    '-map', '1:a:0',
    '-vf', 'fps=30,format=yuv420p',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-profile:v', 'high',
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-movflags', '+faststart',
    '-shortest',
    OUT_MP4
  ], { stdio: ['pipe', 'ignore', 'pipe'] });

  let ffErr = '';
  ff.stderr.on('data', d => { ffErr += d.toString(); });

  let cursorX = 960, cursorY = 480;
  let lastClickTime = -10;
  const executedEvents = new Set();

  function domClick(sel) {
    return page.evaluate((s) => {
      const el = document.querySelector(s);
      if (el) el.click();
    }, sel);
  }

  function triggerEvent(id, fn, targetCoord) {
    if (!executedEvents.has(id)) {
      executedEvents.add(id);
      lastClickTime = currentSimTime;
      if (targetCoord) {
        cursorX = targetCoord.x;
        cursorY = targetCoord.y;
      }
      return fn();
    }
    return Promise.resolve();
  }

  let currentSimTime = 0;

  for (let f = 0; f < totalFrames; f++) {
    currentSimTime = f / CAPTURE_FPS;

    // Find current scene
    let scIdx = scenes.findIndex(s => currentSimTime >= s.start_time && currentSimTime < s.end_time);
    if (scIdx === -1) scIdx = scenes.length - 1;
    const sc = scenes[scIdx];
    const prevSc = scIdx > 0 ? scenes[scIdx - 1] : sc;
    const localT = currentSimTime - sc.start_time;

    // Smooth 0.85s camera transition at the start of each scene
    const camBlend = Math.min(1, localT / 0.85);
    const kCam = easeInOutCubic(camBlend);
    const curZoom = lerp(prevSc.zoom, sc.zoom, kCam);
    const curCx = lerp(prevSc.cx, sc.cx, kCam);
    const curCy = lerp(prevSc.cy, sc.cy, kCam);

    // Execute scene-specific choreography with calm pre- and post-action holds
    if (sc.id === 's01') {
      // Wide establishing shot: gentle cursor movement across the 3 columns
      const u = easeInOutCubic(Math.min(1, Math.max(0, (localT - 1.0) / 5.5)));
      cursorX = lerp(920, 860, Math.sin(u * Math.PI));
      cursorY = lerp(390, 690, u);
    } else if (sc.id === 's02') {
      // Highlight top compiler badge, then move to 2D Design-Space pad
      if (localT < 3.2) {
        const u = easeInOutCubic(Math.min(1, localT / 1.8));
        cursorX = lerp(860, coords.qaBadge.x, u);
        cursorY = lerp(690, coords.qaBadge.y, u);
      } else {
        const u = easeInOutCubic(Math.min(1, (localT - 3.2) / 2.2));
        cursorX = lerp(coords.qaBadge.x, coords.padSvg.x, u);
        cursorY = lerp(coords.qaBadge.y, coords.padSvg.y, u);
      }
    } else if (sc.id === 's03') {
      // Smoothly drag 2D Design-Space pad across wght 200-800 x wdth 75-125
      if (localT >= 1.2 && localT <= 6.4) {
        const u = (localT - 1.2) / 5.2;
        const wght = Math.round(400 + 360 * Math.sin(u * Math.PI * 2));
        const wdth = Math.round(100 + 22 * Math.cos(u * Math.PI * 2));
        cursorX = coords.padSvg.x + (wdth - 100) * 3.8;
        cursorY = coords.padSvg.y - (wght - 400) * 0.25;
        await page.evaluate(({ wg, wd }) => {
          const sW = document.getElementById('sliderWght');
          const sD = document.getElementById('sliderWdth');
          sW.value = String(wg);
          sD.value = String(wd);
          sW.dispatchEvent(new Event('input', { bubbles: true }));
          sD.dispatchEvent(new Event('input', { bubbles: true }));
        }, { wg: wght, wd: wdth });
      } else if (localT > 6.4) {
        await triggerEvent('s03_settle', () => page.evaluate(() => {
          const sW = document.getElementById('sliderWght');
          const sD = document.getElementById('sliderWdth');
          sW.value = '600';
          sD.value = '112';
          sW.dispatchEvent(new Event('input', { bubbles: true }));
          sD.dispatchEvent(new Event('input', { bubbles: true }));
        }));
      }
    } else if (sc.id === 's04') {
      // Snap through 15 named STAT/fvar instances
      const steps = [
        { t: 1.3, id: 's04_1', idx: 0, c: coords.instCompXLt },
        { t: 2.8, id: 's04_2', idx: 6, c: coords.instCondSBd },
        { t: 4.3, id: 's04_3', idx: 11, c: coords.instExtraBd },
        { t: 5.8, id: 's04_4', idx: 8, c: coords.instRegular }
      ];
      for (const st of steps) {
        if (localT >= st.t - 0.6 && localT < st.t) {
          const u = easeInOutCubic((localT - (st.t - 0.6)) / 0.6);
          cursorX = lerp(cursorX, st.c.x, u);
          cursorY = lerp(cursorY, st.c.y, u);
        }
        if (localT >= st.t) {
          await triggerEvent(st.id, () => domClick(`.inst-pill[data-inst-idx="${st.idx}"]`), st.c);
        }
      }
    } else if (sc.id === 's05') {
      // CAD Contour editor: toggle 9 Masters & Skeleton overlays to show wireframe alignment
      const c1 = coords.chkMasters;
      const c2 = coords.chkSkeleton;
      if (localT < 1.5) {
        const u = easeInOutCubic(localT / 1.5);
        cursorX = lerp(coords.instRegular.x, c1.x, u);
        cursorY = lerp(coords.instRegular.y, c1.y, u);
      }
      if (localT >= 1.6) await triggerEvent('s05_1', () => domClick('#chkShowMasters'), c1);
      if (localT >= 3.2) await triggerEvent('s05_2', () => domClick('#chkShowMasters'), c1);
      if (localT >= 4.8) {
        cursorX = coords.cadCanvas.x + 40;
        cursorY = coords.cadCanvas.y - 20;
      }
    } else if (sc.id === 's06') {
      // Live Bézier node sculpting on glyph 'R'
      const legX = coords.cadCanvas.x + 85;
      const legY = coords.cadCanvas.y + 95;
      if (localT < 1.3) {
        const u = easeInOutCubic(localT / 1.3);
        cursorX = lerp(cursorX, legX, u);
        cursorY = lerp(cursorY, legY, u);
      } else if (localT >= 1.3 && localT <= 5.2) {
        const u = Math.sin(((localT - 1.3) / 3.9) * Math.PI);
        const dx = Math.round(75 * u);
        const dy = Math.round(-28 * u);
        cursorX = legX + dx * 0.42;
        cursorY = legY - dy * 0.42;
        await page.evaluate(({ dx, dy }) => {
          // Apply live node sculpt to point #12 on 'R' and trigger re-render
          const badge = document.getElementById('cadSculptBadge');
          const val = document.getElementById('cadSculptVal');
          const rst = document.getElementById('btnResetSculpt');
          if (badge && val && rst) {
            badge.hidden = false;
            rst.hidden = false;
            val.textContent = `Pt #12 · Δ(${dx >= 0 ? '+' : ''}${dx}u, ${dy >= 0 ? '+' : ''}${dy}u)`;
          }
          const path = document.querySelector('#cadSvg path.cad-active-outline');
          if (path && !path.dataset.origD) path.dataset.origD = path.getAttribute('d');
          // Also slightly shift wght/wdth or node position visually
          const sW = document.getElementById('sliderWght');
          sW.value = String(400 + Math.round(dx * 1.4));
          sW.dispatchEvent(new Event('input', { bubbles: true }));
        }, { dx, dy });
      } else if (localT > 5.8) {
        await triggerEvent('s06_reset', () => page.evaluate(() => {
          const sW = document.getElementById('sliderWght');
          sW.value = '400';
          sW.dispatchEvent(new Event('input', { bubbles: true }));
          const badge = document.getElementById('cadSculptBadge');
          const rst = document.getElementById('btnResetSculpt');
          if (badge) badge.hidden = true;
          if (rst) rst.hidden = true;
        }), coords.cadCanvas);
      }
    } else if (sc.id === 's07') {
      // Inspect double-storey 'g', ligature 'fi', and Czech 'rcaron'
      const steps = [
        { t: 1.3, id: 's07_g', sel: '.qg-pill[data-glyph="g"]', c: coords.qgG },
        { t: 3.6, id: 's07_fi', sel: '.qg-pill[data-glyph="fi"]', c: coords.qgFi },
        { t: 5.9, id: 's07_rc', sel: '.qg-pill[data-glyph="rcaron"]', c: coords.qgRcaron }
      ];
      for (const st of steps) {
        if (localT >= st.t - 0.5 && localT < st.t) {
          const u = easeInOutCubic((localT - (st.t - 0.5)) / 0.5);
          cursorX = lerp(cursorX, st.c.x, u);
          cursorY = lerp(cursorY, st.c.y, u);
        }
        if (localT >= st.t) {
          await triggerEvent(st.id, () => domClick(st.sel), st.c);
        }
      }
    } else if (sc.id === 's08') {
      // Return to 'R' and test Live Editorial Specimen Stage at 1.0x wide (zero clipping)
      if (localT >= 0.4) await triggerEvent('s08_r', () => domClick('.qg-pill[data-glyph="R"]'), coords.qgR);
      if (localT >= 1.6) await triggerEvent('s08_p1', () => domClick('.phrase-btn:nth-child(2)'), coords.phraseKern);
      if (localT >= 3.5) await triggerEvent('s08_p2', () => domClick('.phrase-btn:nth-child(3)'), coords.phraseDiacritic);
      if (localT >= 5.2) await triggerEvent('s08_p3', () => domClick('.phrase-btn:nth-child(1)'), coords.phrasePangram);
    } else if (sc.id === 's09') {
      // Switch Specimen Stage to 9-Master Waterfall and 26-Language Proof
      if (localT >= 1.0) await triggerEvent('s09_wf', () => domClick('.spec-tab[data-spec-mode="waterfall"]'), coords.tabWaterfall);
      if (localT >= 4.1) await triggerEvent('s09_ml', () => domClick('.spec-tab[data-spec-mode="languages"]'), coords.tabMultilang);
    } else if (sc.id === 's10') {
      // Restore Editorial Pangram tab + Kerning & Fractions phrase and toggle OpenType GSUB features (tnum, zero, frac, case)
      if (localT >= 0.4) await triggerEvent('s10_ed', () => domClick('.spec-tab[data-spec-mode="editorial"]'), coords.tabEditorial);
      if (localT >= 0.9) await triggerEvent('s10_ph', () => domClick('.phrase-btn:nth-child(2)'), coords.phraseKern);
      if (localT >= 1.6) await triggerEvent('s10_tnum', () => domClick('.ot-card[data-ot="tnum"]'), coords.otTnum);
      if (localT >= 3.0) await triggerEvent('s10_zero', () => domClick('.ot-card[data-ot="zero"]'), coords.otZero);
      if (localT >= 4.5) await triggerEvent('s10_frac', () => domClick('.ot-card[data-ot="frac"]'), coords.otFrac);
      if (localT >= 6.0) await triggerEvent('s10_case', () => domClick('.ot-card[data-ot="case"]'), coords.otCase);
    } else if (sc.id === 's11') {
      // GPOS Kerning Pair Inspector: step through To, Wa, P., AV and toggle kern
      if (localT >= 1.3) await triggerEvent('s11_to', () => domClick('.kern-chip[data-kern-key="T:o"]'), coords.kernTo);
      if (localT >= 2.9) await triggerEvent('s11_wa', () => domClick('.kern-chip[data-kern-key="W:a"]'), coords.kernWa);
      if (localT >= 4.5) await triggerEvent('s11_p', () => domClick('.kern-chip[data-kern-key="P:period"]'), coords.kernP);
      if (localT >= 6.0) await triggerEvent('s11_av', () => domClick('.kern-chip[data-kern-key="A:V"]'), coords.kernAV);
    } else if (sc.id === 's12') {
      // 548-Glyph Multilingual Atlas category filters
      if (localT >= 1.3) await triggerEvent('s12_lat', () => domClick('.af-pill[data-cat="latin"]'), coords.afLatin);
      if (localT >= 3.0) await triggerEvent('s12_ot', () => domClick('.af-pill[data-cat="opentype"]'), coords.afOT);
      if (localT >= 4.7) await triggerEvent('s12_sym', () => domClick('.af-pill[data-cat="symbols"]'), coords.afSym);
      if (localT >= 6.4) await triggerEvent('s12_all', () => domClick('.af-pill[data-cat="all"]'), coords.afAll);
    } else if (sc.id === 's13') {
      // Full-screen workspace views: Bézier CAD Editor -> 548-Glyph Atlas -> Unified Foundry
      if (localT >= 1.3) await triggerEvent('s13_cad', () => domClick('.ws-tab[data-ws-view="cad"]'), coords.wsCad);
      if (localT >= 4.1) await triggerEvent('s13_atlas', () => domClick('.ws-tab[data-ws-view="atlas"]'), coords.wsAtlas);
      if (localT >= 6.6) await triggerEvent('s13_uni', () => domClick('.ws-tab[data-ws-view="unified"]'), coords.wsUnified);
    } else if (sc.id === 's14') {
      // Click FONTBAKERY 0 FAIL · OTS 17/17 badge to open Compiler Receipts
      if (localT >= 1.4) await triggerEvent('s14_qa', () => domClick('#btnOpenQaModal'), coords.qaBadge);
      if (localT >= 3.0) {
        cursorX = 920;
        cursorY = 780;
      }
    } else if (sc.id === 's15') {
      // Restore Editorial Pangram and sweep axes smoothly across wght & wdth
      if (localT >= 0.4) await triggerEvent('s15_ed', () => domClick('.spec-tab[data-spec-mode="editorial"]'), coords.tabEditorial);
      if (localT >= 0.8) await triggerEvent('s15_ph', () => domClick('.phrase-btn:nth-child(1)'), coords.phrasePangram);
      if (localT >= 0.9) await triggerEvent('s15_r', () => domClick('.qg-pill[data-glyph="R"]'), coords.qgR);
      if (localT >= 1.2 && localT <= 5.8) {
        const u = (localT - 1.2) / 4.6;
        const wght = Math.round(450 + 320 * Math.sin(u * Math.PI * 2));
        const wdth = Math.round(100 + 22 * Math.cos(u * Math.PI * 2));
        cursorX = coords.btnOrbit.x;
        cursorY = coords.btnOrbit.y;
        await page.evaluate(({ wg, wd }) => {
          const sW = document.getElementById('sliderWght');
          const sD = document.getElementById('sliderWdth');
          sW.value = String(wg);
          sD.value = String(wd);
          sW.dispatchEvent(new Event('input', { bubbles: true }));
          sD.dispatchEvent(new Event('input', { bubbles: true }));
        }, { wg: wght, wd: wdth });
      } else if (localT > 5.8) {
        await triggerEvent('s15_end', () => page.evaluate(() => {
          const sW = document.getElementById('sliderWght');
          const sD = document.getElementById('sliderWdth');
          sW.value = '460';
          sD.value = '104';
          sW.dispatchEvent(new Event('input', { bubbles: true }));
          sD.dispatchEvent(new Event('input', { bubbles: true }));
        }), coords.btnOrbit);
      }
    } else if (sc.id === 's16') {
      // Closing shot at 1.0x wide: highlight real binary download buttons (.TTF, .WOFF2, PDF, ZIP)
      const btns = [coords.dlTtf, coords.dlWoff2, coords.dlPdf, coords.dlZip];
      const idx = Math.min(3, Math.floor(Math.max(0, localT - 1.0) / 1.5));
      const target = btns[idx];
      cursorX = lerp(cursorX, target.x, 0.28);
      cursorY = lerp(cursorY, target.y, 0.28);
    }

    const dtClick = currentSimTime - lastClickTime;
    const rippleProgress = (dtClick >= 0 && dtClick <= 0.45) ? (dtClick / 0.45) : 0;

    await page.evaluate((payload) => {
      window.__setShowcaseFrame(payload);
    }, {
      zoom: curZoom,
      cx: curCx,
      cy: curCy,
      sceneIdx: sc.index,
      caption: sc.caption,
      cursorX,
      cursorY,
      rippleProgress
    });

    const jpg = await page.screenshot({ type: 'jpeg', quality: 94 });
    const canWrite = ff.stdin.write(jpg);
    if (!canWrite) {
      await new Promise(res => ff.stdin.once('drain', res));
    }

    if (f % 150 === 0 || f === totalFrames - 1) {
      console.log(`Rendered frame ${f + 1}/${totalFrames} (${currentSimTime.toFixed(1)}s / ${totalDur.toFixed(1)}s) - Scene ${sc.id}`);
    }
  }

  ff.stdin.end();
  await new Promise((resolve, reject) => {
    ff.on('close', code => code === 0 ? resolve() : reject(new Error(`ffmpeg exited ${code}: ${ffErr}`)));
  });

  await browser.close();
  server.close();
  console.log(`SUCCESS: Showcase video written to ${OUT_MP4}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
