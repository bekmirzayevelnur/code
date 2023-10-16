import math

a, b, c = map(int, input().split()) 
D = b * b - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"{x1:.4f} {x2:.4f}")
elif D == 0:
    x = -b / (2 * a)
    print(f"{x:.4f}")
else:
    pass
