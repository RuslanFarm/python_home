s = [int(z) for z in open('17-8.txt')]
def f(n):
    k = bin(n)[2:]
    if k.count('1') > 5 and (k.count('1') % 2 != 0):
        return True

sp = []
for i in range(len(s)-1):
    if f(s[i]) or f(s[i+1]):
        sp.append(s[i] + s[i+1])
print(len(sp), max(sp))