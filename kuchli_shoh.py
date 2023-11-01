l = ['a','b','c','d','e','f','g','h']
a,b = map(str,input().split())
x1 = l.index(a[0])+1
y1 = int(a[1])
x2 = l.index(b[0])+1
y2 = int(b[1])
l = max(abs(x1-x2),abs(y1-y2))
if l%2:print(l//2+1)
else:print(l//2)
