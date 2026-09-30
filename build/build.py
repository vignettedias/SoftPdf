#!/usr/bin/env python3
"""Build the textbook-style printout.

Markdown (with custom blocks) -> HTML with print CSS -> headless Chrome PDF
-> PyMuPDF composition onto A4 (mirrored page placement, running heads,
chapter openers, cover).
"""
import os, re, sys, json, html
import markdown
import pymupdf
FIG_SCALE = float(os.environ.get('FIG_SCALE', 0.87))  # global figure reduction for a compact printout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))
sys.path.insert(0, HERE)
from chapters import CHAPTERS            # noqa: E402
import figures                            # noqa: E402

OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
SOM = os.path.join(HERE, '..', 'Soft1.pdf')

# ---------------------------------------------------------------- geometry
# Book page geometry measured on the source PDF (letter-size page, pt).
CONTENT_X = {0: 87.5, 1: 101.35}   # even (verso) / odd (recto) left edge of 424pt content
TOP_Y = 126.2                      # top of chrome page on the letter page (calibrated)
A4 = pymupdf.paper_rect('a4')
DX, DY = (A4.width - 612) / 2, (A4.height - 792) / 2   # letter page centred on A4
CHROME_W, CHROME_H = 424, 562.5
MD_EXT = ['tables', 'fenced_code', 'sane_lists', 'smarty', 'attr_list', 'md_in_html']


def md(text):
    return markdown.markdown(text, extensions=MD_EXT, extension_configs={
        'smarty': {'smart_angled_quotes': False}})


def md_inline(text):
    h = md(text).strip()
    return re.sub(r'^<p>(.*)</p>$', r'\1', h, flags=re.S)


