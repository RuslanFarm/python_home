"""
def f(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]


cnt = 0
for i in range(10_000, 100_000):
    if f(i)[-1] != '8' and f(i)[-1] != '1' and f(i)[-1] != '3' and f(i)[-1] != '5' and \
            f(i)[-1] != '7' and f(i)[-1] != '8' and f(i).count('3') == 1:
        cnt += 1
print(cnt)

# 11
id = 32
alf = 63 + 10
i = 7
base = id * i / 8
print(base)
print(3840*base/2**10)

#12
s = '>' + '1' * 25 + '2' * 17 + '3' * 10
while s.count('>1') or s.count('>2') or s.count('>3'):
    if s.count('>1'):
        s = s.replace(">1", '22>3', 1)
    if s.count('>2'):
        s = s.replace('>2', '2>', 1)
    if s.count(">3"):
        s = s.replace(">3", '11>2', 1)
s = s.replace('>','')
print(s)
print(sum([int(i) for i in s]))

#14
maxx = -999999
for i in range(80):
    if (3*80**3 + i * 80**2 + 7 * 80 + 5 + 1 * 80**3 + 4 * 80**2 + i * 80) % 17 == 0:
        maxx = max(maxx, i)
print(maxx)
print((3*80**3 + 64 * 80**2 + 7 * 80 + 5 + 1 * 80**3 + 4 * 80**2 + 64 * 80) / 17)
"""
#15
for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        f *=(((x % 6 == 0) <= (x % 10 != 0)) or (x + a > 121))
    if f:
        print(a)
        break
"""
#16
def f(n):
    if n == 1:return 1
    if n > 1:
        return n*f(n-1)-1
print(f(1000) / f(997))

with open('17 (4).txt') as f:
    nums = [int(i) for i in f.readlines()]
    mm = min(nums)
    ma = -88888
    cnt = 0
    for i in range(len(nums) - 1):
        if nums[i] % 117 == mm or nums[i + 1] % 117 == mm:
            ma = max(ma, nums[i] + nums[i + 1])
            cnt += 1
    print(cnt, ma)
"""
