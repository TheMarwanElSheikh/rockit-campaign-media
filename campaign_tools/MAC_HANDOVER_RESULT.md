# Result of MAC_HANDOVER.md (Mac session "Marketing — LinkedIn campaign (fork)", 26 Nov 2026)

## 1. Business Suite › Content › Scheduled: NOT re-checked today

Meta is signed out in the Mac session's browser (Business Suite shows the login page), so the list could not be read
today and nothing was re-scheduled. The owner has to sign in again; the check is repeated then.

Last full check, 23 Nov 2026 evening, after the light artwork was swapped in: 18 rows, every one with the light
artwork and 10:00 Cairo.

| Date | Facebook | Instagram |
|---|---|---|
| 24 Nov "we'll revert" | scheduled (has since gone out) | scheduled (has since gone out) |
| 26 Nov "all-in rate" | scheduled | scheduled |
| 1 Dec "ETA: next week" | scheduled | scheduled |
| 3 Dec "noted with thanks" | scheduled | scheduled |
| 8 Dec "on board" | scheduled | scheduled |
| 10 Dec "in transit" | scheduled | scheduled |
| 15 Dec "minor delay" | scheduled | scheduled |
| 17 Dec "Rockit" | scheduled | scheduled |
| 22 Dec "out of office" | scheduled | scheduled |

So on 23 Nov all eight planned Facebook posts from 26 Nov to 22 Dec were there. The "out of office" post was created
on 23 Nov in the Business Suite composer as one post to both the Page and Instagram; the other 16 were created
separately. That may be why an API count shows 7 Facebook posts (or the count was taken after the 26 Nov post went
out). This is a guess until the list is read again.

## 2. Pushed: campaign_tools/lif_light/

Commit 5c07e89ed96e889c23488692b207a147bb278b7a on claude/admiring-euler-5zszx7 (parent 3db155a), 22 files:

- `schedule.json`: the seven January posts (5, 12, 14, 19, 21, 26, 28 Jan 2027, 10:00 Cairo), each with date, stem,
  image files in posting order, the exact Facebook caption (utm link, `utm_source=facebook`) and the exact Instagram
  caption (plain `rockit-transport.com/get-a-quote`). Captions are generated from the Mac runbook's caption table, not
  retyped.
- `images/vol2-thesaurus-light/`: nine pages, JPEG 1080x1350. 28 Jan uses all nine in file order (00 to 08).
- `images/vol1-dictionary-light/`: cover and eight entries, JPEG 1080x1350.
- `overview/`: one contact sheet per volume.
- `README.md`: what the files are and the owner's brand rules that apply.

## 3. Mac session's 30 Dec job: still active

The job that schedules the January Meta posts from the Mac session is still set. The owner has not yet been asked to
cancel it; that is asked now, with the push in place. Until the owner says yes, both the Mac job and any cloud runner
could act on January. Whichever runs second must check Business Suite › Content › Scheduled first and skip a date that
is already there.
