ostatki = []
base = []

for i in range(10):
    for j in range(10):
        if int('12345'+ str(i) + '7' + str(j) + "8") % 23 == 0:
            base.append(int('12345' + str(i) + '7' + str(j) + "8"))
print(*base, sep = '\n')
for x in range(len(base)):
    ostatki.append(int(base[x] / 23))
print(ostatki)
