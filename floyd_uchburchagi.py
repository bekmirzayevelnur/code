a=int(input())
k=0
for i in range(1,a+1):
    for j in range(i):
        k+=1
        print(k,end=" ")
    print()
