a=input()
b,d=map(int,input().split(':'))
c=input()
j={'Andijon':-12,'Angren':-3,"Farg'ona":-10,'Namangan':-9,'Buxoro':20,'Jizzax':7,'Navoiy':17,
   'Qashqadaryo':14,'Samarqand':10,'Sirdaryo':3,'Surxondaryo':11,'Xorazm':35
     ,"Qoraqalpog'iston":36,'Toshkent':0}
h=b*60+d
f=h-j[a]+j[c]
k=f-((f//60)*60)
if len(str(k))>1:
   print('0'+str(f//60)+':'+str(k))
else:
    print('0'+str(f//60)+':0'+str(k))
