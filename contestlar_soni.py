def mc(n):
    c5=n//5
    rp=n%5
    while c5>=0:
        if rp%3==0:
            c3=rp//3
            return c5+c3
        c5-=1
        rp+=5
    return -1
n=int(input())
print(mc(n))
