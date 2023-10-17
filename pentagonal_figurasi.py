import math
a=int(input())
b=(1+math.sqrt(1+24*a))/6
if b==int(b):
    print(int(b))
else:
    print("-1")
