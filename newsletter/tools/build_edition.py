#!/usr/bin/env python3
"""The Rockit Manifest: full edition (A4, multi-page) from edition.json.

    python3 build_edition.py ../issues/<date>/edition.json

Writes into <issue>/edition/:
  edition.html   print-ready A4 document (one .page per sheet), rendered to PDF by render_edition.js
  logo.png       the owner's light-surface logo (brand/rockit-logo.png), cropped to its bounds only
  logo.svg       the owner's vector logo (brand/rockit-logo.svg), frame tightened to the artwork; used on every page
  logo_dark.png  kept for reference only; the owner wants the logo on light backgrounds

Brand rules (brand/BRAND.md, permanent):
  * gold is ALWAYS the logo's own gradient (brand/rockit-logo.svg, "gold-swoosh"), never a flat yellow;
    small text on cream uses the documented fallback #8a6514, small text on navy #DEC163;
  * logo = ONLY the owner's files: rockit-logo on light surfaces, rockit-logo-dark-bg directly on navy.

Editorial rules: every fact carries a source id; sources are listed, numbered, on the last page.
"""
import html
import json
import re
import sys
from pathlib import Path

from PIL import Image

NAVY, MID, CREAM, PAPER, INK, RULE, MUTED = "#16243f", "#080f1f", "#f1eedb", "#faf7ef", "#1b2333", "#e3d8bd", "#5d6577"
GOLD_STOPS = [("#A88329", 0), ("#B18B2D", 8), ("#C09934", 17), ("#CFAC49", 25), ("#DEC163", 33), ("#EDD77E", 42), ("#F7E590", 50),
              ("#ECD57B", 58), ("#DEC161", 67), ("#D0AD48", 75), ("#C29B36", 83), ("#B28C2D", 92), ("#A88228", 100)]
GOLD_GRAD = "linear-gradient(135deg," + ",".join(f"{c} {o}%" for c, o in GOLD_STOPS) + ")"
GOLD_GRAD_H = "linear-gradient(90deg," + ",".join(f"{c} {o}%" for c, o in GOLD_STOPS) + ")"
GOLD_GRAD_V = "linear-gradient(180deg," + ",".join(f"{c} {o}%" for c, o in GOLD_STOPS) + ")"
GOLD_ON_LIGHT = "linear-gradient(135deg,#A88329 0%,#C09934 45%,#A88228 100%)"   # logo stops minus the pale highlight, for text on cream
GOLD_TXT_NAVY, GOLD_TXT_CREAM, GOLD_MID = "#DEC163", "#8a6514", "#C09934"
SPOT_LIGHT, SPOT_DARK = "#3f6db3", "#5c84c6"                                   # validated against the gold mids (dataviz validator)
BAR_LIGHT = [("#A88329", 0), ("#C09934", 45), ("#DEC163", 100)]
UP, DOWN = "#9a3b2e", "#2e6b4a"                                                  # costs-you-more / costs-you-less

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600'
         '&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')


def e(s):
    return html.escape(str(s), quote=True)


def md(s):
    """Tiny inline markup: **bold**, *italic*, [n] source refs are added separately."""
    s = e(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
    return s


def svg_gold(gid, stops=None, x2="1", y2="1"):
    st = stops or GOLD_STOPS
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            + "".join(f'<stop offset="{o}%" stop-color="{c}"/>' for c, o in st) + "</linearGradient>")


