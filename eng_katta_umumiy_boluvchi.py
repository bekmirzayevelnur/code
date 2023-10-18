def funk(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    if min_num == 0:
        return max_num
    elif min_num == 1:
        return 1
    else:
        return funk(min_num, max_num % min_num)
a, b = map(int,input().split())
print(funk(a, b))
