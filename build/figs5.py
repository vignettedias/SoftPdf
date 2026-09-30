import math
from svg import Fig, anchor, CYAN, DARK, GREY, FILL
from figs4 import table_html

FIGS = {}


def fig(fid, caption, **opts):
    def deco(fn):
        FIGS[fid] = (caption, fn, opts)
        return fn
    return deco


# ------------------------------------------------------------------ helpers
def proc(f, cx, cy, r, num, name, size=7):
    f.circle(cx, cy, r, shadow=True)
    f.text(cx, cy - r * 0.32, num, size=size, weight=500)
    f.line(cx - r * 0.55, cy - r * 0.12, cx + r * 0.55, cy - r * 0.12, w=0.4, color=CYAN)
    f.text(cx, cy + r * 0.3, name, size=size)


def ext(f, x, y, w, h, name, size=7.2):
    return f.box(x, y, w, h, name, weight=500, size=size)


def store(f, x, y, w, sid, name, size=6.8):
    h = 13
    f.rect(x, y, w, h, stroke='none', fill='white')
    f.line(x, y, x + w, y, w=0.8, color=CYAN)
    f.line(x, y + h, x + w, y + h, w=0.8, color=CYAN)
    f.line(x, y, x, y + h, w=0.8, color=CYAN)
    f.line(x + 16, y, x + 16, y + h, w=0.6, color=CYAN)
    f.text(x + 8, y + h / 2, sid, size=size, weight=500)
    f.text(x + 16 + (w - 16) / 2, y + h / 2, name, size=size)
    return (x, y, w, h)


def edge_pt(cx, cy, r, tx, ty):
    a = math.atan2(ty - cy, tx - cx)
    return (cx + r * math.cos(a), cy + r * math.sin(a))


def lab(f, x, y, t, size=6.6, anchor='middle'):
    f.text(x, y, t, size=size, anchor=anchor)


# ------------------------------------------------------------------ UML overview
@fig('uml-types', 'Structural and behavioral diagrams of the UML', wide=True)
def _():
    f = Fig(420, 150, fs=7)
    root = f.box(180, 4, 60, 20, 'UML models', weight=500)
    s = f.box(58, 44, 80, 20, 'Structural models', weight=500)
    b = f.box(282, 44, 80, 20, 'Behavioral models', weight=500)
    f.poly([anchor(root, 'b'), (210, 34), (98, 34), anchor(s, 't')]); f.poly([(210, 34), (322, 34), anchor(b, 't')])
    sn = ['Class', 'Object', 'Component', 'Deploy-\nment', 'Package', 'Composite\nstructure', 'Profile']
    for i, t in enumerate(sn):
        x = 2 + i * 29.5
        f.box(x, 86, 27, 26, t, size=5.9, shadow=False)
        f.line(x + 13.5, 76, x + 13.5, 86)
    f.line(15.5, 76, 192.5, 76); f.line(98, 64, 98, 76)
    bn = ['Use case', 'Activity', 'State\nmachine', 'Interaction']
    for i, t in enumerate(bn):
        x = 226 + i * 48
        f.box(x, 86, 42, 26, t, size=6.2, shadow=False)
        f.line(x + 21, 76, x + 21, 86)
    f.line(247, 76, 391, 76); f.line(322, 64, 322, 76)
    inn = ['Sequence', 'Communi-\ncation', 'Timing', 'Interaction\noverview']
    for i, t in enumerate(inn):
        x = 246 + i * 43.5
        f.box(x, 124, 40, 24, t, size=5.9, shadow=False)
        f.line(x + 20, 118, x + 20, 124)
    f.line(266, 118, 396.5, 118); f.line(391, 112, 391, 118)
    return f.svg()


# ------------------------------------------------------------------ DFD
@fig('dfd-symbols', 'Data-flow diagram notation')
def _():
    f = Fig(330, 62)
    ext(f, 6, 14, 58, 26, 'Customer')
    f.text(35, 54, 'External entity\n(source or sink)', size=6.6)
    proc(f, 118, 27, 22, '1.0', 'Validate\norder', size=6.4)
    f.text(118, 57, 'Process', size=6.6)
    f.arrow([(170, 27), (228, 27)])
    f.text(199, 21, 'order details', size=6.6)
    f.text(199, 44, 'Data flow', size=6.6)
    store(f, 246, 20, 78, 'D1', 'Orders')
    f.text(285, 46, 'Data store', size=6.6)
    return f.svg()


@fig('sales-context', 'Context diagram (level-0 DFD) of a sales order system')
def _():
    f = Fig(336, 200)
    cx, cy, r = 176, 100, 36
    f.circle(cx, cy, r, shadow=True)
    f.text(cx, cy, 'Sales order\nsystem', weight=500, size=7.6)
    m = ext(f, 6, 8, 68, 24, 'Managers')
    e = ext(f, 262, 8, 68, 24, 'Employees')
    c = ext(f, 262, 168, 68, 24, 'Customers')
    # managers
    f.arrow([(74, 16), (140, 16), edge_pt(cx, cy, r, 150, 60)]); lab(f, 108, 11, 'New employee')
    f.arrow([edge_pt(cx, cy, r, 60, 110), (40, 110), (40, 32)]); lab(f, 70, 104, 'Employee list')
    f.arrow([edge_pt(cx, cy, r, 60, 130), (22, 130), (22, 32)]); lab(f, 70, 136, 'Vendor and product list')
    # employees
    f.arrow([(262, 16), (205, 16), edge_pt(cx, cy, r, 200, 60)]); lab(f, 232, 11, 'Update employee')
    f.arrow([(262, 26), (230, 26), edge_pt(cx, cy, r, 225, 72)]); lab(f, 246, 38, 'Product and\ncategory')
    # customers
    f.arrow([edge_pt(cx, cy, r, 280, 100), (296, 100), (296, 168)]); lab(f, 268, 94, 'Order invoice')
    f.arrow([(262, 178), (150, 178), edge_pt(cx, cy, r, 150, 150)]); lab(f, 232, 172, 'Order and order lines')
    f.arrow([(262, 186), (200, 186), (200, 170), edge_pt(cx, cy, r, 196, 150)], kind='fill'); lab(f, 232, 194, 'Customer details')
    return f.svg()


@fig('lemon-l0', 'Context diagram (level 0) of the lemonade stand system')
def _():
    f = Fig(336, 190)
    cx, cy, r = 168, 78, 34
    f.circle(cx, cy, r, shadow=True)
    f.text(cx, cy - 10, '0.0', weight=500); f.text(cx, cy + 6, 'Lemonade\nsystem', size=7.4)
    cu = ext(f, 4, 60, 64, 28, 'CUSTOMER')
    em = ext(f, 268, 60, 64, 28, 'EMPLOYEE')
    ve = ext(f, 136, 150, 64, 28, 'VENDOR')
    f.arrow([(68, 64), (cx - r + 2, 64)]); lab(f, 101, 59, 'Customer order')
    f.arrow([(cx - r, 74), (68, 74)]); lab(f, 101, 81, 'Product served', size=6.3)
    f.arrow([(68, 84), (cx - r + 3, 91)]); lab(f, 101, 93, 'Payment')
    f.arrow([(cx + r - 2, 62), (268, 62)]); lab(f, 235, 57, 'Sales forecast', size=6.3)
    f.arrow([(268, 70), (cx + r, 70)]); lab(f, 235, 76, 'Production schedule', size=6.0)
    f.arrow([(cx + r, 80), (268, 80)]); lab(f, 240, 86, 'Pay', size=6.3)
    f.arrow([(268, 88), (cx + r - 4, 90)]); lab(f, 240, 96, 'Time worked', size=6.3)
    f.arrow([(152, 150), (152, cy + r - 3)]); lab(f, 126, 126, 'Received goods', size=6.3)
    f.arrow([(160, cy + r - 1), (160, 150)]); lab(f, 130, 138, 'Payment', size=6.3)
    f.arrow([(182, cy + r - 2), (182, 150)]); lab(f, 212, 132, 'Purchase order', size=6.3)
    return f.svg()


