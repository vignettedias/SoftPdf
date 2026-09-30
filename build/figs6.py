from svg import Fig, anchor, CYAN, DARK, GREY, FILL
from figs5 import proc, ext, store, Seq
from figs4 import table_html

FIGS = {}


def fig(fid, caption, **opts):
    def deco(fn):
        FIGS[fid] = (caption, fn, opts)
        return fn
    return deco


def clip(fid, caption, page, rect, **opts):
    FIGS[fid] = (caption, ('clip', page, rect), opts)


def tree(f, root, kids, y0, y1, bw, bh, size=6.8, gap=None, shadow=True, x0=None, width=None):
    """Draw root box (x,y,w,h,label) and a row of children centred under it."""
    rx, ry, rw, rh, rl = root
    rb = f.box(rx, ry, rw, rh, rl, weight=500, size=size, shadow=shadow)
    n = len(kids)
    gap = gap if gap is not None else 8
    total = n * bw + (n - 1) * gap
    xs = (x0 if x0 is not None else rx + rw / 2 - total / 2)
    mid = (y0 + ry + rh) / 2 if False else ry + rh + (y1 - ry - rh) / 2
    boxes = []
    f.line(rx + rw / 2, ry + rh, rx + rw / 2, mid)
    f.line(xs + bw / 2, mid, xs + (n - 1) * (bw + gap) + bw / 2, mid)
    for i, k in enumerate(kids):
        x = xs + i * (bw + gap)
        f.line(x + bw / 2, mid, x + bw / 2, y1)
        boxes.append(f.box(x, y1, bw, bh, k, size=size, shadow=shadow))
    return rb, boxes


@fig('lms-structural', 'Structural model of a library management system')
def _():
    f = Fig(336, 150)
    rb, subs = tree(f, (118, 4, 100, 22, 'Library management\nsystem'), ['User\nmanagement', 'Book\ninventory', 'Transaction\nmanagement'], 0, 50, 90, 24, gap=18)
    items = [['Register user', 'Login user', 'Update profile'], ['Add book', 'Remove book', 'Check\navailability'], ['Borrow book', 'Return book']]
    for (x, y, w, h), its in zip(subs, items):
        for j, t in enumerate(its):
            yy = 86 + j * 21
            f.box(x + 12, yy, w - 12, 17, t, size=6.2, shadow=False)
            f.line(x + 5, y + h, x + 5, yy + 8.5); f.line(x + 5, yy + 8.5, x + 12, yy + 8.5)
    return f.svg()


@fig('lms-dynamic', 'Dynamic model: borrowing a book')
def _():
    f = Fig(336, 128)
    s = Seq(f, ['User', ':System', ':BookInventory', ':TransactionMgmt'], 20, 92, 12, 124, actors=('User',))
    s.msg('User', ':System', 50, '1: login, borrow request')
    s.msg(':System', ':BookInventory', 66, '2: checkAvailability()')
    s.msg(':BookInventory', ':System', 80, '3: book available', ret=True)
    s.msg(':System', ':TransactionMgmt', 94, '4: recordBorrowing()')
    s.msg(':TransactionMgmt', ':System', 106, '5: transaction recorded', ret=True)
    s.msg(':System', 'User', 118, '6: confirm borrowing', ret=True)
    return f.svg()


