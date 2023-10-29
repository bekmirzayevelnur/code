a,b,c,d=map(int,input().split())
l=[]
for i in range(a):
    s=""
    z=input()
    for i in z:
        s+=i*d
    for i in range(1,c+1):
        l.append(s)
for i in range(len(l)):
    print(l[i])