@fig('lemon-l1', 'Level-1 DFD of the lemonade stand system', wide=True, scale=0.88)
def _():
    f = Fig(420, 230)
    r = 26
    P = {'1': (212, 34), '2': (212, 104), '3': (212, 172), '4': (330, 200)}
    proc(f, *P['1'], r, '1.0', 'Sale')
    proc(f, *P['2'], r, '2.0', 'Production')
    proc(f, *P['3'], r, '3.0', 'Procure-\nment')
    proc(f, *P['4'], r, '4.0', 'Payroll')
    cu = ext(f, 6, 70, 70, 26, 'CUSTOMER')
    ve = ext(f, 6, 160, 70, 26, 'VENDOR')
    em = ext(f, 344, 90, 70, 26, 'EMPLOYEE')
    f.arrow([(60, 70), (60, 30), (186, 30)]); lab(f, 124, 25, 'Customer order')
    f.arrow([(70, 70), (70, 44), (188, 44)]); lab(f, 128, 39, 'Payment')
    f.arrow([(186, 104), (76, 88)]); lab(f, 124, 88, 'Product served')
    f.arrow([(212, 60), (212, 78)]); lab(f, 242, 69, 'Product ordered', anchor='start')
    f.arrow([(238, 30), (360, 30), (360, 90)]); lab(f, 300, 25, 'Sales forecast')
    f.arrow([(344, 100), (238, 100)]); lab(f, 290, 95, 'Production schedule')
    f.arrow([(212, 146), (212, 130)]); lab(f, 240, 138, 'Inventory', anchor='start')
    f.arrow([(76, 166), (186, 166)]); lab(f, 130, 161, 'Received goods')
    f.arrow([(186, 176), (76, 176)]); lab(f, 130, 183, 'Purchase order')
    f.arrow([(192, 190), (40, 190), (40, 186)]); lab(f, 118, 196, 'Payment')
    f.arrow([(356, 196), (390, 196), (390, 116)]); lab(f, 398, 160, 'Pay', anchor='start')
    f.arrow([(400, 116), (400, 214), (356, 208)]); lab(f, 396, 222, 'Time worked')
    return f.svg()


@fig('lemon-l2', 'Level-2 DFD for process 1.0, Sale')
def _():
    f = Fig(336, 170)
    r = 23
    proc(f, 90, 40, r, '1.1', 'Record\norder')
    proc(f, 90, 125, r, '1.2', 'Receive\npayment')
    proc(f, 262, 82, r, '1.3', 'Produce sales\nforecast', size=6.4)
    o = store(f, 150, 26, 82, 'D1', 'ORDER')
    p = store(f, 150, 118, 82, 'D2', 'PAYMENT')
    lab(f, 4, 12, 'Customer order', anchor='start'); f.arrow([(10, 17), (10, 40), (67, 40)])
    lab(f, 4, 150, 'Payment', anchor='start'); f.arrow([(10, 143), (10, 125), (67, 125)])
    f.arrow([(113, 36), (150, 33)])
    f.arrow([(113, 127), (150, 125)])
    f.arrow([(232, 33), (250, 62)])
    f.arrow([(232, 125), (250, 102)])
    f.arrow([(90, 63), (90, 102)]); lab(f, 94, 83, 'Order amount', anchor='start')
    lab(f, 300, 136, 'Sales forecast\n(to EMPLOYEE)', size=6.4); f.arrow([(275, 102), (295, 124)])
    f.arrow([(104, 21), (130, 6), (170, 6)]); lab(f, 174, 6, 'Product ordered (to 2.0)', size=6.4, anchor='start')
    return f.svg()


@fig('lemon-tree', 'Decomposition of the lemonade stand system across DFD levels', wide=True)
def _():
    f = Fig(420, 160, fs=6.6)
    f.circle(34, 75, 22, shadow=True); f.text(34, 69, '0.0', weight=500); f.text(34, 81, 'Lemonade\nsystem', size=6)
    tops = [('1.0', 'Sale'), ('2.0', 'Production'), ('3.0', 'Procurement'), ('4.0', 'Payroll')]
    kids = [[('1.1', 'Record\norder'), ('1.2', 'Receive\npayment'), ('1.3', 'Produce\nforecast')],
            [('2.1', 'Serve\nproduct'), ('2.2', 'Produce\nproduct'), ('2.3', 'Store\nproduct')],
            [('3.1', 'Produce\npurch. order'), ('3.2', 'Receive\nitems'), ('3.3', 'Pay\nvendor')],
            [('4.1', 'Record time\nworked'), ('4.2', 'Calculate\npayroll'), ('4.3', 'Pay\nemployee')]]
    for i, ((n, t), ks) in enumerate(zip(tops, kids)):
        y = 18 + i * 34
        f.circle(140, y, 15); f.text(140, y - 5, n, weight=500); f.text(140, y + 5, t, size=5.6)
        f.line(54, 75, 125, y, w=0.4)
        for j, (kn, kt) in enumerate(ks):
            x = 250 + j * 58
            f.circle(x, y, 15); f.text(x, y - 5, kn, weight=500); f.text(x, y + 5, kt, size=5.2)
            f.line(155, y, x - 15, y, w=0.3, dash='2,2') if j == 0 else None
    for x, t in [(34, 'Level 0\n(context)'), (140, 'Level 1'), (308, 'Level 2')]:
        f.text(x, 150, t, weight=500, size=6.8)
    f.line(88, 4, 88, 150, dash='3,3', color=CYAN); f.line(196, 4, 196, 150, dash='3,3', color=CYAN)
    return f.svg()


# ------------------------------------------------------------------ use cases
@fig('lib-usecase', 'Use cases of a library system')
def _():
    f = Fig(336, 236)
    f.rect(70, 4, 200, 228, stroke=GREY, sw=0.6, fill='white')
    f.text(170, 13, 'Library system', size=7, weight=500)
    f.actor(28, 82, 'Member')
    f.actor(310, 82, 'Librarian')
    uc = {}
    uc['search'] = f.usecase(125, 36, 'Search book')
    uc['borrow'] = f.usecase(125, 78, 'Borrow book')
    uc['return'] = f.usecase(125, 124, 'Return book')
    uc['view'] = f.usecase(125, 178, 'View account')
    uc['avail'] = f.usecase(222, 36, 'Check\navailability', rx=36, ry=14)
    uc['acct'] = f.usecase(222, 86, 'Check account\nstatus', rx=38, ry=14)
    uc['fine'] = f.usecase(222, 140, 'Generate fine', rx=36)
    uc['mm'] = f.usecase(232, 186, 'Manage members', rx=36)
    uc['add'] = f.usecase(232, 214, 'Add book', rx=30)
    for k in ('search', 'borrow', 'return', 'view'):
        cx, cy, rx, ry = uc[k]
        f.line(38, 96, cx - rx, cy, w=0.5)
    f.line(300, 96, 268, 186, w=0.5)
    f.line(300, 96, 256, 207, w=0.5)
    f.arrow([(160, 70), (190, 44)], kind='open', dash='3,2'); f.text(170, 50, '«include»', size=6)
    f.arrow([(163, 80), (184, 84)], kind='open', dash='3,2'); f.text(172, 94, '«include»', size=6)
    f.arrow([(186, 138), (161, 128)], kind='open', dash='3,2'); f.text(170, 146, '«extend»', size=6)
    return f.svg()


