import math
a,b=map(int,input().split())
c=(a+b)/2
v=math.sqrt(((a)*(b)))
if c>v:
  print(">")
elif c==v:
  print("=")
else:
  print("<")
