def f(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]

for i in range(1, 344):
    n = f(i)
    n += n[-1]
    n = bin(int(n, base = 6))[2:]
    n += n[-1]
    if int(n, base =2) < 344:
        print(int(n, base =2))