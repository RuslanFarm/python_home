k = 1600*1200
alg = 0.2
dop = 100 * 2**13
print(2**(int((k*alg + dop)*32/2**23)))
