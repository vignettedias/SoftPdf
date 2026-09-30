"""Automated inspection of out/book.pdf."""
import re, json, pymupdf
d = pymupdf.open('out/book.pdf')
DX, DY = (595.28 - 612) / 2, (841.89 - 792) / 2
rep = json.load(open('out/report.json'))
issues = []
for k in range(1, d.page_count):
    p = d[k]
    folio = rep[k - 1][1] if k - 1 < len(rep) else None
    nxt = rep[k][2] if k < len(rep) else 'opener'
    kind = rep[k - 1][2] if k - 1 < len(rep) else None
    txt = p.get_text()
    if kind == 'blank':
        continue
    for pat in [r'\?\?', r'\[\[', r'\]\]', r'@fig', r':::', r'\*\*', r'(?<!\w)_\w+_', r'<[a-z/]+>', r'&[a-z]+;', '�']:
        if re.search(pat, txt):
            issues.append((folio, 'markup', pat, re.search(pat, txt).group(0)))
    blocks = p.get_text('dict')['blocks']
    ys, xs = [], []
    for b in blocks:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if not t:
                continue
            x0, y0, x1, y1 = l['bbox']
            if y0 - DY < 115:
                continue  # running head
            ys.append(y1 - DY)
            if x1 - DX > 530 or x0 - DX < 80:
                issues.append((folio, 'outside', round(x0 - DX), round(x1 - DX), t[:40]))
    for dr in p.get_drawings():
        r = dr['rect']
        if r.y0 - DY < 115 or r.width > 540:
            continue
        ys.append(r.y1 - DY)
        if r.x1 - DX > 531 or r.x0 - DX < 30:
            issues.append((folio, 'draw-outside', round(r.x0 - DX), round(r.x1 - DX)))
    last = max(ys) if ys else 0
    nxt_kind = rep[k][2] if k < len(rep) else 'opener'
    if kind not in ('opener',) and nxt_kind not in ('opener', 'blank') and last < 600 and 'POINTS' not in txt.replace(' ', '') and 'POINTS' not in d[k + 1].get_text().replace(' ', ''):
        issues.append((folio, 'short page', round(last)))
    # stranded heading: heading line in bottom 60pt
    for b in blocks:
        for l in b.get('lines', []):
            s = l['spans'][0]
            if s['color'] == 0x00ADEF and s['size'] > 10.5 and l['bbox'][1] - DY > 650:
                issues.append((folio, 'stranded heading', ''.join(x['text'] for x in l['spans'])[:40]))
            if 'Example' in s['text'] and s['color'] == 0x00ADEF and l['bbox'][1] - DY > 660:
                issues.append((folio, 'stranded example', s['text']))
for i in issues:
    print(i)
print(len(issues), 'issues')
