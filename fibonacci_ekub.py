def gcd(a,b):
    return a if b==0 else gcd(b, a%b)
def fib(n):
    mod=10**9+7
    a=[[0,1], [1,1]]
    r=[[1,0], [0,1]]
    def mult(a,b):
        c=[[0, 0], [0, 0]] 
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j]=(c[i][j]+a[i][k]*b[k][j])%mod
        return c
    while n > 0:
        if n%2==1:
            r=mult(r,a)
        n=n//2
        a=mult(a,a)
    return r[1][0]
a,b=map(int,input().split())
print(fib(gcd(a,b)))
