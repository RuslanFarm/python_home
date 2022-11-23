a = open("17.txt")
f = a.readlines()
sp = []
cnt = 0
for i in range(len(f)-1):
    if ((int(f[i]) % 7 == 0 ) and (int(f[i+1]) % 3 != 0)) or (((int(f[i+1]) % 7 == 0) and (int(f[i]) % 3 != 0))):
        cnt += 1
        sp += [int(f[i]) * int(f[i+1])]
print(cnt,min(sp))
