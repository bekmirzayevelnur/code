x,l1,r1,l2,r2=map(int,input().split())
k=1
if l1*l2==x:
  print("Right")
  print(l1, l2)
else:
  for i in range(1,int(abs(x)**0.5)+1):
    d=abs(x)/i
    if l1<=d<=r1 and l2<=i<=r2 and d%1==0:
      k=0
      if x>0:
        print('Right')
      else:
        print('Left')
      print(int(d),i)
      break
    elif l1<=i<=r1 and l2<=d<=r2 and d%1==0:
      k=0
      if x>0:
        print('Right')
      else:
        print('Left')
      print(i,int(d))
      break
  if k:
    print("Impossible")
