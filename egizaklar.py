def s(a, n):
    a.sort()
    c = 1
    e = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            c += 1
        else:
            e += c - c%2
            c = 1
    return e + c - c%2

t = int(input())
x = []
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(s(m,n))
