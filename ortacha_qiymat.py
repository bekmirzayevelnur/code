n,m=map(int,input().split())
sumn=0
for i in range(m):
  l,r,k=map(int,input().split())
  sumn+=((r-l+1)*k)
print(sumn//n)
