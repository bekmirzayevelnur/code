n=input()
s,p=0,0
for i in range(len(n)):
  s+=int(n[i])**len(n)
if int(n)==s:
    for i in range(len(n)):
        p+=int(n[i])
    print(p)
else:
  print(n)
