# The Rockit Manifest

The weekly market brief from Rockit Transport Services & Logistics (RTSL). It is published every Monday at 10:00 Cairo time on rockit-transport.com (blog), LinkedIn, Facebook, Instagram and Google Business Profile. Every issue is filed in the blog category "The Rockit Manifest" (slug `newsletter`), so they all collect on one newsletter page: https://www.rockit-transport.com/insights/categories/newsletter. An email version is staged as a Wix Email Marketing draft each week and sent manually.

## Weekly flow

| When (Cairo) | Step |
|---|---|
| Sunday 14:00 | Research the week, write `issues/<date>/content.json`, fact-check every claim into `AUDIT.md`, build and render, then stage the Wix blog draft, the Wix email draft and the images. A preview is posted to the Claude session. |
| Before Monday 10:00 | Review the preview. Reply "hold" in the session to stop publication. |
| Monday 10:00 | Publish the blog post, then post to LinkedIn, Facebook, Instagram and Google Business, linking to the blog post. |

## Build

```bash
python3 tools/build_issue.py issues/<date>/content.json      # email.html, ricos.json, cover HTML, social.json
cd tools && node render_covers.js ../issues/<date>           # cover_4x5.jpg, cover_4x3.jpg, email_preview.png
```

`content.json` is the single source of truth: every channel is generated from it, so every channel carries the same audited wording.

## Editorial rules

- Every figure names its publisher and date, and links to the page it came from.
- A figure that cannot be read on a primary or reputable trade page is not printed. Removals are logged in `AUDIT.md`.
- Nothing from RTSL job files is used: no rates, margins, customer names, B/L or container numbers.
- No claims about RTSL that the ERP or website cannot support.
- Regulatory items are summaries, with a "not legal advice" footer.
- Voice: *Means what it says.* Confident, plain, no hype, and one dry "Lost in Forwarding" line per issue.

## Brand

See `../brand/BRAND.md` (permanent). Gold is always the gradient defined in `brand/rockit-logo.svg` (`#A88329 → #F7E590 → #A88228`, 13 stops), never flat yellow. The official logo goes on every asset. Navy `#16243f`, midnight `#080f1f`, cream `#f1eedb`.