CSS = f"""
@page {{ size: A4; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ background:#8b8f99; }}
body {{ font-family: Inter, 'Helvetica Neue', Arial, sans-serif; color:{INK}; -webkit-font-smoothing:antialiased;
        -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
.page {{ width:210mm; height:297mm; position:relative; overflow:hidden; background:{PAPER}; page-break-after:always; break-after:page; }}
@media screen {{ .page {{ margin:10mm auto; box-shadow:0 2px 14px rgba(0,0,0,.25); }} }}
.inner {{ position:absolute; left:15mm; right:15mm; top:21mm; bottom:17mm; }}
.runhead {{ position:absolute; left:15mm; right:15mm; top:9mm; height:8mm; display:flex; align-items:flex-end; justify-content:space-between;
            font:500 7.2pt 'IBM Plex Mono', monospace; letter-spacing:.16em; text-transform:uppercase; color:{MUTED}; padding-bottom:2mm; }}
.runhead::after {{ content:""; position:absolute; left:0; right:0; bottom:0; height:.7pt; background:{GOLD_GRAD_H}; }}
.runhead .sec {{ color:{GOLD_TXT_CREAM}; font-weight:600; }}
.foot {{ position:absolute; left:15mm; right:15mm; bottom:7mm; height:7mm; display:flex; align-items:center; justify-content:space-between;
         font:500 7pt 'IBM Plex Mono', monospace; letter-spacing:.12em; color:{MUTED}; text-transform:uppercase; border-top:.5pt solid {RULE}; padding-top:1.5mm; }}
.foot img {{ height:7.4mm; display:block; }}
.foot .pn {{ font:600 9pt 'IBM Plex Mono', monospace; color:{INK}; letter-spacing:.05em; }}

.kicker {{ font:600 7.6pt 'IBM Plex Mono', monospace; letter-spacing:.2em; text-transform:uppercase; color:{GOLD_TXT_CREAM}; margin-bottom:2.2mm; }}
.sechead {{ display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:4mm; padding-bottom:2.5mm; border-bottom:1.6pt solid {INK}; }}
.sechead h1 {{ font:600 27pt/1 'Cormorant Garamond', Georgia, serif; letter-spacing:-.01em; }}
.sechead .no {{ font:600 8pt 'IBM Plex Mono', monospace; letter-spacing:.18em; color:{MUTED}; text-transform:uppercase; text-align:right; }}
h2.lead {{ font:600 21pt/1.08 'Cormorant Garamond', Georgia, serif; margin-bottom:2.5mm; }}
h2.mid {{ font:600 15pt/1.12 'Cormorant Garamond', Georgia, serif; margin-bottom:1.6mm; }}
h3 {{ font:700 9.6pt/1.25 Inter, Arial, sans-serif; margin-bottom:1.2mm; color:{INK}; }}
.deck {{ font:italic 500 12.4pt/1.35 'Cormorant Garamond', Georgia, serif; color:#3a4152; margin-bottom:3.4mm; }}
p {{ font-size:8.3pt; line-height:1.47; margin-bottom:2.2mm; hyphens:auto; text-align:left; }}
p.drop::first-letter {{ float:left; font:600 30pt/0.82 'Cormorant Garamond', Georgia, serif; padding:1.2mm 1.6mm 0 0;
        background:{GOLD_ON_LIGHT}; -webkit-background-clip:text; background-clip:text; color:transparent; }}
sup.r {{ font:600 5.6pt 'IBM Plex Mono', monospace; color:{GOLD_TXT_CREAM}; vertical-align:super; margin-left:.3mm; }}
.cols2 {{ column-count:2; column-gap:7mm; column-rule:.5pt solid {RULE}; }}
.cols3 {{ column-count:3; column-gap:6mm; column-rule:.5pt solid {RULE}; }}
.cols2 > *, .cols3 > * {{ break-inside:avoid; }}
.brief {{ margin-bottom:3.4mm; padding-bottom:3mm; border-bottom:.5pt solid {RULE}; break-inside:avoid; }}
.brief:last-child {{ border-bottom:0; }}
.brief .tag {{ font:600 6.6pt 'IBM Plex Mono', monospace; letter-spacing:.16em; text-transform:uppercase; color:{GOLD_TXT_CREAM}; margin-bottom:1mm; }}
.why {{ font-size:8pt; line-height:1.45; color:{INK}; background:#f1e9d4; border-left:2pt solid {GOLD_MID}; border-image:{GOLD_GRAD_V} 1;
        padding:1.6mm 2.4mm; margin-top:1.4mm; }}
.why b {{ font:700 6.6pt 'IBM Plex Mono', monospace; letter-spacing:.14em; text-transform:uppercase; color:{GOLD_TXT_CREAM}; margin-right:1.2mm; }}
.box {{ background:{NAVY}; color:{CREAM}; padding:4.5mm 5mm; break-inside:avoid; }}
.box .kicker {{ color:{GOLD_TXT_NAVY}; }}
.box h3 {{ color:{CREAM}; }}
.box p {{ color:#d6d2c2; }}
.panel {{ background:#f3ecd9; padding:4mm 4.5mm; break-inside:avoid; }}
.gold-rule {{ height:1.2pt; background:{GOLD_GRAD_H}; margin:3mm 0; }}
.chart {{ break-inside:avoid; margin:1mm 0 3mm; }}
.chart .ct {{ font:600 12pt/1.15 'Cormorant Garamond', Georgia, serif; margin-bottom:.8mm; }}
.chart .cs {{ font:500 6.8pt 'IBM Plex Mono', monospace; letter-spacing:.12em; text-transform:uppercase; color:{MUTED}; margin-bottom:2mm; }}
.chart .cn {{ font-size:6.8pt; color:{MUTED}; line-height:1.4; margin-top:1.5mm; }}
table.t {{ width:100%; border-collapse:collapse; font-size:7.8pt; line-height:1.35; }}
table.t th {{ font:600 6.6pt 'IBM Plex Mono', monospace; letter-spacing:.12em; text-transform:uppercase; color:{MUTED}; text-align:left;
              padding:1.4mm 2mm 1.4mm 0; border-bottom:1pt solid {INK}; vertical-align:bottom; }}
table.t td {{ padding:1.6mm 2mm 1.6mm 0; border-bottom:.5pt solid {RULE}; vertical-align:top; }}
table.t td.num {{ font:600 8pt 'IBM Plex Mono', monospace; white-space:nowrap; }}
.up {{ color:{UP}; }} .down {{ color:{DOWN}; }} .flat {{ color:{MUTED}; }}
.tiles {{ display:grid; gap:0; }}
.tile {{ padding:2.1mm 3mm 2.1mm 0; border-top:1.4pt solid {INK}; }}
.tile .v {{ font:700 17.5pt/1 'Cormorant Garamond', Georgia, serif; }}
.tile .l {{ font-size:7pt; line-height:1.3; margin-top:1.2mm; }}
.tile .d {{ font:600 6.8pt 'IBM Plex Mono', monospace; margin-top:1mm; }}
.tile .s {{ font:500 6pt 'IBM Plex Mono', monospace; color:{MUTED}; margin-top:.8mm; letter-spacing:.04em; }}
ul.ticks {{ list-style:none; }}
ul.ticks li {{ font-size:8.2pt; line-height:1.42; padding:1.05mm 0 1.05mm 5mm; position:relative; border-bottom:.5pt solid {RULE}; }}
ul.ticks li::before {{ content:"→"; position:absolute; left:0; font-weight:700; color:{GOLD_TXT_CREAM}; }}
.box ul.ticks li {{ border-color:#2c3b5c; color:#e7e3d3; }}
.box ul.ticks li::before {{ color:{GOLD_TXT_NAVY}; }}
.src-list {{ column-count:3; column-gap:5mm; column-rule:.5pt solid {RULE}; font-size:5.9pt; line-height:1.32; color:#3a4152; }}
.src-list div {{ break-inside:avoid; margin-bottom:.9mm; padding-left:4.2mm; text-indent:-4.2mm; overflow-wrap:anywhere; }}
.src-list b {{ font:600 5.9pt 'IBM Plex Mono', monospace; color:{GOLD_TXT_CREAM}; display:inline-block; width:4.2mm; text-indent:0; }}
.srcline {{ font-size:6.6pt; color:{MUTED}; margin-top:1.5mm; }}
.gt {{ background:{GOLD_GRAD}; -webkit-background-clip:text; background-clip:text; color:transparent; }}
.gtl {{ background:{GOLD_ON_LIGHT}; -webkit-background-clip:text; background-clip:text; color:transparent; }}
"""


