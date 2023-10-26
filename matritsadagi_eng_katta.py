a=int(input())
if a%2==0:
  print(-1)
else:
  g=a//2
  for i in range(a):
    if i+1==g+1:
      print('1 '*a)
    else:
      print(g*'0 '+'1 '+g*'0 ')