@fig('lms-hierarchy', 'Control hierarchy of the library management system', wide=True)
def _():
    f = Fig(420, 120, fs=6.6)
    root = f.box(170, 4, 80, 20, 'Main application', weight=500)
    mids = [('User mgmt', 60), ('Book inventory', 210), ('Transaction mgmt', 344)]
    kids = [['Register', 'Login', 'Update\nprofile'], ['Add book', 'Remove\nbook', 'Check\navail.'], ['Borrow\nbook', 'Return\nbook']]
    f.line(210, 24, 210, 36); f.line(60, 36, 344, 36)
    for (t, cx), ks in zip(mids, kids):
        f.line(cx, 36, cx, 44)
        f.box(cx - 40, 44, 80, 20, t, weight=500)
        n = len(ks); w = 38; g = 6
        x0 = cx - (n * w + (n - 1) * g) / 2
        f.line(cx, 64, cx, 74); f.line(x0 + w / 2, 74, x0 + (n - 1) * (w + g) + w / 2, 74)
        for i, k in enumerate(ks):
            x = x0 + i * (w + g)
            f.line(x + w / 2, 74, x + w / 2, 82)
            f.box(x, 82, w, 24, k, shadow=False, size=6.2)
    for y, t in [(14, 'Level 1'), (54, 'Level 2'), (94, 'Level 3')]:
        f.text(416, y, t, anchor='end', size=6.4, italic=True)
    return f.svg()


@fig('fan-chart', 'A structure chart with a shared module')
def _():
    f = Fig(250, 110)
    pos = {'A': (125, 14), 'B': (55, 54), 'C': (125, 54), 'D': (195, 54), 'E': (35, 94), 'F': (105, 94), 'G': (175, 94)}
    for k, (x, y) in pos.items():
        f.box(x - 18, y - 9, 36, 18, k, weight=500, shadow=False)
    for a, b in ['AB', 'AC', 'AD', 'BE', 'BF', 'CF', 'CG', 'DG']:
        xa, ya = pos[a]; xb, yb = pos[b]
        f.arrow([(xa, ya + 9), (xb, yb - 9)], size=4)
    return f.svg()


@fig('lms-horizontal', 'Horizontal partitioning of the library system into layers')
def _():
    f = Fig(336, 116)
    f.box(4, 4, 328, 30, '', shadow=True)
    f.text(10, 12, 'Presentation layer (input and output)', anchor='start', weight=500)
    f.text(10, 25, 'Web interface (HTML/CSS/JavaScript) · Mobile app', anchor='start', size=6.8)
    f.box(4, 44, 328, 30, '', shadow=True)
    f.text(10, 52, 'Business-logic layer (process)', anchor='start', weight=500)
    f.text(10, 65, 'User management · Book inventory · Transaction management', anchor='start', size=6.8)
    f.box(4, 84, 328, 28, '', shadow=True)
    f.text(10, 92, 'Data layer (storage)', anchor='start', weight=500)
    f.text(10, 104, 'User database · Book database', anchor='start', size=6.8)
    return f.svg()


@fig('lms-vertical', 'Vertical partitioning (factoring) of the library system')
def _():
    f = Fig(336, 108)
    f.text(4, 8, 'decision-making (control) modules', anchor='start', size=6.4, italic=True)
    subs = [('User management\nsubsystem', ['Register and login', 'Update profile']),
            ('Book inventory\nsubsystem', ['Add and remove book', 'Check availability']),
            ('Transaction mgmt\nsubsystem', ['Borrow book', 'Return book'])]
    for i, (t, ws) in enumerate(subs):
        x = 6 + i * 112
        f.box(x, 16, 100, 26, t, weight=500)
        for j, w in enumerate(ws):
            y = 56 + j * 22
            f.box(x + 8, y, 88, 16, w, size=6.4, shadow=False)
            f.line(x + 4, 42, x + 4, y + 8); f.line(x + 4, y + 8, x + 8, y + 8)
    f.text(4, 104, 'worker modules (input, computation, output)', anchor='start', size=6.4, italic=True)
    return f.svg()


@fig('lms-logical', 'Logical data representation for the library system')
def _():
    f = Fig(336, 88, fs=6.8)
    u = f.uclass(4, 4, 90, 'User', ['UserID (key)', 'Name', 'Email', 'Password'])
    t = f.uclass(122, 4, 96, 'Transaction', ['TransactionID (key)', 'UserID', 'BookID', 'BorrowDate'])
    b = f.uclass(246, 4, 88, 'Book', ['BookID (key)', 'Title', 'Author', 'AvailabilityStatus'])
    f.line(94, 40, 122, 40); f.text(97, 35, '1', anchor='start', size=6.2); f.text(119, 35, '*', anchor='end', size=6.2)
    f.line(218, 40, 246, 40); f.text(221, 35, '*', anchor='start', size=6.2); f.text(243, 35, '1', anchor='end', size=6.2)
    return f.svg()


