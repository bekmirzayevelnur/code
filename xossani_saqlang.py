a,b,c=map(str,input().split())
if c=="*":
  d=int(a)*int(b)
  print(1,d)
elif c=="+":
  d=int(a)+int(b)-1
  print(1,d)
elif c=="-":
  d=int(b)-int(a)+1
  print(1,d)
else:
  d=int(b)*2
  f=int(a)*2
  print(f,d)
