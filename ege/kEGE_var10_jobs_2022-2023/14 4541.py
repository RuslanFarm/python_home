a = (7**80 - ((10 - 3) ** 4) + int('234', base=7)) * 40 // 6
print(a)
s = ''
while a > 0:
    s += str(a % 7)
    a = a // 7
print(s.count('4'))