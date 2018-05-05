def avocado(history, spoon, depth=10, move=True):
    if len(history) == 0: return 0
    elif spoon < 0: return 157
    n = history[-1]
    moves = (next((x for x in range(n-1, 1, -1) if n%x==0), n), n**2 % 256, n-spoon, (n+spoon)%256)
    if n < 0 or len(history) != len(set(history)): return 1
    elif depth == 0: return 0
    elif not move: return max(-avocado(history+[x],spoon,depth-1,False) for x in moves)
    scores = [-avocado(history+[x],spoon,depth-1,False) for x in moves]
    return next(x for x in (1, 2, 3, 0) if scores[x] == max(scores))
