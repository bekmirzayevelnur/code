n = int(input())
sum = 0

if n > 0:
    while n > 0:
        d = n % 10
        if d == 0:
            sum += 6
        elif d == 1:
            sum += 2
        elif d == 2 or d == 3 or d == 5 or d == 9:
            sum += 5
        elif d == 4:
            sum += 4
        elif d == 6:
            sum += 6
        elif d == 7:
            sum += 3
        elif d == 8:
            sum += 7
        n = n // 10
    print(sum)
else:
    print(6)
