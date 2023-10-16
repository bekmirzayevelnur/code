t = int(input())
for i in range(t):
    n = int(input())
    result = (2 * n) + (3 * n) + (5 * n) + (6 * n)
    cubic_root = result ** (1 / 3)
    if cubic_root.is_integer():
        print("YES")
    else:
        print("NO")
