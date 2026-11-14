#!/usr/bin/env python3
"""Build every channel format of one issue of The Rockit Manifest from a single content file.

Usage:  python3 build_issue.py ../issues/2026-11-16/content.json

Writes next to the content file:
  email.html        email-safe HTML (600px tables, inline styles) for Wix Email Marketing (HTML editor)
  ricos.json        Wix Blog rich content (Ricos) for rockit-transport.com
  cover_4x5.html    1080x1350 social cover (LinkedIn / Instagram / Facebook), rendered to PNG by render_covers.js
  cover_4x3.html    1200x900 cover for Google Business Profile
  social.json       per-channel post copy (taken verbatim from content.json "social")

One source of truth: every fact appears once in content.json with its source, so each channel
carries the same audited wording.
"""
import html
import json
import sys
from pathlib import Path

NAVY = "#16243f"
MIDNIGHT = "#080f1f"
GOLD = "#d5ae69"
CREAM = "#f1eedb"
INK = "#1b2333"
PAPER = "#faf7ef"
RULE = "#e6dcc4"
MUTED = "#5d6577"
SERIF = "'Cormorant Garamond', Georgia, 'Times New Roman', serif"
SANS = "Inter, 'Helvetica Neue', Arial, sans-serif"


def e(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- email
def eyebrow(text, color=GOLD):
    return (f'<div style="font-family:{SANS};font-size:11px;letter-spacing:3px;text-transform:uppercase;'
            f'color:{color};font-weight:600;margin:0 0 10px 0;">{e(text)}</div>')


def h2(text, color=INK):
    return (f'<h2 style="font-family:{SERIF};font-size:28px;line-height:1.15;font-weight:600;color:{color};'
            f'margin:0 0 14px 0;">{e(text)}</h2>')


def p(text, color=INK, size=16):
    return (f'<p style="font-family:{SANS};font-size:{size}px;line-height:1.6;color:{color};margin:0 0 14px 0;">'
            f'{text}</p>')


def src(item):
    if not item.get("source"):
        return ""
    label = e(item["source"])
    if item.get("url"):
        label = f'<a href="{e(item["url"])}" style="color:{MUTED};text-decoration:underline;">{label}</a>'
    return (f'<div style="font-family:{SANS};font-size:12px;color:{MUTED};margin:-6px 0 16px 0;">'
            f'Source: {label}</div>')


def block(inner, bg=PAPER, pad="32px 36px"):
    return (f'<tr><td style="background:{bg};padding:{pad};">{inner}</td></tr>')


def divider():
    return f'<tr><td style="background:{PAPER};padding:0 36px;"><div style="border-top:1px solid {RULE};height:1px;line-height:1px;font-size:1px;">&nbsp;</div></td></tr>'


def email_html(c):
    rows = []
    # header
    rows.append(f'''<tr><td style="background:{NAVY};padding:28px 36px 26px 36px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td style="font-family:{SERIF};font-size:15px;font-style:italic;color:#b9b3a0;">Issue {e(c["issue_no"])} &middot; {e(c["date_long"])}</td>
<td align="right" style="font-family:{SANS};font-size:10px;letter-spacing:3px;color:#b9b3a0;text-transform:uppercase;">Weekly &middot; Cairo</td>
</tr></table>
<div style="border-top:1px solid #8b7a5e;margin:14px 0 22px 0;height:1px;line-height:1px;font-size:1px;">&nbsp;</div>
<div style="font-family:{SERIF};font-size:46px;line-height:1;color:{CREAM};font-weight:600;">The Rockit Manifest</div>
<div style="font-family:{SERIF};font-size:18px;font-style:italic;color:{GOLD};margin-top:10px;">What moved. What it means. What to do.</div>
</td></tr>''')
    # lead
    L = c["lead"]
    inner = eyebrow(L["eyebrow"]) + h2(L["headline"])
    for para in L["paras"]:
        inner += p(para)
    inner += src(L)
    inner += (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{NAVY};border-left:3px solid {GOLD};">'
              f'<tr><td style="padding:18px 20px;">'
              f'<div style="font-family:{SANS};font-size:11px;letter-spacing:3px;color:{GOLD};font-weight:600;text-transform:uppercase;margin-bottom:8px;">So what, for you</div>')
    for s in L["so_what"]:
        inner += f'<div style="font-family:{SANS};font-size:15px;line-height:1.55;color:{CREAM};margin:0 0 8px 0;">&#10003;&nbsp; {s}</div>'
    inner += '</td></tr></table>'
    rows.append(block(inner))
    rows.append(divider())
    # numbers
    N = c["numbers"]
    inner = eyebrow(N["eyebrow"]) + h2(N["headline"])
    inner += f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">'
    inner += (f'<tr><td style="font-family:{SANS};font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};padding:6px 0;border-bottom:2px solid {INK};">Indicator</td>'
              f'<td align="right" style="font-family:{SANS};font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};padding:6px 0;border-bottom:2px solid {INK};">Latest</td>'
              f'<td align="right" style="font-family:{SANS};font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};padding:6px 0;border-bottom:2px solid {INK};">Change</td></tr>')
    for r in N["rows"]:
        ch = r.get("change", "")
        col = INK
        if ch.startswith("+"):
            col = "#9a3b2e"
        elif ch.startswith("-") or ch.startswith("−"):
            col = "#2e6b4a"
        label = e(r["label"])
        if r.get("url"):
            label = f'<a href="{e(r["url"])}" style="color:{INK};text-decoration:none;border-bottom:1px dotted {MUTED};">{label}</a>'
        inner += (f'<tr><td style="font-family:{SANS};font-size:14px;color:{INK};padding:10px 8px 10px 0;border-bottom:1px solid {RULE};">{label}'
                  f'<div style="font-size:11px;color:{MUTED};margin-top:2px;">{e(r.get("note", ""))}</div></td>'
                  f'<td align="right" style="font-family:{SERIF};font-size:20px;font-weight:600;color:{INK};padding:10px 0;border-bottom:1px solid {RULE};white-space:nowrap;">{e(r["value"])}</td>'
                  f'<td align="right" style="font-family:{SANS};font-size:13px;font-weight:600;color:{col};padding:10px 0 10px 8px;border-bottom:1px solid {RULE};white-space:nowrap;">{e(ch)}</td></tr>')
    inner += '</table>'
    if N.get("footnote"):
        inner += f'<div style="font-family:{SANS};font-size:12px;color:{MUTED};margin-top:10px;line-height:1.5;">{N["footnote"]}</div>'
    rows.append(block(inner))
    rows.append(divider())
    # sections
    for S in c["sections"]:
        inner = eyebrow(S["eyebrow"]) + h2(S["headline"])
        for it in S["items"]:
            inner += (f'<div style="font-family:{SERIF};font-size:20px;font-weight:600;color:{INK};margin:4px 0 6px 0;">{e(it["title"])}</div>')
            inner += p(it["body"], size=15)
            inner += src(it)
        rows.append(block(inner))
        rows.append(divider())
    # actions
    A = c["actions"]
    inner = eyebrow("Your move this week") + h2(A["headline"])
    inner += '<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
    for i, (k, title) in enumerate((("shippers", "Exporters, importers &amp; manufacturers"), ("agents", "Forwarding partners &amp; agents"))):
        pad = "padding:0 10px 0 0;" if i == 0 else "padding:0 0 0 10px;"
        inner += f'<td valign="top" width="50%" style="{pad}"><div style="font-family:{SANS};font-size:12px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;color:{NAVY};border-bottom:2px solid {GOLD};padding-bottom:6px;margin-bottom:10px;">{title}</div>'
        for n, a in enumerate(A[k], 1):
            inner += f'<div style="font-family:{SANS};font-size:14px;line-height:1.55;color:{INK};margin:0 0 10px 0;"><span style="font-family:{SERIF};font-size:18px;color:{GOLD};font-weight:600;">{n:02d}</span>&nbsp; {a}</div>'
        inner += '</td>'
    inner += '</tr></table>'
    rows.append(block(inner))
    rows.append(divider())
    # dates
    D = c["dates"]
    inner = eyebrow("On the calendar") + h2(D["headline"])
    inner += '<table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
    for d in D["rows"]:
        ev = e(d["event"])
        if d.get("url"):
            ev = f'<a href="{e(d["url"])}" style="color:{INK};">{ev}</a>'
        inner += (f'<tr><td valign="top" style="font-family:{SERIF};font-size:17px;font-weight:600;color:{NAVY};padding:8px 14px 8px 0;white-space:nowrap;border-bottom:1px solid {RULE};">{e(d["date"])}</td>'
                  f'<td style="font-family:{SANS};font-size:14px;line-height:1.5;color:{INK};padding:8px 0;border-bottom:1px solid {RULE};">{ev}'
                  f'<div style="font-size:12px;color:{MUTED};">{e(d.get("note", ""))}</div></td></tr>')
    inner += '</table>'
    rows.append(block(inner))
    # explainer
    X = c["explainer"]
    inner = eyebrow("Rockit explains", GOLD)
    inner += f'<div style="font-family:{SERIF};font-size:24px;font-weight:600;color:{CREAM};margin:0 0 10px 0;">{e(X["title"])}</div>'
    inner += f'<p style="font-family:{SANS};font-size:15px;line-height:1.6;color:#d9d4c3;margin:0 0 16px 0;">{X["body"]}</p>'
    inner += (f'<a href="{e(X["url"])}" style="display:inline-block;font-family:{SANS};font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:700;'
              f'color:{MIDNIGHT};background:{GOLD};padding:12px 18px;text-decoration:none;">{e(X["cta"])}</a>')
    rows.append(block(inner, bg=NAVY))
    # lost in forwarding
    W = c["excuse"]
    inner = (f'<div style="font-family:{SANS};font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#b9b3a0;margin-bottom:10px;">Lost in Forwarding &middot; excuse of the week</div>'
             f'<div style="font-family:{SERIF};font-size:30px;font-style:italic;color:{CREAM};">&ldquo;{e(W["phrase"])}&rdquo;</div>'
             f'<div style="font-family:{SERIF};font-size:16px;font-style:italic;color:{GOLD};margin:6px 0 10px 0;">{e(W["pos"])}</div>'
             f'<div style="font-family:{SANS};font-size:14px;line-height:1.6;color:#d9d4c3;">{W["definition"]}</div>')
    rows.append(block(inner, bg=MIDNIGHT))
    # CTA + footer
    inner = (f'<div style="font-family:{SERIF};font-size:24px;color:{INK};font-weight:600;margin-bottom:8px;">{e(c["cta"]["headline"])}</div>'
             + p(c["cta"]["body"], size=15)
             + f'<a href="{e(c["cta"]["url"])}" style="display:inline-block;font-family:{SANS};font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:{CREAM};background:{NAVY};padding:13px 20px;text-decoration:none;">{e(c["cta"]["button"])}</a>')
    rows.append(block(inner))
    foot = (f'<div style="font-family:{SERIF};font-size:22px;letter-spacing:6px;color:{CREAM};">ROCKIT</div>'
            f'<div style="font-family:{SANS};font-size:9px;letter-spacing:3px;color:{GOLD};text-transform:uppercase;margin-top:2px;">Transport Services &amp; Logistics</div>'
            f'<div style="font-family:{SERIF};font-size:16px;font-style:italic;color:{GOLD};margin:14px 0 14px 0;">Means what it says.</div>'
            f'<div style="font-family:{SANS};font-size:12px;line-height:1.6;color:#9aa3b5;">Cairo &middot; Alexandria &middot; Sokhna &middot; Damietta<br>'
            f'<a href="https://www.rockit-transport.com" style="color:#9aa3b5;">rockit-transport.com</a> &middot; +20 2 2690 7601</div>'
            f'<div style="font-family:{SANS};font-size:11px;line-height:1.6;color:#6f7889;margin-top:16px;">{c["disclaimer"]}</div>')
    rows.append(block(foot, bg=MIDNIGHT, pad="28px 36px 34px 36px"))

    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting"><title>{e(c["subject"])}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>@media (max-width:620px){{.wrap{{width:100%!important}} td{{padding-left:20px!important;padding-right:20px!important}}}}</style>
</head><body style="margin:0;padding:0;background:#e9e4d6;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{e(c["preheader"])}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#e9e4d6;"><tr><td align="center" style="padding:24px 0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;">
{"".join(rows)}
</table></td></tr></table></body></html>'''


# ---------------------------------------------------------------- ricos (website)
def t(text, bold=False, italic=False, link=None):
    deco = []
    if bold:
        deco.append({"type": "BOLD", "fontWeightValue": 700})
    if italic:
        deco.append({"type": "ITALIC", "italicData": True})
    if link:
        deco.append({"type": "LINK", "linkData": {"link": {"url": link, "target": "BLANK", "rel": {"noreferrer": True}}}})
    return {"type": "TEXT", "nodes": [], "textData": {"text": text, "decorations": deco}}


def para(*texts):
    return {"type": "PARAGRAPH", "nodes": list(texts), "paragraphData": {}}


def head(text, level=2):
    return {"type": "HEADING", "nodes": [t(text)], "headingData": {"level": level}}


def bullets(items):
    return {"type": "BULLETED_LIST", "nodes": [{"type": "LIST_ITEM", "nodes": [para(*i) if isinstance(i, list) else para(t(i))]} for i in items], "bulletedListData": {"indentation": 0}}


def numbered(items):
    return {"type": "ORDERED_LIST", "nodes": [{"type": "LIST_ITEM", "nodes": [para(t(i))]} for i in items], "orderedListData": {"indentation": 0}}


def strip(s):
    """Plain text from the light inline HTML used in content.json (<b>, &amp;, etc.)."""
    import re
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def source_para(item):
    if not item.get("source"):
        return None
    return para(t("Source: ", italic=True), t(item["source"], italic=True, link=item.get("url")))


def ricos(c):
    n = []
    n.append(para(t(f"Issue {c['issue_no']} · {c['date_long']} · ", italic=True), t("What moved. What it means. What to do.", italic=True)))
    L = c["lead"]
    n.append(head(L["headline"]))
    for x in L["paras"]:
        n.append(para(t(strip(x))))
    s = source_para(L)
    if s:
        n.append(s)
    n.append(para(t("So what, for you", bold=True)))
    n.append(bullets([strip(x) for x in L["so_what"]]))
    N = c["numbers"]
    n.append(head(N["headline"]))
    n.append(bullets([[t(f"{r['label']}: ", bold=True), t(f"{r['value']}" + (f" ({r['change']})" if r.get('change') else "") + (f" — {r['note']}" if r.get('note') else "") + " "), t("source", link=r.get("url"), italic=True)] if r.get("url") else [t(f"{r['label']}: ", bold=True), t(r['value'])] for r in N["rows"]]))
    if N.get("footnote"):
        n.append(para(t(strip(N["footnote"]), italic=True)))
    for S in c["sections"]:
        n.append(head(S["headline"]))
        for it in S["items"]:
            n.append(head(it["title"], 3))
            n.append(para(t(strip(it["body"]))))
            s = source_para(it)
            if s:
                n.append(s)
    A = c["actions"]
    n.append(head(A["headline"]))
    n.append(head("Exporters, importers & manufacturers", 3))
    n.append(numbered([strip(x) for x in A["shippers"]]))
    n.append(head("Forwarding partners & agents", 3))
    n.append(numbered([strip(x) for x in A["agents"]]))
    D = c["dates"]
    n.append(head(D["headline"]))
    n.append(bullets([[t(f"{d['date']}: ", bold=True), t(d["event"], link=d.get("url")), t((" — " + d["note"]) if d.get("note") else "")] for d in D["rows"]]))
    X = c["explainer"]
    n.append(head("Rockit explains: " + X["title"]))
    n.append(para(t(strip(X["body"]) + " "), t(X["cta"], bold=True, link=X["url"])))
    W = c["excuse"]
    n.append(head("Lost in Forwarding: excuse of the week", 3))
    n.append(para(t(f"“{W['phrase']}” ", bold=True, italic=True), t(f"({W['pos']}) ", italic=True), t(strip(W["definition"]))))
    n.append(head(c["cta"]["headline"], 3))
    n.append(para(t(strip(c["cta"]["body"]) + " "), t(c["cta"]["button"], bold=True, link=c["cta"]["url"])))
    n.append(para(t(strip(c["disclaimer"]), italic=True)))
    return {"nodes": n}


# ---------------------------------------------------------------- covers
def cover(c, w, h):
    C = c["cover"]
    big = 96 if w == 1080 else 78
    lines = "".join(f'<li>{e(x)}</li>' for x in C["bullets"])
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;background:radial-gradient(120% 90% at 20% 10%,#1b2b4b 0%,{NAVY} 45%,#101b33 100%);color:{CREAM};font-family:'Cormorant Garamond',Georgia,serif;position:relative;overflow:hidden}}
.top{{position:absolute;left:96px;right:96px;top:{60 if h>1000 else 48}px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:1.5px solid #8b7a5e;padding-bottom:18px}}
.top .l{{font-style:italic;font-size:30px;color:#b9b3a0}}
.top .r{{font-family:Inter,sans-serif;font-size:17px;letter-spacing:6px;color:#b9b3a0}}
.mast{{position:absolute;left:96px;top:{150 if h>1000 else 126}px;font-size:{big}px;font-weight:600;line-height:.95}}
.tag{{position:absolute;left:96px;top:{260 if h>1000 else 210}px;font-style:italic;font-size:34px;color:{GOLD}}}
.eb{{position:absolute;left:96px;top:{390 if h>1000 else 278}px;font-family:Inter,sans-serif;font-size:18px;letter-spacing:6px;color:{GOLD};font-weight:600;text-transform:uppercase}}
.head{{position:absolute;left:96px;right:96px;top:{432 if h>1000 else 312}px;font-size:{66 if h>1000 else 52}px;font-weight:600;line-height:1.05}}
ul{{position:absolute;left:96px;right:96px;top:{720 if h>1000 else 520}px;list-style:none}}
li{{font-size:{40 if h>1000 else 32}px;font-style:italic;line-height:1.25;margin-bottom:{18 if h>1000 else 10}px;padding-left:52px;position:relative}}
li:before{{content:"\\2713";position:absolute;left:0;color:{GOLD};font-style:normal}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:{170 if h>1000 else 140}px;background:{MIDNIGHT};border-top:1.5px solid #8b7a5e;display:flex;justify-content:space-between;align-items:center;padding:0 96px}}
.brand{{font-size:52px;letter-spacing:12px;font-weight:500}}
.brand small{{display:block;font-family:Inter,sans-serif;font-size:14px;letter-spacing:5px;color:{GOLD};margin-top:4px}}
.means{{font-style:italic;font-size:34px;color:{GOLD}}}
</style></head><body>
<div class="top"><div class="l">Issue {e(c["issue_no"])} · {e(c["date_long"])}</div><div class="r">WEEKLY · CAIRO</div></div>
<div class="mast">The Rockit Manifest</div>
<div class="tag">What moved. What it means. What to do.</div>
<div class="eb">{e(C["eyebrow"])}</div>
<div class="head">{e(C["headline"])}</div>
<ul>{lines}</ul>
<div class="foot"><div class="brand">ROCKIT<small>TRANSPORT SERVICES &amp; LOGISTICS</small></div><div class="means">Means what it says.</div></div>
</body></html>'''


def main():
    path = Path(sys.argv[1])
    c = json.loads(path.read_text(encoding="utf-8"))
    out = path.parent
    (out / "email.html").write_text(email_html(c), encoding="utf-8")
    (out / "ricos.json").write_text(json.dumps(ricos(c), ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "cover_4x5.html").write_text(cover(c, 1080, 1350), encoding="utf-8")
    (out / "cover_4x3.html").write_text(cover(c, 1200, 900), encoding="utf-8")
    (out / "social.json").write_text(json.dumps(c["social"], ensure_ascii=False, indent=1), encoding="utf-8")
    print("built", out)


if __name__ == "__main__":
    main()
