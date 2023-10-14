a,b,c=map(int,input().split())
m1=c-a
m2=c-b
if abs(m1)>abs(m2):
  print("2-mushuk")
elif abs(m2)>abs(m1):
  print("1-mushuk")
else:
  print("sichqon")
