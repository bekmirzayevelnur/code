x1, y1, x2, y2 = map(int, input().split())
s = ((abs(x2-x1))**2+(abs(y2-y1))**2)
res = s/8/2
if res == int(res):
    print(int(res))
else:
    print(res)
