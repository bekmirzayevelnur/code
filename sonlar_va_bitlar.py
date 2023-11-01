n=int(input())
s=1
k=0
for i in range(n-60,n+1):
    k=bin(i).count('1')
    if k+i==n:
        print(i)
        s=0
        break
if s:print(-1)
