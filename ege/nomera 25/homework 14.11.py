def m(n):
    delit = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            delit.add(i)
            delit.add(n//i)
    return sorted(list(delit))
maxx = []
print(m(48))
print(len(m(48)))
for i in range(84052, 84131):
    if i == 84084:
        print(i, m(i))
        print(len(m(i)))
