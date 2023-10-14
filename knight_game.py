def play_game(n):
    if n % 2 == 1:
        return 0
    else:
        return 1
T = int(input())
for _ in range(T):
    n = int(input())
    result = play_game(n)
    print(result)
