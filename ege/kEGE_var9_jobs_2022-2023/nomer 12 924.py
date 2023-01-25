a = '1' * 199 + '3' + '3'
while a.count('12') or a.count('13'):
    a = a.replace('12', '21', 1)
    a = a.replace('31', '23', 1)
    a = a.replace('13', '23', 1)

print(a)
s = sum([int(i) for i in a])
print(s)
