import math
from svg import Fig, anchor, CYAN, DARK, GREY, FILL
from figs4 import table_html

FIGS = {}


def fig(fid, caption, **opts):
    def deco(fn):
        FIGS[fid] = (caption, fn, opts)
        return fn
    return deco


def clip(fid, caption, page, rect, **opts):
    FIGS[fid] = (caption, ('clip', page, rect), opts)


R = 8


def cfg(f, pos, edges, pred=(), labels=None, r=R, size=6.6):
    """pos: {node: (x,y)}; edges: list of (a, b, [via points], label)."""
    for e in edges:
        a, b = e[0], e[1]
        via = e[2] if len(e) > 2 and e[2] else []
        lab = e[3] if len(e) > 3 else None
        pts = [pos[a]] + via + [pos[b]]
        # trim to circle edges
        (x1, y1), (x2, y2) = pts[0], pts[1]
        d = math.hypot(x2 - x1, y2 - y1)
        pts[0] = (x1 + (x2 - x1) * r / d, y1 + (y2 - y1) * r / d)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        d = math.hypot(x2 - x1, y2 - y1)
        pts[-1] = (x2 - (x2 - x1) * r / d, y2 - (y2 - y1) * r / d)
        f.arrow(pts, size=4)
        if lab:
            lx, ly, t = lab
            f.text(lx, ly, t, size=5.8, italic=True)
    for n, (x, y) in pos.items():
        f.circle(x, y, r, fill='#B9E5FA' if n in pred else 'white', stroke=CYAN)
        f.text(x, y, str(n), size=size, weight=500)


@fig('cfg-notation', 'Flow-graph notation for structured constructs; shaded nodes are predicate nodes', wide=True)
def _():
    f = Fig(420, 112, fs=6.6)
    r = 6
    # sequence
    cfg(f, {1: (22, 16), 2: (22, 46), 3: (22, 76)}, [(1, 2), (2, 3)], r=r, size=5.8)
    # if-then-else
    cfg(f, {1: (92, 16), 2: (72, 46), 3: (112, 46), 4: (92, 76)}, [(1, 2), (1, 3), (2, 4), (3, 4)], pred=(1,), r=r, size=5.8)
    # if-then
    cfg(f, {1: (162, 16), 2: (148, 46), 3: (162, 76)}, [(1, 2), (2, 3), (1, 3, [(176, 46)])], pred=(1,), r=r, size=5.8)
    # while
    cfg(f, {1: (228, 16), 2: (228, 46), 3: (228, 76)}, [(1, 2), (2, 1, [(244, 46), (244, 16)]), (1, 3, [(212, 16), (212, 76)])], pred=(1,), r=r, size=5.8)
    # do-while
    cfg(f, {1: (292, 16), 2: (292, 46), 3: (292, 76)}, [(1, 2), (2, 1, [(308, 46), (308, 16)]), (2, 3)], pred=(2,), r=r, size=5.8)
    # case
    cfg(f, {1: (374, 16), 2: (344, 46), 3: (364, 46), 4: (384, 46), 5: (404, 46), 6: (374, 76)},
        [(1, 2), (1, 3), (1, 4), (1, 5), (2, 6), (3, 6), (4, 6), (5, 6)], pred=(1,), r=r, size=5.8)
    for x, t in [(22, 'Sequence'), (92, 'If–then–else'), (162, 'If–then'), (228, 'While'), (292, 'Do–while'), (374, 'Case (switch)')]:
        f.text(x, 100, t, weight=500)
    return f.svg()


@fig('cfg-larger', 'Flow graph of the larger-of-two program', scale=0.78)
def _():
    f = Fig(200, 190, fs=6.6)
    pos = {1: (70, 12), 2: (70, 40), 3: (70, 68), 4: (40, 100), 5: (100, 100), 6: (100, 130), 7: (70, 170)}
    cfg(f, pos, [(1, 2), (2, 3), (3, 4, None, (48, 80, 'T')), (3, 5, None, (92, 80, 'F')), (5, 6), (4, 7), (6, 7)], pred=(3,))
    f.text(70, 120, 'R1', size=6.4, weight=600, color=CYAN); f.text(160, 110, 'R2 (outer)', size=6.4, weight=600, color=CYAN)
    return f.svg()


