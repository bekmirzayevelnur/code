a,c=map(int,input().split("/"))
for i in range(2,int(a)+1):
  while int(a)%i==0 and int(c)%i==0:
    a//=i
    c//=i
    if int(a)%i!=0 or int(c)%i!=0:
      break
print(str(a)+"/"+str(c))
