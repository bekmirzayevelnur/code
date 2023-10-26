def next_lexicographically_greater_string(s):

    n = len(s)

    # Step 1

    i = n - 2

    while i >= 0 and s[i] >= s[i + 1]:

        i -= 1

    if i < 0:

        return "no answer"

    # Step 2

    j = n - 1

    while j > i and s[j] <= s[i]:

        j -= 1

    # Step 3

    s_list = list(s)

    s_list[i], s_list[j] = s_list[j], s_list[i]

    # Step 4

    s_list[i + 1:] = sorted(s_list[i + 1:])

    return "".join(s_list)

n = int(input())

for i in range(n):

    s = input()

    print(next_lexicographically_greater_string(s))
