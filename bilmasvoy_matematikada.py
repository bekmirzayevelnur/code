f=10**9+7
a,b,c,d=map(int,input().split())
print(pow((pow(a,c,f)*pow(b,d,f)),(c+d),f))
