for n in range(100):
    i = bin(n)[2:]
    s = sum([int(k) for k in i])
    if s % 2 == 0:
        i = i + '0'
        i.replace(i[:2], '10', 1)
    else:
        i = i + '1'
        i.replace(i[:2], '11', 1)
    if int(i, base=2) > 40:
        print(n)
        break
