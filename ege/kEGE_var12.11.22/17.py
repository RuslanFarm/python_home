s = [int(i) for i in open('17 (8).txt')]
arif = (max(s) + min(s)) // 2
sp = []
for i in range(len(s)):
    p1 = s[i]
    p2 = s[-i]
    if (p1 < arif and p2 > arif):
        sp.append(p1+p2)

print(len(sp), max(sp))

