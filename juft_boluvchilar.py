n = int(input())

def juft(a):
    if (a % 2 == 1):
        return 0
    else:
        a //= 2
        c = 0
        i = 1
        while(i*i<=a):
            if(a % i == 0):
                c+=1
                if (i != a // i):
                    c+=1
            i+=1   
        return c

for i in range(n):
    a = int(input())
    print(juft(a))
