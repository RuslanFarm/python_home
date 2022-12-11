with open('24 (4).txt') as f:
    f = f.readline().replace('AB', "*").replace('CB', "*").replace('BC', "*").replace('BA', "*")
    cnt = 0
    sp = []
    for i in f:
        if i == "*":
            cnt += 1
        else:
            cnt = 0
        sp.append(cnt)
    print()