# ------------------------------------------------------------------ sequence helpers
class Seq:
    def __init__(self, f, names, x0, gap, top, bottom, actors=()):
        self.f, self.x, self.top, self.bottom = f, {}, top, bottom
        for i, n in enumerate(names):
            x = x0 + i * gap
            self.x[n] = x
            if n in actors:
                f.actor(x, top + 5, '')
                f.text(x, top - 7, n, size=6.8)
                y1 = top + 30
            else:
                w = max(40, f.tw(n, 6.8) + 10)
                f.rect(x - w / 2, top, w, 17, stroke=CYAN, fill='white')
                f.text(x, top + 8.5, n, size=6.8)
                y1 = top + 17
            f.line(x, y1, x, bottom, w=0.5, color=GREY, dash='3,2')

    def act(self, n, y0, y1):
        self.f.rect(self.x[n] - 2.5, y0, 5, y1 - y0, stroke=CYAN, fill='white', sw=0.8)

    def msg(self, a, b, y, label, ret=False, size=6.4):
        xa, xb = self.x[a], self.x[b]
        d = 2.5 if xb > xa else -2.5
        pts = [(xa + d, y), (xb - d, y)]
        self.f.arrow(pts, kind='open' if ret else 'fill', dash='3,2' if ret else None, size=4.5)
        self.f.text((xa + xb) / 2, y - 5, label, size=size)

    def self_msg(self, a, y, label):
        x = self.x[a] + 2.5
        self.f.arrow([(x, y), (x + 18, y), (x + 18, y + 9), (x + 3, y + 9)], size=4)
        self.f.text(x + 22, y + 4, label, size=6.2, anchor='start')


@fig('lib-sequence', 'Sequence diagram for borrowing a book', wide=True, scale=0.8)
def _():
    f = Fig(420, 262)
    s = Seq(f, ['Student member', ':Library', ':Book', ':Loan'], 40, 112, 14, 256, actors=('Student member',))
    s.act('Student member', 48, 250)
    s.act(':Library', 56, 240)
    s.msg('Student member', ':Library', 60, '1: searchBook(title)')
    s.act(':Book', 72, 94)
    s.msg(':Library', ':Book', 76, '2: checkAvailability()')
    s.msg(':Book', ':Library', 92, '3: availability status', ret=True)
    s.msg(':Library', 'Student member', 108, '4: display result', ret=True)
    f.rect(8, 118, 408, 124, stroke=GREY, sw=0.6, fill='none')
    f.rect(8, 118, 26, 11, stroke=GREY, sw=0.6, fill='white'); f.text(21, 123.5, 'opt', size=6.4, weight=500)
    f.text(40, 127, '[book available]', size=6.4, anchor='start')
    s.msg('Student member', ':Library', 148, '5: confirmBorrow()')
    s.act(':Book', 156, 176)
    s.msg(':Library', ':Book', 160, '6: reserveBook()')
    s.act(':Loan', 180, 206)
    s.msg(':Library', ':Loan', 184, '7: createLoan(member, book)')
    s.msg(':Loan', ':Library', 202, '8: loan ID created', ret=True)
    s.msg(':Library', ':Book', 216, '9: updateStatus(on loan)')
    s.msg(':Library', 'Student member', 234, '10: borrow confirmed', ret=True)
    return f.svg()


@fig('lib-comm', 'Communication diagram for borrowing a book')
def _():
    f = Fig(336, 166)
    f.raw('<g transform="translate(0,14)">')
    sm = f.box(6, 20, 70, 24, 'Student member', shadow=False)
    li = f.box(140, 20, 60, 24, ':Library', shadow=False)
    bk = f.box(264, 20, 60, 24, ':Book', shadow=False)
    lo = f.box(140, 112, 60, 24, ':Loan', shadow=False)
    f.line(76, 32, 140, 32, w=0.6); f.line(200, 32, 264, 32, w=0.6); f.line(170, 44, 170, 112, w=0.6)
    f.arrow([(86, 26), (130, 26)], size=4); f.text(108, 11, '1: searchBook\n5: confirmBorrow', size=6.2)
    f.arrow([(130, 40), (86, 40)], size=4, kind='open'); f.text(108, 54, '4: display result\n10: borrow confirmed', size=6.2)
    f.arrow([(210, 26), (254, 26)], size=4); f.text(232, 6, '2: checkAvailability\n6: reserveBook\n9: updateStatus', size=6.2)
    f.arrow([(254, 40), (210, 40)], size=4, kind='open'); f.text(232, 50, '3: availability status', size=6.2)
    f.arrow([(178, 60), (178, 100)], size=4); f.text(184, 76, '7: createLoan', size=6.2, anchor='start')
    f.arrow([(162, 100), (162, 60)], size=4, kind='open'); f.text(156, 84, '8: loan ID', size=6.2, anchor='end')
    f.raw('</g>')
    return f.svg()


@fig('swiggy-seq', 'Sequence diagram for payment processing in a food-delivery system', wide=True, scale=0.82)
def _():
    f = Fig(420, 300)
    s = Seq(f, ['Customer', ':App', ':OrderSystem', ':PaymentGateway', ':BankServer', ':OrderDB'], 22, 76, 14, 294, actors=('Customer',))
    s.act('Customer', 48, 284)
    s.msg('Customer', ':App', 56, '1: placeOrder(cart)')
    s.act(':App', 52, 280)
    s.msg(':App', ':OrderSystem', 72, '2: createOrder(cart)')
    s.act(':OrderSystem', 68, 276)
    s.msg(':OrderSystem', ':OrderDB', 88, '3: save(order, PENDING)')
    s.msg(':OrderSystem', ':PaymentGateway', 106, '4: requestPayment(id, amt)')
    s.act(':PaymentGateway', 102, 186)
    s.msg(':PaymentGateway', ':BankServer', 124, '5: authorize(amount)')
    s.act(':BankServer', 120, 146)
    s.msg(':BankServer', ':PaymentGateway', 142, '6: approved / rejected', ret=True)
    s.msg(':PaymentGateway', ':OrderSystem', 164, '7: paymentStatus', ret=True)
    f.rect(96, 174, 320, 106, stroke=GREY, sw=0.6, fill='none')
    f.rect(96, 174, 22, 11, stroke=GREY, sw=0.6, fill='white'); f.text(107, 179.5, 'alt', size=6.4, weight=500)
    f.text(122, 194, '[approved]', size=6.4, anchor='start')
    s.msg(':OrderSystem', ':OrderDB', 204, '8: updateStatus(PAID)')
    s.msg(':OrderSystem', ':App', 220, '9: confirmation(orderId)', ret=True)
    f.line(96, 230, 416, 230, w=0.5, color=GREY, dash='4,2')
    f.text(122, 240, '[rejected]', size=6.4, anchor='start')
    s.msg(':OrderSystem', ':OrderDB', 252, '10: updateStatus(FAILED)')
    s.msg(':OrderSystem', ':App', 270, '11: paymentFailed(retry)', ret=True)
    s.msg(':App', 'Customer', 288, '12: show result', ret=True)
    return f.svg()


