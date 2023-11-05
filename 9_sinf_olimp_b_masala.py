n=input()
m=input()
c=0
k=["a", "e", "i", "o", "u", "y"]
for i in range(len(n)):
    if n[i]==m[i]:
        continue
    else:
        if ((n[i] in k) and (m[i] not in k)) or ((n[i] not in k) and (m[i] in k)):
            
            c+=1
        else:
            continue
print(c)
