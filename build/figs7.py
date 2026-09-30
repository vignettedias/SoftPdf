from svg import Fig, anchor, CYAN, DARK, GREY, FILL, SHADOW
from figs4 import table_html

FIGS = {}


def fig(fid, caption, **opts):
    def deco(fn):
        FIGS[fid] = (caption, fn, opts)
        return fn
    return deco


@fig('design-pyramid', 'Translating the requirements model into the design model', wide=True)
def _():
    f = Fig(420, 170, fs=6.8)
    els = [('Scenario-based elements', 'use cases, use case and\nactivity diagrams'), ('Class-based elements', 'class diagrams, CRC models,\ncollaboration diagrams'),
           ('Flow-oriented elements', 'data-flow and control-flow\ndiagrams, narratives'), ('Behavioral elements', 'state diagrams,\nsequence diagrams')]
    for i, (t, d) in enumerate(els):
        y = 4 + i * 40
        f.box(4, y, 150, 34, '', shadow=True)
        f.text(10, y + 10, t, anchor='start', weight=500)
        f.text(10, y + 24, d, anchor='start', size=6.2)
    f.text(79, 166, 'Requirements model', weight=500, italic=True)
    # pyramid
    ax, ay, bx = 330, 8, 150
    layers = [('Component-level design', 8, 44), ('Interface design', 44, 80), ('Architectural design', 80, 116), ('Data/class design', 116, 152)]
    for t, y0, y1 in layers:
        def w(y):
            return (y - ay) / (152 - ay) * 170
        x0a, x0b = ax - w(y0) / 2, ax - w(y1) / 2
        f.poly([(x0a, y0), (ax + w(y0) / 2, y0), (ax + w(y1) / 2, y1), (x0b, y1)], close=True, color=CYAN, w=1, fill='#EAF7FD' if t.startswith(('Arch', 'Comp')) else 'white')
        f.text(ax, (y0 + y1) / 2 + (6 if y0 == 8 else 0), t if y0 != 8 else 'Component-\nlevel', size=6.6 if y0 != 8 else 6.2)
    f.text(330, 166, 'Design model', weight=500, italic=True)
    for y in (21, 61, 101, 141):
        f.arrow([(158, y), (230, y + (84 - y) * 0.15)], size=4)
    return f.svg()


@fig('design-process', 'The design process: generate, document, and evaluate at three levels')
def _():
    f = Fig(336, 120, fs=6.4)
    f.box(4, 48, 62, 22, 'Analyze the\nproblem', shadow=False)
    cols = [('Generate the\nsystem interface', 'Evaluate the\ninterface'), ('Generate the\narchitecture', 'Evaluate the\narchitecture'), ('Generate the\ndetailed design', 'Evaluate the\ndetailed design')]
    for i, (g, e) in enumerate(cols):
        x = 84 + i * 80
        f.box(x, 14, 66, 24, g)
        f.box(x, 80, 66, 24, e)
        f.arrow([(x + 33, 38), (x + 33, 80)], size=3.5); f.text(x + 37, 59, 'document', size=5.8, anchor='start', italic=True)
        f.arrow([(x + 12, 80), (x + 12, 38)], size=3.5, dash='2,2')
        if i < 2:
            f.arrow([(x + 66, 92), (x + 80, 26)], size=3.5)
    f.arrow([(66, 59), (84, 26)], size=3.5)
    f.text(282, 116, 'dashed arrows: iteration after evaluation', size=5.8, italic=True, anchor='end')
    return f.svg()


@fig('modularity-cost', 'Modularity and software cost')
def _():
    import math
    f = Fig(300, 150, fs=6.6)
    f.arrow([(30, 130), (290, 130)], size=4); f.arrow([(30, 130), (30, 6)], size=4)
    f.text(160, 143, 'Number of modules')
    f.raw('<text x="18" y="68" transform="rotate(-90 18 68)" font-family="Fira Sans, sans-serif" font-size="6.6" text-anchor="middle" fill="#231F20">Cost or effort</text>')
    xs = list(range(36, 284, 4))
    dev = [(x, 128 - 100 * math.exp(-(x - 36) / 45)) for x in xs]
    integ = [(x, 128 - 95 * ((x - 36) / 248) ** 2) for x in xs]
    tot = [(x, a[1] + b[1] - 128 - 0) for (x, a), b in zip([(p[0], p) for p in dev], integ)]
    tot = [(x, y) for x, y in tot if y > 6]
    f.poly(dev, color=GREY, w=0.8, dash='3,2'); f.poly(integ, color=GREY, w=0.8, dash='1,2'); f.poly(tot, color=CYAN, w=1.3)
    m = max(tot, key=lambda p: p[1])
    f.rect(m[0] - 28, 10, 56, 120, stroke='none', fill='#EAF7FD')
    f.el.insert(2, f.el.pop())
    f.line(m[0], m[1], m[0], 130, dash='2,2'); f.text(m[0], 136, 'M', weight=600)
    f.text(m[0], 18, 'region of\nminimum cost', size=6)
    f.text(64, 44, 'cost per\nmodule', size=6); f.text(262, 42, 'cost to\nintegrate', size=6); f.text(250, 90, 'total cost', size=6, weight=500)
    f.text(52, 110, 'under-\nmodular', size=5.6, italic=True); f.text(270, 110, 'over-\nmodular', size=5.6, italic=True)
    return f.svg()


