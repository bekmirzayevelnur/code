def funk(st):
     print(st)
     if len(st) == 0:  
         return             
     else:      
         funk(st[:-1])   
s=input()
print(funk(s))
