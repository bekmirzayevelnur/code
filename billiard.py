a,b=map(int,input().split())

if a>b and a%b==0:
    print(int((a/b)-1), "2")
elif b>a and b%a==0:
    print(int((b/a)-1), "4")
elif a>b:
    print(a+b-2, "4")
elif a==b:
    print("0" , "3")
else:
    print(a+b-2, "2")
