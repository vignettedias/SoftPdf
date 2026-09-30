from svg import Fig, anchor, CYAN, DARK

FIGS = {}


def fig(fid, caption, **opts):
    def deco(fn):
        FIGS[fid] = (caption, fn, opts)
        return fn
    return deco


def clip(fid, caption, page, rect, **opts):
    FIGS[fid] = (caption, ('clip', page, rect), opts)


@fig('req-kinds', 'Business, functional, and non-functional requirements')
def _():
    f = Fig(330, 150)
    top = f.box(115, 6, 100, 26, 'Software\nrequirements', weight=500)
    l = f.box(20, 58, 120, 26, 'What the software\nshould do')
    r = f.box(190, 58, 120, 26, 'Constraints on\nhow it operates')
    f.poly([anchor(top, 'b'), (165, 45), (80, 45), anchor(l, 't')])
    f.poly([(165, 45), (250, 45), anchor(r, 't')])
    ex1 = ['Process user\ninputs', 'Store and\nretrieve data', 'Generate\nreports', 'Control\nexternal\ndevices']
    ex2 = ['Performance', 'Security', 'Usability', 'Compatibility']
    for i, t in enumerate(ex1):
        b = f.box(2 + i * 40, 110, 37, 34, '', shadow=False)
        f.text(20.5 + i * 40, 127, t, size=5.6)
        f.line(80, 84, 80, 97); f.line(20, 97, 140, 97); f.line(20 + i * 40, 97, 20 + i * 40, 110)
    for i, t in enumerate(ex2):
        b = f.box(172 + i * 40, 110, 37, 34, '', shadow=False)
        f.text(190.5 + i * 40, 127, t.replace('Compatibility', 'Compati-\nbility').replace('Performance', 'Perfor-\nmance'), size=5.8)
        f.line(250, 84, 250, 97); f.line(190, 97, 310, 97); f.line(190 + i * 40, 97, 190 + i * 40, 110)
    return f.svg()


@fig('req-nesting', 'Business requirements frame the functional and non-functional requirements')
def _():
    f = Fig(300, 118)
    f.rect(2, 2, 290, 110, fill='#EAF7FD', stroke=CYAN, rx=6)
    f.text(10, 13, 'Business requirements — why the system is needed', anchor='start', weight=500)
    f.rect(12, 24, 270, 80, fill='white', stroke=CYAN, rx=5)
    f.text(20, 35, 'Functional requirements — what the system must do', anchor='start', weight=500)
    f.rect(22, 46, 250, 50, fill='#EAF7FD', stroke=CYAN, rx=4)
    f.text(30, 57, 'Non-functional requirements — how well it must do it', anchor='start', weight=500)
    f.text(30, 77, 'Quality attributes and constraints: response time, security,\nusability, reliability, platform and legal constraints', anchor='start', size=7)
    return f.svg()


clip('nfr-types', 'Types of non-functional requirement', 104, (94.0, 128.3, 505.5, 358.8), wide=True)


def table_html(head, rows, widths=None):
    cols = ''
    if widths:
        cols = '<colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>'
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="pt">{cols}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


FIGS['srs-structure'] = ('The structure of a software requirements specification', table_html(
    ['Part', 'Description'],
    [['1. Introduction', 'Purpose of the document and its intended readers; scope of the product; definitions, acronyms, and abbreviations; references; an overview of how the rest of the document is organized.'],
     ['2. Overall description', 'Product perspective (how the system fits with other systems); a summary of product functions; user classes and their characteristics; the operating environment; design and implementation constraints; assumptions and dependencies.'],
     ['3. External interface requirements', 'User interfaces, hardware interfaces, software interfaces, and communication interfaces.'],
     ['4. System features (specific requirements)', 'The detailed functional requirements, organized by feature, by user class, or by mode of operation. This is normally the largest and most important part of the document.'],
     ['5. Other non-functional requirements', 'Performance, safety, and security requirements; software quality attributes; business rules.'],
     ['Supporting information', 'Glossary, analysis models, a list of items still to be decided, appendices (for example sample input and output formats), and an index.']],
    ['30%', '70%']), {'wide': True})


@fig('re-process', 'The requirements engineering process')
def _():
    f = Fig(330, 205)
    fs = f.box(4, 6, 80, 24, 'Feasibility\nstudy')
    ea = f.box(104, 6, 96, 24, 'Requirements\nelicitation and analysis')
    sp = f.box(160, 70, 90, 24, 'Requirements\nspecification')
    va = f.box(236, 124, 90, 24, 'Requirements\nvalidation')
    f.arrow([anchor(fs, 'r'), anchor(ea, 'l')])
    f.arrow([(160, 30), (160, 50), (205, 50), (205, 70)])
    f.arrow([(230, 94), (230, 110), (281, 110), (281, 124)])
    f.arrow([(281, 124), (281, 110)], kind=None)
    f.arrow([(290, 124), (290, 60), (250, 60), (250, 70)], dash='2,2')
    f.arrow([(212, 70), (212, 44), (200, 18)], dash='2,2')
    # products
    def prod(x, y, t):
        f.ellipse(x, y, 34, 13, stroke=CYAN, sw=0.8)
        f.text(x, y, t, size=6.8)
    prod(44, 64, 'Feasibility\nreport'); f.arrow([(44, 30), (44, 51)])
    prod(120, 118, 'System\nmodels'); f.arrow([(130, 30), (125, 105)])
    prod(185, 150, 'User and system\nrequirements'); f.arrow([(190, 94), (186, 137)])
    prod(281, 184, 'Requirements\ndocument'); f.arrow([(281, 148), (281, 171)])
    f.arrow([(120, 131), (120, 184), (247, 184)])
    f.arrow([(200, 162), (200, 176), (250, 178)])
    return f.svg()


clip('re-spiral', 'A spiral view of the requirements engineering process', 115, (108, 128, 514, 481), wide=True,
     masks=[(100, 428, 176, 482)], scale=0.86)
clip('elicit-process', 'The requirements elicitation and analysis process', 117, (244, 127, 471, 282))
clip('req-evolution', 'Requirements evolution', 127, (249, 127, 466, 236))
clip('change-mgmt', 'Requirements change management', 129, (145, 126, 526, 168), wide=True)


@fig('agile-re', 'Requirements engineering in agile development')
def _():
    f = Fig(334, 120)
    xs = [4, 88, 172, 256]
    names = ['Product\nbacklog', 'User stories\n(refined)', 'Sprint', 'Review and\nfeedback']
    subs = ['Prioritized master list\nof features and fixes', '“As a ⟨role⟩, I want\n⟨feature⟩ so that ⟨benefit⟩”', 'Top items selected;\nscope frozen for sprint', 'Working software shown;\nbacklog updated']
    bs = []
    for x, n, s in zip(xs, names, subs):
        b = f.box(x, 8, 72, 30, n, weight=500)
        bs.append(b)
        f.text(x + 36, 58, s, size=6.4)
    for a, b in zip(bs, bs[1:]):
        f.arrow([anchor(a, 'r'), anchor(b, 'l')])
    f.arrow([(292, 74), (292, 100), (40, 100), (40, 41)], dash='3,2')
    f.text(166, 108, 'new, changed, or dropped items feed back into the backlog', size=6.6, italic=True)
    return f.svg()
