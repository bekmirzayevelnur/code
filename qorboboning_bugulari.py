x=str(input())
y=str(input())


m=""
n=""
k=""
l=""
for i in x:
 if i==".":
  for j in range(x.index(".")+1, len(x)):
   k+=x[j]
  break
 else:
  m+=i
for q in y:
 if q==".":
  for w in range(y.index(".")+1, len(y)):
   l+=y[w]
  break
 else:
  n+=q
m=int(m)
k=int(k)
n=int(n)
l=int(l)
if m>n:
 print(x)
elif m<n:
 print(y)
elif m==n:
 if k>l:
  print(x)
 elif k<l:
  print(y)
 else:
  print(x)
