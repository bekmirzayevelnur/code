l = list(map(int,input().split()))
s = 0
l =sorted(l)
a = l[1] - l[0]
b = l[2] - l[1]
if a == b:
    print(l[2]+b)
elif a > b:
    print(l[0]+b)
else:
    print(l[1]+a)
