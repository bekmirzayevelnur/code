def sarvar_tpy(s):
    p={"+":1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": 0}
    a={"^"}
    l=[]
    ops = ["+", "-", "*", "/", "(", ")", "^"]
    res=""
    for i in s:
        if i in ops:
            if i == "(":
                l.append(i)
            else:
                while l and (p[l[-1]]>p[i] or p[l[-1]]==p[i] and i not in a
                ):
                    res+= l.pop()
                if i == ')':
                    l.pop()
                else:
                    l.append(i)
        else:
            res+= i

    while l:
        res+= l.pop()
    return res
s=str(input())
print(sarvar_tpy(s))
