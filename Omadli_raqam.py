a=int(input())
a+=1
b=bin(a)[3:]
ans=''
for i in b:
  if i=='0':
    ans+='7'
  else:
    ans+='8'
print(ans)
