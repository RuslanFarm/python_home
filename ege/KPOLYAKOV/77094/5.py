for n in range(499, 1, -1):
    i = bin(n)[2:]
    for k in range(3):
        if i.count('1') == i.count('0'):
            i = i + i[-1]
        else:
            if i.count('1') > i.count('0'):
                i = i + '0'
            else:
                i = i + '1'
    i = int(i, 2)
    if (i % 4 == 0 )and (i % 8 != 0):
        print(n, i)
        break
