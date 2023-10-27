a,b = map(int,input().split())
s=list(map(int,input().split()))
c=int(input())
print(c-(sum(s)-s[b])//2)
