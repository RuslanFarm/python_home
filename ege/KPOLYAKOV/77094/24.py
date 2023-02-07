with open('24-221.txt') as f:
    s = f.readline()
    for i in range(2,10):
        s = s.replace(str(i), ' ')
    for i in range(2, 10**4):
        s = s.replace('1'* i, '1')
        s = s.replace('0' * i, '0')
