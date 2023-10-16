def raq(n):
  if n>0 and n<10:
    return n
  else:
    s=0
    x=str(n)
    for i in range(len(x)):
      s=s+int(x[i])
    return raq(s)
k=int(input())
a=[]
for i in range(k):
  b=int(input())
  a.append(raq(b))
for i in a:
  print(i)
