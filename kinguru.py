def check_collision(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        t = (x2 - x1) / (v1 - v2)
        if t >= 0 and t % 1 == 0:
            return "YES"
        else:
            return "NO"
x1, v1, x2, v2 = map(int, input().split())
result = check_collision(x1, v1, x2, v2)
print(result)
