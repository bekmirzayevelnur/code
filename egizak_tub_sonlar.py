from math import*
i,n=map(int,input().split())
s=0
for a in range(1,i+1):
  if i%a==0:
    s+=1

d=0
for t in range(1,n+1):
  if n%t==0:
    d+=1

if s==2 and d==2 and abs(n-i)==2:
  print("YES")
else:
  print("NO")
