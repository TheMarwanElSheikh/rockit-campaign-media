#!/usr/bin/env python3
"""Website (Wix Blog / Ricos) version of a full edition.

    python3 edition_web.py ../issues/<date>/edition.json PDF_URL

Writes <issue>/edition/web/ricos.json. Image nodes carry "@<key>" ids (chart_NN, timeline) that the stager swaps for
Wix media ids after importing edition/web/*.png. Every story ends with a "Sources:" line that links each source used.
Tables become bulleted lists; html-only blocks are converted where they hold text (quote anatomy, glossary).
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_issue import T_, P_, H_, UL  # noqa: E402  (same Ricos node helpers as the short edition)


def plain(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", s)
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def rich(s):
    """**bold** and *italic* to Ricos text nodes."""
    out = []
    for part in re.split(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*))", s):
        if not part:
            continue
        if part.startswith("**"):
            out.append(T_(part[2:-2], bold=True))
        elif part.startswith("*"):
            out.append(T_(part[1:-1], italic=True))
        else:
            out.append(T_(part))
    return out


class Web:
    def __init__(self, ed, dims):
        self.ed, self.dims, self.nodes, self.chart_i = ed, dims, [], 0
        self.src = ed["sources"]

    def srcline(self, ids):
        if not ids:
            return
        out = [T_("Sources: ", italic=True)]
        seen = []
        for i in ids:
            if i in seen:
                continue
            seen.append(i)
            s = self.src[i]
            out.append(T_(f'{s["name"]} ({s["date"]})', italic=True, link=s["url"]))
            out.append(T_(" · ", italic=True))
        self.nodes.append(P_(*out[:-1]))

    def why(self, text, label="Why it matters"):
        self.nodes.append({"type": "BLOCKQUOTE", "nodes": [P_(T_(label + ": ", bold=True), *rich(text))], "blockquoteData": {"indentation": 1}})

    def image(self, key, alt):
        w, h = self.dims[key]
        self.nodes.append({"type": "IMAGE", "nodes": [], "imageData": {"containerData": {"width": {"size": "CONTENT"}, "alignment": "CENTER"},
                                                                       "image": {"src": {"id": "@" + key}, "width": w, "height": h}, "altText": alt}})

    def block(self, b):
        k = b["k"]
        if k == "p":
            if b.get("cls") == "srcline":
                return
            self.nodes.append(P_(*rich(b["text"])))
            self.srcline(b.get("src"))
        elif k == "lead":
            if b.get("kicker"):
                self.nodes.append(P_(T_(b["kicker"].upper(), bold=True)))
            self.nodes.append(H_(plain(b["head"]), 3))
            if b.get("deck"):
                self.nodes.append(P_(T_(plain(b["deck"]), italic=True)))
            for t in b["text"]:
                self.nodes.append(P_(*rich(t)))
            self.srcline(b.get("src"))
            if b.get("why"):
                self.why(b["why"])
        elif k == "brief":
            tag = (b.get("tag") or "")
            head = plain(b["head"])
            self.nodes.append(H_((tag + ": " if tag and tag != "Why it matters" else "") + head, 4))
            for t in b["text"]:
                self.nodes.append(P_(*rich(t)))
            self.srcline(b.get("src"))
            if b.get("why"):
                self.why(b["why"])
        elif k == "chart":
            self.chart_i += 1
            key = f"chart_{self.chart_i:02d}"
            self.image(key, f'{plain(b["title"])}: {plain(b.get("sub", ""))}')
            if b.get("note"):
                self.nodes.append(P_(T_(plain(b["note"]), italic=True)))
            self.srcline(b.get("src"))
        elif k == "table":
            if b.get("caption"):
                self.nodes.append(P_(T_(b["caption"].upper(), bold=True)))
            items, ids = [], []
            for r in b["rows"]:
                c = [plain(x) for x in r["cells"]]
                items.append([T_(c[0] + ": ", bold=True), T_(" · ".join(c[1:]))])
                ids += r.get("src") or []
            self.nodes.append(UL(items))
            if b.get("note"):
                self.nodes.append(P_(T_(plain(b["note"]), italic=True)))
            self.srcline(ids)
        elif k == "tiles":
            items, ids = [], []
            for t in b["items"]:
                extra = " · ".join(x for x in (t.get("delta"), t.get("asof")) if x)
                items.append([T_(t["value"] + " ", bold=True), T_(plain(t["label"]) + (f" ({extra})" if extra else ""))])
                ids += t.get("src") or []
            self.nodes.append(UL(items))
            self.srcline(ids)
        elif k == "ticks":
            srcs = b.get("srcs") or [None] * len(b["items"])
            self.nodes.append(UL([rich(t) for t in b["items"]]))
            ids = [i for s in srcs if s for i in s]
            self.srcline(ids)
        elif k in ("box", "panel"):
            if b.get("kicker") == "How to read this issue":
                return
            if b.get("kicker") and b.get("title"):
                self.nodes.append(H_(f'{b["kicker"]}: {plain(b["title"])}', 4))
            elif b.get("kicker"):
                self.nodes.append(H_(b["kicker"], 4))
            for x in b["blocks"]:
                self.block(x)
        elif k == "kicker":
            self.nodes.append(H_(b["text"], 4))
        elif k == "h":
            self.nodes.append(H_(plain(b["text"]), 3))
        elif k == "grid":
            for col in b["columns"]:
                for x in col:
                    self.block(x)
        elif k == "flow":
            for x in b["blocks"]:
                self.block(x)
        elif k == "html":
            h = b["html"]
            if 'id="tlg"' in h:
                self.image("timeline", "Timeline of key dates from 16 November 2026 to 10 January 2027")
            elif "<table" in h:
                rows = re.findall(r"<tr><td[^>]*><b>(.*?)</b></td><td[^>]*>(.*?)</td><td[^>]*>(.*?)</td></tr>", h, re.S)
                self.nodes.append(UL([[T_(plain(a) + ": ", bold=True), T_(plain(c) + " "), T_("Ask: " + plain(d), italic=True)] for a, c, d in rows]))
            elif "<b" in h:
                pairs = re.findall(r"<b[^>]*>(.*?)</b> · (.*?)</div>", h, re.S)
                self.nodes.append(UL([[T_(plain(a) + ": ", bold=True), T_(plain(c))] for a, c in pairs]))
            elif "class=\"why\"" in h:
                txt = plain(re.sub(r"<b>.*?</b>", "", h)).replace("(see page 11)", "(see Egypt & the region, below)")
                self.why(txt)

    def build(self, pdf_url):
        ed, c = self.ed, self.ed["cover"]
        n = self.nodes
        n.append(P_(T_(f'Voyage {ed["meta"]["voyage"]} · {ed["meta"]["date_long"]} · {ed["meta"]["pages_label"]} · {len(ed["sources"])} sources, each read and checked', italic=True)))
        n.append(P_(T_("Download the full 16-page edition (PDF) ▸", bold=True, link=pdf_url)))
        n.append(H_(plain(c["headline"]), 2))
        n.append(P_(T_(plain(c["deck"]), italic=True)))
        n.append(P_(*rich(c["standfirst"])))
        self.srcline(c.get("src"))
        n.append(H_("Chokepoint status", 3))
        n.append(UL([[T_(f'{x["name"]}: {x["label"]}. ', bold=True), T_(plain(x["note"]))] for x in c["status"]]))
        self.srcline([i for x in c["status"] for i in x.get("src", [])])
        for pg in ed["pages"]:
            if pg.get("sources_page"):
                continue
            n.append(H_(plain(pg["title"]), 2))
            for b in pg["blocks"]:
                self.block(b)
        n.append(H_("Read the full edition", 2))
        n.append(P_(T_("The 16-page PDF has every chart, the full calendar and glossary, and the numbered list of all sources. "),
                    T_("Download it here ▸", bold=True, link=pdf_url)))
        n.append(P_(T_("Send us a lane: ", bold=True), T_("inquiry@rockit.com.eg", link="mailto:inquiry@rockit.com.eg"), T_(" · +20 2 2690 7601 · Rockit. Means what it says.", italic=True)))
        n.append(P_(T_(plain(ed["disclaimer"]), italic=True)))
        return {"nodes": n}


def main():
    ed_path = Path(sys.argv[1]).resolve()
    pdf_url = sys.argv[2]
    ed = json.loads(ed_path.read_text())
    web = ed_path.parent / "edition" / "web"
    dims = json.loads((web / "dims.json").read_text())
    r = Web(ed, dims).build(pdf_url)
    (web / "ricos.json").write_text(json.dumps(r, ensure_ascii=False))
    imgs = sorted({x["imageData"]["image"]["src"]["id"] for x in r["nodes"] if x["type"] == "IMAGE"})
    print(f"ricos nodes {len(r['nodes'])}; images {imgs}")


if __name__ == "__main__":
    main()
