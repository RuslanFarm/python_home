s = '>' + '1'*20 + '3' * 40 + '2'*15 + '<'
while s.count("><") == 0:
    s = s.replace(">1", '3>', 1)
    s = s.replace(">2", '2>', 1)
    s = s.replace(">3", '1>', 1)
    s = s.replace("3<", '<1', 1)
    s = s.replace("2<", '<3', 1)
    s = s.replace("1<", '<2', 1)
s = s.replace('><', '')
print(sum([int(i) for i in s]))