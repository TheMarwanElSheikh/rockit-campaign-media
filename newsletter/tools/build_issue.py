#!/usr/bin/env python3
"""The Rockit Manifest: build every channel of one issue from content.json.

    python3 build_issue.py ../issues/<date>/content.json

Writes into the issue folder:
  visuals/*.html   charts, route map, ACID steps and stamp (light, 600 CSS px), plus slide_*.html (1080x1350, dark)
                   and cover_4x3.html; render_covers.js turns these into PNG/JPG
  email.html       email-safe HTML (600px tables, inline styles; images referenced from IMG_BASE)
  ricos.json       Wix Blog rich content. Image nodes carry "@key" ids that the stager swaps for Wix media ids
  social.json      per-channel post copy

Chart palette, checked with the dataviz validator (all six checks pass):
  light surface #faf7ef: spot #3f6db3, filed #b07f2c
  dark surface  #16243f: spot #5c84c6, filed #b98a35
Every mark is also labelled directly, so colour never carries meaning alone.
"""
import html
import json
import re
import sys
from pathlib import Path

NAVY, MID, GOLD, CREAM, PAPER, INK, RULE, MUTED = "#16243f", "#080f1f", "#d5ae69", "#f1eedb", "#faf7ef", "#1b2333", "#e6dcc4", "#5d6577"
GOLD_INK = "#9a6d22"          # gold dark enough for text on paper (contrast ≥ 4.5:1)
LIGHT = {"bg": PAPER, "ink": INK, "muted": MUTED, "rule": RULE, "spot": "#3f6db3", "filed": "#b07f2c", "accent": GOLD_INK}
DARK = {"bg": NAVY, "ink": CREAM, "muted": "#a9b1c2", "rule": "#2c3b5c", "spot": "#5c84c6", "filed": "#b98a35", "accent": GOLD}
SERIF = "'Cormorant Garamond', Georgia, 'Times New Roman', serif"
SANS = "Inter, 'Helvetica Neue', Arial, sans-serif"
MONO = "'IBM Plex Mono', 'Courier New', Courier, monospace"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'


def e(s):
    return html.escape(str(s), quote=True)


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def page(w, h, body, bg, extra_css=""):
    hh = f"height:{h}px;" if h else ""
    return (f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>*{{margin:0;padding:0;box-sizing:border-box}}'
            f'body{{width:{w}px;{hh}background:{bg};font-family:{SANS};-webkit-font-smoothing:antialiased;overflow:hidden}}{extra_css}</style></head>'
            f'<body>{body}</body></html>')


# ------------------------------------------------------------------ charts (SVG)
def bar_chart(rows, t, width, title, subtitle, legend, unit_max, fmt, note=None, scale=1.0, annot=None):
    """Horizontal bars with direct labels. rows: [(label, value, kind)], kind is 'spot' or 'filed'."""
    s = scale
    pad_l, pad_r = 0, 70 * s
    label_h = 18 * s
    bar_h = 14 * s
    row_h = label_h + bar_h + 16 * s
    top = 0
    plot_w = width - pad_l - pad_r
    out = []
    y = top
    for label, val, kind in rows:
        w = max(4 * s, plot_w * val / unit_max)
        col = t[kind]
        out.append(f'<text x="0" y="{y + 13*s}" font-family="Inter" font-size="{13*s}" fill="{t["ink"]}">{e(label)}</text>')
        out.append(f'<rect x="0" y="{y + label_h}" width="{w}" height="{bar_h}" rx="{3*s}" fill="{col}"/>')
        out.append(f'<text x="{w + 8*s}" y="{y + label_h + bar_h - 2*s}" font-family="Inter" font-weight="700" font-size="{14*s}" fill="{t["ink"]}">{e(fmt(val))}</text>')
        y += row_h
    svg_h = y
    if annot:
        out.append(annot(plot_w, row_h, label_h, bar_h, s))
    svg = f'<svg width="{width}" height="{svg_h}" viewBox="0 0 {width} {svg_h}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">{"".join(out)}</svg>'
    leg = "".join(f'<span style="display:inline-flex;align-items:center;margin-right:{18*s}px"><i style="display:inline-block;width:{12*s}px;height:{12*s}px;border-radius:{2*s}px;background:{t[k]};margin-right:{7*s}px"></i>{e(n)}</span>' for k, n in legend)
    return (f'<div style="font-family:{MONO};font-size:{11*s}px;letter-spacing:{2*s}px;text-transform:uppercase;color:{t["accent"]};margin-bottom:{6*s}px">{e(subtitle)}</div>'
            f'<div style="font-family:{SERIF};font-weight:600;font-size:{26*s}px;line-height:1.1;color:{t["ink"]};margin-bottom:{12*s}px">{e(title)}</div>'
            f'<div style="font-size:{12*s}px;color:{t["muted"]};margin-bottom:{18*s}px">{leg}</div>{svg}'
            + (f'<div style="font-size:{11*s}px;color:{t["muted"]};margin-top:{14*s}px;line-height:1.5">{note}</div>' if note else ""))


