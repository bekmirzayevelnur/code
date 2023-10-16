import math

n = int(input())

k = int(math.log10(n) + 1)

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    if k == 1:
        print("12/09/000" + str(n))
    elif k == 2:
        print("12/09/00" + str(n))
    elif k == 3:
        print("12/09/0" + str(n))
    elif k == 4:
        print("12/09/" + str(n))
else:
    if k == 1:
        print("13/09/000" + str(n))
    elif k == 2:
        print("13/09/00" + str(n))
    elif k == 3:
        print("13/09/0" + str(n))
    elif k == 4:
        print("13/09/" + str(n))
