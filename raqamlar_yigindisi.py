a=int(input())
k=0
while a>0:
    k+=a%10
    a=a//10
print(k)
