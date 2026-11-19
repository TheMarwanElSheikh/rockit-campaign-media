#!/usr/bin/env node
/**
 * The tools of rockit-transport.com on a phone held upright, measured in a real browser.
 *
 *   node website/tools/test/portrait.test.cjs            # dist/ (the fixed tools): must report 0 findings
 *   DIR=src node website/tools/test/portrait.test.cjs    # the tools as the site served them on 19 Nov 2026: 43 of 56
 *
 * Each tool is opened in a frame of the width the site gives it (240px on a 320px phone, 310px on a 390px one, and
 * 280 and 350 between and beyond), untouched and then used (fields filled, a package added, the action pressed). A
 * state has a finding when anything in the tool lies outside the frame, when a box hides content wider than itself,
 * when a field's text is under 16px (iOS zooms the page on focus) or when the current tool's tab is out of sight.
 * WIDTHS=600,980 measures the desk sizes; SHOTS=1 writes screenshots to test/shots/.
 *
 * Needs Playwright with a Chromium (`npm i -D playwright`, or the one already on the machine).
 */
const { chromium } = require('playwright'); const http = require('node:http'); const fs = require('node:fs'); const path = require('node:path');
const ROOT = path.resolve(__dirname, '..');
const DIR = process.env.DIR ?? 'dist'; const WIDTHS = (process.env.WIDTHS ?? '240,280,310,350').split(',').map(Number);
const TOOLS = (process.env.TOOLS ?? 'chargeable-weight,load-calculator,duties-taxes-calculator,vessel-schedules,vessel-tracking,flight-tracking,container-tracking').split(',');
const SHOTS = process.env.SHOTS === '1';
const server = http.createServer((req, res) => { const u = new URL(req.url, 'http://x'); const file = path.join(ROOT, path.normalize(u.pathname).replace(/^\/+/, '')); if (!file.startsWith(ROOT + path.sep) || !fs.existsSync(file)) { res.writeHead(404); return res.end(); } res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); res.end(fs.readFileSync(file)); });
function probe() {
  const d = document.documentElement; const vw = d.clientWidth; const out = [];
  const vis = (e) => { for (let x = e; x; x = x.parentElement) { const s = getComputedStyle(x); if (s.display === 'none' || s.visibility === 'hidden') return false; } return true; };
  for (const e of document.querySelectorAll('body *')) {
    if (e.closest('.rm-tabs') && e.tagName === 'A') continue; // a strip that scrolls by design
    const r = e.getBoundingClientRect(); if (r.width < 2 || r.height < 2 || !vis(e)) continue; if (r.left < -1000) continue;
    const s = getComputedStyle(e);
    const cut = (r.right > vw + 1 || r.left < -1);
    const inner = !['INPUT', 'SELECT', 'TEXTAREA'].includes(e.tagName) && (s.overflowX === 'hidden' || s.overflowX === 'clip') && e.scrollWidth > e.clientWidth + 1 && s.textOverflow !== 'ellipsis';
    const sideways = (s.overflowX === 'auto' || s.overflowX === 'scroll') && e.scrollWidth > e.clientWidth + 1 && !e.classList.contains('rm-tabs');
    if (cut || inner || sideways) out.push(`${cut ? 'CUT' : inner ? 'CLIPS' : 'SCROLLS'} ${e.tagName.toLowerCase()}${e.id ? '#' + e.id : ''}.${String(e.className).replace(/\s+/g, '.').slice(0, 28)} [${Math.round(r.left)}..${Math.round(r.right)}]${inner || sideways ? ' content ' + e.scrollWidth + '/' + e.clientWidth : ''} "${(e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 26)}"`);
  }
  const small = [...document.querySelectorAll('input,select,textarea')].filter((e) => e.getClientRects().length && !['radio', 'checkbox'].includes(e.type) && parseFloat(getComputedStyle(e).fontSize) < 16).length;
  const on = document.querySelector('.rm-tabs a.on'); const tabs = document.querySelector('.rm-tabs');
  let tab = 'n/a'; if (on && tabs) { const a = on.getBoundingClientRect(), t = tabs.getBoundingClientRect(); tab = a.left >= t.left - 1 && a.right <= t.right + 1 ? 'visible' : `HIDDEN [${Math.round(a.left)}..${Math.round(a.right)}] of ${Math.round(t.width)}`; }
  const pad = (() => { const b = document.querySelector('.rm-body') || document.body; let min = 1e9, max = -1e9; for (const e of b.querySelectorAll('input,select,button,table,h3,p,.big,.tot,.line')) { const r = e.getBoundingClientRect(); if (r.width < 2 || !vis(e)) continue; min = Math.min(min, r.left); max = Math.max(max, r.right); } return `${Math.round(min)}..${Math.round(max)} of ${vw}`; })();
  return { out: [...new Set(out)].slice(0, 14), n: out.length, small, tab, pad, h: d.scrollHeight };
}
(async () => {
  await new Promise((r) => server.listen(8765, r));
  const b = await chromium.launch(); let bad = 0, total = 0;
  for (const w of WIDTHS) {
    const c = await b.newContext({ viewport: { width: w + 40, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
    const p = await c.newPage();
    for (const tool of TOOLS) {
      for (const state of ['start', 'used']) {
        await p.goto(`http://localhost:8765/test/harness.html?w=${w}&src=/${DIR}/${tool}.html`);
        await p.waitForTimeout(1200);
        const frame = p.frames().find((f) => f !== p.mainFrame() && f.url().includes(`/${DIR}/${tool}.html`));
        if (state === 'used') {
          await frame.evaluate(() => {
            for (const i of document.querySelectorAll('input[type=text],input[type=search],input:not([type])')) { if (!i.value && i.offsetParent) { i.value = (i.placeholder || '').replace(/^e\.g\.\s*/i, '') || 'MSKU3881107'; i.dispatchEvent(new Event('input', { bubbles: true })); } }
            for (const btn of document.querySelectorAll('button.b.ghost')) { if (btn.offsetParent && /add/i.test(btn.textContent)) btn.click(); }
            for (const btn of document.querySelectorAll('button.b.gold, button[type=submit]')) { if (btn.offsetParent) btn.click(); }
          }).catch(() => {});
          await p.waitForTimeout(1500);
        }
        const r = await frame.evaluate(probe); total++;
        const flag = r.n > 0 || r.small > 0 || /HIDDEN/.test(r.tab);
        if (flag) bad++;
        console.log(`${flag ? '✘' : '✓'} ${tool} w=${w} ${state}: ${r.n} overflow, fields<16px ${r.small}, active tab ${r.tab}, content spans ${r.pad}, height ${r.h}`);
        for (const o of r.out) console.log('     ' + o);
        if (SHOTS) await p.locator('#tool').screenshot({ path: path.join(ROOT, 'test', 'shots', `${DIR}-${tool}-${w}-${state}.png`) });
      }
    }
    await c.close();
  }
  console.log(`\n${total} states, ${bad} with findings`);
  await b.close(); server.close();
  process.exitCode = bad === 0 ? 0 : 1;
})();
