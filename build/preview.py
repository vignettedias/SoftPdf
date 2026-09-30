"""Render all figures of a module to a PNG sheet for checking."""
import sys, os, importlib
sys.path[:0] = ['lib', '.']
import figures
mod = importlib.import_module(sys.argv[1])
ids = sys.argv[2:] or list(mod.FIGS)
parts = []
for fid in ids:
    cap, art, opts = figures.get(fid)
    parts.append(f'<div style="border:1px solid #ccc;margin:6pt;padding:4pt;display:inline-block;vertical-align:top"><div style="font:8pt sans-serif">{fid} — {cap}</div>{art}</div>')
html = f'<html><head><link rel="stylesheet" href="style.css"><style>@page{{size:900pt 1400pt;margin:10pt}}</style></head><body>{"".join(parts)}</body></html>'
open('preview.html', 'w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = b.new_page(); pg.goto('file://' + os.path.abspath('preview.html')); pg.wait_for_timeout(300)
    pg.pdf(path='out/preview.pdf', prefer_css_page_size=True, print_background=True); b.close()
import pymupdf
d = pymupdf.open('out/preview.pdf')
S = '/tmp/claude-0/-home-user-SoftPdf/9d7e7cf2-29c6-519a-965a-625e1d86ff51/scratchpad/'
for i, pg in enumerate(d):
    pg.get_pixmap(dpi=int(os.environ.get('DPI', 110))).save(S + f'prev{i}.png')
print(d.page_count)
