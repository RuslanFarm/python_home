def f(a,b,c,m):
    if a >= 21 or b >= 21: return c%2==m%2
    if c==m: return 0
    h = [f(a+3,b,c+1,m),f(a,b+3,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(1,20):
    for m in range(1,8):
        if f(3,s,0,m):
            print(s,m)
            break
            # 8 10
            # 4
            # 1, 4, 5,6, 7