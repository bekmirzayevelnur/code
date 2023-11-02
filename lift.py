n=int(input())
for i in range(n):
    m,a,b=map(int,input().split())
    if b>a and b<m:
        print("Maqsud")
    elif b<a and b<m and a<m:
        print("Azimjon")
    elif b<a and b<m and a>m:
        print("Maqsud")
    elif b>m and a>b:
        print("Azimjon") 
    elif a==b:
        print("Azimjon")
    elif m==b:
        print("Maqsud") 
    else:
        print("Draw!")                     
