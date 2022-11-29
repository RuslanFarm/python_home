from itertools import *
cnt = 0
for x in product("ПИТОН", repeat = 4):
    x = x[0] + x[1] + x[2] + x[3]
    if 'ПТ' in x or 'ПН' in x or 'ТН' in x or "НТ" in x or "ТП" in x or "НП" in x\
        or 'ИО' in x or 'ОИ' in x or 'ПП' in x or 'ТТ' in x or 'НН' in x or 'ОО' in x or 'ИИ' in x:
        continue
    print(x)
    cnt += 1
print(cnt)
