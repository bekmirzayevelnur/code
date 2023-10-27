from typing import List
import math
mod = 944161110001
Matrix = List[List[int]]
def multiply(a:Matrix,b:Matrix):
  x1,x2 = len(a),len(b)
  y1,y2 = len(a[0]),len(b[0])
  mul = [[0]*y2 for _ in range(x1)]
  for i in range(x1):
    for j in range(y2):
      for k in range(x2):
        mul[i][j] = (mul[i][j] + a[i][k] * b[k][j])%mod
  for i in range(x1):
    for j in range(y2):
      a[i][j] = mul[i][j] % mod
def power(F,n):
  res = [[1,0,0],[0,1,0],[0,0,1]]
  while n > 0:
    if n % 2 == 1: multiply(res,F)
    multiply(F,F)
    n >>= 1
  return (res[0][0] + res[0][1] + res[0][2]) % mod 
F = [[1,2,3],[1,0,0],[0,1,0]]
n = int(input())
if n == 1: print(1)
elif n == 2: print(1)
elif n == 3: print(1)
else: print(power(F,n-3))
