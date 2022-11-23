a = open('inf_26_04_21_24 (1).txt').readlines()
print(a)
maxx = 0
for i in range(len(a)): #Проходим по строкам
    if a[i].count("G") < 25:
        for j in range(len(a[i])-1): #Проходим по буквам
            for k in range(j+1, len(a[i])): #Проходим по следующим буквам до конца пока не встретим совпадение
                if a[i][j] == a[i][k]:
                    maxx = max(maxx, abs(k-j))
print(maxx)
