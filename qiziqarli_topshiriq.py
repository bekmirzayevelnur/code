a,b = map(int, input().split())

d = False
for x in range(1, a):
    y = a - x
    if x * y == b:
        print(y,x)
        d = True
        break

if not d:
    print(-1)
