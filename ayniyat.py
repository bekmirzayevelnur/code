n = int(input())

if n < 3:
    a = 0
elif n < 7:
    a = 1
else:
    k = n // 10
    if n % 10 < 3:
        a = 2 * k
    elif n % 10 < 7:
        a = 2 * k + 1
    else:
        a = 2 * k + 2

print(a)
