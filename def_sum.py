
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
