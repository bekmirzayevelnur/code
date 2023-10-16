import math

MAX = 1000000
primes = []

def sieveSundaram():
    marked = [False] * ((MAX//2) + 100)
    for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
        for j in range((i * (i + 1)) << 1, MAX//2 + 1, 2 * i + 1):
            marked[j] = True
    primes.append(2)
    for i in range(1, MAX//2 + 1):
        if not marked[i]:
            primes.append(2 * i + 1)

def isSmith(n):
    original_no = n
    pDigitSum = 0
    for i in range(len(primes)):
        while n % primes[i] == 0:
            p = primes[i]
            n = n // p
            while p > 0:
                pDigitSum += p % 10
                p = p // 10
    if n != 1 and n != original_no:
        while n > 0:
            pDigitSum += n % 10
            n = n // 10
    sumDigits = 0
    while original_no > 0:
        sumDigits += original_no % 10
        original_no = original_no // 10
    return pDigitSum == sumDigits

n = int(input())
sieveSundaram()
if isSmith(n):
    print(1)
else:
    print(0)
