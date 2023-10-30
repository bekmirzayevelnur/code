c=float(input())
n=int(input())
left=0
right=1e12
while right-left>1e-11:
    mid=(left+right)/2
    if n*pow(mid,n)+pow(mid,1.0/n)<c:
        left=mid
    else:
        right=mid
print(f'{left:0.7f}')
