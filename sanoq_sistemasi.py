def sana(raq, k, upper=False):
    belgi = '0123456789abcdefghijklmnopqrstuvwxyz'
    if k > len(belgi): return None
    res = ''
    while raq > 0:
        res = belgi[raq % k] + res
        raq //= k
    return raqresult.upper() if upper else res
a,b=map(int,input().split())
print(sana(a,b))
