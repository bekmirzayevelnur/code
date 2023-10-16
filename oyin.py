def isPrime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
n=int(input())
s=0
for i in range(1, n+1):
 a=isPrime(i)
 if a==True:
  s+=1
if s%2==0:
 print("Ali")
else:
 print("Bobur")
