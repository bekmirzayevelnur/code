n=int(input())
for i in range(n):
  a=int(input())
  i=1
  while a>0:
    if a>5**i:
      a-=5**i
      i+=1
    else:
      print(i)
      break
