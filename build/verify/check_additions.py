import sys; sys.path.insert(0,'.')
from check_ch8 import vg
# course flowchart a=10
print('flowchart', vg([(1,2),(2,3),(3,4),(3,5),(5,6),(5,7),(4,8),(6,8),(7,8),(8,9)]))
def fc(b,c):
    a=10
    if a>b: a=b
    elif a>c: b=c
    else: c=a
    return a,b,c
print(fc(5,3), fc(20,4), fc(20,30))
# summation loop
print('sumloop', vg([(1,2),(2,3),(3,4),(4,5),(5,3),(3,6),(6,7)]), sum(range(1,6)))
# parallel links matrix: links a,b 1->2, c 1->3, d 3->4
rows={1:{2,3},2:set(),3:{4},4:set()}
print('parallel (one connection)', sum(len(v)-1 for v in rows.values() if v)+1)
print('parallel (per link)', (3-1)+0+1, 'E-N+2 per link', 4-4+2)
# count-positives matrix
cp={1:[2],2:[3],3:[4,7],4:[5,6],5:[6],6:[3],7:[]}
print('countpos matrix', sum(len(v)-1 for v in cp.values() if v)+1, sum(len(v) for v in cp.values()))
# discount decision table
def pay(logged,total):
    if not logged: return 'login'
    return round(total*0.9,2) if total>100 else total
print(pay(True,150),pay(True,80),pay(False,150),pay(False,80),pay(True,100),pay(True,100.01))
# age ECP/BVA
print([ (a,18<=a<=60) for a in (17,18,19,35,59,60,61)], 4*1+1, 6*1+1)
# arithmetic mutants a+b with (2,2)
print([2-2,2*2,2/2],[3-1,3*1,3/1])
print(90/120*100, 1/3*100)
