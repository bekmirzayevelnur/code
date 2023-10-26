n=input()
s=''
for i in n:
    if i!='9':
        s+='9'
        break
    else:
        s+=i
if len(s)==len(n):
    print(s)
else:
    print(s+n[len(s):])
