n = list(map(int, input().split()))
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

res = []
for i1, i2 in zip(n, a):
    res.append(i1*i2)
a= ''.join(str(i) for i in res)
for i in a:
    if i==i:
        rep = a[1:] + a[:1]
    else:
        pass
print(rep)
