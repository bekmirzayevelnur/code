n=int(input())
s=1
p=[1]
while s<n:
    s*=2
    p.append(s)
def foo(n):
    d=0
    while n!=0:
        q=[]
        for i in p:
            q.append(abs(i-n))
        n=min(q)
        d+=1
    return d
print(foo(n))
