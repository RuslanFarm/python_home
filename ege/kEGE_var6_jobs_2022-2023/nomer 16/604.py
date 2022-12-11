k = 0


def f(n):
    global k
    k += (2 * n + 1)
    if n > 1:
        k += 3 * n - 8
        f(n - 1)
        f(n - 4)
    return k


print(f(50))
