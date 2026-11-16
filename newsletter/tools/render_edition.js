// Render <issue>/edition/edition.html to a print PDF and per-page PNG previews.
//   node render_edition.js ../issues/<date>
// Fails (exit 2) if any page's content overflows its frame, so nothing is ever cut off silently.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const dir = path.resolve(process.argv[2], 'edition');
  const file = 'file://' + path.join(dir, 'edition.html');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await page.goto(file, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const inner = pg.querySelector('.inner');
      const r = { page: i + 1, overflow: 0 };
      if (inner) {
        const box = inner.getBoundingClientRect();
        let maxBottom = box.top;
        inner.querySelectorAll('*').forEach(el => { const b = el.getBoundingClientRect(); if (b.height > 0) maxBottom = Math.max(maxBottom, b.bottom); });
        r.overflow = Math.round(maxBottom - box.bottom);
        r.spare = Math.round(box.bottom - maxBottom);
        // multi-column overflow: content pushed into an extra column to the right
        inner.querySelectorAll('.cols2,.cols3').forEach(c => { if (c.scrollWidth > c.clientWidth + 2) r.colOverflow = (r.colOverflow || 0) + (c.scrollWidth - c.clientWidth); });
      }
      out.push(r);
    });
    const fontsOk = [['600','Cormorant Garamond'],['400','Inter'],['600','IBM Plex Mono']].map(([w,f]) => [f, document.fonts.check(`${w} 12px "${f}"`)]);
    return { pages: out, fontsOk };
  });
  console.log(JSON.stringify(report));
  await page.pdf({ path: path.join(dir, 'edition.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  const n = report.pages.length;
  for (let i = 0; i < n; i++) {
    const el = (await page.$$('.page'))[i];
    await el.screenshot({ path: path.join(dir, `page_${String(i + 1).padStart(2, '0')}.png`) });
  }
  await browser.close();
  const bad = report.pages.filter(p => p.overflow > 0 || p.colOverflow);
  if (bad.length) { console.error('OVERFLOW on pages: ' + bad.map(p => p.page).join(', ')); process.exit(2); }
})();
