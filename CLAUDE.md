# Instructions for Claude in this repository

**Read `brand/BRAND.md` before producing or editing any Rockit asset.** It records permanent decisions from the brand owner. These two are non-negotiable:

1. **Gold is always the metallic gradient from the Rockit logo.** Never use a flat yellow.
2. **Only the LATEST official Rockit mark, `brand/rockit_mark_gold_1024_transparent.png` (navy R with the golden-yellow gradient globe), unaltered, on every branded asset.** Always check `origin/main` for a newer logo first. The old "Rock it Transport Services" lockup is retired. Never invert, reverse, recolour or redraw the mark. On navy or dark designs, put it on a light (paper `#faf7ef` or white) panel.

The weekly newsletter (The Rockit Manifest) lives in `newsletter/`. Follow `newsletter/RUNBOOK.md`. Its builder, `newsletter/tools/build_issue.py`, already encodes the brand rules: the gold tokens `GOLD_GRAD`, `GT`, `svg_gold`, and the latest mark (copied from `brand/rockit_mark_gold_1024_transparent.png`, transparent margin trimmed) placed on light panels in every issue. Do not reintroduce `#d5ae69` or any other flat gold.
