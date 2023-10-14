a,b=map(int,input().split())
tvi=(10000*a)/b**2
if tvi<16:
  print("Yuqori vazn yetishmasligi")
elif 16<=tvi<18.5:
  print("Vazn yetishmasligi")
elif 18.5<=tvi<=25:
  print("Ideal vazn")
elif 25<tvi<=30:
  print("Ortiqcha vazn")
elif 30<tvi<=35:
  print("Semizlikning I darajasi")
elif 35<tvi<=40:
  print("Semizlikning II darajasi")
elif tvi>40:
  print("Semizlikning III darajasi")
else:
  print()
