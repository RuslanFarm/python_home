def f(s,fi):
    if s>fi: return 0
    elif s == fi: return 1
    return f(s*3, fi) + f(s-3, fi)
print(f(3,30))