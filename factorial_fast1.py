def fact(x):
    print(x,end=' ')
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
a=int(input())
print(fact(a))
