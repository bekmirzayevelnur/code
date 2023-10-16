def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

egizak_sonlar = []
for num in range(2, n+1):
    if is_prime(num):
        egizak_sonlar.append(str(num))

result = ' '.join(egizak_sonlar)
print(result)
