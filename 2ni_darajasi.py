def p(a):
    c=""
    while a!=0:
        b=a%2
        c+=str(b)
        a//=2
    if c.count("1")==1:
        return "YES"
    else:
        return "NO"
    c=c[::-1]
a=int(input())
print(p(a))
