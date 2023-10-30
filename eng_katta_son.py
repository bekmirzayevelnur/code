def q(n):
    s=str(n)
    a=int(s[:2])
    b=int(s[2:])
    return b+a
n=int(input())
if n>0:print(n)
else:
    if n>-10:
        print(n)
    else:
        print(q(n))
