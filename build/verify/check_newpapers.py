from check_ch8 import vg
# leap year CFG
print('leap', vg([(1,2),(1,3),(3,4),(3,5),(5,6),(5,7),(2,8),(4,8),(6,8),(7,8)]))
def leap(y):
    if y%4!=0: return False
    elif y%100!=0: return True
    elif y%400==0: return True
    else: return False
print([ (y,leap(y)) for y in (2023,2024,2000,1900,1999,2020)])
# selection sort
print('sel', vg([(1,2),(2,3),(2,9),(3,4),(4,5),(4,8),(5,6),(5,7),(6,7),(7,4),(8,2)]))
def sel(a):
    a=list(a); trace=['1','2']
    n=len(a)
    for i in range(n):
        trace.append('3'); m=i; trace.append('4')
        for j in range(i+1,n):
            trace.append('5')
            if a[j]<a[m]: m=j; trace.append('6')
            trace.append('7'); trace.append('4')
        a[m],a[i]=a[i],a[m]; trace+=['8','2']
    trace.append('9'); return a,'-'.join(trace)
for t in ([],[5],[1,2],[2,1],[3,1,2]): print(t, sel(t))
# subscription
def cost(n,p):
    c=100 if p=='basic' else 150
    d=(0.1 if p=='basic' else 0.15) if n>100 else 0
    return n*c*(1-d)
for a in [(50,'basic'),(100,'basic'),(101,'basic'),(100,'premium'),(101,'premium'),(0,'basic'),(-1,'premium'),(50,'gold'),(50,None),(1,'basic')]:
    print('cost',a,round(cost(*a),2))
