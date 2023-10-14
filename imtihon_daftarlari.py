a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
if b==c:
  print("YES")
else:
  print("NO")
