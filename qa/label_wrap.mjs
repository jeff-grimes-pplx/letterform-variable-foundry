// Label/tooltip/banner layout receipt for the Letterform app (v2 artifact pass, §4): at 1440×900,
// 1280×720 and 390×844, for every view, lists label-like elements (tabs, buttons, chips, labels,
// readouts, table cells, legends, meta/notes strips) whose single-line text wrapped onto a second
// line, whose text is clipped by its box (scrollWidth > clientWidth), or whose box leaves the viewport.
// Also records console/page errors per viewport. Exit 1 on any finding. Serves app/ itself unless a
// base URL is given.  Usage: cd /home/user/workspace && node <build>/qa/label_wrap.mjs [baseURL]
import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const appDir = path.resolve(here, '..', 'app');
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.json': 'application/json', '.js': 'text/javascript', '.zip': 'application/zip', '.svg': 'image/svg+xml' };
let base = process.argv[2]; let server;
if (!base) {
  server = http.createServer((req, res) => {
    const u = req.url.split('?')[0]; const p = path.join(appDir, decodeURIComponent(u === '/' ? '/index.html' : u));
    if (!p.startsWith(appDir) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': types[path.extname(p)] || 'application/octet-stream' }); fs.createReadStream(p).pipe(res);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r)); base = `http://127.0.0.1:${server.address().port}`;
}
const SEL = 'button, [role=tab], .chip, label, .lab, output, th, td, legend, summary, .readout, .app-name, .family, .draw-meta span, .grid-head span, .detail dt, .detail dd, .detail h2, .detail h3, .notes h2, .notes h3, .pill, .tag, .meta, .legend, .axis-label, .axis label, .instance, #ro-inst, #grid-count, .scale, .tick, .pad-label, option';
const browser = await chromium.launch();
const findings = []; const lines = [];
for (const [w, h] of [[1440, 900], [1280, 720], [390, 844]]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, isMobile: w < 500, hasTouch: w < 500 });
  const page = await ctx.newPage(); const errors = [];
  page.on('pageerror', e => errors.push('pageerror ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console ' + m.text()); });
  await page.goto(base + '/index.html', { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => !/Loading/.test(document.querySelector('#grid-count')?.textContent || 'Loading'), null, { timeout: 20000 });
  for (const view of ['tester', 'glyphs', 'drawing', 'notes']) {
    await page.click(`[data-view=${view}]`); await page.waitForTimeout(300);
    if (view === 'glyphs') { await page.click('#grid [role=listitem], #grid .cell, #grid > *'); await page.waitForTimeout(200); }
    const found = await page.evaluate((SEL) => {
      const out = []; const vw = window.innerWidth;
      for (const el of document.querySelectorAll(SEL)) {
        if (el.closest('[hidden]') || el.tagName === 'OPTION') continue;
        const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || el.classList.contains('vh')) continue;
        const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
        const text = (el.textContent || '').trim(); if (!text) continue;
        const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.3;
        // a label has wrapped when one of its text nodes occupies more than one line box (block
        // children that are meant to stack, like a grid cell's glyph + name, are separate text nodes)
        let multiLine = false;
        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        for (let n = walker.nextNode(); n; n = walker.nextNode()) {
          if (!n.textContent.trim()) continue;
          const range = document.createRange(); range.selectNodeContents(n);
          const rects = [...range.getClientRects()].filter(q => q.width > 0 && q.height > 0);
          const tops = [...new Set(rects.map(q => Math.round(q.top / (lh * 0.6))))];
          if (tops.length > 1 && !el.matches('p, li, dd, td.note')) { multiLine = true; break; }
        }
        const clipped = (cs.overflow !== 'visible' || cs.textOverflow === 'ellipsis') && el.scrollWidth > el.clientWidth + 1;
        const offscreen = r.right > vw + 0.5 || r.left < -0.5;
        if (multiLine || clipped || offscreen) out.push({ tag: el.tagName.toLowerCase(), id: el.id, cls: el.className && el.className.baseVal === undefined ? el.className : '', text: text.slice(0, 60), multiLine, clipped, offscreen, w: Math.round(r.width), h: Math.round(r.height), sw: el.scrollWidth, cw: el.clientWidth });
      }
      // placeholders are not text nodes: measure them with the input's own font
      for (const inp of document.querySelectorAll('input[placeholder]')) {
        if (inp.closest('[hidden]')) continue; const cs = getComputedStyle(inp); const r = inp.getBoundingClientRect(); if (r.width === 0) continue;
        const c = document.createElement('canvas').getContext('2d'); c.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
        const tw = c.measureText(inp.placeholder).width; const avail = inp.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
        if (tw > avail + 0.5) out.push({ tag: 'input', id: inp.id, cls: 'placeholder', text: inp.placeholder, multiLine: false, clipped: true, offscreen: false, w: Math.round(r.width), h: Math.round(r.height), sw: Math.round(tw), cw: Math.round(avail) });
        else out.__placeholders = (out.__placeholders || 0) + 1;
      }
      return out;
    }, SEL);
    for (const f of found) findings.push({ viewport: `${w}x${h}`, view, ...f });
    lines.push(`${w}x${h} ${view}: ${found.length} finding(s)`);
  }
  lines.push(`${w}x${h} errors: ${errors.length}${errors.length ? ' — ' + errors.join(' | ') : ''}`);
  if (errors.length) findings.push({ viewport: `${w}x${h}`, errors });
  await ctx.close();
}
await browser.close(); if (server) server.close();
const report = [`label/tooltip/banner wrap-clip receipt — ${base.includes('127.0.0.1') ? 'local app/' : base}`, ...lines, '', ...findings.map(f => JSON.stringify(f)), '', findings.length ? `RESULT: ${findings.length} finding(s)` : 'RESULT: 0 findings (no wrapped, clipped or off-screen label-like elements; 0 console/page errors)'].join('\n');
fs.writeFileSync(path.join(here, 'label-wrap.txt'), report + '\n'); console.log(report);
process.exit(findings.length ? 1 : 0);
