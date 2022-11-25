with open('3375.txt') as f:
    x = f.read()
    cnt = 0
    sp = []
    for i in range(0, len(x) - 1, 2):
        if (x[i] == "A" and x[i+1] == "A") or (x[i] == "C" and x[i+1] == "C"):
            cnt += 1
            sp.append(cnt)
        elif (x[i-1] == "A" and x[i] == "A") or (x[i-1] == "C" and x[i] == "C"):
            if x[i-3] != "A" and x[-3] != "B":
                cnt += 1
                sp.append(cnt)
        else:
            cnt = 0


print(max(sp))