@fig('login-refine', 'Stepwise refinement of a login function')
def _():
    f = Fig(336, 104, fs=6.6)
    f.box(118, 4, 100, 20, 'Authenticate user', weight=500)
    kids = ['Prompt for\nusername and\npassword', 'Validate\nuser input', 'Check\ncredentials\nin database', 'Grant or\ndeny access']
    f.line(168, 24, 168, 32); f.line(42, 32, 294, 32)
    for i, k in enumerate(kids):
        x = 8 + i * 84
        f.line(x + 34, 32, x + 34, 40); f.box(x, 40, 68, 34, k, shadow=False)
    f.line(210, 74, 210, 80); f.line(190, 80, 262, 80)
    for x, t in [(160, 'Hash passwords'), (232, 'Use OAuth\nif required')]:
        f.line(x + 30, 80, x + 30, 84); f.box(x, 84, 60, 18, t, size=5.9, shadow=False)
    return f.svg()


@fig('cohesion-scale', 'The scale of cohesion')
def _():
    f = Fig(336, 64, fs=6.6)
    names = ['Coincidental', 'Logical', 'Temporal', 'Procedural', 'Communi-\ncational', 'Sequential', 'Functional']
    w = 44
    for i, n in enumerate(names):
        x = 4 + i * 47
        shade = int(255 - i * 22)
        f.rect(x, 14, w, 26, stroke=CYAN, fill=f'rgb({255-i*38},{255-i*14},255)')
        f.text(x + w / 2, 27, n, size=6.2)
    f.arrow([(4, 50), (330, 50)], size=4)
    f.text(4, 8, 'low (worst)', anchor='start', size=6.2, italic=True); f.text(330, 8, 'high (best)', anchor='end', size=6.2, italic=True)
    f.text(167, 59, 'increasing relatedness of the elements of a module', size=6.2)
    return f.svg()


@fig('coupling-scale', 'The scale of coupling')
def _():
    f = Fig(336, 64, fs=6.6)
    names = ['Content', 'Common', 'External', 'Control', 'Stamp', 'Data']
    w = 50
    for i, n in enumerate(names):
        x = 4 + i * 55
        shade = int(145 + i * 22)
        f.rect(x, 14, w, 26, stroke=CYAN, fill=f'rgb({255-(5-i)*45},{255-(5-i)*16},255)')
        f.text(x + w / 2, 27, n, size=6.4)
    f.arrow([(4, 50), (330, 50)], size=4)
    f.text(4, 8, 'high (worst)', anchor='start', size=6.2, italic=True); f.text(330, 8, 'low (best)', anchor='end', size=6.2, italic=True)
    f.text(167, 59, 'decreasing interdependence between modules', size=6.2)
    return f.svg()


@fig('ui-models', 'The four models of interface design')
def _():
    f = Fig(336, 84, fs=6.6)
    bs = [('User model', 'profile of users;\nset by the engineer'), ('Design model', 'created by the\nsoftware engineer'), ('Mental model', "user's perception\nof the system"), ('Implementation\nmodel', 'look and feel +\ndocumentation')]
    for i, (t, d) in enumerate(bs):
        x = 4 + i * 83
        f.box(x, 6, 72, 26, t, weight=500)
        f.text(x + 36, 46, d, size=6)
    f.arrow([(40, 60), (40, 72), (290, 72), (290, 60)], kind='fill', start='fill', size=4)
    f.text(165, 80, 'goal: make the implementation model coincide with the mental model', size=6.2, italic=True)
    return f.svg()


