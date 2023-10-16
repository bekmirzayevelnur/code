n = int(input())
count = 0

while n > 1:
    if n % 3 == 0:
        n = n // 3
        count += 1
    elif n % 3 == 1:
        n = 2 * n + 1
        count += 1
    elif n % 3 == 2:
        n = 2 * n - 1
        count += 1

print(count)
