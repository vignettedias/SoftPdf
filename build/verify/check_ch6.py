"""Verify control-hierarchy measures used in Chapter 6."""
arrows = ['AB', 'AC', 'AD', 'BE', 'BF', 'CF', 'CG', 'DG']
mods = 'ABCDEFG'
fo = {m: sum(a[0] == m for a in arrows) for m in mods}
fi = {m: sum(a[1] == m for a in arrows) for m in mods}
print('fan-out', fo, 'fan-in', fi, sum(fo.values()), sum(fi.values()))
lms = {'Main': ['User', 'Book', 'Trans'], 'User': ['Reg', 'Login', 'Upd'], 'Book': ['Add', 'Rem', 'Chk'], 'Trans': ['Bor', 'Ret']}
levels = [['Main'], lms['Main'], sum((lms[x] for x in lms['Main']), [])]
print('LMS depth', len(levels), 'width', max(map(len, levels)), {k: len(v) for k, v in lms.items()})
