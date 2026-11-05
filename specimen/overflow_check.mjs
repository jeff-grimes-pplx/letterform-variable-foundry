// Layout receipt for the specimen: loads specimen/index.html in headless Chromium at print media and
// reports every element whose rendered box leaves the page's 16 mm side margins / folio zone, or
// whose text is wider than its box (clipped by overflow:hidden or nowrap). Exit 1 if any.
// Usage: node specimen/overflow_check.mjs   (from the workspace root, like print.mjs)
import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.json': 'application/json' };
const server = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': types[path.extname(p)] || 'application/octet-stream' }); fs.createReadStream(p).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const port = server.address().port;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1000, height: 1400 } });
await page.emulateMedia({ media: 'print' });
await page.goto(`http://127.0.0.1:${port}/specimen/index.html`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
const report = await page.evaluate(() => {
  const mm = 96 / 25.4; const out = []; const pages = [...document.querySelectorAll('.page')];
  pages.forEach((pg, i) => {
    const pr = pg.getBoundingClientRect();
    const left = pr.left + 16 * mm - 0.5, right = pr.right - 16 * mm + 0.5, bottom = pr.bottom - 12 * mm; // text must end above the folio zone
    for (const el of pg.querySelectorAll('*')) {
      if (el.classList.contains('folio') || el.closest('.folio')) continue;
      if (el.tagName === 'svg' || el.closest('svg')) continue;
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (hasText) {
        if (r.right > right + 0.5) out.push({ page: i + 1, issue: 'right-overflow', by_mm: +((r.right - right) / mm).toFixed(2), text: el.textContent.trim().slice(0, 60) });
        if (r.left < left - 0.5) out.push({ page: i + 1, issue: 'left-overflow', by_mm: +((left - r.left) / mm).toFixed(2), text: el.textContent.trim().slice(0, 60) });
        if (r.bottom > bottom) out.push({ page: i + 1, issue: 'into-folio-zone', by_mm: +((r.bottom - bottom) / mm).toFixed(2), text: el.textContent.trim().slice(0, 60) });
        if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflow !== 'visible') out.push({ page: i + 1, issue: 'clipped-text', by_px: el.scrollWidth - el.clientWidth, text: el.textContent.trim().slice(0, 60) });
      }
    }
    // nowrap lines wider than the page content box (would be cut by the page's overflow:hidden)
    for (const el of pg.querySelectorAll('.wf, .sweep, .alpha-s, .punct.accents, .head-demo, .quote, .feat-s, .cover-line, .mx')) {
      const r = el.getBoundingClientRect();
      if (el.scrollWidth > el.clientWidth + 1) out.push({ page: i + 1, issue: 'nowrap-wider-than-box', by_px: el.scrollWidth - el.clientWidth, text: el.textContent.trim().slice(0, 60) });
      if (r.right > right + 0.5) out.push({ page: i + 1, issue: 'nowrap-right-overflow', by_mm: +((r.right - right) / mm).toFixed(2), text: el.textContent.trim().slice(0, 60) });
    }
  });
  return { pages: pages.length, issues: out };
});
await browser.close(); server.close();
console.log(`pages: ${report.pages}`);
console.log(`issues: ${report.issues.length}`);
for (const it of report.issues) console.log(JSON.stringify(it));
process.exit(report.issues.length ? 1 : 0);
