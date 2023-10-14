a=list(map(str,input().split()))
k=""
for i in range(len(a)):
    if a[i][-1]=='v':
        k+=a[i+1]
        k+=" "+a[i]
        break
    else:
        k+=a[i]
        k+=" "+a[i+1]
        break
print(k)
