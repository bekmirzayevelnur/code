a,b,c,d,e,f,g=map(int,input().split())
x=int(input())
m=a+b+c+d+e+f+g
if x-m<=0:
  print(0)
else:
  print(x-m)
