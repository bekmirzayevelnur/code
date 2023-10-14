a=input()
z=0
o=0
for i in a:
  if i=="o":
    o+=1
  elif i=="z":
    z+=1
if z*2==o:
  print("Yes")
else:
  print("No")
