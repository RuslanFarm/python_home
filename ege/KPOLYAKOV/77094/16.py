def f(n):
    if n > 2:
        return f(n-1)+ g(n-2)
    else:
        return n
def g(n):
    if n > 2:
        return g(n-1) + f(n-2)
    else:
        return n+1
print(f(6))