a = (2 ** 345 + 8 ** 65 - 4 ** 130) * (8 ** 123 - 2 ** 89 + 4 ** 45)
s = oct(a)[2:]
cnt = 0
for i in s:
    cnt += int(i)
print(cnt)

print(sum([int(i) for i in oct((2 ** 345 + 8 ** 65 - 4 ** 130) * (8 ** 123 - 2 ** 89 + 4 ** 45))[2:]]))
