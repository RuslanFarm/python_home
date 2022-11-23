def m(n):
    delit = []
    for i in range(2, n):
        if n % i == 0:
            delit.append(i)
    if len(delit) < 5:
        return 0
    else:
        return delit[-5]

counter = []

for k in range(300_000_001, 500_000_000):
    #print(k) #300000003 300000004 300000005 300000006 300000008
    if m(k):
        counter.append(m(k))
    if len(counter) == 5:
        break
print(*sorted(counter), sep='\n')
"""
17
151
1119403
16666667
27272728
"""
