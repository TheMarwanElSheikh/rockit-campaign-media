#!/usr/bin/env python3
"""Replace the old self-made "ROCKIT / Transport Services & Logistics" text wordmark on the Lost in Forwarding
creatives with the owner's logo (brand/rockit-logo.png) on a white strip (owner's rule, 16 Nov 2026: the logo always
sits on a light surface; only the owner's files).

Each creative ends in a navy band: kicker + caption, a thin rule, then the wordmark. The strip covers from just above
the rule to the bottom edge; the caption above it is untouched.

    python3 apply_brand_strip.py vol1 vol2          # rewrites *_feed_4x5.jpg, *_story_9x16.jpg, *_reel_9x16.mp4 in place

Feed (1080x1350): rule at y=1240 -> strip at y=1222.  Story (1080x1920): rule at y=1448-1450 -> strip at y=1430.
Reels: the band slides up from the bottom; the rule is located in every frame (searched only at or below its resting
position) and the strip follows it, so the old wordmark is never visible.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent
FEED = Image.open(HERE / "strip_feed.png").convert("RGB")
STORY = np.asarray(Image.open(HERE / "strip_story.png").convert("RGB"))
FEED_Y, STORY_Y, STORY_RULE_MIN = 1222, 1430, 1440


def find_rule(a, y_from):
    """Row of the thin rule inside the navy band, or None. a: HxWx3 uint8."""
    h = a.shape[0]
    seg = a[y_from:h, 100:990].astype(int)
    rb = (seg[:, :, 0] - seg[:, :, 2]).mean(axis=1)            # navy ~ -40, rule > 0
    edge = a[:, 1040].astype(int).sum(axis=1)                   # navy at the right margin ~ 105
    for i in np.argsort(-rb):
        if rb[i] < -8:
            return None
        y = y_from + int(i)
        if 4 <= y < h - 4 and edge[y - 4] < 200 and edge[min(y + 4, h - 1)] < 200:
            return y
    return None


def do_image(p):
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if h == 1350:
        assert find_rule(np.asarray(im), 1200) in (1239, 1240, 1241), p
        im.paste(FEED, (0, FEED_Y))
    else:
        im.paste(Image.fromarray(STORY), (0, STORY_Y))
    im.save(p, quality=95, subsampling=0, optimize=True)


def iter_frames(p, w=1080, h=1920):
    d = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(p), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    while True:
        buf = d.stdout.read(w * h * 3)
        if len(buf) < w * h * 3:
            break
        yield np.frombuffer(buf, np.uint8).reshape(h, w, 3)
    d.wait()


def patch(a):
    """Mean colour of a plain bottom-right patch: page background until the band arrives, band navy after."""
    return a[1850:1910, 1000:1070].astype(np.float32).mean(axis=(0, 1))


def fit_band(cur, page, final, y0, max_dy=120):
    """The band fades in while sliding up. Model rows >= y0: cur = (1-a)*page + a*final shifted down by dy.
    Returns (a, dy) minimising the residual (closed-form a for each dy). Subsampled for speed."""
    h = cur.shape[0]
    rows = np.arange(y0, h, 2)
    C = cur[rows, 60:1020:2].astype(np.float32)
    P = page[rows, 60:1020:2].astype(np.float32)
    best = (1e30, 0.0, 0)
    for dy in range(0, max_dy + 1, 1):
        src = rows - dy
        B = np.where((src >= y0)[:, None, None], final[np.clip(src, 0, h - 1), 60:1020:2].astype(np.float32), P)
        D = B - P
        den = float((D * D).sum())
        if den < 1:
            continue
        a = float(((C - P) * D).sum() / den)
        a = min(max(a, 0.0), 1.0)
        res = float(((C - P - a * D) ** 2).sum())
        if res < best[0]:
            best = (res, a, dy)
    return best[1], best[2]


def do_reel(p, src=None):
    """p: output path; src: untouched original (defaults to p).
    Pass 1 finds the transition start t0 (bottom-right patch leaves the page colour) and keeps the last frame (band at
    rest). Pass 2: frames < t0 unchanged; frames with the rule found and the band at full strength get the strip pasted
    at rule-20; transition frames get the strip blended at the fitted opacity and offset."""
    w, h = 1080, 1920
    src = src or p
    p0 = None
    t0 = None
    n = 0
    prev = None
    for i, a in enumerate(iter_frames(src)):
        pa = patch(a)
        if p0 is None:
            p0 = pa
        if t0 is None and np.abs(pa - p0).max() > 1.5:
            t0 = i
        if t0 is None:
            prev = a.copy()
        last = a
        n = i + 1
    final = last.copy()
    page = prev
    assert t0 is not None and page is not None, p
    r_final = find_rule(final, STORY_RULE_MIN)
    assert r_final is not None, p
    top_final = r_final - 20
    band_y0 = 1280
    fin_p = patch(final)
    out = p.with_suffix(".tmp.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", "30", "-i", "-",
                            "-i", str(src), "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", "-shortest", str(out)], stdin=subprocess.PIPE)
    stats = {"t0": t0, "paste": 0, "blend": [], "frames": n}
    for i, a in enumerate(iter_frames(src)):
        if i >= t0:
            a = a.copy()
            r = find_rule(a, STORY_RULE_MIN)
            if r is not None and np.abs(patch(a) - fin_p).max() < 3:
                top = r - 20
                k = min(h - top, STORY.shape[0])
                a[top:top + k] = STORY[:k]
                a[top + k:h] = 255
                stats["paste"] += 1
            else:
                al, dy = fit_band(a, page, final, band_y0)
                top = top_final + dy
                if al > 0.005 and top < h:
                    S_ = np.full((h - top, w, 3), 255, np.float32)
                    k = min(h - top, STORY.shape[0])
                    S_[:k] = STORY[:k]
                    src_rows = np.arange(top, h) - dy
                    B = np.where((src_rows >= band_y0)[:, None, None], final[np.clip(src_rows, 0, h - 1)].astype(np.float32),
                                 page[top:h].astype(np.float32))
                    a[top:h] = np.clip(a[top:h].astype(np.float32) + al * (S_ - B), 0, 255).astype(np.uint8)
                stats["blend"].append((i, round(al, 2), dy))
        enc.stdin.write(np.ascontiguousarray(a).tobytes())
    enc.stdin.close()
    enc.wait()
    if enc.returncode or stats["paste"] == 0:
        raise SystemExit(f"{p}: encode rc={enc.returncode}, {stats}")
    out.replace(p)
    return stats


def reels_from(orig_dir, out_dirs):
    """Rebuild reels from untouched originals in orig_dir into the matching vol folders."""
    for o in sorted(Path(orig_dir).glob("*_reel_9x16.mp4")):
        dst = next(Path(d) / o.name for d in out_dirs if (Path(d) / o.name).exists())
        print("reel", dst, do_reel(dst, o), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "--reels-from":
        reels_from(sys.argv[2], sys.argv[3:])
        sys.exit()
    for d in sys.argv[1:]:
        for p in sorted(Path(d).glob("*.jpg")):
            do_image(p)
            print("img", p)
        for p in sorted(Path(d).glob("*_reel_9x16.mp4")):
            print("reel", p, do_reel(p), flush=True)
