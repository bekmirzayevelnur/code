from math import gcd
t=int(input())
res=[]
while t>0:
    t-=1
    a,b,c=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if c<b and c%(gcd(a,b))==0:
        res.append('YES')
    else:
        res.append('NO')
for i in res:
    print(i)