@fig('cfg-nested', 'Flow graph of a nested if–else', scale=0.78)
def _():
    f = Fig(200, 150, fs=6.6)
    pos = {1: (60, 12), 2: (30, 60), 3: (100, 48), 4: (80, 88), 5: (130, 88), 6: (60, 136)}
    cfg(f, pos, [(1, 2, None, (36, 34, 'T')), (1, 3, None, (88, 26, 'F')), (3, 4, None, (84, 66, 'T')), (3, 5, None, (124, 66, 'F')), (2, 6), (4, 6), (5, 6, [(130, 136)])], pred=(1, 3))
    f.text(62, 70, 'R1', size=6.4, weight=600, color=CYAN); f.text(104, 104, 'R2', size=6.4, weight=600, color=CYAN); f.text(170, 60, 'R3', size=6.4, weight=600, color=CYAN)
    return f.svg()


@fig('cfg-fact', 'Flow graph of the factorial function', scale=0.78)
def _():
    f = Fig(230, 196, fs=6.6)
    pos = {1: (60, 14), 2: (20, 56), 3: (100, 50), 4: (100, 90), 5: (150, 124), 6: (100, 150), 7: (60, 184)}
    cfg(f, pos, [(1, 2, None, (30, 30, 'T')), (1, 3, None, (90, 26, 'F')), (3, 4), (4, 5, None, (136, 100, 'T')), (5, 4, [(190, 124), (190, 90)]), (4, 6, None, (94, 120, 'F')), (2, 7, [(20, 184)]), (6, 7)], pred=(1, 4))
    f.text(150, 104, 'R1', size=6.4, weight=600, color=CYAN); f.text(62, 100, 'R2', size=6.4, weight=600, color=CYAN); f.text(210, 30, 'R3', size=6.4, weight=600, color=CYAN)
    return f.svg()


@fig('cfg-countpos', 'Flow graph of the count-positives loop', scale=0.78)
def _():
    f = Fig(200, 176, fs=6.6)
    pos = {1: (60, 12), 2: (60, 40), 3: (60, 70), 4: (60, 102), 5: (100, 126), 6: (60, 152), 7: (140, 70)}
    cfg(f, pos, [(1, 2), (2, 3), (3, 4, None, (54, 86, 'T')), (3, 7, None, (100, 64, 'F')), (4, 5, None, (86, 108, 'T')), (4, 6, None, (54, 128, 'F')), (5, 6), (6, 3, [(20, 152), (20, 70)])], pred=(3, 4))
    return f.svg()


@fig('ecp-line', 'Equivalence classes for a password length of 6 to 12 characters')
def _():
    f = Fig(300, 60, fs=6.6)
    f.arrow([(10, 34), (290, 34)], size=4)
    f.rect(10, 14, 90, 16, stroke=GREY, fill='white'); f.text(55, 22, 'Invalid: L < 6  (I1)')
    f.rect(100, 14, 110, 16, stroke=CYAN, fill='#B9E5FA'); f.text(155, 22, 'Valid: 6 ≤ L ≤ 12  (V1)', weight=500)
    f.rect(210, 14, 80, 16, stroke=GREY, fill='white'); f.text(250, 22, 'Invalid: L > 12  (I2)')
    for x, t in [(100, '6'), (210, '12')]:
        f.line(x, 30, x, 38); f.text(x, 46, t, weight=500)
    f.text(150, 56, 'password length L', size=6.2, italic=True)
    return f.svg()


@fig('bva-line', 'Boundary values for a range [a, b]')
def _():
    f = Fig(300, 50, fs=6.6)
    f.arrow([(10, 24), (290, 24)], size=4)
    f.rect(80, 18, 140, 12, stroke=CYAN, fill='#EAF7FD')
    for x, t in [(70, 'min−'), (80, 'min'), (92, 'min+'), (150, 'nom'), (208, 'max−'), (220, 'max'), (232, 'max+')]:
        f.circle(x, 24, 2.3, fill=DARK, stroke=DARK)
        f.text(x, 12 if t in ('min', 'max', 'nom') else 40, t, size=6)
    f.text(80, 49, '= a', italic=True, anchor='start'); f.text(220, 49, '= b', italic=True, anchor='start')
    return f.svg()


@fig('pin-state', 'State transition diagram for PIN entry at an ATM', wide=True)
def _():
    f = Fig(420, 110, fs=6.6)
    xs = [30, 120, 210, 300]
    names = ['Start', '1st try', '2nd try', '3rd try']
    for x, n in zip(xs, names):
        f.rbox(x - 30, 14, 60, 20, n, shadow=False)
    ag = f.rbox(160, 80, 100, 20, 'Access granted', shadow=False)
    bl = f.rbox(344, 80, 70, 20, 'Account blocked', shadow=False)
    f.arrow([(60, 24), (90, 24)], size=4); f.text(75, 8, 'card inserted', size=5.8)
    f.arrow([(150, 24), (180, 24)], size=4); f.text(165, 8, 'wrong PIN', size=5.8)
    f.arrow([(240, 24), (270, 24)], size=4); f.text(255, 8, 'wrong PIN', size=5.8)
    f.arrow([(330, 24), (379, 80)], size=4); f.text(372, 48, 'wrong PIN', size=5.8)
    for x in (120, 210, 300):
        f.arrow([(x, 34), (210 + (x - 210) * 0.4, 80)], size=4)
    f.text(210, 58, 'correct PIN', size=5.8, italic=True)
    return f.svg()


