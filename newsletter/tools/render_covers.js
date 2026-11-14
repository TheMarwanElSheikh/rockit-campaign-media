// Render an issue's cover HTML files (and an email preview) to PNG with the pre-installed Playwright Chromium.
// Usage: node render_covers.js ../issues/2026-11-16
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = path.resolve(process.argv[2]);
  const browser = await chromium.launch();
  const jobs = [
    ['cover_4x5.html', 'cover_4x5.jpg', 1080, 1350, false],
    ['cover_4x3.html', 'cover_4x3.jpg', 1200, 900, false],
    ['email.html', 'email_preview.png', 680, 900, true],
  ];
  for (const [src, out, w, h, full] of jobs) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.join(dir, src), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const opts = { path: path.join(dir, out), fullPage: full };
    if (out.endsWith('.jpg')) opts.quality = 92;
    await page.screenshot(opts);
    await page.close();
    console.log('rendered', out);
  }
  await browser.close();
})();
