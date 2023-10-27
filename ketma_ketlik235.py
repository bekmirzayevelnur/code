l = [0]
for i in range(39):
    for j in range(59):
        for k in range(64): 
            l.append(3**j*5**i*2**k)
l.sort()
a="int(input())"
t=eval(a)
while t:
  print(l[eval(a)])
  t-=1
