a=int(input())
b=int(input())
if a+b==24:
  print(0)
elif a+b>=0 and a+b<=23:
    print(a+b)
else:
    print((a+b)%24)