@fig('login-state', 'State transition diagram for a login system')
def _():
    f = Fig(336, 120, fs=6.6)
    idle = f.rbox(10, 50, 60, 20, 'Idle', shadow=False)
    un = f.rbox(120, 50, 90, 20, 'Username entered', shadow=False)
    li = f.rbox(260, 10, 70, 20, 'Logged in', shadow=False)
    er = f.rbox(260, 90, 70, 20, 'Error', shadow=False)
    f.arrow([(70, 60), (120, 60)], size=4); f.text(95, 54, 'enter username', size=5.8)
    f.arrow([(210, 56), (260, 22)], size=4); f.text(228, 32, 'valid password', size=5.8, anchor='end')
    f.arrow([(210, 64), (260, 98)], size=4); f.text(226, 92, 'invalid password', size=5.8, anchor='end')
    f.arrow([(295, 10), (295, 4), (40, 4), (40, 50)], size=4); f.text(160, 10, 'logout', size=5.8)
    f.arrow([(295, 110), (295, 116), (40, 116), (40, 70)], size=4); f.text(160, 111, 'retry login', size=5.8)
    return f.svg()


@fig('test-strategy', 'Testing proceeds outward from unit testing to system testing')
def _():
    f = Fig(300, 136, fs=6.6)
    f.raw('<g transform="translate(0,12)">')
    for i, (t, d) in enumerate([('Unit testing', 'Code'), ('Integration testing', 'Design'), ('Validation testing', 'Requirements'), ('System testing', 'System engineering')]):
        r = 16 + i * 17
        f.raw(f'<path d="M {150 - r} 60 A {r} {r} 0 0 1 {150 + r} 60" fill="none" stroke="{CYAN}" stroke-width="0.8"/>')
        f.raw(f'<path d="M {150 - r} 60 A {r} {r} 0 0 0 {150 + r} 60" fill="none" stroke="{GREY}" stroke-width="0.5" stroke-dasharray="2,2"/>')
        f.text(150 + r + 4 if False else 150, 60 - r + 6, t, size=5.8, weight=500)
        f.text(150, 60 + r - 3, d, size=5.8, color=GREY)
    f.line(70, 60, 230, 60, w=0.4, color=GREY)
    f.text(265, 30, 'testing\nproceeds\noutward', size=6, italic=True); f.text(265, 92, 'development\nproceeds\ninward', size=6, italic=True)
    f.raw('</g>')
    return f.svg()


clip('review-process', 'The software review process', 680, (106, 127, 513, 221.5), wide=True)
clip('inspection-checklist', 'An inspection checklist', 683, (101.6, 127.8, 525.2, 411.2), wide=True)


@fig('regression-cycle', 'The regression testing cycle')
def _():
    f = Fig(336, 58, fs=6.4)
    steps = ['Identify areas\naffected by change', 'Select relevant\ntest cases', 'Execute (manually\nor automated)', 'Analyze results\nand report']
    for i, s in enumerate(steps):
        x = 4 + i * 84
        f.box(x, 6, 74, 26, s, shadow=False)
        if i < 3:
            f.arrow([(x + 74, 19), (x + 84, 19)], size=3.5)
    f.arrow([(290, 32), (290, 46), (40, 46), (40, 32)], size=3.5, dash='3,2')
    f.text(165, 53, 'repeated after each fix or change', size=6, italic=True)
    return f.svg()


@fig('cfg-flowchart', 'Flow graph of the three-variable flowchart', scale=0.78)
def _():
    f = Fig(200, 250, fs=6.6)
    pos = {1: (70, 12), 2: (70, 40), 3: (70, 70), 4: (30, 110), 5: (110, 104), 6: (80, 146), 7: (140, 146), 8: (70, 200), 9: (70, 236)}
    cfg(f, pos, [(1, 2), (2, 3), (3, 4, None, (42, 86, 'Yes')), (3, 5, None, (100, 82, 'No')), (5, 6, None, (86, 124, 'Yes')), (5, 7, None, (134, 124, 'No')),
                 (4, 8, [(30, 200)]), (6, 8), (7, 8, [(140, 200)]), (8, 9)], pred=(3, 5))
    f.text(70, 126, 'R1', size=6.4, weight=600, color=CYAN); f.text(112, 172, 'R2', size=6.4, weight=600, color=CYAN); f.text(176, 60, 'R3', size=6.4, weight=600, color=CYAN)
    return f.svg()