class Sources:
    def __init__(self, src):
        self.src = src  # id -> {name, title, url, date}
        self.order = []

    def ref(self, ids):
        if not ids:
            return ""
        nums = []
        for i in ids:
            if i not in self.src:
                raise SystemExit(f"STOP: unknown source id {i!r}")
            if i not in self.order:
                self.order.append(i)
            nums.append(self.order.index(i) + 1)
        return f'<sup class="r">{",".join(str(n) for n in sorted(set(nums)))}</sup>'


def para(text, S, src=None, cls=""):
    return f'<p class="{cls}">{md(text)}{S.ref(src)}</p>'


def why(text):
    return f'<div class="why"><b>Why it matters</b>{md(text)}</div>'


def brief(b, S):
    tag = f'<div class="tag">{e(b["tag"])}</div>' if b.get("tag") else ""
    body = "".join(para(t, S, b.get("src") if i == len(b["text"]) - 1 else None) for i, t in enumerate(b["text"]))
    w = why(b["why"]) if b.get("why") else ""
    return f'<div class="brief">{tag}<h3>{md(b["head"])}</h3>{body}{w}</div>'


def hbar_svg(rows, width_mm, vmax, fmt, kinds=None):
    """Horizontal bars, direct labels. rows: [(label, value, kind)] kind in spot|gold. Units: CSS px at 96dpi (1mm=3.78px)."""
    W = width_mm * 3.7795
    lab_h, bar_h, gap = 13, 10, 9
    plot = W - 56
    y, out = 0, []
    for row in rows:
        label, val, kind = row[0], row[1], row[2]
        shown = row[3] if len(row) > 3 else fmt(val)
        w = max(3, plot * val / vmax)
        fill = "url(#gb)" if kind == "gold" else SPOT_LIGHT
        out.append(f'<text x="0" y="{y+10}" font-family="Inter" font-size="9.2" fill="{INK}">{e(label)}</text>')
        out.append(f'<rect x="0" y="{y+lab_h}" width="{w:.1f}" height="{bar_h}" rx="2" fill="{fill}"/>')
        out.append(f'<text x="{w+5:.1f}" y="{y+lab_h+bar_h-1.5}" font-family="Inter" font-weight="700" font-size="9.6" fill="{INK}">{e(shown)}</text>')
        y += lab_h + bar_h + gap
    H = y - gap + 2
    return (f'<svg width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible;display:block">'
            f'<defs>{svg_gold("gb", BAR_LIGHT, "1", "0")}</defs>{"".join(out)}</svg>')


