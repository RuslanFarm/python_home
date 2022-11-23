def f(n):
    if n < 0:
        return 0
    elif n == 5:
        return 1
    else:
        return f(n-1)+f(int(n/2))
print(f(500))
def f(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return f(n - 1) + f(int(n / 2))
print(f(5))