// Print specimen/index.html to PDF with headless Chromium (Playwright). Serves the build folder over
// HTTP so @font-face can load ../fonts/*. Usage: node print.mjs [out.pdf]
import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const out = process.argv[2] || path.join(here, 'Apertide-Specimen.pdf');
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.json': 'application/json', '.js': 'text/javascript' };
const server = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': types[path.extname(p)] || 'application/octet-stream' }); fs.createReadStream(p).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const port = server.address().port;
const browser = await chromium.launch();
const page = await browser.newPage();
page.on('pageerror', e => console.error('pageerror', e.message));
page.on('requestfailed', r => console.error('requestfailed', r.url()));
await page.goto(`http://127.0.0.1:${port}/specimen/index.html`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
const loaded = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length);
console.log('fontfaces loaded:', loaded, 'of', await page.evaluate(() => document.fonts.size));
await page.emulateMedia({ media: 'print' });
await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
await browser.close(); server.close();
console.log('wrote', out);
