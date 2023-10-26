from bisect import bisect_left , bisect_right
def weekly_4_C(N,k,o,ki):
  y=0
  k.sort()
  o.sort()
  ki.sort()
  for o1 in o:
    ky=bisect_left(k,o1)
    kiy=N-bisect_right(ki,o1)
    y+=ky*kiy
  return y
N=int(input())
k=list(map(int,input().split()))
o=list(map(int,input().split()))
ki=list(map(int,input().split()))
print(weekly_4_C(N,k,o,ki))
