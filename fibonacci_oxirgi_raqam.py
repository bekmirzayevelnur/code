def Algorithms_teacher(n):
    if n == 0 : return 0
    elif n == 1: return 1
    else:
        a,b = 0,1
        for i in range(1,n):
            c = a + b;
            a = b;
            b = c;
        lastdigit = int(repr(c)[-1]);
        return lastdigit
t = int(input())
for i in range(t):
  n = int(input(""))
  if n > 60:
    n%=60
  print(Algorithms_teacher(n))
