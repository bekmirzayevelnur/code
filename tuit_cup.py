n, k = map(int, input().split())
m = list(map(int, input().split()))
m.sort()
res = 0
for i in m:
    res += i>0 and i>=m[-k]
print(res)
