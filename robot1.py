a=[]
i=0
j=0
for x in range(1,8):
    k=list(input().split())[:7]
    if '1' in k:
        i=x-1
        j=k.index('1')
    a.append(k)
print(abs(3-i)+abs(3-j))