FIGS['layered-pattern'] = ('The layered architecture pattern', table_html(['Name', 'Layered architecture'], [
    ['Description', 'Organizes the system into layers with related functionality associated with each layer. A layer provides services to the layer above it, so the lowest-level layers represent core services that are likely to be used throughout the system.'],
    ['Example', 'A web application with presentation, business-logic, and data-access layers; the food-delivery system described in this section.'],
    ['When used', 'When building new facilities on top of existing systems; when development is spread across several teams, each responsible for a layer; when there is a requirement for multi-level security.'],
    ['Advantages', 'Allows replacement of entire layers so long as the interface is maintained. Redundant facilities (e.g., authentication) can be provided in each layer to increase dependability.'],
    ['Disadvantages', 'A clean separation between layers is often difficult, and a high-level layer may have to interact directly with lower layers. Performance can suffer because a request is processed at each layer.']], ['22%', '78%']), {'wide': True})
clip('layered-generic', 'A generic layered architecture', 174, (236.8, 533.6, 450.5, 685.5))
FIGS['cs-pattern'] = ('The client–server pattern', table_html(['Name', 'Client–server'], [
    ['Description', 'The functionality of the system is organized into services, with each service delivered from a separate server. Clients are users of these services and access servers to make use of them.'],
    ['Example', 'A film and video library organized as a set of servers accessed over the Internet by clients.'],
    ['When used', 'When data in a shared database has to be accessed from a range of locations. Because servers can be replicated, also when the load on a system is variable.'],
    ['Advantages', 'Servers can be distributed across a network. General functionality (e.g., a printing service) can be available to all clients and need not be implemented by all services.'],
    ['Disadvantages', 'Each service is a single point of failure, susceptible to denial-of-service attacks or server failure. Performance may be unpredictable because it depends on the network. There may be management problems if servers are owned by different organizations.']], ['22%', '78%']), {'wide': True})
clip('cs-film', 'A client–server architecture for a film library', 178, (198.0, 129.4, 489.3, 291.7))


@fig('call-return', 'A main program/subprogram (call-and-return) architecture')
def _():
    f = Fig(336, 112)
    m = f.box(128, 4, 80, 22, 'Main program', weight=500)
    subs = [('Controller\nsubprogram', 40), ('Controller\nsubprogram', 168), ('Controller\nsubprogram', 296)]
    f.line(168, 26, 168, 34); f.line(40, 34, 296, 34)
    for t, cx in subs:
        f.line(cx, 34, cx, 42)
        f.box(cx - 34, 42, 68, 22, t)
    for cx in (40, 168, 296):
        f.line(cx, 64, cx, 72); f.line(cx - 22, 72, cx + 22, 72)
        for dx in (-22, 22):
            f.line(cx + dx, 72, cx + dx, 80)
            f.box(cx + dx - 18, 80, 36, 18, 'Worker', size=6.2, shadow=False)
    f.text(168, 106, 'arrows of control run downward; results return upward', size=6.4, italic=True)
    return f.svg()


