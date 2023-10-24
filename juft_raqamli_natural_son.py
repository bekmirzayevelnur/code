def Cfg(D, N):
    return (10**N * D-((5**(N+1)-1)//4-1)-5**N*(D//2)-1)
def Gfg(n):
    if n < 10: 
        return n * 2 
    if n < 20:
        return 10 + n
    N = 1
    while True:
        F = Cfg(3, N) - Cfg(1, N)
        N += 1
        P = 10**N
        L = 1 + Cfg(2, N)
        if n < L:
            return P//5 + Gfg(n - F)
        if n < L + P:
            return n + P//5 + Gfg(L - F) - L
print(Gfg(int(input())))
