n=int(input()) 
a=list(map(int, input().split())) 

a.sort() 

for i in range(n): 
  a[i] -= i
a.sort() 
s=0
med=a[n // 2]
for i in range(n): 
  s+=abs(med -a[i]) 
print(s)
