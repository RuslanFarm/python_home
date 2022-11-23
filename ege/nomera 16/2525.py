def f(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        return 2 * n + f(n - 1)
    else:
        return 4 * n + 2 * f(n - 2)
print(f(12) * 3600)