#!/usr/bin/env python3
"""Email version of a full edition (the standard from Voyage 002).

    python3 edition_email.py ../issues/<date>/edition.json --pdf PDF_URL --web POST_URL --img IMG_BASE

Writes <issue>/edition/email.html: a 640px, table-based, inline-styled email that carries the cover story, the
week in 60 seconds, the numbers, the chokepoint status and Rockit's read, then sends readers to the 16-page PDF and the
web post. Brand: the owner's logo (logo.png from brand/rockit-logo.png) on WHITE in the header and footer; gold is the
logo's gradient on rules and buttons (with a solid fallback colour for clients that drop gradients); small gold text
on white uses #8a6514. Every figure in the email is one the edition sources; the footer says where the sources are.
"""
import argparse
import html
import json
import re
from pathlib import Path

from build_issue import GOLD_GRAD_H, GOLD_MID, GOLD_INK, NAVY, INK, MUTED, SERIF, SANS, MONO, FONTS

PAPER = "#faf7ef"
RULE = "#e3d8bd"


def e(s):
    return html.escape(str(s), quote=True)


def md(s):
    """**bold** and *italic* to HTML, everything else escaped."""
    s = e(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    return s


def gold_rule(h=3):
    return (f'<tr><td style="background:{GOLD_MID};background-image:{GOLD_GRAD_H};height:{h}px;line-height:{h}px;font-size:{h}px;">'
            f'&nbsp;</td></tr>')


def row(inner, bg="#ffffff", pad="28px 36px"):
    return f'<tr><td style="background:{bg};padding:{pad};">{inner}</td></tr>'


def kicker(t):
    return (f'<div style="font-family:{MONO};font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:{GOLD_INK};'
            f'font-weight:600;margin:0 0 12px 0;">{e(t)}</div>')


def button(label, url, primary=True):
    if primary:
        return (f'<a href="{e(url)}" style="display:inline-block;font-family:{MONO};font-size:12px;letter-spacing:2px;text-transform:uppercase;'
                f'font-weight:600;color:{NAVY};background-color:{GOLD_MID};background-image:{GOLD_GRAD_H};padding:13px 18px;'
                f'text-decoration:none;margin:0 8px 8px 0;">{e(label)} ▸</a>')
    return (f'<a href="{e(url)}" style="display:inline-block;font-family:{MONO};font-size:12px;letter-spacing:2px;text-transform:uppercase;'
            f'font-weight:600;color:{NAVY};background:#ffffff;border:1px solid {NAVY};padding:12px 17px;text-decoration:none;'
            f'margin:0 8px 8px 0;">{e(label)} ▸</a>')


STATE = {"open": "#2e6b4a", "partial": "#a5561b", "restricted": "#9a3b2e"}


def find_block(pages, kind, kicker_text=None):
    """First block of a kind (searching grids/boxes), optionally right after a kicker with this text."""
    def walk(blocks):
        prev = None
        for b in blocks:
            if b.get("k") == kind and (kicker_text is None or (prev and prev.get("text") == kicker_text)):
                yield b
            for key in ("blocks",):
                if key in b:
                    yield from walk(b[key])
            if b.get("k") == "grid":
                for col in b["columns"]:
                    yield from walk(col)
            prev = b
    for p in pages:
        for b in walk(p["blocks"]):
            return b
    return None


def build(ed, pdf, web, img):
    c, m = ed["cover"], ed["meta"]
    brief = ed["pages"][0]
    ticks = find_block([brief], "ticks", "The week in 60 seconds")
    read = None
    for b in brief["blocks"]:
        if b.get("k") == "grid":
            for col in b["columns"]:
                for x in col:
                    if x.get("k") == "box":
                        read = x
    R = []
    # header: the owner's logo on white
    R.append(f'<tr><td style="background:#ffffff;padding:30px 36px 22px 36px;"><img src="{e(img)}logo.png" width="250" alt="Rock it Transport Services" '
             f'style="display:block;width:250px;height:auto;border:0;"></td></tr>')
    R.append(gold_rule())
    R.append(f'<tr><td style="background:{PAPER};padding:11px 36px;border-bottom:1px solid {RULE};">'
             f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
             f'<td style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:{MUTED};text-transform:uppercase;">The Rockit Manifest · Voyage {e(m["voyage"])} · {e(m["date_long"])}</td>'
             f'<td align="right"><a href="{e(web)}" style="font-family:{MONO};font-size:10px;letter-spacing:2px;color:{GOLD_INK};text-decoration:none;font-weight:600;">READ ONLINE ▸</a></td>'
             f'</tr></table></td></tr>')
    # masthead + cover image
    R.append(row(f'<a href="{e(pdf)}"><img src="{e(img)}web/cover_full_4x3.jpg" width="568" alt="The Rockit Manifest · {e(c["headline"])}" '
                 f'style="display:block;width:100%;max-width:568px;height:auto;border:1px solid {RULE};"></a>', pad="26px 36px 6px 36px"))
    # cover story
    R.append(row(kicker(c["kicker"]) +
                 f'<div style="font-family:{SERIF};font-size:30px;line-height:1.12;font-weight:600;color:{INK};margin-bottom:12px;">{md(c["headline"])}</div>'
                 f'<div style="font-family:{SERIF};font-size:19px;line-height:1.45;font-style:italic;color:#3a4152;margin-bottom:14px;">{md(c["deck"])}</div>'
                 f'<div style="font-family:{SANS};font-size:15px;line-height:1.65;color:{INK};">{md(c["standfirst"])}</div>'
                 f'<div style="margin-top:20px;">{button("Download the full 16-page edition (PDF)", pdf)}{button("Read it online", web, False)}</div>',
                 pad="22px 36px 26px 36px"))
    # numbers
    nums = "".join(
        f'<td width="{100 // len(c["numbers"])}%" valign="top" style="padding:0 6px 0 0;"><div style="border-top:2px solid {INK};padding-top:8px;">'
        f'<div style="font-family:{SERIF};font-size:24px;font-weight:700;color:{NAVY};line-height:1.05;">{e(n["value"])}</div>'
        f'<div style="font-family:{SANS};font-size:11px;line-height:1.4;color:#3a4152;margin-top:4px;">{md(n["label"])}</div></div></td>'
        for n in c["numbers"])
    R.append(row(kicker("The week in numbers") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{nums}</tr></table>',
                 bg=PAPER, pad="24px 36px"))
    # 60 seconds
    if ticks:
        items = "".join(f'<tr><td valign="top" style="font-family:{SANS};font-size:14px;color:{GOLD_INK};padding:0 10px 10px 0;">✓</td>'
                        f'<td style="font-family:{SANS};font-size:14px;line-height:1.6;color:{INK};padding:0 0 10px 0;">{md(t)}</td></tr>' for t in ticks["items"])
        R.append(row(kicker("The week in 60 seconds") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{items}</table>'))
    # status board
    st = "".join(
        f'<tr><td style="padding:9px 0;border-bottom:1px solid {RULE};font-family:{SERIF};font-size:17px;color:{INK};width:34%;" valign="top">{e(s["name"])}</td>'
        f'<td style="padding:11px 8px;border-bottom:1px solid {RULE};font-family:{MONO};font-size:10px;letter-spacing:1.5px;text-transform:uppercase;font-weight:600;color:{STATE[s["state"]]};width:22%;" valign="top">● {e(s["label"])}</td>'
        f'<td style="padding:9px 0;border-bottom:1px solid {RULE};font-family:{SANS};font-size:12.5px;line-height:1.5;color:#3a4152;" valign="top">{md(s["note"])}</td></tr>'
        for s in c.get("status", []))
    if st:
        R.append(row(kicker(f'Chokepoint status · {c.get("status_asof", "")}') + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{st}</table>'))
    # Rockit's read
    if read:
        rt = find_block([{"blocks": read["blocks"]}], "ticks")
        items = "".join(f'<div style="font-family:{SANS};font-size:14px;line-height:1.6;color:{INK};padding:8px 0;border-bottom:1px solid {RULE};">{md(t)}</div>' for t in rt["items"])
        R.append(row(kicker(read.get("kicker", "Rockit's read")) +
                     f'<div style="font-family:{SERIF};font-size:22px;font-weight:600;color:{NAVY};margin-bottom:6px;">{md(read.get("title", ""))}</div>{items}',
                     bg=PAPER))
    # inside the edition
    toc = "".join(f'<tr><td style="font-family:{MONO};font-size:11px;color:{GOLD_INK};font-weight:600;padding:5px 12px 5px 0;" valign="top">{e(x["p"])}</td>'
                  f'<td style="font-family:{SANS};font-size:13px;color:{INK};padding:5px 0;border-bottom:1px solid {RULE};"><b>{e(x["sec"])}</b>'
                  f'<span style="color:{MUTED};"> · {e(x["what"])}</span></td></tr>' for x in c["contents"])
    R.append(row(kicker("Inside the full edition") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{toc}</table>'
                 f'<div style="margin-top:20px;">{button("Download the PDF", pdf)}</div>'))
    # next week + CTA
    b = ed["back"]
    nxt = "".join(f'<div style="font-family:{SERIF};font-size:17px;color:{INK};padding:6px 0;border-bottom:1px solid {RULE};">'
                  f'<span style="font-family:{MONO};font-size:11px;color:{GOLD_INK};font-weight:600;margin-right:10px;">{i:02d}</span>{md(x)}</div>'
                  for i, x in enumerate(b.get("next", []), 1))
    R.append(row(kicker("Next Monday in The Rockit Manifest") + nxt, bg=PAPER))
    R.append(row(f'<div style="font-family:{SERIF};font-size:24px;line-height:1.3;color:{INK};font-weight:600;margin-bottom:16px;">{md(b["cta"])}</div>'
                 f'<a href="mailto:inquiry@rockit.com.eg" style="display:inline-block;font-family:{MONO};font-size:12px;letter-spacing:2px;text-transform:uppercase;'
                 f'font-weight:600;color:#ffffff;background:{NAVY};padding:13px 20px;text-decoration:none;">Send us a lane ▸</a>'
                 f'<div style="font-family:{MONO};font-size:11px;letter-spacing:2px;color:{GOLD_INK};margin-top:18px;">— THE ROCKIT DESK · CAIRO · ALEXANDRIA · SOKHNA · PORT SAID · DAMIETTA</div>'))
    R.append(gold_rule())
    # footer: the owner's logo on white
    R.append(row(f'<img src="{e(img)}logo.png" width="210" alt="Rock it Transport Services" style="display:block;width:210px;height:auto;border:0;">'
                 f'<div style="font-family:{SERIF};font-size:18px;font-style:italic;color:{GOLD_INK};margin:14px 0 10px 0;">Means what it says.</div>'
                 f'<div style="font-family:{SANS};font-size:12px;line-height:1.6;color:#4a5263;"><a href="https://www.rockit-transport.com" style="color:#4a5263;">rockit-transport.com</a> · +20 2 2690 7601 · inquiry@rockit.com.eg</div>'
                 f'<div style="font-family:{SANS};font-size:11px;line-height:1.6;color:#6a7282;margin-top:12px;">Every figure in this email is footnoted to its source in the full edition (pages 14–15 of the PDF). {e(ed["disclaimer"])}</div>',
                 pad="28px 36px 32px 36px"))
    subject = f'{c["headline"]} | The Rockit Manifest {m["voyage"]}'
    pre = re.sub(r"\*", "", c["deck"])[:150]
    return subject, pre, f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><title>{e(subject)}</title>{FONTS}
<style>@media (max-width:620px){{.wrap{{width:100%!important}} td{{padding-left:18px!important;padding-right:18px!important}}}}</style></head>
<body style="margin:0;padding:0;background:#ece7da;"><div style="display:none;max-height:0;overflow:hidden;opacity:0;">{e(pre)}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ece7da;"><tr><td align="center" style="padding:24px 10px;">
<table role="presentation" class="wrap" width="640" cellpadding="0" cellspacing="0" style="width:640px;max-width:640px;background:#ffffff;">
{"".join(R)}
</table></td></tr></table></body></html>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edition")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--web", required=True)
    ap.add_argument("--img", required=True, help="URL prefix of the issue's edition/ folder (ends with /)")
    a = ap.parse_args()
    p = Path(a.edition).resolve()
    ed = json.loads(p.read_text())
    subject, pre, doc = build(ed, a.pdf, a.web, a.img)
    out = p.parent / "edition" / "email.html"
    out.write_text(doc)
    (p.parent / "edition" / "email_meta.json").write_text(json.dumps({"subject": subject, "preheader": pre}, ensure_ascii=False, indent=1))
    print("wrote", out, "|", subject)


if __name__ == "__main__":
    main()
