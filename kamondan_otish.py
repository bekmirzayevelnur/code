n = int(input())
y = {}
for f in range(n):
    a = input().split()
    if a[0] in y.keys():
        y[a[0]] = y[a[0]] + int(a[-1])
    else:
        y[a[0]]=int(a[-1])
m = int(input())
for g in range(m):
    s = input()
    print(s,y[s])
