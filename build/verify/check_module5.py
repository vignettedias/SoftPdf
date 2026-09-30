"""Checks for the Module 5 examples in Chapter 8."""
from collections import deque
tree = {'M1': ['M2', 'M3', 'M4'], 'M2': ['M5', 'M6'], 'M3': [], 'M4': ['M7'], 'M5': [], 'M6': [], 'M7': []}
def dfs(n):
    out = [n]
    for c in tree[n]: out += dfs(c)
    return out
def bfs(n):
    out, q = [], deque([n])
    while q:
        x = q.popleft(); out.append(x); q.extend(tree[x])
    return out
print('top-down depth-first :', dfs('M1'))
print('top-down breadth-first:', bfs('M1'))
print('stubs (top-down):', len(tree) - 1)
parents = {c for p, cs in tree.items() for c in cs}
nonleaf = [p for p, cs in tree.items() if cs]
print('drivers (bottom-up), one per calling module:', nonleaf, len(nonleaf))
# bottom-up levels
depth = {}
def d(n, k=0):
    depth[n] = k
    for c in tree[n]: d(c, k + 1)
d('M1')
height = {}
def h(n):
    height[n] = 0 if not tree[n] else 1 + max(h(c) for c in tree[n]); return height[n]
h('M1')
print('bottom-up by height:', sorted(tree, key=lambda n: (height[n], n)))

# dose examples
def calculate_dose(age, weight):
    dose = 0.5 * weight
    return round(dose * 0.9, 2) if age > 70 else dose
def getPatientData_stub():
    return {"age": 65, "weight": 70}
p = getPatientData_stub(); assert calculate_dose(p["age"], p["weight"]) == 35
print('dose 70kg age 70/71:', calculate_dose(70, 70), calculate_dose(71, 70))

# interface defect
def get_age(): return "25"
def calculate_birth_year(age): return 2025 - age
try:
    calculate_birth_year(get_age()); print('no error')
except TypeError as e:
    print('interface defect:', e)
# data-flow defect
def get_price(): return 100
def apply_discount(price): return price * 0.9
def final_price_bug():
    price = get_price(); return apply_discount(50)
def final_price_ok():
    price = get_price(); return apply_discount(price)
print('data flow: buggy', final_price_bug(), 'correct', final_price_ok())
