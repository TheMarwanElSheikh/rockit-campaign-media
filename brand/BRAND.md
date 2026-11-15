# Rockit brand rules (permanent: apply to every asset, every time)

These are standing instructions from the brand owner. Any person or agent producing Rockit material (newsletter, social, web, decks, documents) follows them without being asked again.

## 1. Gold is always the logo's own metallic gradient

**Never use a flat yellow or flat gold as the brand gold.** The gradient comes directly from the owner's logo file: `brand/rockit-logo.svg`, `linearGradient id="gold-swoosh"`. The globe uses the same colours.

| Offset | Colour |
|---|---|
| 0% | `#A88329` |
| 8% | `#B18B2D` |
| 17% | `#C09934` |
| 25% | `#CFAC49` |
| 33% | `#DEC163` |
| 42% | `#EDD77E` |
| 50% | `#F7E590` (highlight) |
| 58% | `#ECD57B` |
| 67% | `#DEC161` |
| 75% | `#D0AD48` |
| 83% | `#C29B36` |
| 92% | `#B28C2D` |
| 100% | `#A88228` |

The gradient in CSS:

```css
--rockit-gold: linear-gradient(135deg, #A88329 0%, #B18B2D 8%, #C09934 17%, #CFAC49 25%, #DEC163 33%, #EDD77E 42%, #F7E590 50%, #ECD57B 58%, #DEC161 67%, #D0AD48 75%, #C29B36 83%, #B28C2D 92%, #A88228 100%);
```

**Where the gradient applies.** Use it for:
- rules, buttons and step discs
- chart bars that mean "filed / Rockit"
- the stamp and route highlights
- display text in any rendered image, as gradient text

**Where a solid fallback is allowed.** A solid is allowed only where a medium cannot draw a gradient, such as small text in email HTML:
- `#DEC163` for text on navy (a logo stop; contrast 8.8:1)
- `#8a6514` for text on cream (the logo's darkest gold `#A88329`, deepened, because `#A88329` itself is only 3.3:1 on cream)

Every CSS gradient also sets a `background-color` fallback of `#C09934`.

**Charts.** Bars are filled with the gradient: `#A88329 → #C09934 → #DEC163` on light surfaces, and `#A88329 → #B18B2D → #DEC163 → #F7E590` on navy. Both pass the dataviz validator against the spot-series blue.

## 2. Logo: ONLY the owner's files, used exactly as supplied

The owner supplied the official logo on 15 Nov 2026: "Rock it / Transport Services", with a navy R, the gold gradient globe and swoosh, and navy lettering.

| File | Use |
|---|---|
| `rockit-logo.svg` (master), `rockit-logo.pdf` | **Light surfaces.** Paper, white or cream. |
| `rockit-logo-dark-bg.svg` (master), `rockit-logo-dark-bg-on-navy.pdf` | **Dark surfaces.** The owner's own dark version: fine light outline on the R and "ock it", white "Transport Services". It goes directly on navy or midnight. |
| `rockit-logo.png`, `rockit-logo-dark-bg.png` | 2550×1132 transparent PNGs, straight rasterisations of the SVG masters (no edits), for email and social platforms that cannot take SVG. |

**Rules:**
- Use these files and nothing else. Never redraw, re-letter, recolour, invert, tint, stretch, crop into or rotate them, add effects, or set a typeset wordmark in their place.
- Never make your own dark or reversed version. The owner's dark-background file exists for that.
- Light background → `rockit-logo`. Dark background → `rockit-logo-dark-bg`. No light "panels" are needed.
- **Retired, never to be used as the logo:**
  - the older lockup with "Freight & Logistics Solutions" (`RockitShip-v2/packages/docs-engine/assets/brand/rockit-transport-logo.png`)
  - the standalone R mark (`rockit_mark_gold_1024_*.png`; favicon and app-icon use only)
  - any self-made inverted or recoloured file
- If the owner's files are missing, stop and ask. Never substitute another logo. The newsletter builder enforces this.
- **Newsletter placement:** the dark-background logo in the navy email header, in the midnight email footer, and on the footer bar of every slide and cover.

## 3. Other tokens

- **Navy:** `#16243f` for surfaces. The logo's navy is `#0b1f56`.
- **Midnight:** `#080f1f`.
- **Cream:** `#f1eedb`.
- **Paper:** `#faf7ef`.
- **Ink:** `#1b2333`.
- **Type:** Cormorant Garamond for display, Inter for text, IBM Plex Mono for manifest labels.
- **Tagline:** *Means what it says.*