# ------------------------------------------------------------------ class diagrams
@fig('class-rels', 'Notation for relationships between classes')
def _():
    f = Fig(336, 146, fs=7)
    rows = [('Association', None, None, 'Student enrolls in Course'),
            ('Aggregation', 'diamond', None, 'Department has Professors'),
            ('Composition', 'fdiamond', None, 'House has Rooms'),
            ('Generalization', None, 'tri', 'ElectricCar is a Car'),
            ('Dependency', None, 'open', 'ReportGenerator uses Data'),
            ('Realization', None, 'tri', 'CardPayment implements Payable')]
    for i, (n, st, en, ex) in enumerate(rows):
        y = 12 + i * 23
        f.text(4, y, n, anchor='start', weight=500)
        dash = '3,2' if n in ('Dependency', 'Realization') else None
        f.rect(84, y - 7, 22, 14, sw=0.8)
        f.rect(170, y - 7, 22, 14, sw=0.8)
        f.arrow([(106, y), (170, y)], kind=en, dash=dash, start=st, size=5)
        f.text(204, y, ex, anchor='start', size=6.8)
    return f.svg()


@fig('lib-class', 'Class diagram of a library system', wide=True, scale=0.84)
def _():
    f = Fig(420, 235, fs=6.8)
    lib = f.uclass(4, 96, 86, 'Library', ['-name: String', '-address: String'], ['+addBook()', '+registerMember()'])
    bk = f.uclass(4, 4, 104, 'Book', ['-ISBN: String {unique}', '-title: String', '-author: String', '-isAvailable: Boolean'], ['+checkOut()', '+returnBook()'])
    ln = f.uclass(190, 4, 86, 'Loan', ['-loanDate: Date', '-dueDate: Date'], ['+calculateFine()'])
    mb = f.uclass(190, 108, 96, 'Member', ['-memberID: String', '-name: String', '-email: String'], ['+borrowBook()', '+returnBook()', '+getMaxBooks(): int'])
    lb = f.uclass(4, 190, 86, 'Librarian', ['-staffID: String'], ['+issueLoan()'])
    fa = f.uclass(320, 100, 96, 'Faculty', [], ['+getMaxBooks(): int'])
    st = f.uclass(320, 172, 96, 'Student', [], ['+getMaxBooks(): int'])
    # composition Library<>--Book
    f.arrow([(40, 83), (40, 96)], kind='fdiamond', size=4.5)
    f.text(48, 88, '1..*', anchor='start', size=6.2); f.text(48, 93 - 8 + 16, '', size=1)
    f.text(33, 90, '1', anchor='end', size=6.2)
    # composition Library<>--Loan
    f.arrow([(190, 30), (130, 30), (130, 110), (90, 110)], kind='fdiamond', size=4.5)
    f.text(186, 25, '*', anchor='end', size=6.2); f.text(96, 105, '1', anchor='start', size=6.2)
    # aggregation Library<>--Member
    f.arrow([(190, 136), (90, 136)], kind='diamond', size=4.5)
    f.text(186, 131, '*', anchor='end', size=6.2); f.text(96, 131, '1', anchor='start', size=6.2)
    # aggregation Library<>--Librarian
    f.arrow([(40, 190), (40, 158)], kind='diamond', size=4.5)
    f.text(46, 185, '1..*', anchor='start', size=6.2)
    # associations Loan--Book, Loan--Member
    f.line(108, 22, 190, 22); f.text(114, 17, '1', anchor='start', size=6.2); f.text(186, 17, '0..*', anchor='end', size=6.2)
    f.line(233, 62, 233, 108); f.text(237, 68, '0..*', anchor='start', size=6.2); f.text(237, 104, '1', anchor='start', size=6.2)
    # generalization
    f.arrow([(320, 118), (286, 130)], kind='tri', size=5)
    f.arrow([(320, 190), (300, 190), (300, 158), (286, 150)], kind='tri', size=5)
    return f.svg()


@fig('fd-class', 'Class diagram of a food-delivery system showing multiplicities', wide=True)
def _():
    f = Fig(420, 170, fs=6.8)
    cu = f.uclass(4, 60, 76, 'Customer', ['name', 'address'])
    od = f.uclass(150, 60, 86, 'Order', ['orderId', 'status', 'total'])
    it = f.uclass(150, 128, 86, 'OrderItem', ['quantity', 'price'])
    rs = f.uclass(150, 2, 86, 'Restaurant', ['name', 'location'])
    mi = f.uclass(326, 2, 90, 'MenuItem', ['name', 'price'])
    py = f.uclass(326, 60, 90, 'Payment', ['amount', 'status'])
    dp = f.uclass(326, 118, 90, 'DeliveryPartner', ['name', 'location'])
    def assoc(p1, p2, m1, m2, o1=(3, -4), o2=(-3, -4)):
        f.line(*p1, *p2)
        f.text(p1[0] + o1[0], p1[1] + o1[1], m1, anchor='start' if o1[0] >= 0 else 'end', size=6.4)
        f.text(p2[0] + o2[0], p2[1] + o2[1], m2, anchor='end' if o2[0] <= 0 else 'start', size=6.4)
    assoc((80, 80), (150, 80), '1', '0..*')
    assoc((236, 80), (326, 80), '1', '1')
    assoc((193, 42), (193, 60), '1', '0..*', (4, 5), (-4, -2))
    assoc((236, 22), (326, 22), '1', '1..*')
    assoc((236, 96), (326, 136), '0..*', '0..1', (3, -3), (-3, -4))
    f.arrow([(193, 128), (193, 99)], kind='fdiamond', size=4.5)
    f.text(197, 123, '1..*', anchor='start', size=6.4)
    f.line(236, 145, 300, 145); f.line(300, 145, 300, 36); f.line(300, 36, 326, 36)
    f.text(240, 141, '0..*', anchor='start', size=6.4); f.text(322, 32, '1', anchor='end', size=6.4)
    return f.svg()


FIGS['fd-crc'] = ('Principal classes of a food-delivery system and their collaborators', table_html(
    ['Class', 'Responsibilities', 'Collaborators'],
    [['Order Processing System', 'Create orders, compute totals, track order status', 'Customer, Restaurant, Payment Gateway, Delivery Partner Allocator'],
     ['Restaurant Manager', 'Accept or reject orders, update menu and preparation time', 'Menu, Order, Delivery Partner Allocator'],
     ['Payment Gateway (interface)', 'Request authorization and report payment status', 'Order, Customer, Bank Server'],
     ['Delivery Partner Allocator', 'Choose the nearest free partner and assign the order', 'Delivery Partner, Order, Location Service'],
     ['Real-Time Tracker', 'Receive GPS updates and compute the estimated arrival time', 'GPS Service, Order, Delivery Partner'],
     ['Notification Service', 'Send status messages to customers and restaurants', 'Order, Customer, Restaurant']],
    ['26%', '38%', '36%']), {'wide': True})


