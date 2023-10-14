a=int(input())
x=[]
for i in range(1,a+1):
  if i%3==0:
    x.append(i)
  elif i%5==0:
    x.append(i)
  elif i%7==0:
    x.append(i)
print(sum(x))
