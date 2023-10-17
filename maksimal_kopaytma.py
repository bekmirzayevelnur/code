n = int(input())
m = 0
v = 0
while n > 0:
    digit = n % 10
    y = (n // 10) % 10
    p = (n // 100) % 10
    i = y * p * digit
    if i > m:
        m = i
        v = y * 100 + p * 10 + digit
    n //= 10
print(m)