# ------------------------------------------------------------------ component & deployment
def component(f, x, y, w, h, name):
    f.rect(x, y, w, h, stroke=CYAN, fill='white')
    f.rect(x - 4, y + 4, 9, 5, stroke=CYAN, fill='white', sw=0.8)
    f.rect(x - 4, y + 12, 9, 5, stroke=CYAN, fill='white', sw=0.8)
    f.text(x + w / 2 + 3, y + h / 2, name, size=6.8)
    return (x, y, w, h)


def lollipop(f, x1, y1, x2, y2, name, anch='middle', dx=0, dy=-8):
    f.line(x1, y1, x2, y2, w=0.6)
    f.circle(x2, y2, 4, stroke=DARK, sw=0.7)
    f.text(x2 + dx, y2 + dy, name, size=6.2, anchor=anch)


@fig('lib-component', 'Component diagram of a library system', wide=True, scale=0.88)
def _():
    f = Fig(420, 190)
    ui = component(f, 10, 80, 66, 26, 'Web UI')
    mm = component(f, 150, 10, 88, 26, 'Member mgmt')
    bc = component(f, 150, 80, 88, 26, 'Book catalog')
    lp = component(f, 150, 150, 88, 26, 'Loan processor')
    au = component(f, 300, 150, 90, 26, 'Authentication')
    ps = component(f, 300, 80, 90, 26, 'Persistence')
    lollipop(f, 238, 23, 268, 23, 'MemberService', 'start', dx=8, dy=0)
    lollipop(f, 238, 93, 262, 93, '', 'start')
    f.text(250, 86, 'BookSearch', size=6.2)
    lollipop(f, 238, 170, 262, 170, '', 'start')
    f.text(252, 184, 'LoanService', size=6.2)
    lollipop(f, 345, 150, 345, 132, 'AuthService', dx=22, dy=0)
    lollipop(f, 390, 93, 410, 93, '', 'start'); f.text(404, 108, 'DBAccess', size=6.2)
    for tx, ty in [(150, 23), (150, 93), (150, 163)]:
        f.arrow([(76, 93), (tx, ty)], kind='open', dash='3,2', size=4)
    f.arrow([(238, 157), (300, 100)], kind='open', dash='3,2', size=4)
    f.arrow([(238, 30), (300, 86)], kind='open', dash='3,2', size=4)
    f.arrow([(194, 150), (194, 106)], kind='open', dash='3,2', size=4)
    f.arrow([(76, 100), (300, 162)], kind='open', dash='3,2', size=4)
    return f.svg()


def node(f, x, y, w, h, name):
    d = 7
    f.poly([(x, y), (x + d, y - d), (x + w + d, y - d), (x + w + d, y + h - d), (x + w, y + h)], color=CYAN, w=0.9, fill='white')
    f.line(x + w, y, x + w + d, y - d, color=CYAN, w=0.9)
    f.rect(x, y, w, h, stroke=CYAN, fill='white')
    f.text(x + w / 2, y + 9, name, size=6.8, weight=500)
    return (x, y, w, h)


@fig('lib-deploy', 'Deployment diagram of a library system')
def _():
    f = Fig(336, 190)
    ws = node(f, 196, 12, 120, 44, '«device» WebServer')
    component(f, 222, 28, 70, 20, 'UI')
    cs = node(f, 8, 20, 96, 30, '«device» ConfigServer')
    db = node(f, 8, 122, 118, 54, '«device» DatabaseServer')
    component(f, 32, 146, 72, 20, 'Schema')
    ap = node(f, 176, 92, 148, 90, '«executionEnvironment»\nAppServer (JVM)')
    component(f, 198, 118, 110, 16, 'Member management')
    component(f, 198, 140, 110, 16, 'Book catalog')
    component(f, 198, 162, 110, 16, 'Loan processor')
    f.line(104, 34, 196, 34, w=0.6); f.text(150, 29, 'HTTPS', size=6.2)
    f.line(256, 56, 256, 92, w=0.6); f.text(262, 74, 'HTTPS', size=6.2, anchor='start')
    f.line(126, 150, 176, 150, w=0.6); f.text(151, 145, 'JDBC', size=6.2)
    f.line(60, 50, 60, 122, w=0.6); f.line(104, 44, 176, 110, w=0.6)
    f.text(140, 72, 'config API', size=6.2)
    return f.svg()


# ------------------------------------------------------------------ activity & state
@fig('lib-activity', 'Activity diagram with swimlanes for borrowing a book', wide=True, scale=0.85)
def _():
    f = Fig(420, 270, fs=6.8)
    lanes = [('Student member', 4), ('Library system', 144), ('Librarian', 284)]
    for n, x in lanes:
        f.rect(x, 4, 136, 262, stroke=GREY, sw=0.6, fill='none')
        f.rect(x, 4, 136, 14, stroke=GREY, sw=0.6, fill='#EAF7FD')
        f.text(x + 68, 11, n, weight=500)
    f.start(72, 32)
    a1 = f.rbox(34, 46, 76, 18, 'Search book', shadow=False)
    f.arrow([(72, 37), (72, 46)])
    f.diamond(212, 80)
    f.arrow([(110, 55), (212, 55), (212, 74)])
    a2 = f.rbox(160, 98, 104, 18, 'Reserve book', shadow=False)
    f.arrow([(212, 86), (212, 98)]); f.text(216, 92, '[available]', anchor='start', size=6.2)
    a3 = f.rbox(20, 98, 104, 18, 'Display “unavailable”', shadow=False)
    f.arrow([(206, 80), (72, 80), (72, 98)]); f.text(150, 76, '[not available]', size=6.2)
    a4 = f.rbox(160, 128, 104, 18, 'Confirm borrowing', shadow=False)
    f.arrow([(212, 116), (212, 128)])
    f.bar(150, 154, 124, 3)
    f.arrow([(212, 146), (212, 154)])
    b1 = f.rbox(20, 172, 104, 18, 'Update book status', shadow=False)
    b2 = f.rbox(160, 172, 104, 18, 'Update member profile', shadow=False)
    b3 = f.rbox(292, 166, 120, 30, 'Create notifications for\nlibrarian and member', shadow=False)
    f.arrow([(160, 157), (72, 164), (72, 172)]); f.arrow([(212, 157), (212, 172)]); f.arrow([(264, 157), (352, 160), (352, 166)])
    f.bar(150, 208, 124, 3)
    f.arrow([(72, 190), (72, 200), (160, 207)]); f.arrow([(212, 190), (212, 208)]); f.arrow([(352, 196), (352, 202), (264, 207)])
    c = f.rbox(160, 222, 104, 18, 'Issue book', shadow=False)
    f.arrow([(212, 211), (212, 222)])
    f.end(212, 254)
    f.arrow([(212, 240), (212, 248)])
    f.arrow([(20, 107), (12, 107), (12, 258), (206, 256)])
    return f.svg()