@fig('fd-layered', 'Layered architecture of a food-delivery system with call-and-return control', wide=True)
def _():
    f = Fig(420, 210, fs=6.8)
    layers = [('Presentation layer', 'Customer app · Restaurant app · Delivery-partner app'),
              ('Application layer', 'Order processing · Restaurant management · Delivery allocation · Tracking'),
              ('Business-logic layer', 'Payment processing · Validation rules · Notification service'),
              ('Data layer', 'Order DB · Customer DB · Restaurant DB · Payment records · Tracking DB')]
    for i, (n, d) in enumerate(layers):
        y = 6 + i * 50
        f.box(4, y, 260, 34, '', shadow=True)
        f.text(10, y + 11, n, anchor='start', weight=500)
        f.text(10, y + 24, d, anchor='start', size=6.3)
        if i < 3:
            f.arrow([(110, y + 34), (110, y + 50)], size=4); f.arrow([(150, y + 50), (150, y + 34)], dash='3,2', kind='open', size=4)
    f.text(104, 47, 'call', anchor='end', size=6.2, italic=True); f.text(156, 47, 'return', anchor='start', size=6.2, italic=True)
    # call-return chain
    chain = ['Client app', 'Order service', 'Payment service', 'Database']
    for i, t in enumerate(chain):
        y = 10 + i * 48
        f.rbox(320, y, 90, 22, t, shadow=False)
        if i < 3:
            f.arrow([(355, y + 22), (355, y + 48)], size=4)
            f.arrow([(375, y + 48), (375, y + 22)], kind='open', dash='3,2', size=4)
    f.text(365, 186, 'each call waits for its\nresponse before continuing', size=6.2, italic=True)
    return f.svg()


@fig('flow-types', 'Transform flow and transaction flow')
def _():
    f = Fig(336, 104, fs=6.6)
    f.text(78, 8, 'Transform flow', weight=500)
    for i, x in enumerate([14, 44, 110, 142]):
        f.circle(x, 52, 11)
    f.circle(78, 52, 15, fill='#EAF7FD'); f.text(78, 52, 'T', weight=500)
    for a, b in [(25, 33), (55, 63), (93, 99), (121, 131)]:
        f.arrow([(a, 52), (b, 52)], size=3.5)
    f.text(30, 78, 'incoming\nflow', size=6.2); f.text(78, 80, 'transform\ncentre', size=6.2); f.text(126, 78, 'outgoing\nflow', size=6.2)
    f.text(250, 8, 'Transaction flow', weight=500)
    f.circle(196, 52, 11); f.circle(236, 52, 15, fill='#EAF7FD'); f.text(236, 52, 'T', weight=500)
    f.arrow([(207, 52), (221, 52)], size=3.5)
    for y, t in [(22, 'A'), (52, 'B'), (82, 'C')]:
        f.circle(304, y, 11); f.text(304, y, t)
        f.arrow([(250, 52 + (y - 52) * 0.3), (293, y)], size=3.5)
    f.text(236, 84, 'transaction\ncentre', size=6.2); f.text(196, 72, 'transaction', size=6.2)
    f.text(304, 100, 'action paths', size=6.2)
    return f.svg()


@fig('payroll-dfd', 'Payroll DFD with its flow boundaries', wide=True)
def _():
    f = Fig(420, 140, fs=6.6)
    xs = [58, 132, 210, 288, 362]
    names = [('1.1', 'Collect work\nhours'), ('1.2', 'Validate\ndata'), ('1.3', 'Calculate\npay'), ('1.4', 'Generate\npayslip'), ('1.5', 'Update\nrecords')]
    for x, (n, t) in zip(xs, names):
        proc(f, x, 64, 24, n, t, size=6.2)
    ext(f, 4, 14, 58, 20, 'Employee', size=6.6)
    store(f, 90, 118, 90, 'D1', 'Employee details')
    f.arrow([(33, 34), (40, 46)]); f.text(10, 44, 'working\nhours', size=6)
    f.arrow([(135, 118), (132, 88)]); f.text(148, 108, 'fetch', size=6, anchor='start')
    for a, b, t in [(82, 108, 'hours'), (156, 186, 'valid'), (234, 264, 'pay'), (312, 338, 'update')]:
        f.arrow([(a, 64), (b, 64)], size=3.5); f.text((a + b) / 2, 76, t, size=6)
    for x, t in [(171, 'incoming boundary'), (249, 'outgoing boundary')]:
        f.line(x, 22, x, 110, dash='4,2', color=CYAN, w=0.8)
        f.text(x, 16, t, size=6, italic=True)
    f.text(95, 104, 'input domain', size=6.2, weight=500)
    f.text(210, 104, 'transform centre', size=6.2, weight=500)
    f.text(325, 104, 'output domain', size=6.2, weight=500)
    return f.svg()


