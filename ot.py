N,M=map(int,input().split())
b=N*M
a=b*b-b
if N >= 1 and M >= 2:
    a -= 4 * (N - 1) * (M - 2)
if N >= 2 and M >= 1:
    a -= 4 * (N - 2) * (M - 1)
print(a)
