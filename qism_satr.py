n, k = map(int, input().split())
s = input()
ans = 0
indks = [0]*26
lst = 0
for b in range(n):
    indks[ord(s[b])-97]+=1
    while(indks[ord(s[b])-97]>k):
        indks[ord(s[ans])-97]-=1
        ans+=1
    if b-ans>=lst:
        lst= b - ans + 1
print(lst)
