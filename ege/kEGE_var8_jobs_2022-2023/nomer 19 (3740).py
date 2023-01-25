from functools import*
#4599
def moves(h):
    a = h
    for i in range(a,a**2, a):
        return (a*i)
    return (a+2),(a+10)

@lru_cache(None)

def game(h):
    a = h
    if a >= 166: return 'w'
    if any(game(i)=='w' for i in moves(h)): return 'p1'
    if all(game(i)=='p1' for i in moves(h)): return 'v1'
    if any(game(i)=='v1' for i in moves(h)): return 'p2'
    if all(game(i)=='p1' or game(i)=='p2' for i in moves(h)): return 'v2'
for s in range(1,166):
    h = s
    if game(h):
        print(s, game(h))