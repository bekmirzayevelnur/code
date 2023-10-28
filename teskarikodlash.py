n=int(input())
k=""
for i in range(n):
    a,b=map(int,input().split())
    s=0
    for j in range(1, a+1):
        s+=j
    if s==b:
        k+="1"
    else:
        k+="0"
print(k)
