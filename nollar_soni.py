n,m = map(int,input().split())
a = 0
for i in range(n, m+1):
    b=0
    while i%5==0:
        b+=1
        i//=5
    a+=b
print(a)
