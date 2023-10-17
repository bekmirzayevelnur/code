a,b=map(str,input().split())
c=b[-2:]
f=a[-2:]
g=int(c)-int(f)
d=2022-int(a)
e=2022-int(b)
k=e-d
if int(g)==k:
  print(d,e)
else:
  print("NO")
