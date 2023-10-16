import math
T = int(input()) 
results = []  
for _ in range(T):
    a, b, c = map(int, input().split())  
    if c % math.gcd(a, b) == 0:  
        results.append("Yes")
    else:
        results.append("No")
for result in results:
    print(result)
