"""Verify every computed answer used in Chapter 8."""
import math

def vg(edges):
    nodes = {n for e in edges for n in e}
    E, N = len(edges), len(nodes)
    outdeg = {}
    for a, b in edges: outdeg[a] = outdeg.get(a, 0) + 1
    D = sum(d - 1 for d in outdeg.values() if d > 1)
    return E, N, E - N + 2, D + 1

# factorial (correct CFG of the given code)
fact = [(1,2),(1,3),(2,7),(3,4),(4,5),(5,4),(4,6),(6,7)]
print('factorial', vg(fact))
# teacher flowchart (no n==0 test)
fc = [('S','G'),('G','i'),('i','f'),('f','L'),('L','D'),('D','B'),('B','I'),('I','L'),('D','P'),('P','E')]
print('teacher flowchart', vg(fc))
# larger of two
print('larger', vg([(1,2),(2,3),(3,4),(3,5),(5,6),(4,7),(6,7)]))
# nested if
print('nested', vg([(1,2),(1,3),(3,4),(3,5),(2,6),(4,6),(5,6)]))
# count positives
print('countpos', vg([(1,2),(2,3),(3,4),(3,7),(4,5),(4,6),(5,6),(6,3)]))
# compound
print('compound', vg([(1,'2a'),('2a','2b'),('2a',4),('2b',3),('2b',4),(3,5),(4,5)]))
# switch
print('switch', vg([(1,2),(2,3),(2,4),(2,5),(2,6),(3,7),(4,7),(5,7),(6,7)]))

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
for n in [-1,0,1,2,6,11,12,13]:
    print('fact', n, factorial(n), factorial(n) <= 2**31-1)

# classify coverage
def classify(m):
    path=[]; r='Fail'
    if m>=40: r='Pass'; path.append('T')
    else: path.append('F')
    if m>=75: r='Distinction'; path.append('T')
    else: path.append('F')
    return r,''.join(path)
for m in (80,50,30): print('classify',m,classify(m))
# mutation
print('mut', round(35/45*100,2), round(42/45*100,2), 90/120*100)
for x in (10,2,5,6):
    o='High' if x>5 else 'Low'; m1='High' if x>=5 else 'Low'; m2='High' if x<5 else 'Low'; m3='High' if x>6 else 'Low'
    print('mutants',x,o,m1,m2,m3)
# graph matrix example
rows={1:[1,2,3],2:[4],3:[4],4:[]}
print('matrix M', sum(len(v)-1 for v in rows.values() if v)+1)
