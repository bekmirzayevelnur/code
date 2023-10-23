a=int(input())
b=list(map(int,input().split()))
v=[]
for i in b:
  if b.count(i)==2:
  	v.append(i)
if len(v)==0:
    print(-1)
else:
    print(max(v))
