s=str(input())[::-1]
l,k=1,0
for i in s:
    k+=(ord(i)-64)*l
    l*=26
print(k)
