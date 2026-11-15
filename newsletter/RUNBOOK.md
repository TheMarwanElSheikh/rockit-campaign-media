# The Rockit Manifest: weekly runbook

> **Brand rules are permanent. Read `brand/BRAND.md` first.**
> - Gold is ALWAYS the metallic gradient defined in `brand/rockit-logo.svg`, never a flat yellow.
> - Logo: ONLY the owner's files, as supplied. Use `brand/rockit-logo` on light surfaces and the owner's `brand/rockit-logo-dark-bg` on navy. Gold comes from the logo SVG's own gradient. If the files are missing, the build stops: ask the owner, never substitute.
> - The builder enforces both. Do not override them.

The scheduled tasks follow this file. Times are Cairo time (Africa/Cairo).

## IDs

| Thing | ID |
|---|---|
| Wix site (rockit-transport.com) | `0e184a47-8d16-405a-9018-42d1181fadd1` |
| Wix blog author member | `949f2ce3-157e-4cec-b043-a8b019d88fa0` |
| LinkedIn (Windsor `linkedin_organic`) | `18956661` |
| Facebook Page (Windsor `facebook_organic`) | `102089469414840` |
| Instagram (Windsor `instagram`) | `17841456872839570` |
| Google Business (Windsor `google_my_business`) | `locations/16077331135089168616` |
| Repo / branch | `TheMarwanElSheikh/rockit-campaign-media` @ `claude/admiring-euler-5zszx7`, folder `newsletter/` |

## Sunday 14:00: research, write, audit, stage

1. **Repo.** Pull the branch. Create `issues/<next Monday ISO date>/`. Issue number = previous + 1.
2. **Research the last 7 days.** Fetch primary pages with plain `curl` (no custom user-agent) into the scratchpad, and extract text with `python3 -I`. Minimum set:
   - Drewry WCI page
   - Xeneta weekly update
   - Freightos weekly update
   - SCA news
   - Container News (carrier FAK/PSS to the Med and Egypt)
   - The Loadstar / gCaptain / Splash247
   - EnterpriseAM (CBE, inflation, Egypt trade)
   - TAC Index
   - Any Egyptian customs decree news
3. **Write `content.json`** in the same schema as Issue 001 (revision 2: manifest design).
   - Lead story with "So what, for you" for importers, exporters and agents.
   - 6–9 numbers.
   - Egypt desk ×3 and World desk ×3.
   - Actions: shippers ×4 and agents ×4.
   - Dates for the next ~8 weeks.
   - One "Rockit explains" item linking an existing rockit-transport.com post.
   - One "Lost in Forwarding" excuse.
   - Per-channel social copy.
4. **Audit.** Write `AUDIT.md`: one row per claim, with the source page read and a status (P/T/R/S).
   - Remove anything not verified, and list the removals.
   - Never print a figure from a search snippet alone.
   - No RTSL job data, rates, customer names, or claims about RTSL that cannot be supported.
5. **Build and render.**
   - Run `python3 tools/build_issue.py issues/<date>/content.json`.
   - Run `node tools/render_covers.js issues/<date>`.
   - Look at every chart, slide, cover and the email preview, and fix any label collisions before staging.
6. **Commit and push.** Note the commit SHA. The image URL is `https://cdn.jsdelivr.net/gh/TheMarwanElSheikh/rockit-campaign-media@<sha>/newsletter/issues/<date>/visuals/<file>`. Set `img_base` in content.json to that folder URL, then rebuild so email.html points at it.
7. **Stage on Wix** (nothing public yet):
   - Import the visuals (charts, route map, ACID-style explainer graphic, cover) via `POST /site-media/v1/files/import` from the jsDelivr commit URL, and swap the `@key` image ids in `ricos.json` for the returned media ids.
   - Create the blog draft (`POST /blog/v3/draft-posts`, `publish: false`, slug `rockit-manifest-<NNN>-<topic>`).
   - Schedule it natively: `PATCH /blog/v3/draft-posts/{id}` with `action: "UPDATE_SCHEDULE"` and `scheduledPublishDate` = Monday 08:00:00Z (10:00 Cairo, EET). Read it back and confirm `status: SCHEDULED`.
   - Create the HTML email campaign draft (`POST /email-marketing/v1/campaigns`). Never publish it.
8. **Write `publish_plan.json`** with the exact Windsor params (same shape as Issue 001), commit and push.
9. **Post the preview in the session:** the headline, the numbers, the cover image and what was removed in the audit. Say that it publishes Monday 10:00 unless the user replies "hold".

## Monday 10:00: publish

1. **Check for "hold".** If the user replied "hold" (or otherwise objected) since staging, do nothing except report.
2. **Find the plan.** Open `issues/<today>/publish_plan.json`. If it is missing, report and stop. Never improvise an issue on Monday.
3. **Publish in order.**
   - Wix: the post goes live natively at 10:00:00. Verify with `GET /blog/v3/posts/{id}` (`firstPublishedDate` present). Only if it is not live, publish it with `POST /blog/v3/draft-posts/{id}/publish`.
   - Then LinkedIn, Facebook, Instagram and Google Business via Windsor `execute_action` with the exact params.
4. **Failures.** If a step fails, do not retry with altered content. Report it with the error.
5. **Report.** Give the result per channel, with links. Remind the user that the email draft is ready to send by hand in Wix Email Marketing.

## Constraints to remember

- Wix Email Marketing is on the free plan: 200 emails a month, no API scheduling and no contact labels. The user chose to send the email by hand.
- `english.ahram.org.eg` and `egypttoday.com` return 403 to automated requests. `maersk.com` times out. Use corroborating reachable sources.


## Design system (revision 2, from Issue 001)

**Concept: the issue is a cargo manifest.**
- Header fields: Voyage, ETD, Shipper, Consignee: You, Contents, Sources.
- A gold "VERIFIED · N SOURCES" stamp.
- Sections are numbered "Line 01…06".

**Reader path:**
1. The 60-second manifest, with Import / Export / Agents tags.
2. Line 01 · The straight answer, with a chart.
3. Line 02 · Feature, with a chart.
4. Line 03 · By the numbers: six tiles, with ▲ red = costs more and ▼ green = costs less.
5. Line 04 · Egypt desk, with the visual.
6. Line 05 · World desk.
7. Line 06 · Your move, split into Import / Export / Forward.
8. The calendar.
9. Rockit explains, with a diagram.
10. The Thesaurus of Excuses: a dictionary entry in the Lost in Forwarding voice.
11. The sign-off: "That's the manifest. Everything on it, we checked. Anything not on it, ask us."

**Voice:**
- Short statement. A beat. The point.
- No forecasts dressed up as facts.
- Every number links to its source.

**Charts:**
- Palette checked with the dataviz validator: the spot series is blue (`#3f6db3` on light, `#5c84c6` on dark). The filed/Rockit series is the logo-gold gradient (centred on `#C09934` on light and `#B18B2D` on dark).
- Direct labels on every bar, and honest zero baselines.
- Light 600px PNGs rendered at 2×.

**Social:**
- Instagram gets a five-slide 4:5 carousel (`slide_1..5.jpg`).
- LinkedIn and Facebook get `slide_1.jpg`.
- Google Business gets `cover_4x3.jpg`.
