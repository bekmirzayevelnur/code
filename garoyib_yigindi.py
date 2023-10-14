x=[]
a,b=map(int,input().split())
for i in range (a,b+1):
  if i%3==0 and i%7!=0:
    x.append(i)
print(sum(x))
