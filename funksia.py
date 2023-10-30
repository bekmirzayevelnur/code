n=int(input())
k=0
while(n>1):
    if n%3==0:
        n/=3
        k+=1
    elif n%3==1:
        n=2*n+1
        k+=1
    else:
        n=2*n-1
        k+=1
print(k)
