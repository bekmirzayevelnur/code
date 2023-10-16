a = int(input())
l = list(map(int, input().split()))
def avarage(l:list):
    return sum(l)/len(l)
def fill_with_zero(a):
    if a == int(a):
        return f'{a}000000000'
    else:
        k = str(a).split('.')
        d = 10 - len(k[1])
        z = '0'*d
        return f'{int(a)}.{k[1]}{z}'
    
print(fill_with_zero(avarage(l)))
