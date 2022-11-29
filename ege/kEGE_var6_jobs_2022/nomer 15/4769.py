for a in range(0, 300):
    f = 1
    for x in range(100):
        for y in range(100):
            f *= ((7 * y + x < a) or (2 * x + 3 * y > 98))
    if f:
        print(a)
        break

