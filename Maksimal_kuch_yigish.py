def solve():
    n,x,k=map(int,input().split())
    a=list(map(int, input().split()))
    ans=0
    def brute(i,cur,rem):
        nonlocal ans
        if i==n or rem==0:
            ans=max(ans,cur)
            return
        if cur>=a[i]:
            brute(i+1,cur+a[i],rem-1)
        brute(i+1,cur,rem)
    brute(0, x, k)
    print(ans)
def main():
    t=1
    while t > 0:
        solve()
        t-=1
if __name__ == "__main__":
    main()