@fig('ui-spiral', 'The user interface design process')
def _():
    f = Fig(250, 160, fs=6.6)
    import math
    pts = []
    for k in range(0, 560):
        a = k / 40
        r = 8 + a * 4.2
        pts.append((125 + r * math.cos(a), 78 + r * math.sin(a) * 0.82))
    f.poly(pts, color=CYAN, w=1)
    labels = [('Interface analysis\nand modeling', 125, 10), ('Interface design', 225, 78), ('Interface\nconstruction', 125, 150), ('Interface\nvalidation', 22, 78)]
    for t, x, y in labels:
        f.text(x, y, t, weight=500, size=6.6)
    f.line(125, 78, 125, 22, w=0.4, color=GREY); f.line(125, 78, 125, 134, w=0.4, color=GREY)
    f.line(125, 78, 30, 78, w=0.4, color=GREY); f.line(125, 78, 220, 78, w=0.4, color=GREY)
    return f.svg()


# ------------------------------------------------------------------ screen mock-ups
def screen(f, x, y, w, h, title):
    f.rect(x, y, w, h, stroke=DARK, sw=0.8, fill='white', rx=3)
    f.rect(x, y, w, 16, stroke=DARK, sw=0.8, fill=CYAN, rx=3)
    f.rect(x, y + 10, w, 6, stroke='none', fill=CYAN)
    f.text(x + 6, y + 8, title, anchor='start', size=6.8, weight=600, color='white')


def btn(f, x, y, w, t, primary=True, h=12):
    f.rect(x, y, w, h, stroke=CYAN, fill=CYAN if primary else 'white', rx=2, sw=0.7)
    f.text(x + w / 2, y + h / 2, t, size=5.8, weight=500, color='white' if primary else DARK)


def chip(f, x, y, t, fill='#EAF7FD'):
    w = len(t) * 3 + 8
    f.rect(x, y, w, 9, stroke=CYAN, fill=fill, rx=4.5, sw=0.5)
    f.text(x + w / 2, y + 4.5, t, size=5.2)
    return w


@fig('scr-restaurant', 'Layout of the restaurant order management screen', wide=True)
def _():
    f = Fig(420, 214, fs=6.4)
    screen(f, 4, 4, 412, 206, 'Spice Garden — Orders')
    f.text(408, 12, 'Online ●   Tue 12:41', anchor='end', size=5.8, color='white')
    tabs = [('New (3)', True), ('Preparing (5)', False), ('Ready (2)', False), ('Completed', False)]
    for i, (t, a) in enumerate(tabs):
        f.rect(10 + i * 70, 24, 66, 14, stroke=CYAN, fill=CYAN if a else 'white', sw=0.6)
        f.text(43 + i * 70, 31, t, size=6, weight=500, color='white' if a else DARK)
    f.text(410, 31, 'Search order #', anchor='end', size=5.8, color=GREY); f.rect(330, 25, 84, 12, stroke=GREY, sw=0.5, fill='none')
    for j, (oid, items, t, pay) in enumerate([('#4821', '2 × Paneer tikka, 1 × Naan', '2 min ago', 'Paid online'), ('#4822', '1 × Veg biryani (no onion)', '3 min ago', 'Cash'), ('#4823', '3 × Masala dosa', '5 min ago', 'Paid online')]):
        y = 46 + j * 38
        f.rect(10, y, 262, 32, stroke=GREY, sw=0.5, fill='#FBFEFF' if j else '#EAF7FD')
        f.text(16, y + 8, f'Order {oid}', anchor='start', weight=600, size=6.4)
        f.text(16, y + 19, items, anchor='start', size=5.9)
        f.text(16, y + 27, f'{t} · {pay}', anchor='start', size=5.4, color=GREY)
        btn(f, 190, y + 4, 36, 'Accept'); btn(f, 230, y + 4, 36, 'Reject', False)
        f.text(229, y + 24, 'Prep time: [ 15 ▾ ] min', size=5.4)
    f.rect(280, 46, 130, 110, stroke=GREY, sw=0.5, fill='white')
    f.text(286, 54, 'Order #4821', anchor='start', weight=600)
    for k, t in enumerate(['2 × Paneer tikka     ₹ 440', '1 × Butter naan       ₹  60', 'Note: less spicy', '', 'Total                    ₹ 500']):
        f.text(286, 68 + k * 10, t, anchor='start', size=5.8)
    btn(f, 286, 128, 56, 'Mark ready'); btn(f, 346, 128, 58, 'Call rider', False)
    f.rect(280, 162, 130, 24, stroke=CYAN, sw=0.5, fill='#EAF7FD')
    f.text(345, 170, 'Menu item out of stock?', size=5.8); f.text(345, 179, 'Toggle availability ▸', size=5.8, weight=500)
    f.text(10, 196, 'Sound alert on new order · Last sync 5 s ago', anchor='start', size=5.4, color=GREY)
    return f.svg()


