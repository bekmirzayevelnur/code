a=int(input())
b=list(map(int,input().split()))
c=len(b)
if c%2!=0 and b[0]==b[-1] and b[0]==b[c//2]:
    print("Ajoyib ro'yxat")
else:
    print("Ajoyib ro'yxat emas")
