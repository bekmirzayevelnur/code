a = int(input())
b=list(map(str,input().split()))
m=0
g=[]
for i in b:
    if len(b[m])>a:
        g.append(b[m][::-1])
    else:
        g.append(b[m])
    m+=1
print(*g)
