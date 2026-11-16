// Renders the light brand strips that replace the old text wordmark on the Lost in Forwarding creatives.
// Logo: the owner's brand/rockit-logo.png (cropped to its bounds only), on white, never on a dark panel.
// Usage: node render_strips.js  -> campaign_tools/strip_feed.png (1080x128), strip_story.png (1080x490)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">';
const GOLD_H = 'linear-gradient(90deg,#A88329 0%,#B18B2D 8%,#C09934 17%,#CFAC49 25%,#DEC163 33%,#EDD77E 42%,#F7E590 50%,#ECD57B 58%,#DEC161 67%,#D0AD48 75%,#C29B36 83%,#B28C2D 92%,#A88228 100%)';
const dir = __dirname;
const strips = {
  feed: { w: 1080, h: 128, logoH: 92, padX: 96, tag: 30, site: false },
  story: { w: 1080, h: 490, logoH: 150, padX: 80, tag: 40, site: true },
};
(async () => {
  const b = await chromium.launch();
  for (const [name, s] of Object.entries(strips)) {
    const top = name === 'feed' ? Math.round((s.h + 3 - s.logoH) / 2) : 44;
    const html = `<!doctype html><html><head><meta charset="utf-8">${FONTS}<style>*{margin:0;padding:0;box-sizing:border-box}
body{width:${s.w}px;height:${s.h}px;background:#ffffff;position:relative;overflow:hidden}</style></head><body>
<div style="position:absolute;left:0;right:0;top:0;height:3px;background:${GOLD_H}"></div>
<img src="_logo.png" style="position:absolute;left:${s.padX}px;top:${top}px;height:${s.logoH}px">
<div style="position:absolute;right:${s.padX}px;top:${top}px;height:${s.logoH}px;display:flex;align-items:center;font:italic 600 ${s.tag}px 'Cormorant Garamond',serif;color:#8a6514">Means what it says.</div>
${s.site ? `<div style="position:absolute;left:${s.padX}px;right:${s.padX}px;top:${top + s.logoH + 34}px;border-top:1px solid #e3d8bd;padding-top:18px;font:500 17px 'IBM Plex Mono',monospace;letter-spacing:.2em;text-transform:uppercase;color:#5d6577">rockit-transport.com</div>` : ''}
</body></html>`;
    const tmp = path.join(dir, `_strip_${name}.html`);
    fs.writeFileSync(tmp, html);
    const p = await b.newPage({ viewport: { width: s.w, height: s.h }, deviceScaleFactor: 1 });
    await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(dir, `strip_${name}.png`) });
    fs.unlinkSync(tmp);
  }
  await b.close();
  console.log('strips rendered');
})();
