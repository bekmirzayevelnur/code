a=int(input())
if a<38:
  print(a)
elif a%10==9 or a%10==4:
  print(a+1)
elif a%10==8 or a%10==3:
  print(a+2)
elif a%10==7 or a%10==6 or a%10==5:
  print(a)
else:
  print(a)
