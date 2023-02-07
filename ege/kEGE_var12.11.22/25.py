from fnmatch import*
from functools import lru_cache
@lru_cache(None)
def f(x):
    return sum([int(i) for i in str(x)[:len(str(x))//2+1]]) == sum([int(i) for i in str(x)[len(str(x))//2:]])
sp = d =  a = []
for i in range(100_000,160_20000):
    d.append(519*i)
print('ddddddddddd')
for x in range(32540123, 10**13):
    if fnmatch(str(x), '32*54?123') and (str(x).count('0') == 0) and (x in d):
        print(x)
        if f(x) :
            print('YES')
            sp.append(x)
            a.append(x//519)
print(sp)
print('1111')
print(a)
        