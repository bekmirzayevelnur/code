a,b=map(int,input().split())
c=list(map(int,input().split()))
tot=0
f=sorted(c)
co=0
g=0
v=0
for i in range(len(c)):
    tot+=c[i]
if  tot<a:
    g=1
else:
    for j in range(len(c)-1,-1,-1):
        if co<a:
            co+=f[j]
            v+=1
            
if g==1:
    print(-1)
else:
   print(v)
