for i in range(100_000, 1_000_000):
    n = str(i)
    new = str(int(n[0]) + int(n[1])) + str(int(n[2]) + int(n[3])) + str(int(n[4]) + int(n[5]))
    dv = bin(int(new))[2:]
    if dv[-1] == "0":
        dv = dv + "0"
    else:
        dv = dv + "1"
    if int(dv, 2) == 1519:
        print(i)
        break
