for a in range(100, 1, -1):
    f = 1
    for x in range(1,100):
        for y in range(1, 100):
            f*= ((x>a) or (y>a) or (y - 2*x +11 != 0))
    if f:
        print(a)
        break
