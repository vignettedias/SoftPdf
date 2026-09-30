"""Figure registry. Each chapter module defines FIGS = {id: (caption, callable|svg, opts)}."""
import os, re, hashlib, importlib
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
SOM = os.path.join(HERE, '..', 'Soft1.pdf')
_som = None
_cache = {}
REG = {}
for mod in ('figs4', 'figs5', 'figs6', 'figs7', 'figs8'):
    try:
        m = importlib.import_module(mod)
        REG.update(m.FIGS)
    except ModuleNotFoundError:
        pass


def clip_svg(page_idx, rect, prefix, masks=()):
    """Vector clip of a region of a page of the real book, returned as inline SVG at printed size."""
    global _som
    if _som is None:
        _som = pymupdf.open(SOM)
    r = pymupdf.Rect(rect)
    tmp = pymupdf.open()
    p = tmp.new_page(width=r.width, height=r.height)
    p.show_pdf_page(p.rect, _som, page_idx, clip=r)
    for m in masks:
        mr = pymupdf.Rect(m) - (r.x0, r.y0, r.x0, r.y0)
        p.draw_rect(mr, color=None, fill=(1, 1, 1))
    svg = p.get_svg_image(text_as_path=True)
    # make every id unique to this figure so clip paths/glyph defs of several inlined SVGs never collide
    svg = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}_{m.group(1)}"', svg)
    svg = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{prefix}_{m.group(1)})', svg)
    svg = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{prefix}_{m.group(1)}"', svg)
    svg = re.sub(r'<\?xml[^>]*>', '', svg)
    svg = re.sub(r'<svg ', f'<svg style="width:{r.width}pt;height:{r.height}pt" ', svg, count=1)
    return svg


def get(fid):
    if fid not in REG:
        raise KeyError(f'no figure {fid}')
    cap, art, opts = REG[fid]
    if fid not in _cache:
        if isinstance(art, tuple) and art[0] == 'clip':
            _cache[fid] = clip_svg(art[1], art[2], fid.replace('-', '_'), opts.get('masks', ()))
        elif callable(art):
            _cache[fid] = art()
        else:
            _cache[fid] = art
    return cap, _cache[fid], opts
