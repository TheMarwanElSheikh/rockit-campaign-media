// Web and social assets for a full edition.
//   node render_edition_web.js ../issues/<date>
// Writes into <issue>/edition/web/:
//   chart_NN.png      every .chart block in edition.html, on paper, 2x (website post images)
//   timeline.png      the key-dates timeline (first inline SVG with the "tlg" gradient), 2x
//   cover_full_4x3.jpg 1200x900 landscape cover (website cover, Google Business)
//   slide_NN.jpg      1080x1350 (4:5) carousel slides, one per selected page (Instagram, LinkedIn, Facebook)
// Brand: only the owner's logo (logo.svg = brand/rockit-logo.svg, vector, on light surfaces) and the logo-SVG gold gradient.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const GOLD = 'linear-gradient(135deg,#A88329 0%,#B18B2D 8%,#C09934 17%,#CFAC49 25%,#DEC163 33%,#EDD77E 42%,#F7E590 50%,#ECD57B 58%,#DEC161 67%,#D0AD48 75%,#C29B36 83%,#B28C2D 92%,#A88228 100%)';
const GOLD_H = GOLD.replace('135deg', '90deg');
const FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">';

(async () => {
  const issue = path.resolve(process.argv[2]);
  const ed = JSON.parse(fs.readFileSync(path.join(issue, 'edition.json'), 'utf8'));
  const dir = path.join(issue, 'edition');
  const out = path.join(dir, 'web');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();

  // 1) charts + timeline straight from the print document
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(dir, 'edition.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.addStyleTag({ content: '.chart{background:#faf7ef;padding:10px 12px 8px}' });
  const charts = await page.$$('.chart');
  const dims = {};
  for (let i = 0; i < charts.length; i++) {
    const name = `chart_${String(i + 1).padStart(2, '0')}`;
    const box = await charts[i].boundingBox();
    await charts[i].screenshot({ path: path.join(out, name + '.png') });
    dims[name] = [Math.round(box.width * 2), Math.round(box.height * 2)];
  }
  const tl = await page.$('svg:has(#tlg)');
  if (tl) {
    await page.evaluate(el => { el.parentElement.style.background = '#faf7ef'; el.style.background = '#faf7ef'; }, tl);
    const box = await tl.boundingBox();
    await tl.screenshot({ path: path.join(out, 'timeline.png') });
    dims.timeline = [Math.round(box.width * 2), Math.round(box.height * 2)];
  }

  // 2) landscape cover 1200x900
  const c = ed.cover, m = ed.meta;
  const logo = '../logo.svg';   // owner's vector logo, full colour, on a light surface (owner's rule: no dark panel behind it)
  const coverHtml = `<!doctype html><html><head><meta charset="utf-8">${FONTS}<style>*{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:900px;background:#ffffff;font-family:Inter,Arial,sans-serif;color:#1b2333;position:relative;overflow:hidden}
  .k{font:600 15px 'IBM Plex Mono',monospace;letter-spacing:.24em;text-transform:uppercase;color:#8a6514}</style></head><body>
  <div style="position:absolute;left:0;right:0;top:0;height:12px;background:${GOLD_H}"></div>
  <div style="position:absolute;left:72px;right:72px;top:58px;display:flex;justify-content:space-between;align-items:center">
    <img src="${logo}" style="height:150px">
    <div class="k" style="text-align:right;line-height:1.8;color:#5d6577">Voyage ${m.voyage}<br>${m.date_long}<br>${m.pages_label}</div></div>
  <div style="position:absolute;left:72px;right:72px;top:262px">
    <div style="height:3px;background:${GOLD_H};margin-bottom:20px"></div>
    <div class="k">The weekly freight &amp; trade review from Cairo</div>
    <div style="font:600 96px/1 'Cormorant Garamond',serif;margin-top:10px;padding-bottom:6px;color:#16243f">The Rockit Manifest</div>
    <div style="height:3px;background:${GOLD_H};margin-top:16px"></div>
    <div style="font:600 48px/1.08 'Cormorant Garamond',serif;margin-top:36px;max-width:1000px;color:#1b2333">${c.headline}</div>
    <div style="font:italic 500 25px/1.35 'Cormorant Garamond',serif;color:#3a4152;margin-top:16px;max-width:980px">Full edition: ocean and air freight, the logistics business, world politics and the Egypt desk. Every figure sourced.</div>
  </div>
  <div class="k" style="position:absolute;left:72px;bottom:44px;color:#5d6577">rockit-transport.com</div>
  <div style="position:absolute;right:72px;bottom:38px;font:italic 600 28px 'Cormorant Garamond',serif;color:#8a6514">Means what it says.</div>
  </body></html>`;
  const cp = await browser.newPage({ viewport: { width: 1200, height: 900 }, deviceScaleFactor: 1 });
  const tmpCover = path.join(out, '_cover.html');
  fs.writeFileSync(tmpCover, coverHtml);
  await cp.goto('file://' + tmpCover, { waitUntil: 'networkidle' });
  await cp.evaluate(() => document.fonts.ready);
  await cp.screenshot({ path: path.join(out, 'cover_full_4x3.jpg'), type: 'jpeg', quality: 92 });

  // 3) carousel slides 1080x1350 from selected page renders
  const pages = (ed.web && ed.web.carousel_pages) || [1, 2, 3, 4, 6, 8, 10, 12];
  const sp = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (let i = 0; i < pages.length; i++) {
    const n = String(pages[i]).padStart(2, '0');
    const img = `../page_${n}.png`;
    const html = `<!doctype html><html><head><meta charset="utf-8">${FONTS}<style>*{margin:0;padding:0;box-sizing:border-box}
    body{width:1080px;height:1350px;background:#efe9da;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}</style></head><body>
    <img src="${img}" style="height:1290px;box-shadow:0 6px 28px rgba(22,36,63,.18)">
    <div style="position:absolute;right:26px;bottom:14px;font:600 15px 'IBM Plex Mono',monospace;letter-spacing:.14em;color:#8a6514">${i + 1}/${pages.length}</div>
    </body></html>`;
    const tmp = path.join(out, '_slide.html');
    fs.writeFileSync(tmp, html);
    await sp.goto('file://' + tmp, { waitUntil: 'networkidle' });
    await sp.screenshot({ path: path.join(out, `slide_${String(i + 1).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 90 });
  }
  for (const f of ['_cover.html', '_slide.html']) { try { fs.unlinkSync(path.join(out, f)); } catch (e) {} }
  fs.writeFileSync(path.join(out, 'dims.json'), JSON.stringify(dims, null, 1));
  console.log('charts', charts.length, 'timeline', !!tl, 'slides', pages.length);
  await browser.close();
})();
