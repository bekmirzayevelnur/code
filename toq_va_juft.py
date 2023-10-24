a=int(input())
j=0
t=0
for i in range(len(str(a))):
  if i%2==0:
    j+=int(str(a)[i])
  else:
    t+=int(str(a)[i])
if (j-t)==0 or (j-t)%11==0:
  print("Yes")
else:
  print("No")
