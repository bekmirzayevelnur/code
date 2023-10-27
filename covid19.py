n,k = map(int,input().split())
arr = list(map(int,input().split()))
s = 0
for i in range(0,n):
  s+=arr[i]
  if s-k < 0:
    s = 0
  else:
    s = s-k
if s < 0: print(0)
else: print(s)
