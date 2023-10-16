n = int(input())
c = 0
if n == 2 or n == 3:
    print(2)
elif n == 1:
    print(1)
else:
    i = 1
    while i <= (n+1)**(1/2):
        if (n+1)%i == 0:
            c += 1
        i += 1
    if c >= 2:
        print(0)
    else:
        print(n)
