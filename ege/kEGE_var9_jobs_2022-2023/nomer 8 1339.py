from itertools import*
c = 0
s = []
for i in permutations('МАРИ', r= 4):
    i = [*i]
    for j in product('ИНА', repeat = 4):
        j = [*j]
        s.append(i+j)
s = sorted(s)
a = ['М', 'А', 'Р', 'И', 'А', 'Н', 'Н', 'А']
for i in s:
    c += 1
    if i == a:
        print(c)
