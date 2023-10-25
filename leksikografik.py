def tur(n):
    ab = []
    for i in range(1, n+1):
        ab.append(str(i))
    ab.sort()
    return ab
n = int(input())
r=tur(n)
print(*r)
