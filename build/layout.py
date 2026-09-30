"""Fix half-empty pages by deferring the figure that did not fit, front to back.

For each chapter: build it, find the first short page whose successor starts with a
top-level figure, move that figure's @fig line one block later in the source, rebuild.
"""
import re, sys, json, subprocess, pymupdf

DY = (841.89 - 792) / 2


def build(n):
    subprocess.run([sys.executable, 'build.py', str(n)], check=True, capture_output=True)
    return pymupdf.open('out/book.pdf'), json.load(open('out/report.json'))


def page_last_y(p):
    ys = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            if l['bbox'][1] - DY > 115 and ''.join(s['text'] for s in l['spans']).strip():
                ys.append(l['bbox'][3] - DY)
    for dr in p.get_drawings():
        if dr['rect'].y0 - DY > 115 and dr['rect'].width < 540:
            ys.append(dr['rect'].y1 - DY)
    return max(ys) if ys else 0


def first_fig(p):
    """Figure number whose art starts the page, if any."""
    items = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans'])
            if l['bbox'][1] - DY > 115 and t.strip():
                items.append((l['bbox'][1] - DY, t, l['spans'][0]['font']))
    items.sort()
    body_before = [y for y, t, f in items if 'Serif' in f and y < 200]
    m = [re.match(r'Figure (\d+\.\d+)', t) for y, t, f in items]
    nums = [x.group(1) for x in m if x]
    if nums and not body_before:
        return nums[0]
    return None


def blocks_of(src):
    return re.split(r'\n\n+', src)


def move_down(src, fid):
    bl = blocks_of(src)
    idx = [i for i, b in enumerate(bl) if b.strip() == f'@fig {fid}']
    if not idx:
        return None
    i = idx[0]
    j = i + 1
    if j >= len(bl) or bl[j].startswith(('##', ':::', '@fig')):
        return None
    bl[i], bl[j] = bl[j], bl[i]
    return '\n\n'.join(bl)


def run(n, maxit=30):
    import build as B
    path = f'src/ch{n}.md'
    for it in range(maxit):
        d, rep = build(n)
        # figure number -> id
        num2id = {}
        allch = [B.Chapter(m) for m in B.CHAPTERS]
        for c in allch:
            c.number_things()
            num2id.update({v: k for k, v in c.fig_no.items()})
        moved = False
        for k in range(1, d.page_count - 1):
            kind = rep[k - 1][2]
            if kind in ('opener', 'blank') or rep[k][2] in ('blank', 'opener'):
                continue
            if 'POINTS' in d[k + 1].get_text().replace(' ', ''):
                continue
            if page_last_y(d[k]) >= 600:
                continue
            num = first_fig(d[k + 1])
            if not num:
                continue
            fid = num2id[num]
            src = open(path).read()
            new = move_down(src, fid)
            if new:
                open(path, 'w').write(new)
                print(f'ch{n}: page {rep[k-1][1]} short; moved {fid}')
                moved = True
                break
        if not moved:
            return


if __name__ == '__main__':
    for a in sys.argv[1:]:
        run(int(a))
