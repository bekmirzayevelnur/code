import math
def s(n):
    if n <= 1:
        return "No"
    d = range(2, (int(math.sqrt(n))+1))
    for i in d:
        if n % i == 0: 
            return "No"
    return "Yes"
n=int(input())
print(s(n))