@fig('scr-assign', 'Layout of the delivery partner assignment screen', wide=True)
def _():
    f = Fig(420, 196, fs=6.4)
    screen(f, 4, 4, 412, 188, 'Dispatch — Assign delivery partner')
    f.text(12, 30, 'Order #4821 · Spice Garden → Anna Nagar, 3.2 km · Ready in 8 min', anchor='start', weight=500)
    # map
    f.rect(10, 40, 180, 140, stroke=GREY, sw=0.5, fill='#F2FAFD')
    for gx in range(10, 190, 30):
        f.line(gx, 40, gx, 180, w=0.3, color='#CDE9F5')
    for gy in range(40, 180, 28):
        f.line(10, gy, 190, gy, w=0.3, color='#CDE9F5')
    f.rect(92, 102, 10, 10, stroke=DARK, fill=DARK, sw=0.5); f.text(97, 120, 'Restaurant', size=5.4)
    for (x, y, n) in [(60, 80, 'A'), (130, 70, 'B'), (150, 140, 'C')]:
        f.circle(x, y, 5, fill=CYAN, stroke=CYAN); f.text(x, y, n, size=5, color='white', weight=600)
    f.text(100, 174, 'Live map of nearby partners', size=5.4, color=GREY)
    rows = [('A', 'Ravi K.', '0.8 km · 4 min', '★ 4.8', 'Free'), ('B', 'Meena S.', '1.4 km · 6 min', '★ 4.6', 'Free'), ('C', 'Arjun P.', '2.1 km · 9 min', '★ 4.9', 'Finishing a delivery')]
    f.text(200, 48, 'Suggested partners (nearest first)', anchor='start', weight=500)
    for j, (n, name, d, r, st) in enumerate(rows):
        y = 56 + j * 30
        f.rect(200, y, 210, 26, stroke=CYAN if j == 0 else GREY, sw=0.8 if j == 0 else 0.5, fill='#EAF7FD' if j == 0 else 'white')
        f.circle(210, y + 13, 5, fill=CYAN, stroke=CYAN); f.text(210, y + 13, n, size=5, color='white', weight=600)
        f.text(220, y + 9, f'{name}   {r}', anchor='start', size=6, weight=500)
        f.text(220, y + 19, f'{d} · {st}', anchor='start', size=5.6, color=GREY)
        btn(f, 362, y + 7, 42, 'Assign' if j < 2 else 'Queue', j == 0)
    f.rect(200, 150, 210, 30, stroke=GREY, sw=0.5, fill='white')
    f.text(206, 159, 'Auto-assign in 0:45 unless changed', anchor='start', size=5.8)
    btn(f, 206, 164, 60, 'Assign now'); btn(f, 270, 164, 60, 'Undo last', False)
    return f.svg()


@fig('scr-track', 'Layout of the real-time order tracking screen')
def _():
    f = Fig(336, 236, fs=6.4)
    screen(f, 90, 4, 156, 228, 'Track order #4821')
    f.rect(96, 24, 144, 88, stroke=GREY, sw=0.5, fill='#F2FAFD')
    f.poly([(110, 100), (140, 80), (170, 84), (200, 50), (226, 40)], color=CYAN, w=1.4, dash='3,2')
    f.rect(106, 96, 8, 8, fill=DARK, stroke=DARK); f.circle(226, 40, 4, fill='white', stroke=DARK)
    f.circle(170, 84, 5, fill=CYAN, stroke=CYAN)
    f.text(168, 106, 'rider location updates every 10 s', size=5.2, color=GREY)
    f.text(168, 122, 'Arriving in 12 min', size=9, weight=600)
    f.text(168, 133, 'Estimated 12:58 · 1.6 km away', size=5.8, color=GREY)
    steps = ['Order placed', 'Accepted', 'Being prepared', 'Picked up', 'Delivered']
    for i, s in enumerate(steps):
        x = 104 + i * 32
        f.circle(x, 148, 4, fill=CYAN if i < 4 else 'white', stroke=CYAN)
        if i < 4:
            f.line(x + 4, 148, x + 28, 148, w=1, color=CYAN if i < 3 else '#B9E5FA')
        f.text(x, 160, s.replace(' ', '\n', 1) if ' ' in s else s, size=4.9)
    f.rect(96, 172, 144, 26, stroke=GREY, sw=0.5, fill='white')
    f.circle(108, 185, 7, fill='#B9E5FA', stroke=CYAN)
    f.text(120, 181, 'Ravi K. ★ 4.8', anchor='start', size=6, weight=500); f.text(120, 191, 'TN 09 AB 1234', anchor='start', size=5.4, color=GREY)
    btn(f, 196, 178, 38, 'Call', True)
    btn(f, 96, 204, 70, 'Order details', False); btn(f, 170, 204, 70, 'Help', False)
    f.text(168, 225, 'Delayed? We will tell you why here.', size=5.2, color=GREY)
    return f.svg()


