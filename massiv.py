n=int(input())
a=list(map(int,input().split()))
san=0
for i in range(n):
     for j in range(n):
         if i<j and a[i]>2*a[j]:
             san+=1          
print(san)
