a=list(map(int,input().split(".")))
n=0
for i in a:
  if i<256:
    n+=1
if len(a)==4 and n==4:
  print("YES")
else:
  print("NO")
