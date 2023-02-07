def f(s, e):
    if s > e:
        return 0
    elif s==e:
        return 1
    return f(s - 8, e) + f(s // 2, e)

print(f(102, 5))