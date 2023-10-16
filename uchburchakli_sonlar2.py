n = int(input())
numbers = list(map(int, input().split()))

result = ""
for num in numbers:
    triangular = False
    i = 0
    while (i * (i + 1) // 2) <= num:
        if (i * (i + 1) // 2) == num:
            triangular = True
            break
        i += 1

    if triangular:
        result += "1"
    else:
        result += "0"

print(result.strip())
