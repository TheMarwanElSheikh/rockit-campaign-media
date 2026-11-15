# Rockit brand rules (permanent: apply to every asset, every time)

These are standing instructions from the brand owner. Any person or agent producing Rockit material (newsletter, social, web, decks, documents) follows them without being asked again.

## 1. Gold is always the logo's metallic gradient

**Never use a flat yellow or flat gold as the brand gold.** The old `#d5ae69` is retired.

The gradient was sampled from the golden-yellow globe of the latest official artwork (`brand/rockit_mark_gold_1024_transparent.png`, the same globe as the lockup). Re-sample it from `rockit_logo_lockup_transparent.png` once that file is in `brand/`, and update this table if it differs:

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

## 2. Logo: ONLY the owner-supplied "Rock it / Transport Services" lockup, as supplied

The owner supplied the official logo on 15 Nov 2026, in five versions:
- the lockup on a transparent background, at two sizes
- the lockup on a white background, at two sizes
- a version for dark backgrounds, with "Transport Services" in white

The lockup is: a navy "R" with the gold gradient globe, "ock it" in navy, the gold swoosh and arrow, and "Transport Services" underneath.

**Files** (store them in `brand/` exactly as supplied, unedited):

| File | Use |
|---|---|
| `rockit_logo_lockup_transparent.png` | Default. On light surfaces (paper `#faf7ef` or white). |
| `rockit_logo_lockup_white.png` | Where a white-ground file is needed (documents, printing, platforms that reject transparency). |
| `rockit_logo_lockup_dark.png` | The owner's own version for dark backgrounds ("Transport Services" in white). |

**Rules:**
- Use these files and nothing else. Never redraw, re-letter, recolour, invert, tint, stretch, crop into, rotate, add effects, or set type next to the lockup as a substitute. It already carries the name. Trimming transparent margin is the only allowed processing.
- Never create your own dark or reversed version. Use the owner's `rockit_logo_lockup_dark.png`, or place the transparent lockup on a light panel.
- **Retired, never to be used as the logo:**
  - the older lockup with "Freight & Logistics Solutions" (`RockitShip-v2/packages/docs-engine/assets/brand/rockit-transport-logo.png`)
  - the standalone R mark (`rockit_mark_gold_1024_*.png`; favicon and app-icon use only)
  - any self-made inverted or reversed file
- **If the lockup files are missing from `brand/`, stop and ask the owner.** Never substitute another logo. The newsletter builder enforces this.
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
