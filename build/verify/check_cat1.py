"""Balancing check for the electricity billing DFDs (context vs level 1)."""
ctx = {('Customer', 'in', 'connection application'), ('Customer', 'in', 'payment'),
       ('Customer', 'out', 'connection number'), ('Customer', 'out', 'bill'),
       ('EB staff', 'in', 'meter reading'), ('EB manager', 'out', 'monthly report')}
# level-1 external flows: (entity, direction, data, process)
l1 = [('Customer', 'in', 'connection application', '1.0'), ('Customer', 'out', 'connection number', '1.0'),
      ('Customer', 'in', 'payment', '3.0'), ('Customer', 'out', 'bill', '4.0'),
      ('EB staff', 'in', 'meter reading', '2.0'), ('EB manager', 'out', 'monthly report', '5.0')]
print('balanced:', {x[:3] for x in l1} == ctx)
# every level-1 process has input and output (internal flows included)
flows = [('Customer', '1.0'), ('1.0', 'Customer'), ('1.0', 'D1'), ('D1', '2.0'), ('EB staff', '2.0'), ('2.0', 'D2'),
         ('D1', '3.0'), ('D2', '3.0'), ('Customer', '3.0'), ('3.0', 'D3'), ('3.0', '4.0'), ('4.0', 'Customer'),
         ('4.0', 'D4'), ('D4', '5.0'), ('D3', '5.0'), ('5.0', 'EB manager')]
for p in ('1.0', '2.0', '3.0', '4.0', '5.0'):
    print(p, 'in' if any(b == p for a, b in flows) else 'NO INPUT', 'out' if any(a == p for a, b in flows) else 'NO OUTPUT')
ents = {'Customer', 'EB staff', 'EB manager'}
print('no entity-entity or entity-store flows:', all(not ((a in ents or a[0] == 'D') and (b in ents or b[0] == 'D')) for a, b in flows))
