def f(n):
    print(2*n+1)
    if n > 1:
        print(3*n - 8)
        f(n-1)
        f(n-4)
print(sum(f(50)))
