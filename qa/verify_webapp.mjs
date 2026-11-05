import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(here, '..', 'app');
const outDir = path.resolve(here, 'screenshots');
fs.mkdirSync(outDir, { recursive: true });

const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.ttf': 'font/ttf',
  '.woff2': 'font/woff2',
  '.pdf': 'application/pdf',
  '.zip': 'application/zip'
};

const server = http.createServer((req, res) => {
  const urlPath = decodeURIComponent(req.url.split('?')[0]);
  const rel = urlPath === '/' ? '/index.html' : urlPath;
  const p = path.join(appRoot, rel);
  if (!p.startsWith(appRoot) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) {
    res.writeHead(404);
    return res.end('Not found');
  }
  res.writeHead(200, { 'content-type': types[path.extname(p)] || 'application/octet-stream' });
  fs.createReadStream(p).pipe(res);
});

await new Promise(r => server.listen(0, '127.0.0.1', r));
const port = server.address().port;
const baseUrl = `http://127.0.0.1:${port}/`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });

const errors = [];
page.on('console', m => {
  if (m.type() === 'error') errors.push(`console.error: ${m.text()}`);
});
page.on('pageerror', e => errors.push(`pageerror: ${e.message}`));
page.on('requestfailed', r => errors.push(`requestfailed: ${r.url()}`));

await page.goto(baseUrl, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(350);

// 0. Capture 1280x800 validator viewport
await page.setViewportSize({ width: 1280, height: 800 });
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(outDir, '00-validator-1280x800.png') });

// 1. Capture Default Unified Workbench (1920x1080)
await page.setViewportSize({ width: 1920, height: 1080 });
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(outDir, '01-unified-default-1920x1080.png') });

// Check specimen text clipping
const clipCheck = await page.evaluate(() => {
  const el = document.getElementById('liveSpecimenText');
  const r = el.getBoundingClientRect();
  const parentR = el.parentElement.getBoundingClientRect();
  return {
    text: el.textContent.trim(),
    leftInside: r.left >= parentR.left - 1,
    rightInside: r.right <= parentR.right + 1,
    scrollWidth: el.scrollWidth,
    clientWidth: el.clientWidth
  };
});
console.log('Specimen clipping check:', clipCheck);

// 2. Test dragging Weight to 800 & Width to 125 (Extended ExtraBold) + selecting 'g'
await page.click('.qg-pill[data-glyph="g"]');
await page.fill('#sliderWght', '760');
await page.dispatchEvent('#sliderWght', 'input');
await page.fill('#sliderWdth', '120');
await page.dispatchEvent('#sliderWdth', 'input');
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(outDir, '02-unified-glyph-g-760-120.png') });

// 3. Test dragging an on-curve node in the CAD editor & toggling OpenType features
const nodeBox = await page.locator('#cadSvg .cad-node-on').first().boundingBox();
if (nodeBox) {
  await page.mouse.move(nodeBox.x + nodeBox.width / 2, nodeBox.y + nodeBox.height / 2);
  await page.mouse.down();
  await page.mouse.move(nodeBox.x + 28, nodeBox.y - 18, { steps: 6 });
  await page.mouse.up();
}
await page.click('.ot-card[data-ot="zero"]');
await page.click('.ot-card[data-ot="frac"]');
await page.click('.kern-chip[data-kern-key="T:o"]');
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(outDir, '03-node-drag-and-opentype.png') });

// 4. Test 26-Language HarfBuzz Proof mode & Waterfall mode
await page.click('.spec-tab[data-spec-mode="languages"]');
await page.waitForTimeout(150);
await page.screenshot({ path: path.join(outDir, '04-languages-26-proof.png') });

// 5. Test Full CAD Editor view mode
await page.click('.ws-tab[data-ws-view="cad"]');
await page.click('.qg-pill[data-glyph="fi"]');
await page.waitForTimeout(150);
await page.screenshot({ path: path.join(outDir, '05-cad-full-view.png') });

// 6. Test Mobile Responsive layout (375x812)
await page.click('.ws-tab[data-ws-view="unified"]');
await page.setViewportSize({ width: 375, height: 812 });
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(outDir, '06-mobile-375x812.png') });

await browser.close();
server.close();

if (errors.length) {
  console.error('ERRORS:', errors);
  process.exit(1);
}
console.log('ALL WEBAPP QA CHECKS PASSED (0 console/page/request errors).');
