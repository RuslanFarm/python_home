from functools import *
@lru_cache(None)
def f(n):
    if n < 3: return n+1
    elif n >= 3 and n % 2 == 0:
        return f(n-2) + n - 2
    #elif n >= 3 and n % 2 != 0:
    #   return f(n+2) + n + 2
cnt = 0
for i in range(1, 5600):
    if len(str(f(i))) == 5:
        cnt += 1
print(cnt)