@fig('cfg-sumloop', 'Flow graph of the summation loop', scale=0.78)
def _():
    f = Fig(200, 190, fs=6.6)
    pos = {1: (60, 12), 2: (60, 40), 3: (60, 72), 4: (110, 100), 5: (110, 136), 6: (60, 150), 7: (60, 180)}
    cfg(f, pos, [(1, 2), (2, 3), (3, 4, None, (96, 78, 'T')), (4, 5), (5, 3, [(160, 136), (160, 72)]), (3, 6, None, (52, 112, 'F')), (6, 7)], pred=(3,))
    return f.svg()


@fig('gm-graph', 'A flow graph with a self-loop, and its graph and connection matrices', wide=True)
def _():
    f = Fig(420, 120, fs=6.6)
    pos = {1: (40, 30), 2: (16, 78), 3: (64, 78), 4: (40, 110)}
    cfg(f, pos, [(1, 2, None, (22, 52, 'b')), (1, 3, None, (58, 52, 'c')), (2, 4, None, (22, 98, 'd')), (3, 4, None, (58, 98, 'e'))])
    f.raw(f'<path d="M 34 23 C 20 4, 60 4, 46 23" fill="none" stroke="{DARK}" stroke-width="0.5"/>'); f.head(50, 14, 46, 23, 'fill', 4); f.text(40, 8, 'a', size=5.8, italic=True)
    def matrix(x0, title, cells, extra=None):
        f.text(x0 + 60, 6, title, weight=500)
        cw, ch = 22, 16
        for j in range(4):
            f.text(x0 + 24 + j * cw + cw / 2, 18, str(j + 1), weight=500)
        for i in range(4):
            y = 22 + i * ch
            f.text(x0 + 12, y + ch / 2, str(i + 1), weight=500)
            for j in range(4):
                f.rect(x0 + 24 + j * cw, y, cw, ch, stroke=CYAN, sw=0.5, fill='#EAF7FD' if cells.get((i, j)) else 'white')
                if cells.get((i, j)):
                    f.text(x0 + 24 + j * cw + cw / 2, y + ch / 2, cells[(i, j)])
        if extra:
            f.text(x0 + 24 + 4 * cw + 4, 18, extra[0], anchor='start', weight=500, size=6)
            for i, t in enumerate(extra[1]):
                f.text(x0 + 24 + 4 * cw + 6, 22 + i * ch + ch / 2, t, anchor='start', size=6.2)
    matrix(96, 'Graph matrix', {(0, 0): 'a', (0, 1): 'b', (0, 2): 'c', (1, 3): 'd', (2, 3): 'e'})
    matrix(236, 'Connection matrix', {(0, 0): '1', (0, 1): '1', (0, 2): '1', (1, 3): '1', (2, 3): '1'}, ('count − 1', ['3 − 1 = 2', '1 − 1 = 0', '1 − 1 = 0', 'ignore']))
    return f.svg()


FIGS['discount-table'] = ('Decision table for the checkout discount', table_html(
    ['', 'R1', 'R2', 'R3', 'R4'],
    [['C1: Logged in?', 'T', 'T', 'F', 'F'],
     ['C2: Cart total > ₹1,000?', 'T', 'F', 'T', 'F'],
     ['A1: Apply 10% discount', '×', '', '', ''],
     ['A2: Charge full price', '', '×', '', ''],
     ['A3: Redirect to login', '', '', '×', '×']],
    ['40%', '15%', '15%', '15%', '15%']), {'wide': True})


@fig('cfg-leap', 'Flow graph of the leap-year function', scale=0.8)
def _():
    f = Fig(220, 190, fs=6.6)
    pos = {1: (40, 14), 2: (14, 60), 3: (80, 50), 4: (54, 96), 5: (120, 86), 6: (100, 132), 7: (156, 132), 8: (80, 178)}
    cfg(f, pos, [(1, 2, None, (20, 34, 'T')), (1, 3, None, (66, 26, 'F')), (3, 4, None, (60, 70, 'T')), (3, 5, None, (106, 62, 'F')),
                 (5, 6, None, (104, 106, 'T')), (5, 7, None, (146, 104, 'F')), (2, 8, [(14, 178)]), (4, 8), (6, 8), (7, 8, [(156, 178)])], pred=(1, 3, 5))
    return f.svg()


