with open('17 (2).txt') as f:
    n = [-int(i.strip().replace('-', '')) if i.startswith('-') else int(i) for i in f.readlines()]
    arifm = sum(n) / len(n)
    pairs = []
    cnt = 0
    for i in range(1, len(n)-2):
        if (n[i] * n[i+1]) > (n[i-1] * n[i+2]):
            pairs.append(n[i]+n[i+1])
            if n[i] > arifm or n[i+1] > arifm:
                cnt += 1
    print(max(pairs), cnt)

