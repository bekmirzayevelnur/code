x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=(((y3-y1)**2+(x3-x1)**2))**0.5
b=(((y2-y1)**2+(x2-x1)**2))**0.5
c=(((y3-y2)**2+(x3-x2)**2))**0.5
if a+b>c and a+c>b and b+c>a:
    print("uchburchak")
else:
    print("uchburchak emas")
