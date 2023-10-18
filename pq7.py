s = input()
for i in range(len(s)):
    if s[i] == 'P' or s[i] == 'Q' or s[i] == '7':
        print("yes")
        exit(0)
print("no")
