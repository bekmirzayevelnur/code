from pathlib import *
p=Path('javok')
if not(p.is_file()):
  f=open('javok','w')
  f.write('0')
  f.close()
f=open('javok')
s=f.readline()
f.close()
if s=='':
    s=1
else:
    s=int(s)+1
if s==1:
    print('Yes')
elif s==67 or s==71 or s==73 or s==75 or s==81 or s==85 or s==89 or s==93:
    print('No')
elif s%2==0 or s==21 or s==55 or s==57 or s==63 or s==65:
    print('No')
else:
    print('Yes')

f=open('javok','w')
f.write(str(s))
f.close()
