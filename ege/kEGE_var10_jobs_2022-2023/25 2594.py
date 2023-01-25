def f(n):
    s = []
    c = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and i % 2 == 0:
            s.append(i)
            c +=1
    if len(s) == 3 and c == 3:
        return s
    else:
        c = 0
sp = [[], []]
for i in range(113_000_000, 114_000_001):
    if f(i) is not None:
        sp[0].append(i)
        sp[1].append(f(i)[1])
    print(sp[0], sp[1])