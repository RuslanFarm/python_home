for i in range(203):
    s =  '1' * i + '2' + '1' * (203-i)
    while s.count('111') or s.count('222'):
        if s.count('111'):
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)
    if len(s) > 6:
        print(s)