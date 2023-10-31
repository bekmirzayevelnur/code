for i in range(int(input())):
    a,b,c = map(int, input().split())
    k = b%2
    b >>= 1
    l = min(a,b,c)
    arr = [0,0,0]
    arr[0] = a - l
    arr[1] = b*2+k - l*2
    arr[2] = c - l
    s = l * 4
    while True:
        if arr[0]:
            arr[0] -= 1
            s += 1
        else:
            break
        if arr[1]:
            arr[1] -= 1
            s += 1
        else:
            break
        if arr[2]:
            arr[2] -= 1
            s += 1
        else:
            break
        if arr[1]:
            arr[1] -= 1
            s += 1
        else:
            break
    print(s)
