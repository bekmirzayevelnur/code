def asd(t):
    r=[]
    for i in range(len(t)-1):
        r.append(t[i]%10+t[i+1]%10)
    return r
t=int(input())
s = list(map(int,input().split()))
while len(s) > 1:
    s = asd(s)
print(s[0]%10)