@fig('lib-state', 'State machine diagram for a book in a library')
def _():
    f = Fig(336, 210, fs=6.8)
    f.start(22, 50)
    av = f.rbox(10, 70, 76, 22, 'Available', shadow=False)
    rs = f.rbox(128, 8, 84, 22, 'Reserved', shadow=False)
    lo = f.rbox(236, 70, 84, 22, 'On loan', shadow=False)
    ov = f.rbox(236, 152, 84, 22, 'Overdue', shadow=False)
    wd = f.rbox(10, 152, 76, 22, 'Withdrawn', shadow=False)
    f.arrow([(22, 55), (22, 70)])
    f.arrow([(70, 70), (128, 22)]); f.text(80, 36, 'reserve\n[member eligible]', size=6.2, anchor='end')
    f.arrow([(140, 30), (84, 72)]); f.text(118, 56, 'cancel /\nexpire', size=6.2, anchor='start')
    f.arrow([(200, 30), (256, 70)]); f.text(240, 36, 'issue /\ncreateLoan', size=6.2, anchor='start')
    f.arrow([(86, 76), (236, 76)]); f.text(160, 71, 'issue / createLoan', size=6.2)
    f.arrow([(236, 87), (86, 87)]); f.text(160, 95, 'return / updateStatus', size=6.2)
    f.arrow([(278, 92), (278, 152)]); f.text(282, 122, 'due date passed', size=6.2, anchor='start')
    f.arrow([(236, 158), (76, 92)]); f.text(170, 142, 'return / generateFine', size=6.2)
    f.arrow([(48, 92), (48, 152)]); f.text(44, 122, 'withdraw\n[damaged]', size=6.2, anchor='end')
    f.end(48, 196)
    f.arrow([(48, 174), (48, 189)])
    return f.svg()


# ------------------------------------------------------------------ antivirus requirements model
@fig('av-usecase', 'Scenario-based element: use cases of the antivirus product')
def _():
    f = Fig(336, 172)
    f.rect(70, 4, 196, 164, stroke=GREY, sw=0.6)
    f.text(168, 13, 'Antivirus product', size=7, weight=500)
    f.actor(26, 60, 'User')
    f.actor(310, 96, 'Update\nserver')
    ucs = [('Run scan', 30), ('Configure real-time\nprotection', 60), ('Quarantine or remove\nmalware', 94), ('View threat report', 126), ('Update definitions', 154)]
    for t, y in ucs:
        f.usecase(150, y, t, rx=54, ry=13)
    for t, y in ucs[:4]:
        f.line(36, 76, 96, y, w=0.5)
    f.line(300, 108, 204, 154, w=0.5)
    f.arrow([(204, 94), (226, 94), (226, 30), (204, 30)], kind='open', dash='3,2', size=4)
    f.text(246, 62, '«extend»\n[threat\nfound]', size=6)
    return f.svg()


@fig('av-class', 'Class-based element: principal classes of the antivirus product', wide=True)
def _():
    f = Fig(420, 132, fs=6.6)
    sc = f.uclass(4, 4, 92, 'ScanEngine', ['mode', 'lastScan'], ['scan(target)', 'monitor()'])
    q = f.uclass(4, 78, 92, 'Quarantine', ['items'], ['isolate(file)', 'restore(file)'])
    de = f.uclass(160, 4, 110, '«interface»\nDetector', [], ['inspect(file): Verdict'])
    sig = f.uclass(130, 84, 90, 'SignatureDetector', [], [])
    heu = f.uclass(226, 84, 90, 'HeuristicDetector', [], [])
    ml = f.uclass(322, 84, 94, 'MLDetector', ['model'], [])
    f.line(96, 24, 160, 24); f.text(100, 19, '1', anchor='start', size=6.2); f.text(156, 19, '1..*', anchor='end', size=6.2)
    for x in (175, 271, 369):
        f.poly([(x, 84), (x, 70), (215, 70)], dash='3,2')
    f.poly([(175, 70), (369, 70)], dash='3,2')
    f.arrow([(215, 70), (215, 46)], kind='tri', size=4, dash='3,2')
    f.arrow([(50, 56), (50, 78)], kind='open', dash='3,2', size=4)
    f.text(54, 67, '«uses»', size=6.2, anchor='start')
    return f.svg()


@fig('av-state', 'Behavioral element: state diagram of the real-time protection engine', wide=True)
def _():
    f = Fig(420, 132, fs=6.8)
    f.start(14, 40)
    idle = f.rbox(34, 30, 70, 20, 'Monitoring', shadow=False)
    scan = f.rbox(150, 30, 80, 20, 'Scanning', shadow=False)
    thr = f.rbox(290, 30, 96, 20, 'Threat detected', shadow=False)
    qu = f.rbox(290, 96, 96, 20, 'Quarantining', shadow=False)
    up = f.rbox(34, 96, 70, 20, 'Updating', shadow=False)
    f.arrow([(19, 40), (34, 40)])
    f.arrow([(104, 36), (150, 36)]); f.text(127, 29, 'file/web event', size=6.2)
    f.arrow([(150, 46), (104, 46)]); f.text(127, 56, '[clean]', size=6.2)
    f.arrow([(230, 40), (290, 40)]); f.text(260, 33, '[malicious]', size=6.2)
    f.arrow([(338, 50), (338, 96)]); f.text(342, 74, 'remove / notify user', size=6.2, anchor='start')
    f.arrow([(290, 106), (120, 106), (90, 50)]); f.text(200, 115, 'done / log event', size=6.2)
    f.arrow([(60, 50), (60, 96)]); f.text(56, 74, 'daily update\ndue', size=6.2, anchor='end')
    f.arrow([(80, 96), (80, 50)]); f.text(84, 74, 'installed', size=6.2, anchor='start')
    return f.svg()


@fig('av-dfd', 'Flow-oriented element: level-1 DFD for scanning a file')
def _():
    f = Fig(336, 120)
    ext(f, 4, 44, 52, 24, 'User')
    proc(f, 100, 56, 22, '1.0', 'Intercept\nfile')
    proc(f, 190, 56, 22, '2.0', 'Analyse\nfile')
    proc(f, 280, 56, 22, '3.0', 'Take\naction')
    store(f, 150, 4, 80, 'D1', 'Signatures')
    store(f, 240, 102, 88, 'D2', 'Quarantine')
    f.arrow([(56, 56), (78, 56)]); f.text(66, 49, 'file', size=6.2)
    f.arrow([(122, 56), (168, 56)]); f.text(145, 49, 'file data', size=6.2)
    f.arrow([(212, 56), (258, 56)]); f.text(235, 49, 'verdict', size=6.2)
    f.arrow([(190, 17), (190, 34)]); f.text(194, 26, 'signatures, model', size=6.2, anchor='start')
    f.arrow([(280, 78), (280, 102)]); f.text(284, 92, 'infected file', size=6.2, anchor='start')
    f.arrow([(270, 78), (270, 92), (30, 92), (30, 68)]); f.text(150, 99, 'alert, report', size=6.2)
    return f.svg()


