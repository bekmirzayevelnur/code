l, m = map(int, input().split())

if l == 0 or l > m:
    print(-1)
else:
    v = 0
    for n in range(m, 0, -1):
        k = n
        y = k
        while True:
            s = 0
            while k > 0:
                p = k % 10
                k = k // 10
                s += p
            if s == l:
                v = 1
                z = y
                break
            if s < 10:
                break
            k = s
        if v == 1:
            print(z)
            break
