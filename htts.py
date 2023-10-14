n=int(input())
x=0
for s in str(n):
  if int(s)%2!=0:
    x+=1
if len(str(n))%2!=0 and x%2!=0:
  print("YES")
else:
  print("NO")
