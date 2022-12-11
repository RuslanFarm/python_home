from itertools import *
sp = []
for x in permutations("МИМИКРИЯ"):
    if x not in sp:
        sp.append(x)
print(len(sp))