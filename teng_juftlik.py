a,b=map(int,input().split())
r = max(a,b)-min(a,b)
r1 = r//10
if a==b:
    print(0)
elif max(a,b)%10==min(a,b):
    print(r1)
elif r%10==0:
    print(r//10)
else:
    print(r1+1)
