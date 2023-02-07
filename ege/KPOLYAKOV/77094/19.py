from functools import*

def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)


@lru_cache(None)

def game(h):
    a, b = h
    if a + b >= 83: return 'w'
    if any(game(i)=='w' for i in moves(h)): return 'p1'
    if all(game(i)=='p1' for i in moves(h)): return 'v1'
    if any(game(i)=='v1' for i in moves(h)): return 'p2'
    if all(game(i)=='p1' or game(i)=='p2' for i in moves(h)): return 'v2'
for s in range(1,74):
    h = 9, s
    if game(h):
        print(s, game(h))