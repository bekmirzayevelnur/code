a=int(input())
l=[a]
while a!=1:
    if a%2==0:
        a=a//2
        l.append(a)
    else:
        a=a*3+1
        l.append(a)
    if a==1:
        print(*l)
