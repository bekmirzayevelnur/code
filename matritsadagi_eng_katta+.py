n = int(input())
if n % 2 == 0:
    print(-1)
    exit()
for i in range(n):
    for j in range(n):
        if n // 2 == j or n // 2 == i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
