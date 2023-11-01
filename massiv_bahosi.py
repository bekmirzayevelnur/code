n = int(input()) 
a = list(map(int,input().split()))  
l=[]
l1=[]
m=[]
for j in range(n):
    if a[j]%2==0:
        l.append(a[j])
    elif a[j]<0:
        m.append(a[j])
    else:
        l1.append(a[j])
l.sort()
l.reverse()
m.sort()
l1.sort()
print(*(l1+m+l))
