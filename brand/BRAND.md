# Rockit brand rules (permanent: apply to every asset, every time)

These are standing instructions from the brand owner. Any person or agent producing Rockit material (newsletter, social, web, decks, documents) follows them without being asked again.

## 1. Gold is always the logo's metallic gradient

**Never use a flat yellow or flat gold as the brand gold.** The old `#d5ae69` is retired.

The gradient was sampled from the globe of `brand/rockit_mark_gold_1024_transparent.png`, the latest official mark:

| Stop | Colour | Role |
|---|---|---|
| 0% | `#a47420` | deep shadow |
| 20% | `#c08f2f` | body |
| 40% | `#e1b348` | light body |
| 52% | `#f6d77a` | highlight |
| 70% | `#d7a73e` | return |
| 100% | `#b17f25` | edge shadow |

The gradient in CSS:

```css
--rockit-gold: linear-gradient(135deg, #a47420 0%, #c08f2f 20%, #e1b348 40%, #f6d77a 52%, #d7a73e 70%, #b17f25 100%);
```

**Where the gradient applies.** Use it for:
- rules
- buttons
- chart bars that mean "filed / Rockit"
- stamps, icons, dots and step discs
- route highlights
- display text in any rendered image (slides, covers, mastheads), drawn as gradient text with `background-clip:text`
- SVG `linearGradient`

**Where a solid fallback is allowed.** A solid is allowed only where the medium cannot draw a gradient. That means small text inside email HTML, because Gmail and Outlook do not support gradient text. Use these solids, both taken from the logo:
- `#e1b348` for text on navy (contrast 7.9:1)
- `#8a6514` for text on cream (contrast 5.0:1)

Every CSS gradient also sets a `background-color` fallback of `#c08f2f`.

**Charts.** Bars are filled with the gradient: `#a47420 → #c08f2f → #e1b348` on light surfaces, and `#a47420 → #b17f25 → #e1b348 → #f6d77a` on navy. Both pass the dataviz palette validator against the spot-series blue (`#3f6db3` light, `#5c84c6` dark).

## 2. Logo: ONLY the latest official Rockit mark, unaltered, on every branded asset

- **The logo is `brand/rockit_mark_gold_1024_transparent.png`**: the navy "R" with the golden-yellow gradient globe. It was added to `main` on 14 Nov 2026 in commit `aa70bb8`, "Logo globe: golden-yellow gradient". `brand/rockit_mark_gold_1024_white.png` is the same mark on a white ground.
- **Before using any logo, check `main`** (`git fetch origin && git log origin/main -- brand/`) for a newer one. The latest file on `main` always wins.
- **Retired, never to be used again:**
  - the older "Rock it Transport Services" lockup with the flat globe (`RockitShip-v2/packages/docs-engine/assets/brand/rockit-transport-logo.png`)
  - any inverted, reversed or recoloured version (rejected 15 Nov 2026)
- **Never** invert, reverse, recolour, tint, redraw, stretch, rotate or add effects. Trimming the transparent margin is the only allowed processing.
- **On a navy or dark design, place the mark on a light panel**: paper `#faf7ef` or white. The mark itself never changes to suit the background.
- **The typeset wordmark sits beside the mark, never instead of it.** "ROCKIT" is set in Cormorant Garamond in the logo navy `#0b1f56`. "TRANSPORT SERVICES & LOGISTICS" is set in Inter caps in gold.
- **Newsletter placement:**
  - a light band at the top of the email
  - a light panel in the email footer
  - a light footer bar on every social slide and cover

## 3. Other tokens

- **Navy:** `#16243f` for surfaces. The logo's navy is `#0b1f56`.
- **Midnight:** `#080f1f`.
- **Cream:** `#f1eedb`.
- **Paper:** `#faf7ef`.
- **Ink:** `#1b2333`.
- **Type:** Cormorant Garamond for display, Inter for text, IBM Plex Mono for manifest labels.
- **Tagline:** *Means what it says.*
