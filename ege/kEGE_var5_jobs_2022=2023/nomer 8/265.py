from itertools import *
k = 1
for i in product('АГИЛМОРТ', repeat=4):
    print(k, i)
    k += 1
