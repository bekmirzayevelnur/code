from math import gcd
a,b,c,d=map(int,input().split())
print(gcd(pow(a,b,d)-(c%d),d))
