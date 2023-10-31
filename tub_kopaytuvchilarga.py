import math  
def func(num):  
    while num % 2 == 0:  
        l.append(2)  
        num = num // 2  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
        while num % i == 0:  
            l.append(i)  
            num = num // i  
    if num > 2:  
        l.append(num) 
l=[]
num = int(input())
func(num)
res=""
for k in l:
    res+=str(k)
    res+="*"
print(res[0:-1])
