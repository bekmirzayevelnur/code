n=int(input())
for i in range(n):
    a=int(input())
    a=(a//2)+1 if a%2 else a//2
    print(a)
