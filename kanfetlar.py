mod = int(1e9) + 7
dp = [[0] * 1001 for _ in range(1001)]

dp[0][0] = 1

for n in range(1, 1001):
    dp[n][0] = 1
    for k in range(1, 1001):
        dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % mod

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(dp[n][k])