@fig('payroll-l1', 'First-level factoring of the payroll system')
def _():
    f = Fig(336, 74)
    rb, bs = tree(f, (118, 4, 100, 22, 'Payroll system\n(main controller)'), ['Input controller\n(get valid hours)', 'Transform controller\n(compute pay)', 'Output controller\n(produce outputs)'], 0, 44, 98, 26, gap=10)
    return f.svg()


@fig('payroll-l2', 'Program structure of the payroll system after second-level factoring', wide=True)
def _():
    f = Fig(420, 124, fs=6.6)
    f.box(160, 4, 100, 20, 'Payroll system', weight=500)
    ctr = [('Input controller', 76), ('Transform controller', 210), ('Output controller', 344)]
    kids = [['Collect work\nhours()', 'Validate\ndata()'], ['Calculate\npay()'], ['Generate\npayslip()', 'Update\nrecords()']]
    f.line(210, 24, 210, 32); f.line(76, 32, 344, 32)
    for (t, cx), ks in zip(ctr, kids):
        f.line(cx, 32, cx, 40); f.box(cx - 48, 40, 96, 20, t)
        n = len(ks); w = 58; g = 8; x0 = cx - (n * w + (n - 1) * g) / 2
        f.line(cx, 60, cx, 68); f.line(x0 + w / 2, 68, x0 + (n - 1) * (w + g) + w / 2, 68)
        for i, k in enumerate(ks):
            x = x0 + i * (w + g); f.line(x + w / 2, 68, x + w / 2, 76)
            f.box(x, 76, w, 26, k, shadow=False, size=6.4)
    for cx, t in [(76, 'input modules'), (210, 'transform centre'), (344, 'output modules')]:
        f.text(cx, 116, t, size=6.2, italic=True)
    return f.svg()


@fig('atm-dfd', 'ATM DFD showing transaction flow')
def _():
    f = Fig(336, 120, fs=6.6)
    ext(f, 4, 48, 50, 22, 'User', size=6.6)
    proc(f, 128, 59, 28, 'T', 'Menu\nselection', size=6.4)
    for y, (n, t) in zip([18, 59, 100], [('A', 'Withdraw'), ('B', 'Deposit'), ('C', 'Balance\nenquiry')]):
        proc(f, 276, y, 17, n, t, size=6)
        f.arrow([(156, 59 + (y - 59) * 0.4), (259, y)], size=3.5)
    f.arrow([(54, 59), (100, 59)], size=3.5); f.text(77, 53, 'menu choice', size=6)
    f.text(128, 100, 'transaction centre', size=6.2, italic=True)
    return f.svg()


@fig('atm-structure', 'Program structure of the ATM system after transaction mapping', wide=True)
def _():
    f = Fig(420, 132, fs=6.6)
    f.box(170, 4, 80, 20, 'ATM system', weight=500)
    f.line(210, 24, 210, 32); f.line(80, 32, 300, 32)
    f.line(80, 32, 80, 40); f.box(24, 40, 112, 24, 'Read menu selection\n(reception branch)')
    f.line(300, 32, 300, 40); f.box(236, 40, 128, 24, 'Menu selection process\n(transaction dispatcher)', weight=500)
    kids = [('Withdraw', 236), ('Deposit', 300), ('Balance\nenquiry', 364)]
    f.line(300, 64, 300, 72); f.line(236, 72, 364, 72)
    for t, cx in kids:
        f.line(cx, 72, cx, 80); f.box(cx - 28, 80, 56, 22, t, shadow=False)
    f.text(300, 116, 'transaction modules (one per action path)', size=6.2, italic=True)
    return f.svg()
