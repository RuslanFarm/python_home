#https://youtu.be/4S8j8t34vG0
with open('27-75b.txt') as f:
    n = int(f.readline())
    summa, maxsum, len_sp, cor_maxsum, cor_len = 0, 0, 0, 0, 0
    ostatki = 43 * [0]
    sp_sum = 43 * [100000000000]
    for i in range(n):
        summa += int(f.readline())
        ost = summa % 43
        if ost == 0:
            maxsum = ost
            len_sp = i
        else:
            cor_maxsum = summa - sp_sum[ost]
            cor_len = i - ostatki[ost]
            if cor_maxsum > maxsum or(cor_maxsum == maxsum and cor_len < len_sp):
                maxsum = cor_maxsum
                len_sp = cor_len
        if summa < sp_sum[ost]:
            sp_sum[ost] = summa
            ostatki[ost] = i
    print(len_sp)



