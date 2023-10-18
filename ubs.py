def Common(a, b):
    if a > b:
        for c in range(2, b + 1):
            if b % c == 0 and a % c == 0:
                print(c, end=", ")
    else:
        for c in range(2, a + 1):
            if a % c == 0 and b % c == 0:
                print(c, end=", ")
a,b=map(int,input().split())
print(Common(a,b))
