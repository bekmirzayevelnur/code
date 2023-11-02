n=int(input())
a=input()
b=input()
a=a.split()
b=b.split()
a1=""
b1=""
for i in a:
    a1+=str(i)
for j in b:
    b1+=str(j)
c=int(a1,2)^int(b1,2)
c1=bin(c)
c1=c1[2:]
k=n-len(c1)
s="0"*k+c1
print(" ".join(s))
