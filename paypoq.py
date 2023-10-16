n = int(input())
a = list(map(int, input().split()))  

a.sort() 

k = a[0]  
sum = 0  
count = 0  
for i in range(n):
    if k == a[i]:
        count += 1
        if i == n - 1:
            sum += count // 2
    else:
        sum += count // 2
        count = 0
        k = a[i]
        i = i - 1

print(sum)
