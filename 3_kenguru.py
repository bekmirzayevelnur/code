a,b,c=map(int,input().split())
n=b-a
m=c-b
if n>m:
  print(n-1)
else:
  print(m-1)
