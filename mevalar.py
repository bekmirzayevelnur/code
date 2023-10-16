s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
d = list(map(int,input().split()))
d1 = list(map(int,input().split()))
x = 0
y = 0

for i in d:
    if i >= (s-a) and i <= (t-a):
        x+=1

for j in d1:
    if j <= (t - b) and j >= (s - b):
        y += 1

print(x)
print(y)