def gap_chart(t, width, scale=1.0):
    rows = [("Drewry WCI · Shanghai → Genoa · 12 Nov", 4168, "spot"),
            ("Freightos FBX13 · Asia → Med · 10 Nov", 4300, "spot"),
            ("Xeneta · Far East → Med · 13 Nov", 4666, "spot"),
            ("MSC FAK · Far East → East Med · from 1 Dec", 6500, "filed")]

    def annot(plot_w, row_h, label_h, bar_h, s):
        x_spot = plot_w * 4666 / 7000
        x_fak = plot_w * 6500 / 7000
        y = 3 * row_h + label_h + bar_h + 10 * s
        c = t["accent"]
        return (f'<line x1="{x_spot}" y1="{2*row_h + label_h}" x2="{x_spot}" y2="{y}" stroke="{c}" stroke-width="{1.5*s}" stroke-dasharray="{3*s} {3*s}"/>'
                f'<line x1="{x_spot}" y1="{y}" x2="{x_fak}" y2="{y}" stroke="{c}" stroke-width="{1.5*s}"/>'
                f'<line x1="{x_fak}" y1="{y-5*s}" x2="{x_fak}" y2="{y+5*s}" stroke="{c}" stroke-width="{1.5*s}"/>'
                f'<line x1="{x_spot}" y1="{y-5*s}" x2="{x_spot}" y2="{y+5*s}" stroke="{c}" stroke-width="{1.5*s}"/>'
                f'<text x="{(x_spot+x_fak)/2}" y="{y + 18*s}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{13*s}" fill="{c}">+$1,834 above the highest spot reading</text>')
    return bar_chart(rows, t, width, "What the index says vs. what the tariff says", "US$ per 40ft · Asia → Mediterranean",
                     [("spot", "Spot index (market average)"), ("filed", "Filed tariff (published FAK)")], 7000, lambda v: f"${v:,.0f}",
                     note="Spot indices are weekly market averages. The FAK is MSC's published base tariff, port to port; your quote may differ. "
                          "Sources: Drewry, Freightos, Xeneta, Container News.", scale=scale, annot=annot)


def rebate_chart(t, width, scale=1.0):
    rows = [("Sea & land freight → Africa, Latin America, SE Asia, Australia, Russia", 50, "filed"),
            ("Air freight → UK (agricultural exports)", 50, "filed"),
            ("Air freight → Europe (agricultural exports)", 25, "filed"),
            ("Domestic transport", 25, "filed"),
            ("Cargo insurance", 25, "filed"),
            ("Express-vessel invoices", 25, "filed")]
    return bar_chart(rows, t, width, "Half the freight. Paid by Cairo.", "Share of cost covered by the state · from November shipments",
                     [("filed", "State-covered share of the cost")], 100, lambda v: f"{v}%",
                     note="On top of rebates raised by 35% on average; free-zone exporters excluded. Source: Cabinet statement via EnterpriseAM, 8 Nov 2026.",
                     scale=scale)


def route_map(t, width, scale=1.0):
    s = scale
    W = width
    out_row = ["Ningbo", "Shanghai", "Shekou", "Singapore", "Sokhna", "SUEZ", "Damietta", "Ambarli", "Izmit", "Mersin"]
    back_row = ["Ningbo", "Kaohsiung", "Singapore", "SUEZ", "Damietta"]  # drawn right-to-left under the outbound row
    egypt = {"Sokhna", "Damietta", "SUEZ"}
    x0, x1 = 20 * s, W - 44 * s
    y1, y2 = 70 * s, 190 * s
    g = []
    step = (x1 - x0) / (len(out_row) - 1)
    g.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{t["ink"]}" stroke-width="{2*s}"/>')
    g.append(f'<path d="M{x1},{y1} C{x1+16*s},{y1} {x1+16*s},{y2} {x1},{y2}" fill="none" stroke="{t["ink"]}" stroke-width="{2*s}"/>')
    g.append(f'<line x1="{x0}" y1="{y2}" x2="{x1}" y2="{y2}" stroke="{t["ink"]}" stroke-width="{2*s}" stroke-dasharray="{6*s} {4*s}"/>')
    g.append(f'<path d="M{x0},{y2} C{x0-16*s},{y2} {x0-16*s},{y1} {x0},{y1}" fill="none" stroke="{t["ink"]}" stroke-width="{2*s}" stroke-dasharray="{6*s} {4*s}"/>')

    def stop(x, y, name, below):
        eg = name in egypt
        if name == "SUEZ":
            g.append(f'<rect x="{x-7*s}" y="{y-7*s}" width="{14*s}" height="{14*s}" transform="rotate(45 {x} {y})" fill="{t["filed"]}"/>')
            label, fw, col = "Suez Canal", "700", t["accent"]
        else:
            r = 7 * s if eg else 5 * s
            fill = t["filed"] if eg else t["bg"]
            g.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{t["filed"] if eg else t["ink"]}" stroke-width="{2*s}"/>')
            label, fw, col = name, "700" if eg else "500", t["accent"] if eg else t["ink"]
        ty = y + (24 * s if below else -16 * s)
        g.append(f'<text x="{x}" y="{ty}" text-anchor="middle" font-family="Inter" font-size="{(12 if eg else 11)*s}" font-weight="{fw}" fill="{col}">{e(label)}</text>')

    for i, n in enumerate(out_row):
        stop(x0 + i * step, y1, n, below=(i % 2 == 1 and n != "Mersin"))
    xs_back = {"Damietta": x0 + 6 * step, "SUEZ": x0 + 5 * step, "Singapore": x0 + 3 * step, "Kaohsiung": x0 + 1.5 * step, "Ningbo": x0}
    for n in back_row:
        stop(xs_back[n], y2, n, below=(n != "SUEZ"))
    g.append(f'<text x="{x1 - 4*s}" y="{y1 - 34*s}" text-anchor="end" font-family="IBM Plex Mono" font-size="{10*s}" letter-spacing="{1.5*s}" fill="{t["muted"]}">OUTBOUND ▸</text>')
    g.append(f'<text x="{x0 + 4*s}" y="{y2 + 46*s}" font-family="IBM Plex Mono" font-size="{10*s}" letter-spacing="{1.5*s}" fill="{t["muted"]}">◂ RETURN</text>')
    H = 250 * s
    svg = f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">{"".join(g)}</svg>'
    chip = lambda big, small: (f'<div style="flex:1"><div style="font-family:{SERIF};font-weight:700;font-size:{28*s}px;color:{t["ink"]};line-height:1">{big}</div>'
                               f'<div style="font-family:{MONO};font-size:{10*s}px;letter-spacing:{1.5*s}px;text-transform:uppercase;color:{t["muted"]};margin-top:{4*s}px">{small}</div></div>')
    return (f'<div style="font-family:{MONO};font-size:{11*s}px;letter-spacing:{2*s}px;text-transform:uppercase;color:{t["accent"]};margin-bottom:{6*s}px">Premier Alliance · MD1 · via Suez</div>'
            f'<div style="font-family:{SERIF};font-weight:600;font-size:{26*s}px;color:{t["ink"]};margin-bottom:{8*s}px">Sokhna & Damietta, back on the Asia–Med map</div>'
            f'{svg}<div style="display:flex;gap:{16*s}px;margin-top:{4*s}px">{chip("84", "days, round voyage")}{chip("12", "ships · 16 on the Cape")}{chip("13 Nov", "first sailing, Ningbo")}</div>'
            f'<div style="font-size:{11*s}px;color:{t["muted"]};margin-top:{12*s}px">Gold = Egyptian calls. Schematic, not to scale. Source: The Loadstar.</div>')


