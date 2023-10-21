a,b,c=map(int,input().split())
if min(a,b,c)==a:
    print(min(a,b,c)*3)
elif min(a,b,c)==b and min(a,b,c)!=a and min(a,b,c)!=c:
    print(b*3+1)
elif min(a,b,c)==b and min(a,b,c)!=a and min(a,b,c)==c:
    print(b*3+1)
elif min(a,b,c)==c and min(a,b,c)!=a and min(a,b,c)!=b:
    print(c*3+2)
else:
    print(min(a,b,c)*3)
