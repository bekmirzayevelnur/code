a=list(map(int,input().split()))
mus=[]
man=[]
for i in a:
    if int(i)>0:
        mus.append(i)
    else:
        man.append(i)
if len(mus)==0:
    print(max(man))
elif len(man)==0:
    print(min(mus))
elif abs(max(man))>min(mus):
    print(min(mus))
elif abs(max(man)) == min(mus):
    print(min(mus))
else:
    print(max(man))