def acid_steps(c, t, width, scale=1.0):
    s = scale
    X = c["explainer"]
    n = len(X["steps"])
    col_w = width / n
    cells = []
    for i, st in enumerate(X["steps"]):
        line = (f'<div style="position:absolute;top:{19*s}px;left:{col_w/2 + 22*s}px;width:{col_w - 44*s}px;height:{2*s}px;background:{t["filed"]}"></div>' if i < n - 1 else "")
        cells.append(f'<div style="position:relative;width:{col_w}px;padding:0 {10*s}px;text-align:center">{line}'
                     f'<div style="margin:0 auto;width:{40*s}px;height:{40*s}px;border-radius:50%;border:{2*s}px solid {t["filed"]};color:{t["accent"]};font-family:{SERIF};font-weight:700;font-size:{22*s}px;line-height:{36*s}px">{st["n"]}</div>'
                     f'<div style="font-family:{MONO};font-size:{10*s}px;letter-spacing:{1.5*s}px;text-transform:uppercase;color:{t["accent"]};margin:{12*s}px 0 {6*s}px">{e(st["who"])}</div>'
                     f'<div style="font-size:{13*s}px;line-height:1.45;color:{t["ink"]}">{e(st["text"])}</div></div>')
    return f'<div style="display:flex;width:{width}px">{"".join(cells)}</div>'


def stamp(c, size=150):
    r = size / 2
    txt = f"VERIFIED · {c['_source_count']} SOURCES · MEANS WHAT IT SAYS · "
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><path id="c" d="M{r},{r} m-{r-16},0 a{r-16},{r-16} 0 1,1 {2*(r-16)},0 a{r-16},{r-16} 0 1,1 -{2*(r-16)},0"/></defs>'
            f'<g transform="rotate(-12 {r} {r})" fill="none" stroke="{GOLD}" opacity="0.95">'
            f'<circle cx="{r}" cy="{r}" r="{r-3}" stroke-width="2.5"/><circle cx="{r}" cy="{r}" r="{r-28}" stroke-width="1.2"/>'
            f'<text font-family="IBM Plex Mono" font-size="10.5" letter-spacing="1.6" fill="{GOLD}" stroke="none"><textPath href="#c">{e(txt)}</textPath></text>'
            f'<text x="{r}" y="{r-4}" text-anchor="middle" font-family="Cormorant Garamond" font-weight="700" font-size="30" fill="{GOLD}" stroke="none">R</text>'
            f'<text x="{r}" y="{r+16}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" letter-spacing="2" fill="{GOLD}" stroke="none">VOY {e(c["issue_no"])}</text></g></svg>')


def light_visual(inner, width=600):
    return page(width, None, f'<div style="padding:28px 30px 24px;width:{width}px">{inner}</div>', PAPER)


