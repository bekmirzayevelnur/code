t = int(input())

for j in range(t):
  n = int(input())
  i=1
  while True:
    a = str(bin(i))
    b = a[2::]
    s = 9 * int(b)
    if s % n == 0:
        print(s)
        break
    i +=1
