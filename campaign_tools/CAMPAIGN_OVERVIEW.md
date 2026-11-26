# Rockit social calendar: single source of truth (owner decision, 24 Nov 2026)

Owner, 24 Nov 2026: "don't remove anything but organize yourself properly going forward."

## Rules
1. Nothing already published or already scheduled is deleted or cancelled.
2. There is ONE Lost in Forwarding (LiF) campaign: the one scheduled natively in Meta Business Suite and on LinkedIn
   by the owner's Mac session "Marketing — LinkedIn campaign (fork)" (session_01Nsrmiaf3NnkWS7TafJe8K2).
   Its plan lives on the owner's SSD: Linkedin Campaign/lost-in-forwarding/CAMPAIGN-PLAN.md.
3. The repo's older LiF set (vol1/, vol2/, 16 Nov artwork, 40 per-slot tasks + 2 dispatchers) is RETIRED.
   Every one of those tasks is disabled. No cloud session posts LiF content.
4. The cloud runner (session_01Nsrmia94ZmyDMV8xYCYUzo) only handles The Rockit Manifest newsletter.
5. Before any post on any channel: check the live channel for the same content first.

## Already published (stays up)
| Date | Channel | Post |
|---|---|---|
| 19 Nov | LinkedIn | LiF Vol. I swipe-through document post (urn:li:ugcPost:7529096428816728065), paid promotion to 30 Nov |
| 24 Nov 09:30 Cairo | LinkedIn | "Noted with thanks" (repo set, urn:li:share:7530896315862536192) |
| 24 Nov 10:00 Cairo | Facebook, Instagram (+ LinkedIn as scheduled) | "We'll revert" (Mac set) |
| 16 Nov, 23 Nov | Web, LinkedIn newsletter, Facebook, Instagram, Google | The Rockit Manifest 001 and 002 |

## Lost in Forwarding: scheduled, 10:00 Cairo, Facebook + Instagram + LinkedIn
| Date | Post | Meta (FB + IG) | LinkedIn |
|---|---|---|---|
| Thu 26 Nov | All-in rate | scheduled | scheduled |
| Tue 1 Dec | ETA: next week | scheduled | scheduled |
| Thu 3 Dec | Noted with thanks | scheduled | scheduled |
| Tue 8 Dec | On board | scheduled | scheduled |
| Thu 10 Dec | In transit | scheduled | scheduled |
| Tue 15 Dec | Minor delay | scheduled | scheduled |
| Thu 17 Dec | Rockit (Vol. I close) | scheduled | scheduled |
| Tue 22 Dec | Out of office (first look at Vol. II) | scheduled | scheduled |
| Tue 5 Jan | The vessel was rolled | Mac session may schedule ~30 Dec; otherwise the cloud runner posts at 10:05 | scheduled |
| Tue 12 Jan | It's with customs | to be scheduled | scheduled |
| Thu 14 Jan | We're on it | to be scheduled | scheduled |
| Tue 19 Jan | Kindly resend the documents | to be scheduled | scheduled |
| Thu 21 Jan | Our agent will handle it | to be scheduled | scheduled |
| Tue 26 Jan | Free time included | to be scheduled | scheduled |
| Thu 28 Jan | Vol. II thesaurus (9 pages) | to be scheduled | scheduled |

Open checks:
- Facebook reports 7 scheduled posts; the Mac plan expects 8 (26 Nov to 22 Dec). One may be missing; check Business Suite › Content › Scheduled.
- January Meta posts: artwork and captions handed over by the Mac session on 26 Nov (campaign_tools/lif_light/). The cloud task "LiF January Meta posts" runs Tue/Thu 10:05 Cairo in January: it posts on Facebook and Instagram only if the post is not already live (so the Mac session's own 30 Dec job, if it runs, cannot cause doubles). 28 Jan: Instagram 9-page carousel; Facebook 9-page video (the Facebook API takes one photo per post).

## The Rockit Manifest (weekly, every Monday)
| When (Cairo) | Who | What |
|---|---|---|
| Sun 13:47 | cloud runner | research + 16-page edition, Wix post scheduled for Mon 10:00, email draft, LinkedIn edition material |
| Mon 10:00 | Wix | website post goes live |
| Mon 10:05 | cloud runner | website check, then Facebook photo, Instagram carousel, Google Business post (no LinkedIn image post) |
| Mon 11:00 | Mac session | LinkedIn newsletter edition (owner confirms in that session) |
| any time | owner | sends the Wix email draft manually |

Next issues: Voyage 003 Mon 30 Nov, 004 Mon 7 Dec, 005 Mon 14 Dec, 006 Mon 21 Dec, 007 Mon 28 Dec.
On Mondays nothing from LiF is scheduled, so the two never collide.

## Automatic checks (cloud runner, read-only)
- Every Tue and Thu at 10:20 Cairo: confirms today's Lost in Forwarding post went out once on Facebook, Instagram and
  LinkedIn; logs to campaign_tools/post_checks.md and tells the owner only if something is missing or doubled.
- 31 Dec, 10:00 Cairo: confirms the January Meta posts are scheduled.
- Every Monday: the newsletter publish task checks the live website before posting anywhere.
