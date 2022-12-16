with open('24 (4).txt') as f:
    f = f.readline().strip()
    words = {'AB', "CB", "BC", "BA"}
    cnt = 0
    sp = 0
    for i in range(len(f)):
        if f[i:i+2] in words:
            cnt += 1
        else:
            cnt = 0
        sp = max(sp, cnt)
    print(sp)
