def f(n, e):
    if e == n[-1] and len(n) > 1 and 'Б' in n:
        return 1
    elif n[-1] in n[:-1]:
        return 0
    return sum([f(n + c, e) for c in d[n[-1]]])

s = 'АВ БАД ВБЕ ГВБД ДЗ ЕЖ ЖКГ ЗГЖ КЗ'
d = {x[0]: x[1:] for x in s.split()}

print(f("Г", "Г"))
