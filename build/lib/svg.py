"""Tiny SVG drawing kit in the figure style of the book (units: pt)."""
import math, html

CYAN = '#00ADEF'
SHADOW = '#6CCFF6'
FILL = '#00BDF2'
TINT = '#D4EFFC'
DARK = '#231F20'
GREY = '#6D6E71'
FONT = "'Fira Sans', sans-serif"


def esc(s):
    return html.escape(str(s), quote=False)


class Fig:
    _n = 0

    def __init__(self, w, h, fs=7.6):
        Fig._n += 1
        self.w, self.h, self.fs = w, h, fs
        self.el = []

    # ---- primitives -------------------------------------------------
    def raw(self, s):
        self.el.append(s)

    def line(self, x1, y1, x2, y2, w=0.5, color=DARK, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{w}"{d}/>')

    def poly(self, pts, w=0.5, color=DARK, fill='none', dash=None, close=False):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        tag = 'polygon' if close else 'polyline'
        p = ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)
        self.el.append(f'<{tag} points="{p}" stroke="{color}" stroke-width="{w}" fill="{fill}"{d}/>')

    def rect(self, x, y, w, h, stroke=CYAN, sw=1, fill='white', rx=0, shadow=False, dash=None):
        if shadow:
            self.el.append(f'<rect x="{x+3:.2f}" y="{y+3:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{SHADOW}"/>')
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def ellipse(self, cx, cy, rx, ry, stroke=CYAN, sw=1, fill='white', shadow=False):
        if shadow:
            self.el.append(f'<ellipse cx="{cx+3:.2f}" cy="{cy+3:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" fill="{SHADOW}"/>')
        self.el.append(f'<ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def circle(self, cx, cy, r, **k):
        self.ellipse(cx, cy, r, r, **k)

    def text(self, x, y, s, size=None, anchor='middle', weight=400, color=DARK, italic=False, lh=None, family=None):
        """Multi-line text; y is the vertical centre of the block."""
        size = size or self.fs
        lines = str(s).split('\n')
        lh = lh or size * 1.2
        y0 = y - (len(lines) - 1) * lh / 2 + size * 0.35
        st = ' font-style="italic"' if italic else ''
        fam = family or FONT
        for i, ln in enumerate(lines):
            self.el.append(f'<text x="{x:.2f}" y="{y0+i*lh:.2f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}"{st}>{esc(ln)}</text>')

    def tw(self, s, size=None):
        """Rough text width estimate for Fira Sans."""
        size = size or self.fs
        return max(len(l) for l in str(s).split('\n')) * size * 0.5

    # ---- arrows -----------------------------------------------------
    def head(self, x1, y1, x2, y2, kind='fill', size=5, color=DARK):
        a = math.atan2(y2 - y1, x2 - x1)
        ca, sa = math.cos(a), math.sin(a)
        L, W = size, size * 0.45
        p1 = (x2 - L * ca + W * sa, y2 - L * sa - W * ca)
        p2 = (x2 - L * ca - W * sa, y2 - L * sa + W * ca)
        if kind == 'fill':
            self.poly([p1, (x2, y2), p2], fill=color, close=True, w=0.3, color=color)
        elif kind == 'open':
            self.poly([p1, (x2, y2), p2], w=0.6, color=color)
        elif kind == 'tri':  # hollow triangle (generalization / realization)
            L, W = size * 1.6, size * 0.9
            p1 = (x2 - L * ca + W * sa, y2 - L * sa - W * ca)
            p2 = (x2 - L * ca - W * sa, y2 - L * sa + W * ca)
            self.poly([p1, (x2, y2), p2], fill='white', close=True, w=0.6, color=color)
        elif kind in ('diamond', 'fdiamond'):
            L, W = size * 2.2, size * 0.8
            m = (x2 - L / 2 * ca, y2 - L / 2 * sa)
            p1 = (m[0] + W * sa, m[1] - W * ca)
            p3 = (x2 - L * ca, y2 - L * sa)
            p2 = (m[0] - W * sa, m[1] + W * ca)
            self.poly([(x2, y2), p1, p3, p2], fill=(color if kind == 'fdiamond' else 'white'), close=True, w=0.6, color=color)

    def arrow(self, pts, kind='fill', dash=None, w=0.5, color=DARK, start=None, size=5):
        self.poly(pts, w=w, color=color, dash=dash)
        if kind:
            (x1, y1), (x2, y2) = pts[-2], pts[-1]
            self.head(x1, y1, x2, y2, kind, size, color)
        if start:
            (x1, y1), (x2, y2) = pts[1], pts[0]
            self.head(x1, y1, x2, y2, start, size, color)

    # ---- composite shapes --------------------------------------------
    def box(self, x, y, w, h, label='', shadow=True, rx=0, size=None, weight=400, fill='white', stroke=CYAN):
        self.rect(x, y, w, h, rx=rx, shadow=shadow, fill=fill, stroke=stroke)
        if label:
            self.text(x + w / 2, y + h / 2, label, size=size, weight=weight)
        return (x, y, w, h)

    def rbox(self, x, y, w, h, label='', **k):
        return self.box(x, y, w, h, label, rx=min(h / 2, 9), **k)

    def actor(self, x, y, label='', size=None):
        """Stick figure with head centred at (x, y)."""
        self.circle(x, y, 4.2, stroke=DARK, sw=0.7)
        self.line(x, y + 4.2, x, y + 15, w=0.7)
        self.line(x - 7, y + 8, x + 7, y + 8, w=0.7)
        self.line(x, y + 15, x - 6, y + 23, w=0.7)
        self.line(x, y + 15, x + 6, y + 23, w=0.7)
        if label:
            self.text(x, y + 32, label, size=size)

    def usecase(self, cx, cy, label, rx=None, ry=12):
        rx = rx or max(28, self.tw(label) / 2 + 10)
        self.ellipse(cx, cy, rx, ry)
        self.text(cx, cy, label)
        return (cx, cy, rx, ry)

    def uclass(self, x, y, w, name, attrs=(), ops=(), lh=None, stroke=CYAN):
        lh = lh or self.fs * 1.28
        hn = lh * (name.count('\n') + 1) + 6
        ha = lh * len(attrs) + 5 if attrs else 0
        ho = lh * len(ops) + 5 if ops else 0
        h = hn + ha + ho
        self.rect(x, y, w, h, fill='white', stroke=stroke)
        self.rect(x, y, w, hn, fill=FILL, stroke=stroke)
        self.text(x + w / 2, y + hn / 2, name, weight=500)
        yy = y + hn
        for grp in (attrs, ops):
            if not grp:
                continue
            self.line(x, yy, x + w, yy, w=1, color=stroke)
            for i, a in enumerate(grp):
                self.text(x + 4, yy + 3 + lh * (i + 0.5), a, anchor='start')
            yy += lh * len(grp) + 5
        return (x, y, w, h)

    def diamond(self, cx, cy, r=6, fill='white'):
        self.poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], close=True, color=CYAN, w=1, fill=fill)

    def start(self, cx, cy, r=5):
        self.circle(cx, cy, r, fill=CYAN, stroke=CYAN)

    def end(self, cx, cy, r=6):
        self.circle(cx, cy, r, fill='white', stroke=CYAN)
        self.circle(cx, cy, r - 2.5, fill=CYAN, stroke=CYAN)

    def bar(self, x, y, w, h):
        self.rect(x, y, w, h, fill=DARK, stroke=DARK, sw=0.5)

    def svg(self):
        body = '\n'.join(self.el)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}pt" height="{self.h}pt" '
                f'viewBox="0 0 {self.w} {self.h}">{body}</svg>')


def anchor(b, side):
    """Point on the edge of a box tuple (x,y,w,h)."""
    x, y, w, h = b
    return {'l': (x, y + h / 2), 'r': (x + w, y + h / 2), 't': (x + w / 2, y), 'b': (x + w / 2, y + h),
            'c': (x + w / 2, y + h / 2)}[side]
