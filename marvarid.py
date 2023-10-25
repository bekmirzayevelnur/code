a,b = input().split()
a = [c.lower() for c in a if c.isalpha()]
h=list(set(a))
b = [c.lower() for c in b if c.isalpha()]
s=0
k = len(b)
for i in range(k):
    for j in range(len(h)):
      if b[i]==h[j]:
            s+=1
print(s)
