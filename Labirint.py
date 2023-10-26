import sys
sys.setrecursionlimit(10**9)
def t(u):
    if u < 10: return '0'+str(u)
    else: return u
n,m = map(int,input().split())
r=[]
for i in range(n):
    r.append([])
    for j in range(m):
        r[i].append(0)
l=[]
for i in range(2*n+1):
    x=list(input())
    if x.count("B")==1:b_nuqta=[i//2,x.index("B")//4]
    if x.count("A")==1:a_nuqta=[i//2,x.index("A")//4]
    l.append(x)
ai,aj,bi,bj = 0,0,0,0
for i in range(2*n+1):
    for j in range(4*m+1):
        if i%2==1and j%4==2and l[i][j]=='A':ai,aj=(i-1)//2,(j-2)//4
        if i%2==1and j%4==2and l[i][j]=='B':bi,bj=(i-1)//2,(j-2)//4
q = [[ai,aj]]
def bfs(q,u):
    if(len(q) == 0): return
    nq = []
    while(len(q) > 0):
        i = q[-1][0]
        j = q[-1][1]
        q.pop()
        r[i][j] = u
        if(j != 0 and r[i][j-1] == 0 and l[2*i+1][4*j] != '│'): nq.append([i,j-1])
        if(i != 0 and r[i-1][j] == 0 and l[2*i][4*j+2] != '─'): nq.append([i-1,j])
        if(j != m-1 and r[i][j+1] == 0 and l[2*i+1][4*j+4] != '│'): nq.append([i,j+1])
        if(i != n-1 and r[i+1][j] == 0 and l[2*i+2][4*j+2] != '─'): nq.append([i+1,j])
    bfs(nq,u+1)
bfs(q,1)
bchi=b_nuqta
ddd=b_nuqta
def onch(a):
    i=ddd[0]*2+1
    onl=ddd[1]*4+2
    if a=="t":l[i][onl],l[i][onl+1],l[i][onl+2],l[i][onl+3]="┌","─","─","─"
    elif a=="p":l[i][onl],l[i][onl+1],l[i][onl+2],l[i][onl+3]="└","─","─","─"
    elif a=="u":l[i][onl],l[i][onl+1],l[i][onl+2],l[i][onl+3]="─","─","─","─"
    else:l[i][onl+2],l[i][onl+3]="╶","─"
def pach(a):
    i=ddd[0]*2+1
    onl=ddd[1]*4+2
    if a=='u':l[i][onl],l[i+1][onl]="┐","│"
    elif a=='c':l[i][onl],l[i+1][onl]="┌","│"
    elif a=="p":l[i][onl],l[i+1][onl]="│","│"
    else:l[i+1][onl]="╷"
def yuch(a):
    i=ddd[0]*2+1
    onl=ddd[1]*4+2
    if a=='u':l[i][onl],l[i-1][onl]='┘',"│"
    elif a=="c":l[i][onl],l[i-1][onl]='└',"│"
    elif a=='t':l[i][onl],l[i-1][onl]='│','│'
    else:l[i-1][onl]="╵"
def chach(a):
    i=ddd[0]*2+1
    onl=ddd[1]*4+2
    if a=='p':l[i][onl],l[i][onl-1],l[i][onl-2],l[i][onl-3]="┘","─",'─',"─"
    elif a=='t':l[i][onl],l[i][onl-1],l[i][onl-2],l[i][onl-3]="┐","─",'─',"─"
    elif a=='c':l[i][onl],l[i][onl-1],l[i][onl-2],l[i][onl-3]="─","─","─","─"
    else:l[i][onl-2],l[i][onl-3]="╴","─"
chnn=r[b_nuqta[0]][b_nuqta[1]]
def oxti(a):
    ff=a_nuqta
    i=ff[0]*2+1
    onl=ff[1]*4+2
    if a=="u":l[i][onl-1],l[i][onl-2]=' ','╴'
    elif a=="t":l[i+1][onl]='╷'
    elif a=="c":l[i][onl+1],l[i][onl+2]=" ","╶"
    elif a=='p':l[i-1][onl]='╵'
a='0'
for i in  range(chnn-1):
    zi=ddd[0]*2+1
    zio=ddd[1]*4+2
    if ddd[0]>0 and l[zi-1][zio]!="─" and r[ddd[0]-1][ddd[1]]==chnn-1:yuch(a);a='t';ddd=[ddd[0]-1,ddd[1]];chnn-=1
    elif ddd[1]<m-1 and l[zi][zio+2]!="│" and r[ddd[0]][ddd[1]+1]==chnn-1:onch(a);a="u";ddd=[ddd[0],ddd[1]+1];chnn-=1
    elif ddd[0]<n-1 and l[zi+1][zio]!="─" and r[ddd[0]+1][ddd[1]]==chnn-1:pach(a);a='p';ddd=[ddd[0]+1,ddd[1]];chnn-=1
    elif ddd[1]>0 and l[zi][zio-2]!="│"and r[ddd[0]][ddd[1]-1]==chnn-1:chach(a);a='c';ddd=[ddd[0],ddd[1]-1];chnn-=1
if a!='0':oxti(a)
for li in range(len(l)):
    ls=''
    for lj in range(len(l[li])):
        ls+=l[li][lj]
    print(ls)
