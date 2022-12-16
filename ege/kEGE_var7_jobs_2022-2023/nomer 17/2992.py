with open('17 (3).txt') as f:
    s = [int(i.strip()) for i in f.readlines()]
    nai = 0
    for i in s[::-1]:
        if i % 107 == 0:
            nai = max(i, nai)


    def F(n):
        s = ''
        while n > 0:
            s += str(n % 7)
            n //= 7
        return s[::-1]


    pairs = []
    for k in range(len(s) - 1):
        if (F(s[k]).count('36') or F(s[k + 1]).count('36')) and (s[k] > nai or s[k + 1] > nai):
            pairs.append(s[k] + s[k + 1])
    print(len(pairs), min(pairs))
