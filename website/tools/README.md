# The free tools of rockit-transport.com

The seven tools under **E-services** on https://www.rockit-transport.com are HTML embeds on a Wix Studio site: each
page holds one HTML element whose code is one self-contained file. This folder is where that code is kept, fixed and
tested.

| Page | File |
|---|---|
| `/chargeable-weight` | `chargeable-weight.html` |
| `/load-calculator` | `load-calculator.html` |
| `/duties-taxes-calculator` | `duties-taxes-calculator.html` |
| `/vessel-schedules` | `vessel-schedules.html` |
| `/vessel-tracking` | `vessel-tracking.html` |
| `/flight-tracking` | `flight-tracking.html` |
| `/container-tracking` | `container-tracking.html` |

```
src/            each tool's code as the site served it on 19 Nov 2026 (read from the published pages)
portrait.css    the fix: what a phone held upright needs, appended to every tool
portrait.js     the part of the fix a stylesheet cannot do (the tab strip, tables)
build.py        src/ + the fix -> dist/
dist/           what is pasted into each page's HTML element
test/           the browser test
```

## What was wrong (19 Nov 2026)

The owner reported that the tools "do not fit in the page in portrait mode". Measured on the published pages on phone
screens of 320, 360, 390 and 430px:

- The page gives a tool's frame the screen's width less 80px (two paddings of 20px a side): **310px on a 390px phone,
  240px on a 320px one.**
- The tools were laid out for a desk and for one phone width. Narrower than that, their grids (four fields to a row,
  three or four tiles to a row) and their one-line buttons are wider than the frame, and the frame's body hides what
  overflows (`overflow: hidden`): the right-hand side of the form, of the result and of every paragraph is cut off.
  On a 320px phone this hit the chargeable weight calculator, the load calculator and the vessel schedules; the
  container tracker's result was cut off on every phone up to 390px.
- The strip of tools at the top scrolls sideways with its scrollbar hidden. On five of the seven pages the current
  tool's tab was off the edge of the strip, with nothing to show the strip moves.
- **20 of 28 states** on the published pages (7 tools × 4 phone widths) had something cut off or the current tab out
  of sight. In frames served locally, untouched and used: **43 of 56**.

Also found, at every width: the step numbers 1, 2, 3 in the duty calculator's navy discs were invisible (they
inherited the transparent fill of the gradient title beside them).

## What the fix does

`portrait.css` and `portrait.js` are appended to each tool, never merged into it:

- nothing in a tool has a minimum width the frame cannot give: grids use tracks that may shrink, four fields to a row
  become two rows of two, tiles go as many to a row as fit, long buttons and long words wrap;
- a table's cells wrap; a table of four columns is a list of blocks on the narrowest phones; a table that still cannot
  fit scrolls inside its own box instead of being cut by the frame;
- the current tool's tab is brought into view, and the strip fades at the end that has more;
- buttons are 44px tall under a finger; the tracking maps take a little over half the screen, not a screen and a half;
- the duty calculator's step numbers are white on their discs;
- gold follows `brand/BRAND.md` §1: the logo's own gradient for buttons, rules, bars and borders, and the allowed solid
  `#8a6514` only where a gradient cannot be drawn (focus rings, text behind a gradient clip). The tools carried
  another gradient and a flat `#D0AF50`.

Everything a phone needs is inside `@media (max-width: 480px)` (the frame's own width), so a desk is laid out exactly
as before: the test confirms every tool's height is unchanged at 600px and 980px.

Result: **0 of 56** states with a finding locally, and **0 of 28** on the published pages with the fixed files served
in their place in the test browser.

## Putting a fixed tool on the site

The code of an HTML element lives in the Wix Studio editor; no Wix API writes it. For each of the seven pages:

1. Open the site in the Wix Studio editor and go to the tool's page.
2. Select the tool's HTML embed and open its code setting.
3. Select all of the code in the box, delete it, and paste the whole of the matching file in `dist/`.
4. Apply / update the embed. Repeat for the other pages, then **Publish**.

Check on a phone: the current tool's tab is visible in the strip, nothing touches or runs past the right edge, and
Calculate / Check shows a result that is not cut off.

A wider frame is better still: the two 20px paddings around the embed's section and its container are set per
breakpoint in the editor. Reducing them on the mobile breakpoint gives a tool up to 40px more width. The fixed tools
do not depend on this.

## Changing a tool later

1. Save the tool's new code over its file in `src/` (the code without the `rm-portrait` block: `build.py` removes an
   earlier block itself, so pasting a file from `dist/` back into `src/` is also fine).
2. `python3 website/tools/build.py`
3. `node website/tools/test/portrait.test.cjs` — it must report `0 with findings`.
4. Paste the file from `dist/` into the page's HTML element and publish.

`python3 website/tools/build.py --check` fails when `dist/` is not what `src/` and the fix give.

## Not covered by the test

The tracking tools draw maps and results from other services (VesselFinder, adsb.lol / adsb.fi, the carriers' own
sites). Those were not reachable from where the test was written, so the test measures those tools' forms, texts and
layout, not a live map or a live result.
