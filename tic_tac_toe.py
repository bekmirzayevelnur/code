a=input()
b=input()
c=input()
d=a.count("X")+b.count("X")+c.count("X")
e=a.count("O")+b.count("O")+c.count("O")
if d==e:
  print("O")
elif d>e:
  print("X")
else:
  print("O")
