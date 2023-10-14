n=input().split("0")
k=0
for i in n:
    if len(i)>0:
        k+=1
if k>1:
    print("NO")
else:
    print("YES")
