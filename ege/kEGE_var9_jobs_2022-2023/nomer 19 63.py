from functools import*
#4599
def moves(h):
    a, b = h
    return (a+b, b), (a,a+b)

@lru_cache(None)

def game(h):
    a, b = h
    if a + b >= 80: return 'w'
    if any(game(i)=='w' for i in moves(h)): return 'p1'
    if any(game(i)=='p1' for i in moves(h)): return 'v1'
    if any(game(i)=='v1' for i in moves(h)): return 'p2'
    if all(game(i)=='p1' or game(i)=='p2' for i in moves(h)): return 'v2'
for s in range(1,60):
    h = 20, s
    if game(h):
        print(s, game(h))