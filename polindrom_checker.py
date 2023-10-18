def man(s):
	return s == s[::-1]
s = input()
ans = man(s)
if ans:
	print("Yes")
else:
	print("No")