@fig('cfg-sort', 'Flow graph of the selection sort', scale=0.8)
def _():
    f = Fig(220, 250, fs=6.6)
    pos = {1: (70, 12), 2: (70, 42), 3: (70, 72), 4: (70, 104), 5: (110, 136), 6: (150, 166), 7: (110, 198), 8: (40, 150), 9: (180, 42)}
    cfg(f, pos, [(1, 2), (2, 3, None, (62, 58, 'T')), (2, 9, None, (126, 36, 'F')), (3, 4), (4, 5, None, (96, 114, 'T')), (4, 8, None, (50, 124, 'F')),
                 (5, 6, None, (138, 146, 'T')), (5, 7, None, (104, 168, 'F')), (6, 7), (7, 4, [(80, 230), (20, 230), (20, 104)]), (8, 2, [(40, 42)])], pred=(2, 4, 5))
    return f.svg()


@fig('cfg-discount', 'Flow graph of the discount function', scale=0.8)
def _():
    f = Fig(220, 300, fs=6.4)
    pos = {1: (40, 14), 2: (14, 60), 3: (80, 50), 4: (50, 86), 5: (80, 118), 6: (50, 156), 7: (120, 150), 8: (150, 186), 9: (100, 220), 10: (140, 250), 11: (100, 280), 12: (40, 290)}
    cfg(f, pos, [(1, 2, None, (20, 32, 'T')), (1, 3, None, (66, 26, 'F')), (3, 4, None, (58, 64, 'T')), (3, 5, None, (92, 82, 'F')), (4, 5),
                 (5, 6, None, (58, 132, 'T')), (5, 7, None, (106, 130, 'F')), (6, 9), (7, 8, None, (142, 164, 'T')), (7, 9, None, (106, 186, 'F')), (8, 9),
                 (9, 10, None, (126, 232, 'T')), (9, 11, None, (92, 250, 'F')), (10, 11), (2, 12, [(14, 290)]), (11, 12)], pred=(1, 3, 5, 7, 9))
    return f.svg()