# ------------------------------------------------------------------ slides (Instagram carousel, 1080x1350, dark)
def slide(c, n, total, inner, footer=True):
    foot = (f'<div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:{MID};border-top:1.5px solid #8b7a5e;display:flex;justify-content:space-between;align-items:center;padding:0 80px">'
            f'<div style="font-family:{SERIF};font-size:42px;letter-spacing:10px;color:{CREAM}">ROCKIT</div>'
            f'<div style="font-family:{MONO};font-size:18px;letter-spacing:4px;color:{GOLD}">{n:02d} / {total:02d}</div></div>') if footer else ""
    top = (f'<div style="position:absolute;left:80px;right:80px;top:56px;display:flex;justify-content:space-between;border-bottom:1.5px solid #8b7a5e;padding-bottom:16px;'
           f'font-family:{MONO};font-size:17px;letter-spacing:4px;color:#b9b3a0"><span>THE ROCKIT MANIFEST</span><span>VOYAGE {e(c["issue_no"])}</span></div>')
    return page(1080, 1350, f'{top}<div style="position:absolute;left:80px;right:80px;top:150px">{inner}</div>{foot}',
                f"radial-gradient(120% 90% at 20% 10%,#1b2b4b 0%,{NAVY} 45%,#101b33 100%)", "body{position:relative}")


def slides(c):
    C = c["cover"]
    total = 5
    s1 = slide(c, 1, total,
               f'<div style="font-family:{SERIF};font-weight:600;font-size:104px;line-height:.95;color:{CREAM}">The Rockit<br>Manifest</div>'
               f'<div style="font-family:{SERIF};font-style:italic;font-size:36px;color:{GOLD};margin-top:18px">What moved. What it means. What to do.</div>'
               f'<div style="font-family:{MONO};font-size:18px;letter-spacing:5px;color:{GOLD};margin-top:70px">THIS WEEK · {e(c["read_time"]).upper()} READ</div>'
               f'<div style="font-family:{SERIF};font-weight:600;font-size:64px;line-height:1.05;color:{CREAM};margin-top:14px">{e(C["headline"])}</div>'
               + "".join(f'<div style="font-family:{SERIF};font-style:italic;font-size:36px;color:{CREAM};margin-top:16px"><span style="color:{GOLD};font-style:normal;margin-right:18px">✓</span>{e(b)}</div>' for b in C["bullets"])
               + f'<div style="position:absolute;right:-10px;top:-40px">{stamp(c, 210)}</div>')
    big = lambda txt: f'<div style="font-family:{SERIF};font-weight:600;font-size:72px;line-height:1.02;color:{CREAM};margin:10px 0 56px">{txt}</div>'
    s2 = slide(c, 2, total, big("The index fell 2%.<br><span style='color:" + GOLD + "'>The December tariff rose $800.</span>") + gap_chart(DARK, 900, 1.85))
    s3 = slide(c, 3, total, big("From November shipments,<br><span style='color:" + GOLD + "'>the state pays up to half.</span>") + rebate_chart(DARK, 900, 1.5))
    s4 = slide(c, 4, total, big("Two Egyptian calls.<br><span style='color:" + GOLD + "'>One canal. 84 days.</span>") + route_map(DARK, 880, 1.8))
    T = c["thesaurus"]
    s5 = slide(c, 5, total,
               f'<div style="font-family:{MONO};font-size:18px;letter-spacing:5px;color:{GOLD}">LOST IN FORWARDING · THE THESAURUS OF EXCUSES</div>'
               f'<div style="font-family:{SERIF};font-weight:600;font-size:118px;color:{CREAM};margin-top:60px;line-height:1">{e(T["word"])}</div>'
               f'<div style="font-family:{SERIF};font-style:italic;font-size:38px;color:#b9b3a0;margin-top:14px">{e(T["phon"])} &nbsp;<span style="color:{GOLD}">{e(T["pos"])}</span></div>'
               f'<div style="font-family:{SERIF};font-style:italic;font-size:50px;line-height:1.25;color:{CREAM};margin-top:56px">1. {e(T["def"])}</div>'
               f'<div style="font-family:{MONO};font-size:18px;letter-spacing:4px;color:{GOLD};margin-top:60px">USAGE</div><div style="font-family:{SERIF};font-style:italic;font-size:40px;color:{CREAM};margin-top:8px">{e(T["usage"])}</div>'
               f'<div style="font-family:{MONO};font-size:18px;letter-spacing:4px;color:{GOLD};margin-top:44px">SYNONYMS (VERIFIED)</div><div style="font-family:{SERIF};font-style:italic;font-size:40px;color:{CREAM};margin-top:8px">{e(T["synonyms"])}.</div>'
               f'<div style="font-family:{MONO};font-size:18px;letter-spacing:4px;color:{GOLD};margin-top:44px">SEE ALSO</div><div style="font-family:{SERIF};font-style:italic;font-size:36px;color:{CREAM};margin-top:8px">{e(T["see"])}</div>'
               f'<div style="font-family:{SERIF};font-style:italic;font-size:34px;color:{GOLD};margin-top:60px">Rockit. Means what it says.</div>')
    return {"slide_1.html": s1, "slide_2.html": s2, "slide_3.html": s3, "slide_4.html": s4, "slide_5.html": s5}


