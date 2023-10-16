def a(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        n //= 2
        return 3 * a(n) + (n * (n - 1)) // 2
    else:
        n = (n - 1) // 2
        return 2 * a(n) + a(n + 1) + ((n + 1) * n) // 2
n = int(input())  
print(a(n+1))
