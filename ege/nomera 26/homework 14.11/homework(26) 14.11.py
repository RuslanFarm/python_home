
a = open('27882 (1).txt').readlines()
bank = int((a[0].split())[0])
a.remove(a[0])
for i in range(len(a)):
    a[i] = int(a[i])
a = sorted(a)
cnt = 0
last = 0
users_data = 0
for k in range(len(a)):
    if users_data + int(a[k]) > bank:
        break
    users_data += int(a[k])
    cnt += 1
print(cnt)
ostatok = (bank - users_data)
print(ostatok)