FIGS['ui-principles-table'] = ('User interface design principles and how the three screens satisfy them', table_html(
    ['Principle', 'Meaning', 'How the screens apply it'],
    [['Consistency', 'The same layout, colors, terms, and controls are used throughout.', 'All three screens share the title bar, button styles, primary color, and order number format; Accept, Assign, and Call are always filled primary buttons.'],
     ['Visibility of system status', 'Users always know what the system is doing.', 'Order tabs with counts and “last sync 5 s ago” (restaurant); auto-assign countdown (dispatch); five-step progress bar and ETA (tracking).'],
     ['Simplicity', 'Only what is needed for the task is shown.', 'Each order card shows items, time, and payment only; details appear in a side panel on selection (progressive disclosure).'],
     ['User control and freedom', 'Users can undo, cancel, and override.', 'Reject and prep-time selector; manual Assign and Undo last instead of forced auto-assignment; Help and Order details on the tracking screen.'],
     ['Error prevention and handling', 'Designs prevent mistakes and explain problems.', 'Partners who are busy are shown “Queue” not “Assign”; out-of-stock toggle prevents orders that cannot be met; delays are explained on the tracking screen.'],
     ['Efficiency of use', 'Frequent tasks need few actions.', 'One-tap Accept and Mark ready; partners ranked nearest first; sound alert on new orders; Call rider directly from the order.']],
    ['20%', '28%', '52%']), {'wide': True})


@fig('wx-arch', 'Module interactions in the weather sensing and alert system', wide=True, scale=0.92)
def _():
    from svg import anchor
    f = Fig(420, 150, fs=6.2)
    s = [f.box(4, 6 + i * 44, 70, 26, t, shadow=False) for i, t in enumerate(['Temperature\nprobe', 'Humidity\nsensor', 'Pressure\ntransducer'])]
    t = f.box(104, 6, 92, 26, 'Temperature data\ncollection & refinement')
    h = f.box(104, 50, 92, 26, 'Humidity & pressure\npackager')
    p = f.box(104, 94, 92, 26, 'External API poller')
    sy = f.box(226, 40, 80, 40, 'Multi-sensor\nsynchronizer', weight=500)
    ev = f.box(336, 40, 80, 40, 'Alert threshold\nevaluator & tracker', weight=500)
    lg = f.box(336, 104, 80, 26, 'Global alert log\n(shared store)')
    f.arrow([(74, 19), (104, 19)], size=3.5); f.text(89, 14, 'a', weight=600, color=CYAN)
    f.arrow([(74, 63), (104, 63)], size=3.5); f.arrow([(74, 107), (104, 107)], size=3.5)
    f.arrow([(196, 19), (240, 19), (240, 40)], size=3.5); f.text(218, 14, 'b', weight=600, color=CYAN)
    f.arrow([(196, 63), (226, 63)], size=3.5); f.text(211, 58, 'c', weight=600, color=CYAN)
    f.arrow([(196, 107), (266, 107), (266, 80)], size=3.5); f.text(230, 102, 'd', weight=600, color=CYAN)
    f.arrow([(306, 60), (336, 60)], size=3.5)
    f.arrow([(376, 80), (376, 104)], start='fill', size=3.5); f.text(384, 92, 'e', weight=600, color=CYAN)
    f.text(116, 140, 'remote weather service (third-party API) feeds the poller', size=5.6, italic=True)
    return f.svg()


