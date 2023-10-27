*a,=map(int,input().split())
a.sort()
cnt=a[2]-a[1]
rg=cnt
a[1]+=cnt;a[0]+=cnt
rg=a[1]-a[0]
if (rg%2==0):
  print(cnt+rg//2)
else:
  print(cnt+(rg+1)//2+1)
