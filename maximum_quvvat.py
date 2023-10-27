n,k = map(int,input().split())
ls = set(map(int,input().split()))
i = 0
while k > 0:
    if i not in ls:
        k -= 1
    i += 1
while i in ls:
    i += 1
print(i)
