a=float(input())
if a%100==0:
  if a%400==0:
    print("Kabisa yili")
  else:
    print("Kabisa yili emas")
elif (a%4==0):
  print("Kabisa yili")
else:
    print("Kabisa yili emas")
