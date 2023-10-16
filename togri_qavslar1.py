s=str(input())
a=s.count("(")
b=s.count(")")
ochish=0
yopish=0
for i in range(len(s)):
  if s[i]=="(":
    ochish+=i
  elif s[i]==")":
    yopish+=i
if a==b and ochish<yopish:
  print("TRUE")
else:
  print("FALSE")
