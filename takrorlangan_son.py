n=int(input())
a=list(map(int,input().split()))
k=0
s=0
q=0
while q<n-1:
  for j in range(q,n):
    if a[q]==a[j]:
      k+=1
      q=j
  q+=1
  if k>s:
    s=k
  k=0
print(s)