# ------------------------------------------------------------------ additional past-paper models
@fig('ticket-usecase', 'Use cases of a ticket reservation system')
def _():
    f = Fig(336, 200, fs=6.8)
    f.rect(64, 4, 230, 192, stroke=GREY, sw=0.6)
    f.text(179, 13, 'Ticket reservation system', size=7, weight=500)
    f.actor(24, 70, 'Passenger')
    f.actor(318, 104, 'Payment\ngateway')
    f.actor(318, 150, 'Admin')
    u = {}
    u['search'] = f.usecase(120, 32, 'Search seats', rx=40)
    u['book'] = f.usecase(120, 76, 'Book ticket', rx=40)
    u['cancel'] = f.usecase(120, 120, 'Cancel ticket', rx=40)
    u['view'] = f.usecase(120, 162, 'View booking', rx=40)
    u['fare'] = f.usecase(222, 34, 'Calculate fare', rx=40)
    u['pay'] = f.usecase(222, 124, 'Make payment', rx=40)
    u['conc'] = f.usecase(222, 80, 'Apply concession /\npeak pricing', rx=44, ry=14)
    u['fares'] = f.usecase(222, 180, 'Manage fares', rx=38, ry=11)
    for k in ('search', 'book', 'cancel', 'view'):
        cx, cy, rx, ry = u[k]
        f.line(34, 84, cx - rx, cy, w=0.5)
    f.line(308, 118, 262, 124, w=0.5); f.line(308, 164, 260, 178, w=0.5)
    f.arrow([(152, 68), (190, 40)], kind='open', dash='3,2', size=4); f.text(160, 46, '«include»', size=5.8)
    f.arrow([(150, 86), (190, 118)], kind='open', dash='3,2', size=4); f.text(158, 110, '«include»', size=5.8)
    f.arrow([(240, 66), (240, 46)], kind='open', dash='3,2', size=4); f.text(244, 52, '«extend»', size=5.2, anchor='start'); f.text(244, 60, '[child, senior, peak]', size=5.2, anchor='start')
    return f.svg()


@fig('ticket-seq', 'Sequence diagram for booking a ticket', wide=True, scale=0.8)
def _():
    f = Fig(420, 290)
    s = Seq(f, ['Passenger', ':BookingUI', ':Reservation', ':SeatInventory', ':FareCalc', ':PayGateway'], 24, 74, 14, 286, actors=('Passenger',))
    s.act('Passenger', 46, 280)
    s.act(':BookingUI', 50, 276)
    s.msg('Passenger', ':BookingUI', 54, '1: search(route, date)')
    s.act(':Reservation', 66, 270)
    s.msg(':BookingUI', ':Reservation', 70, '2: findSeats(route, date)')
    s.msg(':Reservation', ':SeatInventory', 86, '3: checkAvailability()')
    s.msg(':SeatInventory', ':Reservation', 100, '4: free seats', ret=True)
    s.msg(':Reservation', ':BookingUI', 114, '5: seat map', ret=True)
    s.msg('Passenger', ':BookingUI', 130, '6: select seat, enter details')
    s.msg(':BookingUI', ':Reservation', 146, '7: book(seat, passenger)')
    s.msg(':Reservation', ':SeatInventory', 160, '8: holdSeat(seat)')
    s.msg(':Reservation', ':FareCalc', 176, '9: fare(distance, type, time)')
    s.act(':FareCalc', 180, 208)
    f.rect(296, 184, 110, 20, stroke=GREY, sw=0.5, fill='none'); f.text(299, 190, 'opt [peak hour]', size=5.4, anchor='start', weight=500)
    s.self_msg(':FareCalc', 194, 'addPeakRate()')
    s.msg(':FareCalc', ':Reservation', 214, '10: fare', ret=True)
    s.msg(':Reservation', ':PayGateway', 230, '11: pay(fare)')
    s.msg(':PayGateway', ':Reservation', 244, '12: payment status', ret=True)
    s.msg(':Reservation', ':SeatInventory', 258, '13: confirmSeat(seat)')
    s.msg(':Reservation', ':BookingUI', 270, '14: ticket', ret=True)
    s.msg(':BookingUI', 'Passenger', 282, '15: show ticket', ret=True)
    return f.svg()


@fig('uni-class', 'Class diagram of a university account system', wide=True, scale=0.9)
def _():
    f = Fig(420, 200, fs=6.6)
    ua = f.uclass(4, 4, 104, 'UniversityAccount', ['-accountId: String', '-studentName: String'], [])
    la = f.uclass(4, 86, 104, 'LinkAccount', ['-email: String {readOnly}', '-password: String'], ['+resetPassword()'])
    bb = f.uclass(158, 4, 104, 'Blackboard', [], ['+addCourse()', '+downloadHomework()', '+uploadHomework()'])
    zm = f.uclass(158, 118, 104, 'Zoom', [], ['+createMeeting()', '+deleteMeeting()'])
    co = f.uclass(310, 4, 106, 'Course', ['-courseId: String', '-courseName: String'], [])
    hw = f.uclass(310, 70, 106, 'Homework', ['-courseId: String', '-homeworkNo: int', '-questions: List'], [])
    me = f.uclass(310, 140, 106, 'Meeting', ['-meetingId: String', '-invitationLink: URL'], ['+join(id, password)'])
    f.arrow([(56, 86), (56, 49)], kind='fdiamond', size=4.5)
    f.text(60, 81, '1', anchor='start', size=6); f.text(60, 60, '1', anchor='start', size=6)
    f.arrow([(108, 104), (158, 30)], kind='open', dash='3,2', size=4); f.text(128, 58, 'uses', size=6)
    f.arrow([(108, 118), (158, 140)], kind='open', dash='3,2', size=4); f.text(124, 138, 'uses', size=6)
    f.arrow([(310, 22), (262, 22)], kind='fdiamond', size=4.5); f.text(306, 17, '*', anchor='end', size=6)
    f.arrow([(310, 158), (262, 140)], kind='fdiamond', size=4.5); f.text(304, 152, '*', anchor='end', size=6)
    f.line(363, 40, 363, 70); f.text(367, 45, '1', anchor='start', size=6); f.text(367, 66, '1..*', anchor='start', size=6)
    f.line(404, 40, 412, 40); f.line(412, 40, 412, 140); f.text(408, 46, '1', anchor='end', size=6); f.text(408, 136, '1..*', anchor='end', size=6)
    return f.svg()


@fig('zoom-seq', 'Sequence diagram for joining an online lecture')
def _():
    f = Fig(336, 214)
    s = Seq(f, ['Student', ':ZoomApp', ':UniAccount', ':ZoomServer'], 20, 94, 14, 210, actors=('Student',))
    s.act('Student', 46, 204)
    s.msg('Student', ':ZoomApp', 52, '1: join(meetingId)')
    s.act(':ZoomApp', 48, 200)
    s.msg(':ZoomApp', ':UniAccount', 68, '2: authenticate(email, pwd)')
    s.act(':UniAccount', 64, 86)
    s.msg(':UniAccount', ':ZoomApp', 82, '3: token', ret=True)
    s.msg(':ZoomApp', ':ZoomServer', 98, '4: joinMeeting(id, pwd, token)')
    s.act(':ZoomServer', 94, 190)
    f.rect(114, 128, 218, 70, stroke=GREY, sw=0.6); f.rect(114, 128, 20, 10, stroke=GREY, sw=0.6); f.text(124, 133, 'alt', size=6, weight=500)
    f.text(144, 146, '[valid]', size=6, anchor='start')
    s.msg(':ZoomServer', ':ZoomApp', 156, '5: admit, stream', ret=True)
    f.line(114, 166, 332, 166, dash='4,2', color=GREY)
    f.text(144, 176, '[invalid]', size=6, anchor='start')
    s.msg(':ZoomServer', ':ZoomApp', 188, '6: error message', ret=True)
    s.msg(':ZoomApp', 'Student', 200, '7: lecture or error', ret=True)
    return f.svg()


def entity(f, x, y, w, name, attrs):
    return f.uclass(x, y, w, name, attrs, [])


