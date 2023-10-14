s = input()
prefixes = set()
for i in range(len(s)):
    prefixes.add(s[0:i+1])
print(len(prefixes))