@fig('wx-dashboard', 'Annotated dashboard for the weather sensing and alert system', wide=True)
def _():
    f = Fig(420, 250, fs=6.2)
    screen(f, 4, 4, 330, 242, 'Weather Monitor — Station WS-12')
    f.text(328, 12, 'Live ● 12:41   ⚙  ?', anchor='end', size=5.8, color='white')
    # nav
    f.rect(4, 20, 58, 226, stroke=GREY, sw=0.5, fill='#F2FAFD')
    for i, t in enumerate(['Dashboard', 'Alerts (2)', 'History', 'Thresholds', 'Sensors', 'Help']):
        f.rect(8, 28 + i * 20, 50, 15, stroke=CYAN if i == 0 else GREY, sw=0.5, fill=CYAN if i == 0 else 'white')
        f.text(33, 35.5 + i * 20, t, size=5.6, color='white' if i == 0 else DARK, weight=500 if i == 0 else 400)
    # tiles
    for i, (n, v, st) in enumerate([('Temperature', '31.4 °C', 'normal'), ('Humidity', '88 %', 'HIGH'), ('Pressure', '1002 hPa', 'normal')]):
        x = 70 + i * 86
        f.rect(x, 26, 80, 44, stroke=CYAN, sw=0.8, fill='#FFF4F2' if st == 'HIGH' else 'white')
        f.text(x + 6, 34, n, anchor='start', size=5.8, color=GREY)
        f.text(x + 6, 50, v, anchor='start', size=10, weight=600)
        f.text(x + 6, 63, st, anchor='start', size=5.6, weight=600, color='#D0342C' if st == 'HIGH' else '#1B8A3C')
    # alert banner
    f.rect(70, 76, 252, 26, stroke='#D0342C', sw=0.8, fill='#FFF4F2')
    f.text(76, 84, '⚠ Humidity above 85 % for 10 min (threshold 85 %)', anchor='start', size=5.8, weight=600)
    f.text(76, 95, 'Users notified by SMS and e-mail.', anchor='start', size=5.4)
    btn(f, 244, 82, 36, 'Acknowledge', True, 12); btn(f, 284, 82, 34, 'Undo', False, 12)
    # chart
    f.rect(70, 108, 252, 86, stroke=GREY, sw=0.5, fill='white')
    f.text(76, 116, 'Last 24 hours', anchor='start', size=5.8, weight=500)
    import math
    pts = [(80 + k * 6, 170 - 20 * math.sin(k / 5) - k * 0.4) for k in range(40)]
    f.poly(pts, color=CYAN, w=1)
    f.line(80, 142, 318, 142, dash='3,2', color='#D0342C', w=0.6); f.text(318, 138, 'threshold', anchor='end', size=5.2, color='#D0342C')
    for i, t in enumerate(['Temp', 'Humidity', 'Pressure']):
        f.rect(210 + i * 38, 111, 34, 10, stroke=CYAN, sw=0.5, fill=CYAN if i == 1 else 'white'); f.text(227 + i * 38, 116, t, size=5, color='white' if i == 1 else DARK)
    # table & threshold form
    f.rect(70, 200, 150, 42, stroke=GREY, sw=0.5, fill='white'); f.text(76, 208, 'Recent alerts', anchor='start', size=5.8, weight=500)
    f.text(76, 220, '12:31  Humidity high   open', anchor='start', size=5.4); f.text(76, 230, '09:05  Pressure low    closed', anchor='start', size=5.4)
    f.rect(226, 200, 96, 42, stroke=GREY, sw=0.5, fill='white'); f.text(232, 208, 'Humidity threshold', anchor='start', size=5.8, weight=500)
    f.rect(232, 214, 40, 11, stroke=GREY, sw=0.5); f.text(236, 219.5, '85  %', anchor='start', size=5.4)
    btn(f, 278, 213, 38, 'Save', True, 12); f.text(232, 236, 'range 0–100; default 85', anchor='start', size=4.8, color=GREY)
    # annotations
    notes = [(38, 'A', 'User familiarity'), (86, 'B', 'Consistency'), (126, 'C', 'Recoverability'), (166, 'D', 'User diversity'), (214, 'E', 'User guidance')]
    for y, k, t in notes:
        f.circle(346, y, 6, fill=CYAN, stroke=CYAN); f.text(346, y, k, size=6, color='white', weight=600)
        f.text(356, y, t, anchor='start', size=6, weight=500)
    for (x, y), k in [((70, 30), 'A'), ((70, 80), 'B'), ((322, 76), 'C'), ((322, 108), 'D'), ((322, 200), 'E')]:
        f.circle(x, y, 5, fill=CYAN, stroke='white', sw=0.6); f.text(x, y, k, size=5.4, color='white', weight=600)
    return f.svg()
