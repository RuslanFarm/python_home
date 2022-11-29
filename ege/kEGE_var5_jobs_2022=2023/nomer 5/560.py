for n in range(1, 100):
    i = n
    b = bin(i)[2:]  # 1
    b = b + b[-1]  # 2
    if b.count('1') % 2 == 0:  # 3
        b = b + '0'  # 3
    else:  # 3
        b = b + '1'  # 3
    if b.count('1') % 2 == 1:  # 4
        b = b + '1'  # 4
    R = int(b, base=2)
    if R > 105:
        print(R)
        break
