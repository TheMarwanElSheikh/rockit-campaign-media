# The Rockit Manifest: weekly runbook

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
3. **Write `content.json`** in the same schema as Issue 001.
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
   - Look at both covers and the email preview.
6. **Commit and push.** Note the commit SHA. The image URL is `https://cdn.jsdelivr.net/gh/TheMarwanElSheikh/rockit-campaign-media@<sha>/newsletter/issues/<date>/cover_4x5.jpg` (and `cover_4x3.jpg`).
7. **Stage on Wix** (nothing public yet):
   - Import `cover_4x3.jpg` (`POST /site-media/v1/files/import`).
   - Create the blog draft (`POST /blog/v3/draft-posts`, `publish: false`, slug `rockit-manifest-<NNN>-<topic>`).
   - Create the HTML email campaign draft (`POST /email-marketing/v1/campaigns`). Never publish it.
8. **Write `publish_plan.json`** with the exact Windsor params (same shape as Issue 001), commit and push.
9. **Post the preview in the session:** the headline, the numbers, the cover image and what was removed in the audit. Say that it publishes Monday 10:00 unless the user replies "hold".

## Monday 10:00: publish

1. **Check for "hold".** If the user replied "hold" (or otherwise objected) since staging, do nothing except report.
2. **Find the plan.** Open `issues/<today>/publish_plan.json`. If it is missing, report and stop. Never improvise an issue on Monday.
3. **Publish in order.**
   - Wix: `POST /blog/v3/draft-posts/{id}/publish`, then verify with `GET /blog/v3/posts/{id}`.
   - Then LinkedIn, Facebook, Instagram and Google Business via Windsor `execute_action` with the exact params.
4. **Failures.** If a step fails, do not retry with altered content. Report it with the error.
5. **Report.** Give the result per channel, with links. Remind the user that the email draft is ready to send by hand in Wix Email Marketing.

## Constraints to remember

- Wix Email Marketing is on the free plan: 200 emails a month, no API scheduling and no contact labels. The user chose to send the email by hand.
- `english.ahram.org.eg` and `egypttoday.com` return 403 to automated requests. `maersk.com` times out. Use corroborating reachable sources.