def cover_4x3(c):
    C = c["cover"]
    inner = (f'<div style="position:absolute;left:80px;right:80px;top:50px;display:flex;justify-content:space-between;border-bottom:1.5px solid #8b7a5e;padding-bottom:14px;font-family:{MONO};font-size:15px;letter-spacing:4px;color:#b9b3a0"><span>THE ROCKIT MANIFEST · VOYAGE {e(c["issue_no"])}</span><span>{e(c["date_long"]).upper()}</span></div>'
             f'<div style="position:absolute;left:80px;top:130px;width:760px"><div style="font-family:{MONO};font-size:16px;letter-spacing:5px;color:{GOLD}">THE STRAIGHT ANSWER</div>'
             f'<div style="font-family:{SERIF};font-weight:600;font-size:76px;line-height:1.02;color:{CREAM};margin-top:14px">{e(C["headline"])}</div>'
             + "".join(f'<div style="font-family:{SERIF};font-style:italic;font-size:30px;color:{CREAM};margin-top:12px"><span style="color:{GOLD};font-style:normal;margin-right:14px">✓</span>{e(b)}</div>' for b in C["bullets"])
             + f'</div><div style="position:absolute;right:70px;top:150px">{stamp(c, 230)}</div>'
             f'<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:{MID};border-top:1.5px solid #8b7a5e;display:flex;justify-content:space-between;align-items:center;padding:0 80px">'
             f'<div style="font-family:{SERIF};font-size:42px;letter-spacing:10px;color:{CREAM}">ROCKIT</div><div style="font-family:{SERIF};font-style:italic;font-size:30px;color:{GOLD}">Means what it says.</div></div>')
    return page(1200, 900, inner, f"radial-gradient(120% 90% at 20% 10%,#1b2b4b 0%,{NAVY} 45%,#101b33 100%)", "body{position:relative}")


# ------------------------------------------------------------------ email
def kicker(text, color=GOLD_INK):
    return f'<div style="font-family:{MONO};font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:{color};margin:0 0 10px 0;">{e(text)}</div>'


def h2(text, color=INK, size=30):
    return f'<h2 style="font-family:{SERIF};font-size:{size}px;line-height:1.12;font-weight:600;color:{color};margin:0 0 14px 0;">{e(text)}</h2>'


def p(text, color=INK, size=16, mb=14):
    return f'<p style="font-family:{SANS};font-size:{size}px;line-height:1.62;color:{color};margin:0 0 {mb}px 0;">{text}</p>'


def srcs(items, color=MUTED):
    links = " · ".join(f'<a href="{e(x["url"])}" style="color:{color};text-decoration:underline;">{e(x["name"])}</a>' for x in items)
    return f'<div style="font-family:{SANS};font-size:12px;color:{color};margin:4px 0 0 0;line-height:1.6;">Sources: {links}</div>'


def img(url, alt, w=600):
    return f'<img src="{e(url)}" width="{w}" alt="{e(alt)}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;margin:6px 0 10px 0;">'


def row(inner, bg=PAPER, pad="34px 36px"):
    return f'<tr><td style="background:{bg};padding:{pad};">{inner}</td></tr>'


def rule():
    return f'<tr><td style="background:{PAPER};padding:0 36px;"><div style="border-top:1px solid {RULE};height:1px;line-height:1px;font-size:1px;">&nbsp;</div></td></tr>'


