for a in range(1, 100):
    f = 1
    for x in range(1, 100):
        f *= ((x % a == 0) <= ((x % 28 != 0) or (x % 42 == 0)))
    if f:
        print(a)
        break
