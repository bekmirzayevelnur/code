def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def find(x, y):
    if not check(y):
        return 0
    s = x // y
    for i in range(2, min(x // y, y - 1) + 1):
        s -= find(x // y, i)
    return s
l, r, k = map(int, input().split())
print(find(r, k) - find(l - 1, k))