@fig('rec-er', 'Entity–relationship diagram of an academic record system', wide=True)
def _():
    f = Fig(420, 112, fs=6.4)
    st = entity(f, 4, 4, 92, 'Student', ['RollNo (PK)', 'Name', 'Address', 'Semester'])
    en = entity(f, 150, 4, 110, 'Enrollment', ['RollNo (FK)', 'CourseNo (FK)', 'Semester', 'Marks'])
    co = entity(f, 316, 4, 100, 'Course', ['CourseNo (PK)', 'Credits', 'Syllabus'])
    tr = entity(f, 150, 64 - 0, 110, 'Transcript', ['RollNo, Semester (PK)', 'SWA'])
    f.line(96, 30, 150, 30); f.text(100, 25, '1', anchor='start', size=6); f.text(146, 25, 'N', anchor='end', size=6)
    f.line(260, 30, 316, 30); f.text(264, 25, 'N', anchor='start', size=6); f.text(312, 25, '1', anchor='end', size=6)
    f.poly([(50, 62), (50, 78), (150, 78)]); f.text(54, 72, '1', anchor='start', size=6); f.text(146, 73, 'N', anchor='end', size=6)
    return f.svg()


@fig('rec-context', 'Context diagram of the academic record system')
def _():
    f = Fig(336, 150, fs=6.4)
    cx, cy, r = 168, 74, 32
    f.circle(cx, cy, r, shadow=True); f.text(cx, cy - 8, '0.0', weight=500); f.text(cx, cy + 6, 'Academic\nrecord system', size=6.4)
    ext(f, 4, 10, 70, 24, 'Registrar', size=6.6)
    ext(f, 4, 116, 70, 24, 'Faculty', size=6.6)
    ext(f, 262, 10, 70, 24, 'Student', size=6.6)
    ext(f, 262, 116, 70, 24, 'Academic\noffice', size=6.4)
    f.arrow([(74, 20), (cx - r + 6, cy - 20)], size=4); lab(f, 100, 16, 'course details,\nadmission details', size=5.8)
    f.arrow([(74, 128), (cx - r + 6, cy + 20)], size=4); lab(f, 100, 118, 'marks', size=5.8)
    f.arrow([(cx + r - 6, cy - 20), (262, 22)], size=4); lab(f, 236, 38, 'grade report\nwith SWA', size=5.8)
    f.arrow([(cx + r - 6, cy + 20), (262, 128)], size=4); lab(f, 232, 118, "VC's list,\nconditional\nstanding list", size=5.8)
    return f.svg()


@fig('rec-l1', 'Level-1 DFD of the academic record system', wide=True, scale=0.9)
def _():
    f = Fig(420, 196, fs=6.2)
    r = 21
    P = {'1': (96, 30), '2': (96, 98), '3': (96, 166), '4': (236, 132), '5': (340, 78), '6': (348, 166)}
    proc(f, *P['1'], r, '1.0', 'Maintain\ncourses', size=6)
    proc(f, *P['2'], r, '2.0', 'Admit and\nregister', size=6)
    proc(f, *P['3'], r, '3.0', 'Record\nmarks', size=6)
    proc(f, *P['4'], r, '4.0', 'Compute\nSWA', size=6)
    proc(f, *P['5'], r, '5.0', 'Print grade\nreport', size=6)
    proc(f, *P['6'], r, '6.0', 'Determine\nstanding', size=6)
    store(f, 170, 16, 84, 'D1', 'Courses', size=6)
    store(f, 170, 80, 84, 'D2', 'Students', size=6)
    store(f, 150, 176, 84, 'D3', 'Enrollments', size=6)
    store(f, 290, 118, 84, 'D4', 'Transcripts', size=6)
    ext(f, 2, 50, 50, 20, 'Registrar', size=6)
    ext(f, 2, 156, 50, 20, 'Faculty', size=6)
    ext(f, 370, 14, 48, 20, 'Student', size=6)
    ext(f, 388, 106 + 80, 30, 0.01, '', size=1) if False else None
    ext(f, 370, 180, 48, 16, 'Acad. office', size=5.6)
    f.arrow([(40, 50), (78, 38)], size=3.5); lab(f, 40, 36, 'course\ndetails', size=5.4)
    f.arrow([(40, 70), (76, 92)], size=3.5); lab(f, 36, 86, 'admission\ndetails', size=5.4)
    f.arrow([(52, 166), (75, 166)], size=3.5); lab(f, 62, 160, 'marks', size=5.4)
    f.arrow([(117, 30), (170, 22)], size=3.5)
    f.arrow([(117, 98), (170, 86)], size=3.5)
    f.arrow([(110, 114), (160, 176)], size=3.5)
    f.arrow([(117, 170), (150, 180)], size=3.5)
    f.arrow([(200, 189), (225, 148)], size=3.5); lab(f, 222, 172, 'marks', size=5.4, anchor='start')
    f.arrow([(212, 29), (232, 111)], size=3.5); lab(f, 226, 60, 'credits', size=5.4, anchor='start')
    f.arrow([(257, 128), (290, 125)], size=3.5)
    f.arrow([(332, 118), (338, 99)], size=3.5)
    f.arrow([(340, 131), (346, 145)], size=3.5); lab(f, 356, 138, 'SWA', size=5.4, anchor='start')
    f.arrow([(352, 57), (380, 34)], size=3.5); lab(f, 380, 48, 'grade\nreport', size=5.4, anchor='start')
    f.arrow([(368, 176), (380, 182)], size=3.5)
    return f.svg()


@fig('bank-usecase', 'Use cases of an online banking system', scale=0.88)
def _():
    f = Fig(336, 232, fs=6.6)
    f.rect(64, 4, 230, 224, stroke=GREY, sw=0.6)
    f.text(179, 13, 'Online banking system', size=7, weight=500)
    f.actor(24, 84, 'Customer')
    f.actor(318, 70, 'Payment\ngateway')
    f.actor(318, 172, 'Admin')
    u = {}
    for i, (k, t) in enumerate([('reg', 'Register'), ('login', 'Log in'), ('bal', 'View balance'), ('xfer', 'Transfer funds'),
                                ('bill', 'Pay utility bill'), ('hist', 'View transaction\nhistory')]):
        u[k] = f.usecase(116, 32 + i * 34, t, rx=38, ry=12 if k != 'hist' else 14)
    u['otp'] = f.usecase(232, 34, 'Verify OTP', rx=34, ry=11)
    u['proc'] = f.usecase(232, 82, 'Process bill\npayment', rx=36, ry=14)
    u['appr'] = f.usecase(232, 138, 'Approve\nregistration', rx=36, ry=14)
    u['acct'] = f.usecase(232, 176, 'Manage accounts', rx=38, ry=11)
    u['rep'] = f.usecase(232, 208, 'Generate reports', rx=38, ry=11)
    for k in ('reg', 'login', 'bal', 'xfer', 'bill', 'hist'):
        cx, cy, rx, ry = u[k]
        f.line(34, 98, cx - rx, cy, w=0.5)
    f.line(308, 84, 268, 84, w=0.5)
    for k in ('appr', 'acct', 'rep'):
        cx, cy, rx, ry = u[k]
        f.line(308, 186, cx + rx, cy, w=0.5)
    f.arrow([(148, 126), (206, 42)], kind='open', dash='3,2', size=4); f.text(160, 76, '«include»', size=5.6, anchor='start')
    f.arrow([(152, 162), (200, 90)], kind='open', dash='3,2', size=4); f.text(160, 134, '«include»', size=5.6, anchor='start')
    return f.svg()
