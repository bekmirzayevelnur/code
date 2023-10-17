def l(string):
    return string == string[::-1]
s = input()
p = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        g = s[i:j]
        if l(g) and len(g) > len(p):
            p = g
print(p)
