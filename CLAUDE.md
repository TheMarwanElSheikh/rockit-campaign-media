# Instructions for Claude in this repository

**Read `brand/BRAND.md` before producing or editing any Rockit asset.** It records permanent decisions from the brand owner. These two are non-negotiable:

1. **Gold is always the metallic gradient from the Rockit logo.** Never use a flat yellow.
2. **Logo: ONLY the owner-supplied "Rock it / Transport Services" lockup, as supplied** (`brand/rockit_logo_lockup_transparent.png`, `_white.png`, and the owner's own `_dark.png`). Never redraw, recolour, invert, crop into or replace it, and never make your own dark version. The old "Freight & Logistics Solutions" lockup and the standalone R mark are retired as logos. If the lockup files are missing, stop and ask the owner; never substitute.

The weekly newsletter (The Rockit Manifest) lives in `newsletter/`. Follow `newsletter/RUNBOOK.md`. Its builder, `newsletter/tools/build_issue.py`, already encodes the brand rules: the gold tokens `GOLD_GRAD`, `GT`, `svg_gold`, and the owner's lockup (`brand/rockit_logo_lockup_*.png`) placed on light panels in every issue. The build stops if the lockup is missing. Do not reintroduce `#d5ae69` or any other flat gold.
