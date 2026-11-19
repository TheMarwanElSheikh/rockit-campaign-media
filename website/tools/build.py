#!/usr/bin/env python3
"""Applies the portrait fix to each tool of rockit-transport.com.

    python3 website/tools/build.py            # src/*.html -> dist/*.html
    python3 website/tools/build.py --check    # exit 1 if dist/ is not what src/ + the fix give

src/   each tool's embed code as the site serves it (the HTML element's code in Wix Studio)
dist/  the same code with portrait.css and portrait.js appended: what is pasted back into the HTML element

The fix is appended, never merged into a tool's own code, so a tool edited in Wix later is re-fixed by saving its new
code over its file in src/ and running this again. Building twice changes nothing: an earlier fix is removed first.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
OPEN, CLOSE = '<!-- rm-portrait -->', '<!-- /rm-portrait -->'


def strip(html: str) -> str:
    return re.sub(re.escape(OPEN) + r'.*?' + re.escape(CLOSE) + r'\n?', '', html, flags=re.S)


def fixed(html: str) -> str:
    css = (HERE / 'portrait.css').read_text(encoding='utf-8')
    js = (HERE / 'portrait.js').read_text(encoding='utf-8')
    if '</style' in css.lower() or '</script' in js.lower():
        raise SystemExit('portrait.css / portrait.js must not contain a closing style or script tag')
    block = f'{OPEN}\n<style id="rm-portrait">\n{css}</style>\n<script id="rm-portrait-js">\n{js}</script>\n{CLOSE}\n'
    return strip(html).rstrip('\n') + '\n' + block


def main() -> int:
    check = '--check' in sys.argv
    (HERE / 'dist').mkdir(exist_ok=True)
    stale = []
    for src in sorted((HERE / 'src').glob('*.html')):
        out = HERE / 'dist' / src.name
        html = fixed(src.read_text(encoding='utf-8'))
        if check:
            if not out.exists() or out.read_text(encoding='utf-8') != html:
                stale.append(src.name)
        else:
            out.write_text(html, encoding='utf-8')
            print(f'{src.name}: {len(html):,} bytes')
    if stale:
        print('dist/ is out of date for: ' + ', '.join(stale) + ' (run build.py)')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
