def asd(n, k):
    m=10**9+7
    dp=[[0]*(k+1) for _ in range(2)]
    dp[1][0] = 1
    for i in range(2, n+1):
        p=[0]*(k+2)
        for j in range(1,k+2):
            p[j]=(p[j-1]+dp[(i-1)%2][j-1])%m
        for j in range(k+1):
            dp[i % 2][j]=(p[j+1]-p[max(0,j-i+1)])%m
    return dp[n%2][k]
n,k=map(int,input().split())
r=asd(n,k)
print(r)
