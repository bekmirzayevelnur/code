n,k=map(int, input().split())
f=1000000007
if n!=0:
  print((pow(k,n,f)-1)*pow(k-1,f-2,f)%f)
else:
  print(0)
