def check_solution(a, b, c):
    if c % math.gcd(a, b) == 0:
        return "Yes"
    else:
        return "No"

import math

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    result = check_solution(a, b, c)
    print(result)