# ---------------------------------------------------------------- source
class Chapter:
    def __init__(self, meta):
        self.meta = meta
        self.n = meta['n']
        self.src = open(os.path.join(HERE, 'src', meta['file'])).read()
        self.fig_no, self.ex_no = {}, {}

    def number_things(self):
        f = e = 0
        for m in re.finditer(r'^(@fig|@table|::: example) +([\w-]+)', self.src, re.M):
            if m.group(1) == '::: example':
                e += 1
                self.ex_no[m.group(2)] = f'{self.n}.{e}'
            else:
                f += 1
                self.fig_no[m.group(2)] = f'{self.n}.{f}'

    def refs(self, s):
        def r(m):
            kind, key = m.group(1), m.group(2)
            table = (GLOBAL_FIG if kind == 'fig' else GLOBAL_EX)
            if key not in table:
                raise KeyError(f'unresolved reference {kind}:{key} in chapter {self.n}')
            return ('Figure ' if kind == 'fig' else 'Example ') + table[key]
        return re.sub(r'\[\[(fig|ex):([\w-]+)\]\]', r, s)

    def figure_html(self, fid, extra=''):
        cap, art, opts = figures.get(fid)
        num = self.fig_no[fid]
        cls = 'fig' + (' wide' if opts.get('wide') else '') + (' top' if opts.get('top') else '') + (' tbl' if '<table' in art else '')
        caph = f'<div class="cap"><b>Figure {num}</b>&ensp;{md_inline(cap)}</div>'
        sc = opts.get('scale', 1) * (1 if '<table' in art else FIG_SCALE)
        if sc != 1:
            art = re.sub(r'width="([\d.]+)pt" height="([\d.]+)pt"', lambda m: f'width="{float(m.group(1))*sc:.1f}pt" height="{float(m.group(2))*sc:.1f}pt"', art, count=1)
            art = re.sub(r'style="width:([\d.]+)pt;height:([\d.]+)pt"', lambda m: f'style="width:{float(m.group(1))*sc:.1f}pt;height:{float(m.group(2))*sc:.1f}pt"', art, count=1)
        arth = f'<div class="art">{art}</div>'
        if '<table' in art:
            capt = f'<caption class="tcap"><div class="cap"><b>Figure {num}</b>&ensp;{md_inline(cap)}</div></caption>'
            return f'<div class="fig top tbl" id="{fid}">{caph}<div class="art">{art}</div></div>'
        if opts.get('wide'):
            return f'<div class="{cls}" id="{fid}">{arth}{caph}</div>'
        return f'<div class="{cls}" id="{fid}">{caph}{arth}</div>'

    def example_html(self, eid, title, body):
        parts = re.split(r'^--- *(solution|answer) *$', body, flags=re.M)
        q = parts[0]
        sections = dict(zip(parts[1::2], parts[2::2]))
        # figures named in the question are set after the frame, which spans the full width
        qfigs = re.findall(r'^@(?:fig|table) +[\w-]+\s*$', q, flags=re.M)
        q = re.sub(r'^@(?:fig|table) +[\w-]+\s*$\n?', '', q, flags=re.M)
        out = [f'<div class="ex" id="{eid}"><div class="qbox"><div class="ext"><span class="n">Example {self.ex_no[eid]}</span>{md_inline(title)}</div>']
        out.append(f'<div class="q">{self.blocks(q)}</div></div>')
        if qfigs:
            out.append(self.blocks('\n\n'.join(qfigs)))
        tail = []
        if 'solution' in sections:
            tail.append(f'<div class="sol">{self.blocks(sections["solution"], lead="Solution")}</div>')
        if 'answer' in sections:
            tail.append(f'<div class="ans">{self.blocks(sections["answer"], lead="Answer")}</div>')
        if tail:
            last = tail[-1]
            k = max(last.rfind('</p>'), last.rfind('</li>'))
            if k > 0:  # end-of-example mark after the last line of text
                tail[-1] = last[:k] + '<span class="eoe"></span>' + last[k:]
        out += tail
        out.append('</div>')
        return '\n'.join(out)

    def blocks(self, text, lead=None):
        """Convert a chunk that may contain @fig lines and headings."""
        out, buf = [], []

        def flush():
            if buf:
                out.append(md('\n'.join(buf)))
                buf.clear()
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            ln = lines[i]
            m = re.match(r'^@(fig|table) +([\w-]+)\s*$', ln)
            if m:
                flush(); out.append(self.figure_html(m.group(2))); i += 1; continue
            m = re.match(r'^(##|###) +([\d.]+) +(.*)$', ln)
            if m:
                flush()
                if m.group(1) == '##':
                    out.append(f'<h2 class="sec" data-num="{m.group(2)}"><span class="num">{m.group(2)}</span><span class="t">{md_inline(m.group(3))}</span></h2>')
                else:
                    out.append(f'<h3 class="sub"><span class="num">{m.group(2)}</span>{md_inline(m.group(3))}</h3>')
                i += 1; continue
            m = re.match(r'^::: *example +([\w-]+) *\| *(.*)$', ln)
            if m:
                flush()
                j = i + 1
                depth = 0
                while j < len(lines) and not (lines[j].strip() == ':::' and depth == 0):
                    j += 1
                out.append(self.example_html(m.group(1), m.group(2), '\n'.join(lines[i + 1:j])))
                i = j + 1; continue
            m = re.match(r'^::: *keypoints *$', ln)
            if m:
                flush()
                j = i + 1
                while lines[j].strip() != ':::':
                    j += 1
                out.append(f'<div class="kp"><h2>KEY POINTS</h2><div class="box">{md(chr(10).join(lines[i+1:j]))}</div></div>')
                i = j + 1; continue
            buf.append(ln); i += 1
        flush()
        h = '\n'.join(out)
        if lead:
            h = re.sub(r'^\s*<p>', f'<p><span class="lbl">{lead}</span>', h, count=1)
        return h

    def opener_html(self, parity):
        m = self.meta
        cx = CONTENT_X[parity]
        X = lambda x: x - cx       # letter-page x -> chrome x
        Y = lambda y: y - TOP_Y
        title = '<br>'.join(m['title_lines'])
        obj = ''.join(f'<li>{md_inline(o)}</li>' for o in m['objectives'])
        toc = ''.join(f'<div><b>{n}</b>{md_inline(t)}</div>' for n, t in m['toc'])
        ob_top = 322.5 if len(m['title_lines']) == 1 else 330
        return f'''<div class="opener">
<div class="cn" style="left:{X(200.3)}pt;top:{Y(148.8)}pt">{self.n}</div>
<div class="rule" style="left:{X(188.4)}pt;top:{Y(192.1)}pt"></div>
<div class="ct" style="left:{X(193.2)}pt;top:{Y(199.5)}pt">{title}</div>
<div class="ob" style="left:{X(231.4)}pt;top:{Y(ob_top)}pt"><h4>Objectives</h4>
<p>{md_inline(m['objective_lead'])}</p><ul>{obj}</ul>
<div class="toc"><h4>Contents</h4>{toc}</div></div></div>'''

    def html(self):
        parity = self.meta['start'] % 2
        body = self.blocks(self.refs(self.src))
        body = body.replace('<h2 class="sec"', '<h2 class="sec first"', 1) if self.meta.get('first_sec_top') else body
        return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<link rel="stylesheet" href="style.css"></head><body>
{self.opener_html(parity)}
<div class="flow">{body}</div></body></html>'''


# ---------------------------------------------------------------- chrome
def render(chs):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        for ch in chs:
            path = os.path.join(HERE, f'ch{ch.n}.html')
            open(path, 'w').write(ch.html())
            pg.goto('file://' + path)
            pg.wait_for_timeout(300)
            pg.pdf(path=os.path.join(OUT, f'ch{ch.n}.pdf'), prefer_css_page_size=True, print_background=True)
        b.close()


# ---------------------------------------------------------------- compose
FONTS = {k: os.path.join(HERE, 'fonts', v) for k, v in
         {'reg': 'FiraSans-400.ttf', 'med': 'FiraSans-500.ttf', 'bold': 'FiraSans-700.ttf'}.items()}
INK = (0x23 / 255, 0x1F / 255, 0x20 / 255)
SQ = (0x6C / 255, 0xCF / 255, 0xF6 / 255)
CYAN = (0, 0xAD / 255, 0xEF / 255)
KP = (0xE9 / 255, 0xF7 / 255, 0xFE / 255)


def page_is_blank(p):
    return not p.get_text().strip() and not p.get_drawings() and not p.get_images()


def section_heads(p):
    """Return section headings (number, title) that start on this chrome page."""
    found = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if abs(s['size'] - 13.4) < 0.3 and s['color'] == 0x00ADEF:
                    found.append((l['bbox'][1], s['text']))
    heads = []
    nums = [(y, t) for y, t in found if re.match(r'^\d+\.\d+$', t.strip())]
    return found


def text_w(s, font, size):
    return pymupdf.Font(fontfile=FONTS[font]).text_length(s, fontsize=size)


def compose(chs, out_pdf):
    doc = pymupdf.open()
    som = pymupdf.open(SOM)
    # cover: the book's front cover, at trim size
    cov = doc.new_page(width=A4.width, height=A4.height)
    trim = pymupdf.Rect(36 + DX, 63.5 + DY, 576 + DX, 729.5 + DY)
    cov.insert_image(trim, filename=os.path.join(HERE, 'cover_src.jpeg'))
    opener_img = os.path.join(HERE, 'opener.png')
    report = []
    for ch in chs:
        src = pymupdf.open(os.path.join(OUT, f'ch{ch.n}.pdf'))
        # drop empty trailing pages
        while src.page_count and page_is_blank(src[src.page_count - 1]):
            src.delete_page(src.page_count - 1)
        while (doc.page_count + 1) % 2 != ch.meta['start'] % 2:
            doc.new_page(width=A4.width, height=A4.height)
            report.append((ch.n, None, 'blank'))
        cur_sec = None
        heads = {k: re.sub(r'[*_`]', '', v) for k, v in re.findall(r'^## ([\d.]+) +(.*)$', ch.src, re.M)}
        for k in range(src.page_count):
            folio = ch.meta['start'] + k
            par = folio % 2
            sp = src[k]
            txt = sp.get_text()
            kp = 'KEY POINTS' in txt
            pg = doc.new_page(width=A4.width, height=A4.height)
            if kp:
                pg.draw_rect(pymupdf.Rect(32.9 + DX, 59.5 + DY, 579.97 + DX, 733.54 + DY), color=None, fill=KP)
            x0 = CONTENT_X[par] + DX
            pg.show_pdf_page(pymupdf.Rect(x0, TOP_Y + DY, x0 + CHROME_W, TOP_Y + DY + CHROME_H), src, k)
            nums = []
            for bl in sp.get_text('dict')['blocks']:
                for l in bl.get('lines', []):
                    for s_ in l['spans']:
                        if s_['color'] == 0xFFFFFF and abs(s_['size'] - 12.2) < 0.3 and re.match(r'^\d+\.\d+$', s_['text'].strip()):
                            nums.append((l['bbox'][1], s_['text'].strip()))
            nums.sort()
            if k == 0:
                pg.insert_image(pymupdf.Rect(32.42 + DX, 59.02 + DY, 180.02 + DX, 734.09 + DY), filename=opener_img)
                pg.draw_line((179.4 + DX, 59.05 + DY), (179.4 + DX, 734.02 + DY), color=CYAN, width=1.5)
                report.append((ch.n, folio, 'opener'))
                continue
            head_sec = nums[0][1] if nums and nums[0][0] < 40 else cur_sec
            if nums:
                cur_sec = nums[-1][1]
            # running head
            y = 103.2 + DY
            if par == 0:
                xl = 87.5 + DX
                pg.insert_text((xl, y), str(folio), fontfile=FONTS['bold'], fontname='FB', fontsize=10, color=INK)
                xx = xl + text_w(str(folio), 'bold', 10) + 10.7
                left = f'Chapter {ch.n}'
                right = 'Key points' if kp else ch.meta['title']
                pg.insert_text((xx, y), left, fontfile=FONTS['reg'], fontname='FR', fontsize=10, color=INK)
                xx += text_w(left, 'reg', 10) + 4.2
                pg.draw_rect(pymupdf.Rect(xx, y - 6.4, xx + 5.6, y - 0.8), color=None, fill=SQ)
                xx += 5.6 + 4.4
                pg.insert_text((xx, y), right, fontfile=FONTS['reg'], fontname='FR', fontsize=10, color=INK)
                pg.draw_line((87.48 + DX, 110.38 + DY), (511.38 + DX, 110.38 + DY), color=INK, width=0.5)
            else:
                xr = 525.4 + DX
                wn = text_w(str(folio), 'bold', 10)
                pg.insert_text((xr - wn, y), str(folio), fontfile=FONTS['bold'], fontname='FB', fontsize=10, color=INK)
                if kp:
                    left, right = f'Chapter {ch.n}', 'Key points'
                elif head_sec:
                    left, right = head_sec, heads[head_sec]
                else:
                    left, right = f'Chapter {ch.n}', ch.meta['title']
                xx = xr - wn - 10.7 - text_w(right, 'reg', 10)
                pg.insert_text((xx, y), right, fontfile=FONTS['reg'], fontname='FR', fontsize=10, color=INK)
                xx -= 4.4 + 5.6
                pg.draw_rect(pymupdf.Rect(xx, y - 6.4, xx + 5.6, y - 0.8), color=None, fill=SQ)
                xx -= 4.2 + text_w(left, 'reg', 10)
                pg.insert_text((xx, y), left, fontfile=FONTS['reg'], fontname='FR', fontsize=10, color=INK)
                pg.draw_line((101.35 + DX, 110.4 + DY), (525.33 + DX, 110.4 + DY), color=INK, width=0.5)
            report.append((ch.n, folio, head_sec))
        # page labels
    doc.set_metadata({'title': 'Software Engineering', 'author': 'Ian Sommerville', 'creator': '', 'producer': ''})
    doc.save(out_pdf, garbage=4, deflate=True)
    return report


GLOBAL_FIG, GLOBAL_EX = {}, {}

if __name__ == '__main__':
    only = [int(a) for a in sys.argv[1:] if a.isdigit()]
    allch = [Chapter(m) for m in CHAPTERS]
    for c in allch:
        c.number_things(); GLOBAL_FIG.update(c.fig_no); GLOBAL_EX.update(c.ex_no)
    chs = [c for c in allch if not only or c.n in only]
    render(chs)
    rep = compose(chs, os.path.join(OUT, 'book.pdf'))
    json.dump(rep, open(os.path.join(OUT, 'report.json'), 'w'))
    print('pages', len(rep) + 1)
