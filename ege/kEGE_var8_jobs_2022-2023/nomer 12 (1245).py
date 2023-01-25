
s = '1' * 26 + 54 * '2' + 48 * '3'
while not (s.count('00')):
    s = s.replace('3012', '03', 1)
    s = s.replace('320', '02', 1)
    s = s.replace('210', '01', 1)


# s = s.replace('01', '210', 1)
# s = s.replace('02', '320', 1)
# s = s.replace('03', '3012', 1)
if s[0] == '0' and s[-1] == '0':
    print(s)
