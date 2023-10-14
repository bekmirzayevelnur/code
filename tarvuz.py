n,a,b=map(int,input().split())
c=n*(b/a)
if n==1:
    print("0.50000")
else:
    print("%.5f"%c)
