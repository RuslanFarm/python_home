a = 7**103 + 49**98 - 7**120 - 7**33
s = ''
while a > 0:
    s += str(a % 7)
    a //= 7
s = s[::-1]
print(s)
i = 0
while s[i] == '6':
    i += 1
print(len(s) - i)
