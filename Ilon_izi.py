n=int(input())
a=[['' for j in range(n)] for i in range(n)]
k=2
i=0
j=0
a[0][0]=1
while k<=n*n:
    if i+1<n:
        i+=1
        a[i][j]=k
        k+=1
    while i-1>-1 and j+1<n and a[i-1][j+1]=='':
        i-=1
        j+=1
        a[i][j]=k
        k+=1
    if j+1<n:
        j+=1
        a[i][j]=k
        k+=1
    while i+1<n and j-1>-1 and a[i+1][j-1]=='':
        i+=1
        j-=1
        a[i][j]=k
        k+=1
for r in a:
    print(*r)
