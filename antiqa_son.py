def asd(n):
    if (len(n)==1 and n=='6') or (len(n)==1 and n=='9'):
        return False
    elif '2' in n or "3" in n or "4" in n or '5' in n or '7' in n:
        return False
    elif n.count('9') == n.count('6'):
        n=n.replace('6','9')
    r=n[::-1]
    if int(n) == int(r):
        return True
    else:
        return False
n=input()
if asd(n):
    print("YES")
else:
    print("NO")
