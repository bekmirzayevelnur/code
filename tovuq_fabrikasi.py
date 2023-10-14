a=input()
b=list(map(int,input().split()))
c=0
v=0
d=0
h=0
k=0
for i in b:
    if i==1:
        c+=1
    elif i==2:
        v+=1
    elif i==3:
        d+=1
    elif i==4:
        h+=1
    else:
        k+=1
r=max(c,v,d,h,k)
if r==c:
    print(1)
elif r==v:
    print(2)
elif r==d:
    print(3)
elif r==h:
    print(4)
else:
    print(5)
