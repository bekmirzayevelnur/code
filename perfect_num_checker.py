def is_perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum = sum + i + n//i
            i += 1
    return sum == n and n!=1
number = int(input())
if is_perfect(number):
    print("YES")
else:
    print("NO")