def vbar_svg(series, width_mm, height_mm, vmin, vmax, fmt, kind="spot", ticks=None):
    """Vertical bars/columns with value labels; series: [(label, value)]."""
    W, H = width_mm * 3.7795, height_mm * 3.7795
    n = len(series)
    top, bot = 14, 18
    ph = H - top - bot
    bw = W / n * 0.62
    out = []
    for i, (lab, v) in enumerate(series):
        x = W / n * i + (W / n - bw) / 2
        h = max(2, ph * (v - vmin) / (vmax - vmin))
        fill = "url(#gv)" if kind == "gold" else SPOT_LIGHT
        out.append(f'<rect x="{x:.1f}" y="{top+ph-h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="1.5" fill="{fill}"/>')
        out.append(f'<text x="{x+bw/2:.1f}" y="{top+ph-h-3:.1f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="8.6" fill="{INK}">{e(fmt(v))}</text>')
        out.append(f'<text x="{x+bw/2:.1f}" y="{H-5:.1f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="7.4" fill="{MUTED}">{e(lab)}</text>')
    out.append(f'<line x1="0" y1="{top+ph:.1f}" x2="{W:.1f}" y2="{top+ph:.1f}" stroke="{INK}" stroke-width=".8"/>')
    return (f'<svg width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" style="display:block">'
            f'<defs>{svg_gold("gv", BAR_LIGHT, "0", "1")}</defs>{"".join(out)}</svg>')


def chart(c, S):
    if c["type"] == "hbar":
        svg = hbar_svg([tuple(r) for r in c["rows"]], c.get("width_mm", 80), c["max"], lambda v: c.get("prefix", "") + f"{v:,.{c.get('dp', 0)}f}" + c.get("suffix", ""))
    elif c["type"] == "vbar":
        svg = vbar_svg([tuple(r) for r in c["rows"]], c.get("width_mm", 80), c.get("height_mm", 40), c.get("min", 0), c["max"],
                       lambda v: c.get("prefix", "") + f"{v:,.{c.get('dp', 0)}f}" + c.get("suffix", ""), c.get("kind", "spot"))
    else:
        svg = c["svg"]
    leg = ""
    if c.get("legend"):
        sw = {"spot": SPOT_LIGHT, "gold": GOLD_ON_LIGHT}
        leg = '<div style="font-size:6.8pt;color:%s;margin-bottom:2mm">%s</div>' % (MUTED, "".join(
            f'<span style="margin-right:4mm;display:inline-flex;align-items:center"><i style="display:inline-block;width:2.6mm;height:2.6mm;border-radius:.5mm;margin-right:1.4mm;background:{sw[k]}"></i>{e(t)}</span>'
            for k, t in c["legend"]))
    return (f'<div class="chart"><div class="cs">{e(c.get("sub", ""))}</div><div class="ct">{md(c["title"])}</div>{leg}{svg}'
            f'<div class="cn">{md(c.get("note", ""))}{S.ref(c.get("src"))}</div></div>')


