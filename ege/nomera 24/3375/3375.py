with open('3375.txt') as f:
    x = f.readline()
    cnt = 0
    sp = []
    for i in range(0, len(x) - 1, 2):
        if (x[i] == "A" and x[i+1] == "A") or (x[i] == "C" and x[i+1] == "C"):
            cnt += 1
            sp.append(cnt)
        else:
            cnt = 0

print(max(sp))