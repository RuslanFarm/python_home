sp = []
ost = []
if int('1245') % 51 == 0:
    sp.append(int('1245'))
    ost.append(int(int('1245') / 51))

if int('124500') % 51 == 0:
    sp.append(int('124500'))
    ost.append(int(int('124500') / 51))

if int('120045') % 51 == 0:
    sp.append(int('120045'))
    ost.append(int(int('120045')) / 51)

for i in range(100):
    if int('12' + str(i) + '45') % 51 == 0:
        sp.append(int('12' + str(i) + '45'))
        ost.append(int(int('12' + str(i) + '45') / 51))

for i in range(100):
    if int('1245' + str(i)) % 51 == 0:
        sp.append(int('1245' + str(i)))
        ost.append(int(int('1245' + str(i)) / 51))

for i in range(10):
    for j in range(10):
        if int('12' + str(i) + '45' + str(j)) % 51 == 0:
            sp.append(int('12' + str(i) + '45' + str(j)))
            ost.append(int(int('12' + str(i) + '45' + str(j)) / 51))

print(sorted(sp), sorted(ost), sep='\n')
