a=int(input())
b=input()
isdig=0
small=0
big=0
symbol=0
for i in range(len(b)):
    if b[i].isdigit():
        isdig+=1
    elif 96 < ord(b[i]) and ord(b[i]) < 123:
        small+=1
    elif 64 < ord(b[i]) and ord(b[i]) < 91:
        big+=1
    else:
        symbol+=1
errors=0
if isdig==0:
    errors+=1
if small==0:
    errors+=1
if big==0:
    errors+=1
if symbol==0:
    errors+=1
if len(b)+errors<6:
    errors+=(6-(len(b)+errors))
print(errors)
