p,d,m,s=map(int,input().split())
x=0
k=0
n=0
while k<=s:
    if p>m:
        k+=p
        p=p-d
    else:
        k+=m
    x+=k
    n+=1 
print(n-1)
