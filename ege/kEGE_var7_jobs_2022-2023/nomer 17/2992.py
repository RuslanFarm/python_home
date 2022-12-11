def f(n):
    s = ''
    while n > 0:
        if s.count('36'):
            return True
        s += str(n % 7)
        n //= 7


with open('17 (3).txt') as f:
    pairs = []
    file = [int(i.strip()) for i in f.readlines()]
    maa = 0
    for i in range(len(file)):
        if file[i] % 107 == 0:
            maa = max(maa, file[i])
    for k in range(len(file) - 1):
        if (file[k] > maa or file[k+1] > maa) and f(file[k]) and f(file[k+1]):
            pairs.append(file[k] + file[k+1])


