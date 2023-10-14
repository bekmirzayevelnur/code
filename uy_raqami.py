a=int(input())
for i in range(1,1000):
  if i+i%100==a:
    print(i,end=" ")
