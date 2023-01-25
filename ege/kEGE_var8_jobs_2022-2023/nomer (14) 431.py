def f(n):
    s = ''
    while n > 0:
        s += str(n%7)
        n//= 7
    return s[::-1]
for x in range(100):
    if sum([int(i) for i in f(3 * 7**(x+1) + 13 * 7**(x+2) + 31* 7**(3*x) + 7**(2*x))]) == 18:
        print(x)
        break