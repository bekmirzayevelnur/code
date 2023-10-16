A, B = map(int, input().split())  
c = [] 
for i in range(1, B+1):
    c.extend([i]*i)

s = sum(c[A-1:B])  

print(s)
