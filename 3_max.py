a=int(input())
for i in range(1):
  b=list(map(int,input().split()))
v=b.remove(max(b))
n=b.remove(max(b))
print(max(b))
