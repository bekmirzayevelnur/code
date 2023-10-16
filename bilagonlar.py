n, m, h, f = map(int, input().split())
if m <= n + h + f:
    print(n + h + f - m)
else:
    print(-1)