# ------------------------------------------------------------------ Module 5: process, V model, unit and integration testing
def ell(f, cx, cy, t, rx=30, ry=12, fill='white', size=5.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    f.raw(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{CYAN}" stroke-width="1"{d}/>')
    f.text(cx, cy, t, size=size)


@fig('test-process', 'The fundamental test process', wide=True)
def _():
    f = Fig(420, 132, fs=6)
    st = [('Test planning\nand control', 'Define the approach\nand monitor progress', 'Set objectives, scope,\nstrategy; allocate\nresources; define entry\nand exit criteria; monitor\nmetrics; take corrective\naction'),
          ('Test analysis', 'Identify what\nto test', 'Analyze the test basis\nto identify testable\nfeatures and derive\ntest conditions'),
          ('Test design', 'Define how\nto test', 'Elaborate conditions\ninto test cases with\ninputs, expected\nresults, and\npreconditions'),
          ('Implementation\nand execution', 'Prepare the\nenvironment; run tests', 'Build testware and\nenvironment; organize\ncases into suites;\nexecute; log results'),
          ('Test completion', 'Close testing\nactivities', 'Evaluate exit criteria;\narchive testware; hand\nover deliverables;\ncapture lessons\nlearned')]
    w = 80
    for i, (h, a, b) in enumerate(st):
        x = 4 + i * 83
        shade = ['#E0F4FB', '#CDEDF8', '#B8E5F5', '#A2DCF2', '#8BD3EE'][i]
        f.poly([(x, 4), (x + w - 8, 4), (x + w, 16), (x + w - 8, 28), (x, 28), (x + 8, 16)] if i else [(x, 4), (x + w - 8, 4), (x + w, 16), (x + w - 8, 28), (x, 28)], close=True, color=CYAN, w=0.8, fill=shade)
        f.text(x + w / 2, 16, h, weight=600, size=5.8)
        f.rect(x + 2, 32, w - 10, 96, stroke=CYAN, sw=0.5, fill='white')
        f.text(x + w / 2 - 3, 46, a, weight=500, size=5.6)
        f.text(x + w / 2 - 3, 88, b, size=5.4)
    return f.svg()


FIGS['test-case-tbl'] = ('A test case and its components', table_html(['Component', 'Content for TC-LOGIN-01'], [
    ['Test case ID', 'TC-LOGIN-01 (unique identifier)'],
    ['Objective', 'Verify that a registered user can log in with valid credentials'],
    ['Preconditions', 'User testuser1 exists and is active; the user is logged out'],
    ['Test steps', '1. Open the login page. 2. Enter username and password. 3. Press Log in.'],
    ['Test data', 'Username: testuser1; Password: Pass@1234'],
    ['Expected result', 'The dashboard is shown with "Welcome, testuser1" within 2 seconds'],
    ['Actual result and status', 'Recorded during execution; Pass or Fail (with a defect ID if it fails)']], ['26%', '74%']), {'wide': True})


@fig('v-model', 'The V&V model (V model)', wide=True)
def _():
    f = Fig(420, 250, fs=6)
    L = [(54, 28, 'Requirements\nanalysis'), (84, 74, 'System\ndesign'), (114, 120, 'Architecture\ndesign'), (144, 166, 'Module\ndesign')]
    M = [(210, 28, 'Acceptance\ntest design'), (210, 74, 'System\ntest design'), (210, 120, 'Integration\ntest design'), (210, 166, 'Unit\ntest design')]
    R = [(366, 28, 'Acceptance\ntesting'), (336, 74, 'System\ntesting'), (306, 120, 'Integration\ntesting'), (276, 166, 'Unit\ntesting')]
    # the V
    f.raw(f'<path d="M 28 14 L 198 236 L 222 236 L 392 14" fill="none" stroke="#9FD9F0" stroke-width="10" stroke-linejoin="round" opacity="0.55"/>')
    f.head(378, 36, 392, 14, 'fill', 10, color='#5BBFE6')
    for (x1, y1, _), (x2, y2, _) in zip(L, M):
        f.arrow([(x1 + 30, y1), (x2 - 30, y2)], dash='3,2', size=3.5)
    for (x1, y1, _), (x2, y2, _) in zip(M, R):
        f.arrow([(x1 + 30, y1), (x2 - 30, y2)], dash='3,2', size=3.5)
    for a, b in zip(L, L[1:]):
        f.arrow([(a[0] + 8, a[1] + 12), (b[0] - 6, b[1] - 12)], dash='3,2', size=3.5)
    for a, b in zip(R[::-1], R[::-1][1:]):
        f.arrow([(a[0] + 6, a[1] - 12), (b[0] - 8, b[1] + 12)], dash='3,2', size=3.5)
    f.arrow([(154, 178), (194, 214)], dash='3,2', size=3.5); f.arrow([(226, 214), (266, 178)], dash='3,2', size=3.5)
    for x, y, t in L + M + R:
        ell(f, x, y, t, rx=27, fill='#FFF7F0' if (x, y, t) in L else ('#F2FAFD' if (x, y, t) in M else '#EFF9F1'))
    ell(f, 210, 222, 'Coding', rx=26, ry=10, fill='#FFF7F0')
    f.text(18, 150, 'VERIFICATION\n(static: reviews,\ninspections,\nwalkthroughs, audits)\n"Are we building the\nproduct right?"', size=5.6, anchor='start', weight=500)
    f.text(408, 150, 'VALIDATION\n(dynamic: execute\nthe software at\neach test level)\n"Are we building the\nright product?"', size=5.6, anchor='end', weight=500)
    f.text(210, 246, 'test design on the left feeds test execution on the right at the same level', size=5.4, italic=True)
    return f.svg()


@fig('val-levels', 'Levels of testing in the validation phase', wide=True)
def _():
    f = Fig(420, 64, fs=6)
    for i, t in enumerate(['Component\n(unit) testing', 'Component\nintegration\ntesting', 'System\nintegration\ntesting', 'System\ntesting', 'Acceptance\ntesting']):
        cx = 44 + i * 83
        f.circle(cx, 32, 28, fill=['#E0F4FB', '#CDEDF8', '#B8E5F5', '#A2DCF2', '#8BD3EE'][i], stroke=CYAN)
        f.text(cx, 32, t, size=5.8, weight=500)
        if i < 4:
            f.arrow([(cx + 28, 32), (cx + 55, 32)], size=4)
    return f.svg()


@fig('fagan', 'The six steps of a Fagan inspection', wide=True)
def _():
    f = Fig(420, 76, fs=6)
    st = [('Planning', 'moderator checks entry\ncriteria, picks team,\nschedules'), ('Overview', 'author explains the\nwork product to\nthe team'), ('Preparation', 'each inspector studies\nit with the checklist'),
          ('Inspection\nmeeting', 'reader paraphrases;\ndefects found and\nlogged by recorder'), ('Rework', 'author corrects\nevery logged\ndefect'), ('Follow-up', 'moderator verifies\nfixes and exit\ncriteria')]
    for i, (h, d) in enumerate(st):
        x = 4 + i * 69.5
        f.rbox(x, 4, 62, 24, h, weight=500, fill='#EAF7FD', shadow=False)
        f.text(x + 31, 50, d, size=5.2)
        if i < 5:
            f.arrow([(x + 62, 16), (x + 69.5, 16)], size=3)
    return f.svg()


@fig('unit-process', 'The component testing process')
def _():
    f = Fig(336, 128, fs=6)
    st = [('Test analysis', 'identify test conditions from component specifications and code'),
          ('Test design', 'white-box (statement, decision, condition coverage) and\nblack-box (equivalence partitions, boundary values) cases'),
          ('Test implementation', 'write unit tests in a framework (JUnit, NUnit, pytest);\nbuild stubs and drivers to isolate the unit'),
          ('Test execution', 'run tests automatically on every build (CI/CD pipeline)'),
          ('Evaluation', 'measure code coverage (statement, branch)')]
    for i, (h, d) in enumerate(st):
        y = 4 + i * 25
        f.rect(4, y, 82, 20, fill='#EAF7FD', stroke=CYAN); f.text(45, y + 10, h, weight=500)
        f.text(94, y + 10, d, size=5.6, anchor='start')
        if i < 4:
            f.arrow([(45, y + 20), (45, y + 25)], size=3)
    return f.svg()


def mod(f, x, y, t, fill='white', dash=None, w=96):
    f.rect(x, y, w, 20, fill=fill, stroke=CYAN, dash=dash)
    f.text(x + w / 2, y + 10, t, size=5.6)


@fig('stub-driver', 'A stub replaces a called module; a driver replaces a calling module', wide=True)
def _():
    f = Fig(420, 120, fs=6)
    for x0, title, stub in [(10, 'Testing B with a stub (C not yet developed)', True), (222, 'Testing B with a driver (A not yet developed)', False)]:
        f.text(x0 + 94, 8, title, weight=600, size=6)
        mod(f, x0 + 46, 20, 'driver_test_calculate_dose()' if not stub else 'A: Main_Controller()', fill='#FFF4E5' if not stub else 'white', dash='3,2' if not stub else None)
        mod(f, x0 + 46, 56, 'B: CalculateDose()', fill='#E3F6E8')
        mod(f, x0 + 46, 92, 'getPatientData_stub()' if stub else 'C: Database.getPatientData()', fill='#FFF4E5' if stub else 'white', dash='3,2' if stub else None)
        f.arrow([(x0 + 94, 40), (x0 + 94, 56)], size=3.5); f.text(x0 + 98, 48, 'calls', size=5.4, anchor='start')
        f.arrow([(x0 + 94, 76), (x0 + 94, 92)], size=3.5); f.text(x0 + 98, 84, 'calls', size=5.4, anchor='start')
        f.text(x0 + 150, 102 if stub else 30, 'returns fixed data\n{age: 65, weight: 70}' if stub else 'supplies inputs,\nchecks the output', size=5.2, italic=True, anchor='start')
        f.text(x0 + 150, 66, 'unit under test', size=5.2, italic=True, anchor='start')
    f.line(212, 4, 212, 116, w=0.4, color=GREY)
    return f.svg()


FIGS['stub-driver-tbl'] = ('Stubs, drivers, and test harnesses', table_html(['Aspect', 'Stub', 'Driver'], [
    ['Replaces', 'A called (lower-level) component', 'A calling (higher-level) component'],
    ['Does', 'Returns predefined responses to the unit under test', 'Invokes the unit under test with test data and checks its results'],
    ['Direction', 'Downward dependency', 'Upward dependency'],
    ['Test focus', 'Does the unit handle the responses correctly?', 'Does the unit produce the correct outputs?'],
    ['Position', 'Injected into the unit under test', 'Wraps around the unit under test'],
    ['Integration strategy', 'Top-down', 'Bottom-up'],
    ['Test harness', 'The environment of stubs, drivers, and utilities that executes the tests; used in both strategies', '']], ['22%', '39%', '39%']), {'wide': True})


@fig('integ-orders', 'Top-down and bottom-up integration of a module hierarchy', wide=True)
def _():
    f = Fig(420, 116, fs=6)
    for x0, title in [(0, 'Top-down: start at M1; stubs below'), (214, 'Bottom-up: start at the leaves; drivers above')]:
        f.text(x0 + 104, 8, title, weight=600)
        pos = {'M1': (104, 22), 'M2': (44, 56), 'M3': (104, 56), 'M4': (164, 56), 'M5': (22, 90), 'M6': (66, 90), 'M7': (164, 90)}
        for a, b in [('M1', 'M2'), ('M1', 'M3'), ('M1', 'M4'), ('M2', 'M5'), ('M2', 'M6'), ('M4', 'M7')]:
            (x1, y1), (x2, y2) = pos[a], pos[b]
            f.line(x0 + x1, y1 + 8, x0 + x2, y2 - 8)
        for k, (x, y) in pos.items():
            f.rect(x0 + x - 16, y - 8, 32, 16, fill='#EAF7FD' if k in ('M1', 'M2', 'M3', 'M4') and x0 == 0 or k in ('M5', 'M6', 'M7', 'M3') and x0 else 'white', stroke=CYAN)
            f.text(x0 + x, y, k, weight=500)
        if x0 == 0:
            f.text(104, 108, 'shaded: integrated so far; M5, M6, M7 still stubs', size=5.4, italic=True)
        else:
            f.text(x0 + 104, 108, 'shaded: tested with drivers; M2, M4, M1 added later', size=5.4, italic=True)
    f.line(210, 4, 210, 112, w=0.4, color=GREY)
    return f.svg()


FIGS['integ-strategies'] = ('Integration testing strategies', table_html(['Strategy', 'How it works', 'Stubs and drivers', 'Best for'], [
    ['Big bang', 'All components are integrated at once, then tested', 'None', 'Very small systems (fewer than about five components)'],
    ['Top-down', 'Start with the top-level component; integrate downward', 'Stubs for missing lower components', 'Systems whose major functions are in the upper layers'],
    ['Bottom-up', 'Start with the lowest-level components; integrate upward', 'Drivers for missing higher components', 'Systems that need stable foundation services first'],
    ['Sandwich (hybrid)', 'Top-down and bottom-up together, meeting at a middle layer', 'Both stubs and drivers', 'Medium and large systems']], ['16%', '32%', '24%', '28%']), {'wide': True})


FIGS['sit-techniques'] = ('Techniques of system integration testing', table_html(['Technique', 'Purpose', 'Example'], [
    ['End-to-end flow testing', 'Validate a complete business process across systems (the primary technique)', 'Patient registration → lab order → results delivery across three systems'],
    ['Contract testing', 'Verify that a consumer and a provider agree on an API (critical for microservices)', 'The provider publishes a contract (e.g., Pact); the consumer is tested against it before integration'],
    ['Service virtualization', 'Simulate an unavailable or costly external system; replaces stubs for complex dependencies', 'A virtual payment gateway instead of one that charges for every test call'],
    ['Message/queue testing', 'Validate asynchronous communication in event-driven systems', 'An order event published to a queue is consumed correctly by the inventory system'],
    ['Database integration testing', 'Check data consistency across systems (often overlooked)', "An order created in system A appears correctly in system B's reporting database"]], ['22%', '40%', '38%']), {'wide': True})


FIGS['cit-vs-sit'] = ('Component integration and system integration testing', table_html(['Aspect', 'Component integration testing', 'System integration testing'], [
    ['Scope', 'Components within one system', 'Multiple independent systems'],
    ['Boundaries', 'Internal interfaces (method calls, internal APIs)', 'External interfaces (REST APIs, message queues, files)'],
    ['Environment', 'Developer workstation or CI pipeline', 'Integration test environment that mirrors production'],
    ['Dependencies', 'Other components, replaced by stubs and drivers', 'External systems, replaced by service virtualization'],
    ['Defect focus', 'Data corruption at interface boundaries', 'Availability, protocol compliance, data consistency'],
    ['Typical tools', 'JUnit with Mockito (stubs and mocks)', 'Postman, Pact, WireMock, Kafka test containers']], ['20%', '40%', '40%']), {'wide': True})


@fig('sys-test-types', 'Types of system testing')
def _():
    f = Fig(336, 106, fs=6.2)
    f.rbox(128, 4, 80, 20, 'System testing', weight=600, fill='#EAF7FD', shadow=False)
    f.rbox(40, 40, 80, 18, 'Functional', weight=500, shadow=False); f.rbox(216, 40, 80, 18, 'Non-functional', weight=500, shadow=False)
    f.line(168, 24, 168, 32); f.line(80, 32, 256, 32); f.line(80, 32, 80, 40); f.line(256, 32, 256, 40)
    f.text(80, 76, 'what the system does:\nequivalence partitions,\nboundary values, decision\ntables, state transitions', size=5.4)
    nf = ['Performance', 'Load', 'Stress', 'Security', 'Usability', 'Compatibility', 'Recovery']
    for i, t in enumerate(nf):
        x = 150 + (i % 4) * 46; y = 66 + (i // 4) * 18
        f.rect(x, y, 42, 14, stroke=CYAN, sw=0.6); f.text(x + 21, y + 7, t, size=5.2)
    f.line(256, 58, 256, 66)
    return f.svg()
