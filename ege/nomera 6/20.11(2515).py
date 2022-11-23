for s in range(5,100):
    k = s
    n = 5
    while n > 1:
        n -= 1
        s = (s*3)/(n*2)
    if s > 5:
        print(k, s)