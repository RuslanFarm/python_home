def f(st, s, ex):
    if st > s or st == ex:
        return 0
    elif st == s:
        return 1
    else:
        return f(st + 1, s, ex) + f(st + 2, s, ex)


print(f(11, 17, 0) * f(17, 23, 0) * f(23, 29, 0))
print(f(11, 23, 17) * f(23, 29, 0))
print(f(11, 17, 0) * f(17, 29, 23))
print(2197 + 832 + 832)
