
k = set()
for a in range(1000):
    f = 1
    for x in range(1000):
        for y in range(100):
            f*=(((x>8)<=((x**2 + 3*x) >= a)) and (((y**2+5*y)>a) <= (y>=4)))
    if f:
        k.add(a)
print(len(k))