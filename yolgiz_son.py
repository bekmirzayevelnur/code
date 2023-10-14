a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
  if b.count(i)==1:
    c+=i
print(c)
