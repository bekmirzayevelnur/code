a=input()
b=len(a)
c=0
for i in a:
  c+=int(i)
if c%2!=0 and a[0]!=0 and b==9:
  print("yes")
else:
  print("no")
