def jas(n):
    if n <= 0:
        return 0
    if n <= 3:
        return 1
    
    asd = [0] * (n + 1)
    asd[0] = 1
    asd[1] = 2
    asd[2] = 2
    head = 2
    tail = 3
    num = 1
    result = 1
    
    while tail < n:
        for i in range(asd[head]):
            asd[tail] = num
            if num == 1 and tail < n:
                result += 1
            tail += 1
        num = num ^ 3
        head += 1
    
    return result
n = int(input())
print(jas(n))
