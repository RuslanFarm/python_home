s = '1' * 50 + '2' * 50 + "3" * 50
while s.count('21') or s.count('31') or s.count('23'):
    if s.count('21'):
        s = s.replace('21', '12', 1)
    if s.count('31'):
        s = s.replace('31', '13', 1)
    if s.count('23'):
        s = s.replace('23', '32', 1)
print(s[9], s[89], s[129])