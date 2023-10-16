Z = int(input("Z ni kiriting: "))  
if Z == 0:
    print("-1")
    exit()
c = 0
n = abs(Z)
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        c += 1
        if i*i != n:
            c += 1
if c % 2 == 1 and Z > 0:
    res = c + 1
else:
    res = c
print(res)