def email_html(c, IMG):
    R = []
    R.append(f'<tr><td style="background:{MID};padding:10px 36px;font-family:{MONO};font-size:10px;letter-spacing:2px;color:#8f97a8;text-transform:uppercase;">'
             f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:#8f97a8;">Voyage {e(c["issue_no"])} · {e(c["read_time"])} read</td>'
             f'<td align="right"><a href="{e(c["blog_url"])}" style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:{GOLD};text-decoration:none;">VIEW ON THE WEB ▸</a></td></tr></table></td></tr>')
    fields = [("VOYAGE", c["issue_no"]), ("ETD", c["etd"]), ("SHIPPER", "Rockit, Cairo"), ("CONSIGNEE", "You"),
              ("CONTENTS", "6 line items + 1 excuse"), ("SOURCES", f'{c["_source_count"]}, each checked')]
    cells = "".join(f'<tr><td style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:#8f97a8;padding:5px 12px 5px 0;white-space:nowrap;vertical-align:top;">{k}</td>'
                    f'<td style="font-family:{MONO};font-size:12px;color:{CREAM};padding:5px 0;border-bottom:1px dashed #33456b;">{e(v)}</td></tr>' for k, v in fields)
    R.append(f'''<tr><td style="background:{NAVY};padding:30px 36px 30px 36px;">
<div style="font-family:{SERIF};font-size:50px;line-height:.95;color:{CREAM};font-weight:600;">The Rockit Manifest</div>
<div style="font-family:{SERIF};font-size:19px;font-style:italic;color:{GOLD};margin:10px 0 22px 0;">What moved. What it means. What to do.</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td valign="top"><table role="presentation" cellpadding="0" cellspacing="0" width="100%">{cells}</table></td>
<td valign="middle" align="right" width="150" style="padding-left:12px;"><img src="{IMG}stamp.png" width="130" alt="Verified stamp: {c["_source_count"]} sources checked. Means what it says." style="display:block;width:130px;height:auto;border:0;"></td>
</tr></table></td></tr>''')
    R.append(row(f'<p style="font-family:{SERIF};font-size:20px;line-height:1.5;font-style:italic;color:{INK};margin:0;">{e(c["opening"])}</p>'
                 f'<div style="font-family:{MONO};font-size:11px;letter-spacing:2px;color:{GOLD_INK};margin-top:10px;">THE ROCKIT DESK, CAIRO</div>', pad="30px 36px 6px 36px"))
    tl = "".join(f'<tr><td valign="top" style="padding:9px 14px 9px 0;width:70px;"><span style="display:inline-block;font-family:{MONO};font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:{CREAM};background:{NAVY};padding:4px 7px;">{e(x["tag"])}</span></td>'
                 f'<td style="font-family:{SANS};font-size:15px;line-height:1.5;color:{INK};padding:9px 0;border-bottom:1px solid {RULE};">{e(x["text"])}</td></tr>' for x in c["tldr"])
    R.append(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f3ecd9;border-left:3px solid {GOLD};"><tr><td style="padding:18px 20px;">'
                 + kicker("The 60-second manifest") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{tl}</table></td></tr></table>', pad="22px 36px 30px 36px"))
    L = c["lead"]
    R.append(row(kicker(L["kicker"]) + h2(L["headline"], size=34) + "".join(p(x) for x in L["paras"]) + img(IMG + "chart_gap.png", L["chart_alt"]) + srcs(L["sources"])))
    R.append(rule())
    F = c["feature"]
    R.append(row(kicker(F["kicker"]) + h2(F["headline"], size=34) + p(F["paras"][0]) + img(IMG + "chart_rebate.png", F["chart_alt"]) + p(F["paras"][1]) + srcs(F["sources"])))
    N = c["numbers"]
    arrow = {"up": ("▲", "#9a3b2e"), "down": ("▼", "#2e6b4a"), "flat": ("◆", MUTED)}
    tiles = []
    for i in range(0, len(N["tiles"]), 3):
        tds = ""
        for tl_ in N["tiles"][i:i + 3]:
            a, col = arrow[tl_["dir"]]
            tds += (f'<td valign="top" width="33%" style="padding:14px 10px 14px 0;border-top:2px solid {INK};">'
                    f'<a href="{e(tl_["url"])}" style="text-decoration:none;color:{INK};"><div style="font-family:{SERIF};font-size:34px;font-weight:700;color:{INK};line-height:1;">{e(tl_["value"])}</div>'
                    f'<div style="font-family:{SANS};font-size:12px;line-height:1.4;color:{INK};margin-top:8px;">{e(tl_["label"])}</div>'
                    f'<div style="font-family:{MONO};font-size:11px;color:{col};margin-top:6px;">{a} {e(tl_["delta"])}</div></a></td>')
        tiles.append(f'<tr>{tds}</tr>')
    R.append(row(kicker(N["kicker"]) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{"".join(tiles)}</table>'
                 f'<div style="font-family:{SANS};font-size:11px;color:{MUTED};margin-top:10px;line-height:1.5;">{e(N["footnote"])} Red ▲ = costs you more; green ▼ = costs you less.</div>', bg="#f3ecd9"))
    for key in ("egypt", "world"):
        D = c[key]
        inner = kicker(D["kicker"])
        for it in D["items"]:
            inner += f'<div style="font-family:{SERIF};font-size:23px;font-weight:600;color:{INK};margin:8px 0 6px 0;">{e(it["title"])}</div>'
            inner += p(e(it["body"]), size=15, mb=6)
            if it.get("visual") == "route":
                inner += img(IMG + "route_md1.png", it["alt"])
            inner += f'<div style="font-family:{SANS};font-size:12px;color:{MUTED};margin:0 0 18px 0;">Source: <a href="{e(it["url"])}" style="color:{MUTED};">{e(it["source"])}</a></div>'
        R.append(row(inner))
        R.append(rule())
    M = c["moves"]
    tr = "".join(f'<tr><td valign="top" style="padding:12px 16px 12px 0;width:120px;border-top:1px solid {RULE};font-family:{MONO};font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{GOLD_INK};">{e(t["tag"])}</td>'
                 f'<td style="padding:12px 0;border-top:1px solid {RULE};font-family:{SANS};font-size:15px;line-height:1.55;color:{INK};">'
                 + "".join(f'<div style="margin-bottom:4px;"><span style="color:{GOLD_INK};font-weight:700;">→</span>&nbsp; {e(x)}</div>' for x in t["items"]) + '</td></tr>' for t in M["tracks"])
    R.append(row(kicker(M["kicker"]) + h2("Before Friday", size=28) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{tr}</table>'))
    D = c["dates"]
    dr = "".join(f'<tr><td valign="top" style="padding:7px 12px 7px 0;white-space:nowrap;font-family:{MONO};font-size:12px;color:{GOLD_INK};font-weight:600;width:84px;">{e(d["date"])}</td>'
                 f'<td valign="top" style="padding:7px 10px 7px 0;width:14px;"><div style="width:9px;height:9px;border-radius:9px;background:{GOLD};margin-top:4px;"></div></td>'
                 f'<td style="padding:7px 0;font-family:{SANS};font-size:14px;color:{INK};border-bottom:1px dotted {RULE};"><a href="{e(d["url"])}" style="color:{INK};text-decoration:none;">{e(d["event"])}</a></td></tr>' for d in D["rows"])
    R.append(row(kicker(D["kicker"]) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{dr}</table>', bg="#f3ecd9"))
    X = c["explainer"]
    R.append(row(kicker(X["kicker"], GOLD) + h2(X["title"], CREAM, 30) + f'<img src="{IMG}acid_steps.png" width="528" alt="{e(X["visual_alt"])}" style="display:block;width:100%;max-width:528px;height:auto;border:0;margin:6px 0 14px 0;background:{PAPER};">'
                 + p(e(X["note"]), "#d9d4c3", 14) + f'<a href="{e(X["url"])}" style="display:inline-block;font-family:{MONO};font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MID};background:{GOLD};padding:12px 18px;text-decoration:none;">{e(X["cta"])} ▸</a>', bg=NAVY))
    T = c["thesaurus"]
    R.append(row(f'<div style="font-family:{MONO};font-size:10px;letter-spacing:2.5px;text-transform:uppercase;color:#b9b3a0;margin-bottom:14px;">{e(T["kicker"])}</div>'
                 f'<div style="font-family:{SERIF};font-size:44px;font-weight:600;color:{CREAM};line-height:1;">{e(T["word"])}</div>'
                 f'<div style="font-family:{SERIF};font-size:17px;font-style:italic;color:#b9b3a0;margin:6px 0 14px 0;">{e(T["phon"])} &nbsp;<span style="color:{GOLD};">{e(T["pos"])}</span></div>'
                 f'<div style="font-family:{SERIF};font-size:22px;font-style:italic;line-height:1.35;color:{CREAM};">1. {e(T["def"])}</div>'
                 f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin-top:16px;">'
                 + "".join(f'<tr><td style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:{GOLD};padding:4px 14px 4px 0;vertical-align:top;white-space:nowrap;">{k}</td><td style="font-family:{SERIF};font-size:17px;font-style:italic;color:#d9d4c3;padding:2px 0;">{e(v)}</td></tr>'
                           for k, v in (("USAGE", T["usage"]), ("SYNONYMS (VERIFIED)", T["synonyms"] + "."), ("SEE ALSO", T["see"])))
                 + '</table>', bg=MID))
    S = c["signoff"]
    R.append(row(f'<div style="font-family:{SERIF};font-size:26px;line-height:1.3;color:{INK};font-weight:600;margin-bottom:16px;">{e(S["line"])}</div>'
                 f'<a href="{e(S["url"])}" style="display:inline-block;font-family:{MONO};font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{CREAM};background:{NAVY};padding:13px 20px;text-decoration:none;">{e(S["cta"])} ▸</a>'
                 f'<div style="font-family:{MONO};font-size:11px;letter-spacing:2px;color:{GOLD_INK};margin-top:18px;">— THE ROCKIT DESK · CAIRO · ALEXANDRIA · SOKHNA · DAMIETTA</div>'))
    R.append(row(f'<div style="font-family:{SERIF};font-size:24px;letter-spacing:8px;color:{CREAM};">ROCKIT</div>'
                 f'<div style="font-family:{SANS};font-size:9px;letter-spacing:3px;color:{GOLD};text-transform:uppercase;margin-top:2px;">Transport Services &amp; Logistics</div>'
                 f'<div style="font-family:{SERIF};font-size:17px;font-style:italic;color:{GOLD};margin:14px 0;">Means what it says.</div>'
                 f'<div style="font-family:{SANS};font-size:12px;line-height:1.6;color:#9aa3b5;"><a href="https://www.rockit-transport.com" style="color:#9aa3b5;">rockit-transport.com</a> · +20 2 2690 7601 · inquiry@rockit.com.eg</div>'
                 f'<div style="font-family:{SANS};font-size:11px;line-height:1.6;color:#6f7889;margin-top:14px;">{c["disclaimer"]}</div>', bg=MID, pad="28px 36px 34px 36px"))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><title>{e(c["subject"])}</title>{FONTS}
<style>@media (max-width:620px){{.wrap{{width:100%!important}} td{{padding-left:18px!important;padding-right:18px!important}}}}</style></head>
<body style="margin:0;padding:0;background:#e9e4d6;"><div style="display:none;max-height:0;overflow:hidden;opacity:0;">{e(c["preheader"])}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#e9e4d6;"><tr><td align="center" style="padding:24px 0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;">{"".join(R)}</table></td></tr></table></body></html>'''


# ------------------------------------------------------------------ ricos (website)
def T_(text, bold=False, italic=False, link=None):
    d = []
    if bold:
        d.append({"type": "BOLD", "fontWeightValue": 700})
    if italic:
        d.append({"type": "ITALIC", "italicData": True})
    if link:
        d.append({"type": "LINK", "linkData": {"link": {"url": link, "target": "BLANK", "rel": {"noreferrer": True}}}})
    return {"type": "TEXT", "nodes": [], "textData": {"text": text, "decorations": d}}


def P_(*t):
    return {"type": "PARAGRAPH", "nodes": list(t), "paragraphData": {}}


def H_(text, level=2):
    return {"type": "HEADING", "nodes": [T_(text)], "headingData": {"level": level}}


def UL(items):
    return {"type": "BULLETED_LIST", "nodes": [{"type": "LIST_ITEM", "nodes": [P_(*i) if isinstance(i, list) else P_(T_(i))]} for i in items], "bulletedListData": {"indentation": 0}}


def IMG_(key, w, h, alt):
    return {"type": "IMAGE", "nodes": [], "imageData": {"containerData": {"width": {"size": "CONTENT"}, "alignment": "CENTER"},
                                                        "image": {"src": {"id": "@" + key}, "width": w, "height": h}, "altText": alt}}


def SRC_(items):
    out = [T_("Sources: ", italic=True)]
    for i, x in enumerate(items):
        out.append(T_(x["name"], italic=True, link=x["url"]))
        if i < len(items) - 1:
            out.append(T_(" · ", italic=True))
    return P_(*out)


def ricos(c, dims):
    n = [P_(T_(f"Voyage {c['issue_no']} · {c['date_long']} · {c['read_time']} read · {c['_source_count']} sources, each checked", italic=True)),
         P_(T_(c["opening"], italic=True)), P_(T_("— The Rockit desk, Cairo", italic=True)),
         H_("The 60-second manifest"), UL([[T_(x["tag"] + ": ", bold=True), T_(x["text"])] for x in c["tldr"]])]
    L = c["lead"]
    n += [H_(L["headline"])] + [P_(T_(strip(x))) for x in L["paras"]] + [IMG_("chart_gap", *dims["chart_gap"], L["chart_alt"]), SRC_(L["sources"])]
    F = c["feature"]
    n += [H_(F["headline"]), P_(T_(F["paras"][0])), IMG_("chart_rebate", *dims["chart_rebate"], F["chart_alt"]), P_(T_(F["paras"][1])), SRC_(F["sources"])]
    N = c["numbers"]
    n += [H_("By the numbers"), UL([[T_(t["value"] + " ", bold=True), T_(f'{t["label"]} ({t["delta"]}) '), T_("source", italic=True, link=t["url"])] for t in N["tiles"]]), P_(T_(N["footnote"], italic=True))]
    for key, title in (("egypt", "Egypt desk"), ("world", "World desk")):
        n.append(H_(title))
        for it in c[key]["items"]:
            n += [H_(it["title"], 3), P_(T_(it["body"]))]
            if it.get("visual") == "route":
                n.append(IMG_("route_md1", *dims["route_md1"], it["alt"]))
            n.append(SRC_([{"name": it["source"], "url": it["url"]}]))
    n += [H_("Your move, before Friday")] + [UL([[T_(t["tag"] + ": ", bold=True), T_(" ".join(t["items"]))] for t in c["moves"]["tracks"]])]
    n += [H_("On the calendar"), UL([[T_(d["date"] + ": ", bold=True), T_(d["event"], link=d["url"])] for d in c["dates"]["rows"]])]
    X = c["explainer"]
    n += [H_("Rockit explains: " + X["title"]), IMG_("acid_steps", *dims["acid_steps"], X["visual_alt"]),
          {"type": "ORDERED_LIST", "nodes": [{"type": "LIST_ITEM", "nodes": [P_(T_(s["who"] + ": ", bold=True), T_(s["text"]))]} for s in X["steps"]], "orderedListData": {"indentation": 0}},
          P_(T_(X["note"] + " "), T_(X["cta"], bold=True, link=X["url"]))]
    TH = c["thesaurus"]
    n += [H_("The Thesaurus of Excuses", 3), P_(T_(TH["word"] + " ", bold=True), T_(f'{TH["phon"]} {TH["pos"]}', italic=True)),
          P_(T_("1. " + TH["def"], italic=True)), P_(T_("Usage: ", bold=True), T_(TH["usage"], italic=True)),
          P_(T_("Synonyms (verified): ", bold=True), T_(TH["synonyms"] + ".")), P_(T_("See also: ", bold=True), T_(TH["see"]))]
    S = c["signoff"]
    n += [H_(S["line"], 3), P_(T_(S["cta"], bold=True, link=S["url"]), T_(" · Rockit. Means what it says.", italic=True)), P_(T_(strip(c["disclaimer"]), italic=True))]
    return {"nodes": n}


def count_sources(c):
    urls = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "url" and isinstance(v, str) and v.startswith("http") and "rockit-transport.com" not in v:
                    urls.add(v.split("#")[0])
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk({k: v for k, v in c.items() if k not in ("social", "blog_url")})
    return len(urls)


def main():
    path = Path(sys.argv[1])
    c = json.loads(path.read_text(encoding="utf-8"))
    c["_source_count"] = count_sources(c)
    out = path.parent
    vis = out / "visuals"
    vis.mkdir(exist_ok=True)
    files = {
        "chart_gap.html": light_visual(gap_chart(LIGHT, 540)),
        "chart_rebate.html": light_visual(rebate_chart(LIGHT, 540)),
        "route_md1.html": light_visual(route_map(LIGHT, 540)),
        "acid_steps.html": page(528, None, f'<div style="padding:22px 0 20px;width:528px">{acid_steps(c, LIGHT, 528)}</div>', PAPER),
        "stamp.html": page(150, 150, stamp(c, 150), "transparent"),
        "cover_4x3.html": cover_4x3(c),
    }
    files.update(slides(c))
    for k, v in files.items():
        (vis / k).write_text(v, encoding="utf-8")
    img_base = c.get("img_base", "IMG_BASE/")
    (out / "email.html").write_text(email_html(c, img_base), encoding="utf-8")
    dims_path = vis / "dims.json"
    dims = json.loads(dims_path.read_text()) if dims_path.exists() else {k: [1200, 800] for k in ("chart_gap", "chart_rebate", "route_md1", "acid_steps")}
    (out / "ricos.json").write_text(json.dumps(ricos(c, dims), ensure_ascii=False, indent=1), encoding="utf-8")
    soc = {k: v.replace("BLOG_URL", c["blog_url"]) for k, v in c["social"].items()}
    (out / "social.json").write_text(json.dumps(soc, ensure_ascii=False, indent=1), encoding="utf-8")
    print("built", out, "sources:", c["_source_count"])


if __name__ == "__main__":
    main()
