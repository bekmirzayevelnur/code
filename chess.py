def possible_moves(n, m):
    moves = []
    x, y = n, m
    dit = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
    for a in dit:
        move = (x + a[0], y + a[1])
        if move[0] < 1 or move[0] > 8 or move[1] < 1 or move[1] > 8:
            continue
        moves.append(move)
    return moves
a,b=map(int,input().split())
c=list(possible_moves(a,b))
print(len(c))