def table(t, S):
    head = "".join(f"<th>{e(h)}</th>" for h in t["head"])
    rows = []
    for r in t["rows"]:
        cells = []
        for j, c in enumerate(r["cells"]):
            cls = t.get("num_cols", [])
            klass = "num" if j in cls else ""
            dirc = r.get("dir", {}).get(str(j), "")
            cells.append(f'<td class="{klass} {dirc}">{md(c)}{S.ref(r.get("src")) if j == len(r["cells"]) - 1 else ""}</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    cap = f'<div class="cs" style="font:500 6.8pt IBM Plex Mono,monospace;letter-spacing:.12em;text-transform:uppercase;color:{MUTED};margin-bottom:1.5mm">{e(t["caption"])}</div>' if t.get("caption") else ""
    note = f'<div style="font-size:6.6pt;color:{MUTED};margin-top:1.4mm;line-height:1.4">{md(t["note"])}</div>' if t.get("note") else ""
    return f'<div style="break-inside:avoid;margin-bottom:3mm">{cap}<table class="t"><tr>{head}</tr>{"".join(rows)}</table>{note}</div>'


def tiles(ts, S, cols=4):
    out = []
    for t in ts:
        d = f'<div class="d {t.get("dir", "flat")}">{e(t["delta"])}</div>' if t.get("delta") else ""
        out.append(f'<div class="tile"><div class="v">{e(t["value"])}</div><div class="l">{md(t["label"])}{S.ref(t.get("src"))}</div>{d}'
                   f'<div class="s">{e(t.get("asof", ""))}</div></div>')
    return f'<div class="tiles" style="grid-template-columns:repeat({cols},1fr);column-gap:4mm">{"".join(out)}</div>'


def block(b, S):
    k = b["k"]
    if k == "p":
        return para(b["text"], S, b.get("src"), b.get("cls", ""))
    if k == "lead":
        body = "".join(para(t, S, b.get("src") if i == len(b["text"]) - 1 else None, "drop" if i == 0 and b.get("drop", True) else "") for i, t in enumerate(b["text"]))
        kick = f'<div class="kicker">{e(b["kicker"])}</div>' if b.get("kicker") else ""
        deck = f'<div class="deck">{md(b["deck"])}</div>' if b.get("deck") else ""
        w = why(b["why"]) if b.get("why") else ""
        return f'<div>{kick}<h2 class="lead">{md(b["head"])}</h2>{deck}{body}{w}</div>'
    if k == "brief":
        return brief(b, S)
    if k == "chart":
        return chart(b, S)
    if k == "table":
        return table(b, S)
    if k == "tiles":
        return tiles(b["items"], S, b.get("cols", 4))
    if k == "box":
        inner = "".join(block(x, S) for x in b["blocks"])
        kick = f'<div class="kicker">{e(b["kicker"])}</div>' if b.get("kicker") else ""
        title = f'<h2 class="mid" style="color:{CREAM}">{md(b["title"])}</h2>' if b.get("title") else ""
        return f'<div class="box" style="{b.get("style", "")}">{kick}{title}{inner}</div>'
    if k == "panel":
        inner = "".join(block(x, S) for x in b["blocks"])
        kick = f'<div class="kicker">{e(b["kicker"])}</div>' if b.get("kicker") else ""
        title = f'<h2 class="mid">{md(b["title"])}</h2>' if b.get("title") else ""
        return f'<div class="panel" style="{b.get("style", "")}">{kick}{title}{inner}</div>'
    if k == "ticks":
        return '<ul class="ticks">' + "".join(f"<li>{md(t)}{S.ref(s) if (s := (b.get('srcs') or [None]*len(b['items']))[i]) else ''}</li>" for i, t in enumerate(b["items"])) + "</ul>"
    if k == "h":
        return f'<h2 class="mid" style="{b.get("style", "")}">{md(b["text"])}</h2>'
    if k == "kicker":
        return f'<div class="kicker">{e(b["text"])}</div>'
    if k == "rule":
        return '<div class="gold-rule"></div>'
    if k == "grid":
        colsdef = b.get("cols", "1fr 1fr")
        inner = "".join(f'<div style="min-width:0">{"".join(block(x, S) for x in col)}</div>' for col in b["columns"])
        return f'<div style="display:grid;grid-template-columns:{colsdef};column-gap:{b.get("gap", "7mm")};{b.get("style", "")}">{inner}</div>'
    if k == "flow":
        inner = "".join(block(x, S) for x in b["blocks"])
        return f'<div class="cols{b.get("n", 2)}" style="{b.get("style", "")}">{inner}</div>'
    if k == "html":
        return b["html"]
    if k == "space":
        return f'<div style="height:{b["mm"]}mm"></div>'
    raise SystemExit(f"unknown block kind {k}")


def runhead(meta, section):
    return f'<div class="runhead"><span>The Rockit Manifest · Voyage {e(meta["voyage"])} · {e(meta["date_long"])}</span><span class="sec">{e(section)}</span></div>'


def foot(n):
    return (f'<div class="foot"><img src="logo.svg" alt="Rock it Transport Services">'
            f'<span>rockit-transport.com · inquiry@rockit.com.eg · +20 2 2690 7601</span><span class="pn">{n:02d}</span></div>')


STATE_COL = {"open": "#2e6b4a", "partial": "#a5561b", "restricted": "#9a3b2e"}   # readable on paper (WCAG AA for 7pt bold caps)


def status_board(c, S):
    if not c.get("status"):
        return ""
    rows = "".join(
        f'<div style="display:grid;grid-template-columns:36mm 30mm 1fr;column-gap:4mm;align-items:baseline;padding:2mm 0;border-bottom:.5pt solid {RULE}">'
        f'<span style="font:600 11pt Cormorant Garamond,serif;color:{INK}">{e(x["name"])}</span>'
        f'<span style="font:600 6.8pt IBM Plex Mono,monospace;letter-spacing:.12em;text-transform:uppercase;color:{STATE_COL[x["state"]]}">'
        f'<i style="display:inline-block;width:2.2mm;height:2.2mm;border-radius:50%;background:{STATE_COL[x["state"]]};margin-right:1.6mm;vertical-align:.1mm"></i>{e(x["label"])}</span>'
        f'<span style="font-size:7.8pt;line-height:1.4;color:#3a4152">{md(x["note"])}{S.ref(x.get("src"))}</span></div>'
        for x in c["status"])
    return (f'<div><div style="font:600 7.6pt IBM Plex Mono,monospace;letter-spacing:.2em;text-transform:uppercase;color:{GOLD_TXT_CREAM};margin-bottom:1mm">'
            f'Chokepoint status · {e(c.get("status_asof", ""))}</div>{rows}</div>')


def cover(c, meta, S):
    """Light cover: the owner's original logo on paper, full colour, vector."""
    contents = "".join(f'<div style="display:flex;gap:3mm;padding:1.2mm 0;border-bottom:.5pt solid {RULE};align-items:baseline">'
                       f'<span style="font:600 7.4pt IBM Plex Mono,monospace;color:{GOLD_TXT_CREAM};width:6mm">{e(x["p"])}</span>'
                       f'<span style="font-size:7.9pt;color:{INK};flex:1;line-height:1.3"><b>{e(x["sec"])}</b><span style="color:{MUTED}"> · {e(x["what"])}</span></span></div>' for x in c["contents"])
    nums = "".join(f'<div style="padding:2.4mm 3mm 0 0;border-top:1.4pt solid {INK}"><div style="font:700 20pt/1 Cormorant Garamond,serif;color:{NAVY}">{e(t["value"])}</div>'
                   f'<div style="font-size:7pt;color:#3a4152;margin-top:1mm;line-height:1.3">{md(t["label"])}{S.ref(t.get("src"))}</div></div>' for t in c["numbers"])
    kick = lambda t: f'<div style="font:600 7.6pt IBM Plex Mono,monospace;letter-spacing:.2em;text-transform:uppercase;color:{GOLD_TXT_CREAM};margin-bottom:2.5mm">{e(t)}</div>'
    return f'''<section class="page" style="background:#ffffff">
  <div style="position:absolute;left:0;right:0;top:0;height:3.2mm;background:{GOLD_GRAD_H}"></div>
  <div style="position:absolute;left:15mm;right:15mm;top:13mm;bottom:9mm;display:flex;flex-direction:column">
    <div style="display:flex;justify-content:space-between;align-items:center">
      <img src="logo.svg" style="height:25mm;display:block" alt="Rock it Transport Services">
      <div style="text-align:right;font:500 7.4pt IBM Plex Mono,monospace;letter-spacing:.16em;text-transform:uppercase;color:{MUTED};line-height:1.7">
        Voyage {e(meta["voyage"])}<br>{e(meta["date_long"])}<br>{e(meta["pages_label"])}</div>
    </div>
    <div style="margin-top:8mm">
      <div style="height:1.4pt;background:{GOLD_GRAD_H};margin-bottom:4mm"></div>
      <div style="font:600 8pt IBM Plex Mono,monospace;letter-spacing:.3em;text-transform:uppercase;color:{GOLD_TXT_CREAM}">The weekly freight &amp; trade review from Cairo</div>
      <div style="font:600 54pt/0.95 Cormorant Garamond,serif;letter-spacing:-.01em;margin-top:2.5mm;padding-bottom:2mm;color:{NAVY}">The Rockit Manifest</div>
      <div style="font:italic 500 12.5pt Cormorant Garamond,serif;color:#3a4152;margin-top:.5mm">What moved. What it means. What to do.</div>
      <div style="height:1.4pt;background:{GOLD_GRAD_H};margin-top:4mm"></div>
    </div>
    <div style="margin-top:6mm;display:grid;grid-template-columns:1.3fr 1fr;column-gap:9mm">
      <div>
        {kick(c["kicker"])}
        <div style="font:600 27pt/1.03 Cormorant Garamond,serif;color:{INK};margin-bottom:3.5mm">{md(c["headline"])}</div>
        <div style="font:italic 500 11.6pt/1.4 Cormorant Garamond,serif;color:#3a4152;margin-bottom:3.5mm">{md(c["deck"])}</div>
        <div style="font-size:8.3pt;line-height:1.55;color:{INK}">{md(c["standfirst"])}{S.ref(c.get("src"))}</div>
      </div>
      <div>{kick("Inside this issue")}{contents}</div>
    </div>
    <div style="margin-top:5mm">{status_board(c, S)}</div>
    <div style="margin-top:auto">
      {kick("The week in numbers")}
      <div style="display:grid;grid-template-columns:repeat({len(c["numbers"])},1fr);column-gap:4mm">{nums}</div>
      <div style="display:flex;justify-content:space-between;margin-top:5mm;padding-top:2mm;border-top:.5pt solid {RULE};font:500 6.8pt IBM Plex Mono,monospace;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}">
        <span>Cairo · Alexandria · Sokhna · Port Said · Damietta</span><span>Every figure sourced</span></div>
    </div>
  </div>
</section>'''


def sources_items(S, data_sources):
    items = []
    for n, sid in enumerate(S.order, 1):
        s = data_sources[sid]
        short = re.sub(r"^https?://(www\.)?", "", s["url"])
        items.append(f'<div><b>{n}</b>{e(s["name"])}, “{e(s["title"])}”, {e(s["date"])}. <span style="color:{MUTED}">{e(short)}</span></div>')
    return items


def back_cover(b, meta):
    """Light back cover: the owner's original logo on paper, full colour, vector."""
    cols = "".join(f'<div><div style="font:600 7.6pt IBM Plex Mono,monospace;letter-spacing:.2em;text-transform:uppercase;color:{GOLD_TXT_CREAM};margin-bottom:2mm">{e(c["h"])}</div>'
                   + "".join(f'<div style="font-size:8.6pt;line-height:1.5;color:{INK};padding:1.2mm 0;border-bottom:.5pt solid {RULE}">{md(x)}</div>' for x in c["items"]) + "</div>"
                   for c in b["columns"])
    nxt = "".join(f'<div style="font:500 12pt/1.35 Cormorant Garamond,serif;color:{INK};padding:1.3mm 0;border-bottom:.5pt solid {RULE}"><span style="color:{GOLD_TXT_CREAM};font:600 8pt IBM Plex Mono,monospace;margin-right:3mm">{i:02d}</span>{md(x)}</div>'
                  for i, x in enumerate(b.get("next", []), 1))
    return f'''<section class="page" style="background:#ffffff">
  <div style="position:absolute;left:0;right:0;bottom:0;height:3.2mm;background:{GOLD_GRAD_H}"></div>
  <div style="position:absolute;left:15mm;right:15mm;top:20mm">
    <img src="logo.svg" style="height:34mm;display:block" alt="Rock it Transport Services">
    <div style="height:1.4pt;background:{GOLD_GRAD_H};margin:9mm 0 7mm"></div>
    <div style="font:600 32pt/1.05 Cormorant Garamond,serif;color:{NAVY};padding-bottom:1mm">{md(b["headline"])}</div>
    <div style="font:italic 500 13pt/1.45 Cormorant Garamond,serif;color:#3a4152;margin-top:4mm;max-width:150mm">{md(b["deck"])}</div>
  </div>
  <div style="position:absolute;left:15mm;right:15mm;top:122mm;display:grid;grid-template-columns:repeat({len(b["columns"])},1fr);column-gap:8mm">{cols}</div>
  <div style="position:absolute;left:15mm;right:15mm;top:178mm;background:#f6f1e4;padding:5mm 6mm;border-left:2pt solid {GOLD_MID};border-image:{GOLD_GRAD_V} 1">
    <div style="font:600 7.6pt IBM Plex Mono,monospace;letter-spacing:.2em;text-transform:uppercase;color:{GOLD_TXT_CREAM};margin-bottom:2.5mm">Next Monday in The Rockit Manifest</div>
    {nxt}
  </div>
  <div style="position:absolute;left:15mm;right:15mm;bottom:30mm">
    <div style="font:600 7.6pt IBM Plex Mono,monospace;letter-spacing:.2em;text-transform:uppercase;color:{GOLD_TXT_CREAM};margin-bottom:3mm">{e(b["cta_kicker"])}</div>
    <div style="font:600 20pt/1.2 Cormorant Garamond,serif;color:{NAVY}">{md(b["cta"])}</div>
  </div>
  <div style="position:absolute;left:15mm;right:15mm;bottom:12mm;display:flex;justify-content:space-between;align-items:baseline;padding-top:3mm;border-top:.5pt solid {RULE};font:500 7pt IBM Plex Mono,monospace;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}">
    <span>rockit-transport.com · inquiry@rockit.com.eg · +20 2 2690 7601</span><span class="gtl" style="font:italic 600 13pt Cormorant Garamond,serif;letter-spacing:.02em;text-transform:none">Means what it says.</span></div>
</section>'''


def build(ed_path):
    ed_path = Path(ed_path).resolve()
    ed = json.loads(ed_path.read_text())
    out = ed_path.parent / "edition"
    out.mkdir(exist_ok=True)
    brand = Path(__file__).resolve().parents[2] / "brand"
    for src_name, out_name in (("rockit-logo.png", "logo.png"), ("rockit-logo-dark-bg.png", "logo_dark.png")):
        src = brand / src_name
        if not src.exists():
            raise SystemExit(f"STOP: owner logo file brand/{src_name} is missing. Do not substitute another logo; ask the owner.")
        im = Image.open(src).convert("RGBA")
        im.crop(im.getbbox()).save(out / out_name)
    svg_src = brand / "rockit-logo.svg"
    if not svg_src.exists():
        raise SystemExit("STOP: owner logo file brand/rockit-logo.svg is missing. Do not substitute another logo; ask the owner.")
    # Vector master for print. Only the viewBox (the frame) is tightened to the artwork's bounds, measured on the owner's
    # own rasterisation; every path, gradient and colour stays exactly as supplied.
    bbox = Image.open(brand / "rockit-logo.png").getbbox()          # (47, 40, 2502, 1090) on a 2550x1132 canvas
    svg = svg_src.read_text()
    vb = re.search(r'viewBox="([\d.\- ]+)"', svg).group(1).split()
    x0, y0 = float(vb[0]) + bbox[0], float(vb[1]) + bbox[1]
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    svg = svg.replace(f'viewBox="{" ".join(vb)}"', f'viewBox="{x0:g} {y0:g} {w} {h}"', 1)
    svg = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", svg, count=1)
    svg = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", svg, count=1)
    (out / "logo.svg").write_text(svg)
    S = Sources(ed["sources"])
    meta = ed["meta"]
    pages = [cover(ed["cover"], meta, S)]
    for i, pg in enumerate(ed["pages"], start=2):
        if pg.get("sources_page"):
            continue
        body = "".join(block(b, S) for b in pg["blocks"])
        sh = (f'<div class="sechead"><h1>{md(pg["title"])}</h1><div class="no">{e(pg.get("label", ""))}</div></div>' if pg.get("title") else "")
        pages.append(f'<section class="page">{runhead(meta, pg["section"])}<div class="inner" data-page="{i}">{sh}{body}</div>{foot(i)}</section>')
    # sources pages: the numbered list (built after all refs are known), split over two pages, then the back cover
    last = next((p for p in ed["pages"] if p.get("sources_page")), None)
    if last:
        items = sources_items(S, ed["sources"])
        cut = last.get("split", (len(items) + 1) // 2)
        for part, chunk in enumerate((items[:cut], items[cut:])):
            i = len(pages) + 1
            intro = "".join(block(b, S) for b in last["blocks"]) if part == 0 else ""
            title = last["title"] if part == 0 else last["title"] + " (continued)"
            tail = (f'<div style="font-size:6.4pt;color:{MUTED};line-height:1.45;margin-top:3mm;border-top:.5pt solid {RULE};padding-top:2mm">{md(ed["disclaimer"])}</div>'
                    if part == 1 else "")
            sh = f'<div class="sechead"><h1>{md(title)}</h1><div class="no">{e(last.get("label", ""))}</div></div>'
            pages.append(f'<section class="page">{runhead(meta, last["section"])}<div class="inner" data-page="{i}">{sh}{intro}'
                         f'<div class="src-list">{"".join(chunk)}</div>{tail}</div>{foot(i)}</section>')
    if ed.get("back"):
        pages.append(back_cover(ed["back"], meta))
    unused = set(ed["sources"]) - set(S.order)
    if unused:
        print("note: sources defined but not cited:", ", ".join(sorted(unused)))
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(meta["title"])}</title>{FONTS}<style>{CSS}</style></head>'
           f'<body>{"".join(pages)}</body></html>')
    (out / "edition.html").write_text(doc)
    (out / "sources_order.json").write_text(json.dumps(S.order))
    print(f"wrote {out/'edition.html'} · {len(pages)} pages · {len(S.order)} sources cited")


if __name__ == "__main__":
    build(sys.argv[1])
