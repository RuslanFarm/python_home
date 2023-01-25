with open('17 (5).txt') as f:
    n = [int(i) for i in f.readlines()]
    pairs = []
    cnt = 0
    seredina = []
    """for k in range(len(n)):
        if 100 <= abs(n[k]) <= 999:
            cnt += 1
            seredina.append(str(abs(n[k]))[-2])
    for h in range(10):
        print(seredina.count(str(h)), h)""" # 4
    for i in range(len(n)-1):
        if str(n[i])[-1] == '4' or str(n[i+1])[-1] == '4':
            pairs.append(n[i]+n[i+1])
    print(len(pairs), max(pairs))
