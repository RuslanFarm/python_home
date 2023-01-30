s = '1' * 32 + '3' + '1' + "2" *32 +  '2'
while s.count('11') or s.count('22') or s.count('13') or s.count('23'):
    s = s.replace('11', '2', 1)
    s = s.replace('22', '1', 1)
    s = s.replace('13', '2', 1)
    s = s.replace('23', '1', 1)
print(s)
print(sum([int(i) for i in s]))