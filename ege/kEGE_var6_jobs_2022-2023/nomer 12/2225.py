for x in range(100, 200):
    s = '5' * x
    while s.count('555') or s.count('888'):
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    if s.count('8') == 0:
        print(x)
        break


