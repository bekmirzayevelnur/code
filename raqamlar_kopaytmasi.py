def smallestNumber(n):
    if n >= 0 and n <= 9:
        return n
    digits = []
    for i in range(9, 1, -1):
        while n % i == 0:
            digits.append(i)
            n = n // i
    if n != 1:
        return -1
    k = 0
    while digits:
        k = k * 10 + digits.pop()
    return k

n = int(input())
print(smallestNumber(n))
