def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
k=int(input())
data = list(fibonacci(k))
print(data)
