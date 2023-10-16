s=input()
a=0
for i in s:
    if i=='s' or i=='z':
        a+=4
    elif i=='c' or i=='f' or i=='i' or i=='l' or i=='o' or i=='r' or i=='v' or i=='y':
        a+=3
    elif i=='b' or i=='e' or i=='h' or i=='k' or i=='n' or i=='q' or i=='u' or i=='x':
        a+=2
    elif i==' ' or i=='a' or i=='d' or i=='g' or i=='j' or i=='m' or i=='p' or i=='t' or i=='w':
        a+=1
print(a)
