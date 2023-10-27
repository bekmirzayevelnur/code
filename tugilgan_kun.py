n=int(input())
a=list(map(int,input().split()))
d,m=map(int,input().split())
k=0
for i in range (n-m+1):
  if sum (a [i:i+m])== d:
    k+=1
print(k)
