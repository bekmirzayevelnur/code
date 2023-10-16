n=int(input())
S=0
if n>0:
    for i in range(1,n+1):
        S+=i
elif n<0:
    for i in range(n,2):
        S+=i
print(S)
