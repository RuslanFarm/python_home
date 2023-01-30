from functools import lru_cache
import sys
sys.setrecursionlimit(2**23)
@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return f(n-1) * 3**(n%5)/3**(n%7)
for i in range(1, 1032-1):
    f(i)
print(f(1025), f(666), f(1027), f(1028), f(1029))