def asd(n):
    f=int(n[0])
    for i in n[1:]:
        c=int(i)
        if c==1:
            if f not in [2,4]:
                return "NO"
        elif c==2:
            if f not in [1,3,5]:
                return "NO"
        elif c==3:
            if f not in [2, 6]:
                return "NO"
        elif c==4:
            if f not in [1,5,7]:
                return "NO"
        elif c==5:
            if f not in [2,4,6,8]:
                return "NO"
        elif c==6:
            if f not in [3,5,9]:
                return "NO"
        elif c==7:
            if f not in [4,8]:
                return "NO"
        elif c==8:
            if f not in [5,7,9,0]:
                return "NO"
        elif c==9:
            if f not in [6,8]:
                return "NO"
        elif c==0:
            if f!=8:
                return "NO"
        f=c
    return "YES"
n=input()
print(asd(n))
