from math import lcm
a,b,c=map(int,input().split())

if lcm(lcm(a,b),c)==lcm(a,b,c):
  print("=")
elif lcm(lcm(a,b),c)>lcm(a,b,c):
  print(">")
else:
  print("<")
