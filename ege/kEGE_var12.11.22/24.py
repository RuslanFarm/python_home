with open('24 (8).txt') as f:
    s = f.readline()
    comb = ['AAA', 'BBB', 'CCC', "DDD", "EEE", "FFF"]
    c = 0
    sp = []
    for i in range(0,len(s),3):
        if s[i:i+3] in comb:
            c += 1
        else:
            sp.append(c)
            c = 0
print(max(sp))