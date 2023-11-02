a,b=map(int,input().split())
s=max(a,b)
p=6
k=p-s+1
if k%6==0:
  print(str(k//6)+"/"+str(int(p/6)))
elif k%3==0:
  print(str(k//3)+"/"+str(int(p/3)))
elif k%2==0:
  print(str(int(k//2))+"/"+str(int(p/2)))
else:
  print(str(k)+"/"+str(p))
