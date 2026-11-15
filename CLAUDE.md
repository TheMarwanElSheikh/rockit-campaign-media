# Instructions for Claude in this repository

**Read `brand/BRAND.md` before producing or editing any Rockit asset.** It records permanent decisions from the brand owner. These two are non-negotiable:

1. **Gold is always the metallic gradient from the logo file itself** (`brand/rockit-logo.svg`, gradient `gold-swoosh`: `#A88329 → … → #F7E590 → … → #A88228`; full table in BRAND.md). Never use a flat yellow.
2. **Logo: ONLY the owner's files, exactly as supplied.** On light surfaces use `brand/rockit-logo.svg` (PNG: `rockit-logo.png`). On dark surfaces use the owner's own `brand/rockit-logo-dark-bg.svg` (PNG: `rockit-logo-dark-bg.png`) directly on navy. Never redraw, recolour, invert or make your own versions. The old "Freight & Logistics Solutions" lockup and the standalone R mark are retired as logos. If the files are missing, stop and ask the owner.

The weekly newsletter (The Rockit Manifest) lives in `newsletter/`. Follow `newsletter/RUNBOOK.md`. Its builder, `newsletter/tools/build_issue.py`, already encodes the brand rules: the gold tokens `GOLD_GRAD`, `GT`, `svg_gold`, and the owner's logo files (`rockit-logo` on light, `rockit-logo-dark-bg` on navy). The build stops if they are missing. Do not reintroduce `#d5ae69` or any other flat gold.
