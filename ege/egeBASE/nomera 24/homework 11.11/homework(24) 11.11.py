a = open('24 (1).txt').readline()
a = a.replace('D', 'C')
a = a.replace('F', 'C')
a = a.replace('O', 'A')
a = list(a)

cnt = 0
sp = []
for i in range(0, len(a)-1, 2):
    if a[i] == "C" and a[i+1] == "A":
        cnt += 1
        sp.append(cnt)
    else:
        cnt = 0
print(max(sp))#95