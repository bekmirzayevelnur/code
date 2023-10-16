from math import *
v,a,b,c=map(int,input().split())
l=0
while(v>0):
    l+=1
    if(l%3==1):
        v=v-a
    elif(l%3==2):
        v=v-b
    else:
        v=v-c
if(l%3==1):
    print("Azim")
elif(l%3==2):
    print("Aziz")
else:
    print("Akbar")
