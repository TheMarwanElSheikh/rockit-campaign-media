// Render an issue's visuals to images with the pre-installed Playwright Chromium.
// Usage: node render_covers.js ../issues/<date>
//   light visuals -> PNG at 2x (crisp in email and on the web); stamp -> transparent PNG
//   slides and covers -> JPEG at 1x (exact platform pixel sizes)
//   email.html -> email_preview.png (full page), for review only
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = path.resolve(process.argv[2]);
  const vis = path.join(dir, 'visuals');
  const browser = await chromium.launch();
  const dims = {};
  const shot = async (src, out, opts) => {
    const page = await browser.newPage({ viewport: { width: opts.w, height: opts.h || 60 }, deviceScaleFactor: opts.dsf || 1 });
    await page.goto('file://' + src, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const o = { path: out, fullPage: !opts.h, omitBackground: !!opts.transparent };
    if (out.endsWith('.jpg')) o.quality = 92;
    await page.screenshot(o);
    if (!opts.h) {
      const hgt = await page.evaluate(() => document.body.scrollHeight);
      dims[path.basename(out, path.extname(out))] = [opts.w * (opts.dsf || 1), hgt * (opts.dsf || 1)];
    }
    await page.close();
    console.log('rendered', path.basename(out));
  };
  for (const n of ['chart_gap', 'chart_rebate', 'route_md1']) await shot(path.join(vis, n + '.html'), path.join(vis, n + '.png'), { w: 600, dsf: 2 });
  await shot(path.join(vis, 'masthead.html'), path.join(vis, 'masthead.png'), { w: 528, dsf: 2 });
  await shot(path.join(vis, 'acid_steps.html'), path.join(vis, 'acid_steps.png'), { w: 528, dsf: 2 });
  await shot(path.join(vis, 'stamp.html'), path.join(vis, 'stamp.png'), { w: 150, h: 150, dsf: 2, transparent: true });
  await shot(path.join(vis, 'cover_4x3.html'), path.join(vis, 'cover_4x3.jpg'), { w: 1200, h: 900 });
  for (let i = 1; i <= 5; i++) await shot(path.join(vis, `slide_${i}.html`), path.join(vis, `slide_${i}.jpg`), { w: 1080, h: 1350 });
  fs.writeFileSync(path.join(vis, 'dims.json'), JSON.stringify(dims, null, 1));
  // email preview with local images
  const html = fs.readFileSync(path.join(dir, 'email.html'), 'utf8').replace(/https:\/\/cdn\.jsdelivr\.net\/[^"]*?\/visuals\//g, 'file://' + vis + '/').replace(/IMG_BASE\//g, 'file://' + vis + '/');
  fs.writeFileSync(path.join(dir, '.email_local.html'), html);
  await shot(path.join(dir, '.email_local.html'), path.join(dir, 'email_preview.png'), { w: 680 });
  fs.unlinkSync(path.join(dir, '.email_local.html'));
  await browser.close();
})();
