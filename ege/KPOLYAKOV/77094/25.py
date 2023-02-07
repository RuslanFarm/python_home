from functools import lru_cache
@lru_cache(None)
def prost(n):
    a = []
    for i in range(2, n):
        if n % i == 0:
            a.append(i)
    return 
p = [prost(i) for i in range(10)]
print(p)
@lru_cache(None)
def f(n):
    sp = []
    for i in range(1, n//2):
        if n % i == 0:
            sp.append(i)
    return sum(sp)

for i in range(912673, 1, -2):
    if f(i) == 0:
        continue
    if i % f(i) == 0:
        print(i, f(i))
    print(i)
