n=int(input())
h=(n//3600)%24
m=((n-(h*3600))//60)%60
s=(n-(m*60+h*3600))%86400
print((str(h)+":"+str(m).rjust(2,"0")+":"+str(s).rjust(2,"0")))
