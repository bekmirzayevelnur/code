a=int(input())
b=list(map(int,input().split()))
b.sort()
k=sum(b[1:-1])/(a-2)
if k==int(k):
    print(int(k))
else:
    print("%.5f"%k)
