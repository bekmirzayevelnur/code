a=input()
b=[]
c=[]
m=0
n=0
b.append(a[0])
b.append(a[1])
b.append(a[2])
c.append(a[3])
c.append(a[4])
c.append(a[5])
for i in b:
    m+=int(i)
for i in c:
    n+=int(i)
if m==n:
    print("YES")
else:
    print("NO")
