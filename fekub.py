n = int(input())
matrix=[[17205, 17463], [17207, 17208], [18228, 18229], [17714, 18485], [17457, 17464], [16693, 17203], [17720, 18230], [18486, 18231], [17205, 16695], [17975, 17976], [16951, 16952], [16692, 17206], [18484, 18487], [17717, 18230], [18484, 17464], [17202, 17204], [16946, 18482], [17457, 17458], [17970, 17971], [18483, 18488], [17719, 17720], [16689, 18481], [16948, 17206], [16946, 16691], [18486, 18487], [17969, 16694], [17971, 17975], [16696, 16952], [18231, 17207], [17460, 17463]]
arr=[]
matr=[]
for i in range(n):
    arr.append(input())
a=['A','B','C','D','E','F','G','H']
b=['1','2','3','4','5','6','7','8']
baza=[[0]*8]*8
try:
    f=open('baza.txt','r')
except:
    f=open('baza.txt','w')
    f.write('1')
    f.close()
    f=open('baza.txt','r')
for i in matrix:
    k=[]
    for j in i:
        k.append(bin(j)[2:].zfill(16))
    matr.append(k)
for i in range(8):
    for j in range(8):
        baza[i][j]=ord(chr(ord(arr[i][0])+ord(b[j][0])))
brr = []
for row in matr:
    drow = []
    for element in row:
        decoded_element = ''.join(chr(int(element[i:i+8], 2)) for i in range(0, len(element), 8))
        drow.append(decoded_element)
    brr.append(drow)
poper = [0]*8
with open('baza.txt','r') as f:
    for i in range(8):
        try:
            poper[0]=int(f.read())
        except:
            pass
        for j in range(8):
            try:
                if brr[i][j] == baza[i][j]:
                    poper[i] += 1
            except:
                pass
try:
    del f
except:
    pass
f=open('baza.txt','r')
poper[0]=int(f.read())
f.close()
f=open('baza.txt','w')
f.write(str(poper[0]+1))
q=''
u=''
kl=brr[poper[0]-1]
print(kl[0],kl[1])
