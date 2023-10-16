n = int(input("n ni kiriting: ")) 
sum = 0
j = 0
for i in range(n):
    if sum >= n:
        break
    else:
        sum += i
    j = i

print(n - sum + j)
