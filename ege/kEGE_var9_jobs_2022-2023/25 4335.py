from fnmatch import*
def prime(n):
    s = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s.append(i)
    s.append(n)
    if len(s) == 2:
        return True

def pri(n):
    s = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 and prime(i) and fnmatch(str(i), '*3'):
            s.append(i)
    if len(s) >= 3:
        return s

for i in range(960_000, 9999999999999):
    if pri(i):
        print(sum(pri(i)), i)

