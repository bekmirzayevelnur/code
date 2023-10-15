def find_minimum_bolalar(M, N, a):
    total_stones = sum(a)
    if total_stones < M:
        return -1
    sorted_a = sorted(a, reverse=True)
    min_bolalar = 0
    sum_stones = 0
    for i in range(N):
        sum_stones += sorted_a[i]
        min_bolalar += 1
        if sum_stones >= M:
            return min_bolalar
    return -1
M, N = map(int, input().split())
a = list(map(int, input().split()))
result = find_minimum_bolalar(M, N, a)
print(result)
