a,b=map(int,input().split())
c=list(map(int,input().split()))
x=0
v=[]
for i in range(len(c)):
  if c[i]==b:
    x+=c[i]
    v.append(i+1)
print(x)
print(*v)
