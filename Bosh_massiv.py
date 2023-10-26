a=int(input())
for i in range(a):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    k=[]
    for j in range(len(l)-1):
      if l[j]==0 and l[j+1]==0 or l[j]==1 and l[j+1]==1 or l[j]==0 and l[j+1]==1:
        s+=1
      else:
        k.append(s)
        s=0
    print(len(k)+1)
