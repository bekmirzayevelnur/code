a=int(input())
b=list(map(int,input().split()))
x=[]
for i in b:
  if i%2==0:
    x.append(i)
if len(x)==0:
    print("-1")
else:
    print(max(x))
