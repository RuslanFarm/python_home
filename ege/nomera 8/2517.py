from itertools import *
nachalo = "8"
for x in product('0123456789', repeat=6):
    number = nachalo + ''.join(x)
    if '34' not in number:
        if '0' in number:
            for k in range(0,len(number)-1):
                if (int(number[k]) % 2 == 0) and (int(number[k+1]) % 2 == 0)\
                        and (int(number[k]) % 2 != 0) and (int(number[k+1]) % 2 != 0):
                    continue
                print(number)







