# Rockit brand rules (permanent: apply to every asset, every time)

These are standing instructions from the brand owner. Any person or agent producing Rockit material (newsletter, social, web, decks, documents) follows them without being asked again.

## 1. Gold is always the logo's metallic gradient

**Never use a flat yellow or flat gold as the brand gold.** The old `#d5ae69` is retired.

The gradient was sampled from `brand/rockit-logo.png`, the official logo (from the globe and the swoosh):

| Stop | Colour | Role |
|---|---|---|
| 0% | `#966f1b` | deep shadow |
| 20% | `#b8912e` | body |
| 40% | `#d7b754` | light body |
| 52% | `#f7e58e` | highlight |
| 70% | `#d2b04b` | return |
| 100% | `#ab8528` | edge shadow |

The gradient in CSS:

```css
--rockit-gold: linear-gradient(135deg, #966f1b 0%, #b8912e 20%, #d7b754 40%, #f7e58e 52%, #d2b04b 70%, #ab8528 100%);
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
- `#d7b754` for text on navy (contrast 7.9:1)
- `#8a6514` for text on cream (contrast 5.0:1)

Every CSS gradient also sets a `background-color` fallback of `#b8912e`.

**Charts.** Bars are filled with the gradient: `#966f1b → #b8912e → #d7b754` on light surfaces, and `#966f1b → #ab8528 → #d7b754 → #f7e58e` on navy. Both pass the dataviz palette validator against the spot-series blue (`#3f6db3` light, `#5c84c6` dark).

## 2. The Rockit logo appears on every branded asset

- **`brand/rockit-logo.png`:** the official full-colour logo (navy and gold, transparent background). Use it on light backgrounds.
- **`brand/rockit-logo-reversed.png`:** the same logo with the navy recoloured to cream `#f1eedb`, gold untouched. Use it on navy or midnight backgrounds.
- **Source:** `RockitShip-v2/packages/docs-engine/assets/brand/rockit-transport-logo.png`.
- **Do not** redraw, re-letter, recolour the gold, stretch or crop the logo. Use a typeset "ROCKIT" wordmark only beside the real logo, never instead of it.
- **Newsletter placement:**
  - email header and footer
  - every social slide footer
  - covers, including the blog cover and the Google Business image

## 3. Other tokens

- **Navy:** `#16243f` for surfaces. The logo's navy is `#0b1f56`.
- **Midnight:** `#080f1f`.
- **Cream:** `#f1eedb`.
- **Paper:** `#faf7ef`.
- **Ink:** `#1b2333`.
- **Type:** Cormorant Garamond for display, Inter for text, IBM Plex Mono for manifest labels.
- **Tagline:** *Means what it says.*
