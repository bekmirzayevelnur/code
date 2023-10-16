N = int(input())
def g(n, current, open_count, close_count, result):
    if open_count == n and close_count == n:
        result.append(current)
        return
    if open_count < n:
        g(n, current + '(', open_count + 1, close_count, result)
    if close_count < open_count:
        g(n, current + ')', open_count, close_count + 1, result)
parentheses = []
g(N, '', 0, 0, parentheses)

for p in parentheses:
    print(p)
