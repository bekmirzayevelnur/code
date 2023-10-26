a=[]
for i in range(8):
  for i in input().split():
    a.append(int(i))
s=a.index(1)
x,y=s%8,s//8
for i in range(2,65):
  s=a.index(i)
  o=s%8
  p=s//8
  if not(abs(p-y)==2 and abs(o-x)==1 or abs(p-y)==1 and abs(o-x)==2):break
  x=o
  y=p
else:print("Yes")
if x!=o or y!=p:
  print("No")
  print(chr(x+97)+str(8-y),chr(o+97)+str(8-p))
