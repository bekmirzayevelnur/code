def jadval(satr, ustun):
    if satr==1 and ustun==1: return 0
    start=1
    while start<=satr:
        start*=2
    start//=2
    r = start-ustun
    if r>=0:
        nat = ustun*start*(start-1)//2
    else:
        nat = start*start*(start-1)//2
        nat += -r * (start*(start-1)//2+start*start)
    if start==satr: return nat
    n = ustun
    m = satr-start
    if n>start:
        nat += start*m*start
        nat += jadval(start, m)
        n -= start;
        if n<m:
            nat+=jadval(m, n)
        else:
            nat+=jadval(n,m)
#code by ave_owner 
    else:
        nat += start*n*m;
        if n<m:
            nat+=jadval(m, n)
        else:
            nat+=jadval(n,m) 
    return nat;
n,m=map(int,input().split())
if n<m:
    nat=jadval(m+1, n+1)
else:
    nat=jadval(n+1,m+1)
print(nat)
