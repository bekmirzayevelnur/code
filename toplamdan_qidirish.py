n,q=map(int,input().split())
a=set(input().split())
for i in range(q):
  x=input()
  if x in a:
    print("YES")
  else:
    print("NO")
