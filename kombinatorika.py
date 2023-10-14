a=int(input())
r=((a-2)*(a-1)*a)%1000000007
if a==1 or a==2:
  print(a)
else:
  print(r)
