for a in range(1, 100):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            f*= (((x % a == 0) and (not (x%50 == 0))) <= (not(x % 18 == 0) or (x % 50 == 0)))
    if f:
        print(a)
        break