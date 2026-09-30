"""Verify DFD balancing for the lemonade stand (Figures 5.14-5.16)."""
ctx = {('CUSTOMER','in','Customer order'),('CUSTOMER','out','Product served'),('CUSTOMER','in','Payment'),
       ('EMPLOYEE','out','Sales forecast'),('EMPLOYEE','in','Production schedule'),('EMPLOYEE','out','Pay'),('EMPLOYEE','in','Time worked'),
       ('VENDOR','in','Received goods'),('VENDOR','out','Payment'),('VENDOR','out','Purchase order')}
# level-1 flows: (src, dst, label)
l1 = [('CUSTOMER','1.0','Customer order'),('CUSTOMER','1.0','Payment'),('2.0','CUSTOMER','Product served'),
      ('1.0','2.0','Product ordered'),('1.0','EMPLOYEE','Sales forecast'),('EMPLOYEE','2.0','Production schedule'),
      ('3.0','2.0','Inventory'),('VENDOR','3.0','Received goods'),('3.0','VENDOR','Purchase order'),('3.0','VENDOR','Payment'),
      ('4.0','EMPLOYEE','Pay'),('EMPLOYEE','4.0','Time worked')]
ext = {'CUSTOMER','EMPLOYEE','VENDOR'}
l1_ext = {(s,'in',l) if s in ext else (d,'out',l) for s,d,l in l1 if s in ext or d in ext}
print('level0 vs level1 balanced:', l1_ext == ctx, ctx ^ l1_ext)
# process 1.0 boundary at level 1 vs level 2
p1_l1 = {(l, 'in') for s,d,l in l1 if d=='1.0'} | {(l,'out') for s,d,l in l1 if s=='1.0'}
p1_l2 = {('Customer order','in'),('Payment','in'),('Product ordered','out'),('Sales forecast','out')}
print('1.0 vs level2 balanced:', p1_l1 == p1_l2, p1_l1 ^ p1_l2)
