F1 = 0
F2 = 1
S=0
For i in range (0,n+1):
    F3 = F1 + F2
    F1 = F2 
    F2 = F3
if (i%2==0):
     S += F2
