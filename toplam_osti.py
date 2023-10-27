n,k=map(int,input().split())
a=list(map(int,input().split()))
q=[0]*k
for i in range(n):
    q[a[i]%k]+=1
z=0
if q[0]>0:
    z+=1
if k%2==0 and a[k//2]>0:
    z+=1
    q.pop(k//2)
q.pop(0)
for i in range(len(q)//2):
    z+=max(q[i],q[-1*i-1])
print(z)
