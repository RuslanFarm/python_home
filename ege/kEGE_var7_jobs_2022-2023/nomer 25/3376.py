from itertools import *

f = [['']]
s = [['']]
for i in range(1, 4):
    f += combinations('234', r=i)
    s += combinations('678', r=i)
se = set()
for a, b in product(f, s):
    x = '1' + ''.join(a) + '5' + ''.join(b) + '9'
    se.add(int(x))
for k in sorted(se):
    if k % 21 == 0:
        print(k, k // 21)
