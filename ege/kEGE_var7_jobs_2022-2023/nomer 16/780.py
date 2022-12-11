def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n-1) + 2
print(f(50))
for i in range(51):
    print(i, f(i))


