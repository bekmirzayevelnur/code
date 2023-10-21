n = int(input())
t = int(input())
games = list(map(int, input().split()))
played_games = 0
total_charge = 0
for game in games:
    total_charge += game
    if total_charge > n:
        break
    played_games += 1
print(played_games)
