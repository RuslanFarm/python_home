sp = []
for x in range(10, 3000):
    i = bin(x - bin(x)[2:].count('0'))[2:]
    i = i[-3] + i[-2] + i[-1] + i
    if int(i, base=2) > 224:
        sp.append(int(i, base =2))
print(min(sp))