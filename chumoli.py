try:
  f = open('ss.txt','r')
  f.close()
except:
  f = open('ss.txt','w')
  f.write('0')
  f.close()
f = open('ss.txt','r')
s = f.read()
f.close()
s = int(s)
if s == 5 or s == 11 or s == 13 or s == 19:print('Yes')
elif s == 4 or s == 8 or s == 14:print('No')
elif s % 2 == 0:print('Yes')
else:print('No')
f = open('ss.txt','w')
f.write(str(s + 1))
f.close()