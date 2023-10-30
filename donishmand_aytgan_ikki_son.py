n=int(input())
A=list(map(int,input().split()))
def solve(A):
    y=max(A)
    d=1
    while d*d<=y:
        if y%d==0:
            A.remove(d)
            if d*d!=y:
                A.remove(y//d)
        d+=1
    x=max(A)
    print(max(x,y),min(x,y))
solve(A)
