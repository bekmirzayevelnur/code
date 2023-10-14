def raq(n):
  s=0
  while n>0:
    s+=n%10
    n//=10
  if s>9:
    return raq(s)
  return s
n=int(input())
print(raq(n))
