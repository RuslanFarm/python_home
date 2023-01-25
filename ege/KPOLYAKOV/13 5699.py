def f(n, e):
    if e == n[-1] and len(n) > 1:
        return 1
    elif n[-1] in n[:-1]:
        return 0
    return sum([f(n + c, e) for c in d[n[-1]]])

s = 'АБ БВ ВЕГЖ ГЕД ДЕЖК ЕЖ ЖНЗ ЗЛКД ЛМ КЛ МАНЗ НАБВ'
d = {x[0]: x[1:] for x in s.split()}

print(f("Ж", "Ж"))
