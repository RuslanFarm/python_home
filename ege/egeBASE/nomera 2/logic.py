print("d",'m','z','r')
for d in range(2):
    for m in range(2):
        for z in range(2):
            for r in range(2):
                f = 1
                if (  ((d * (not (m and z))) and (not m == r)) and ((d==m)<=((not r) or (z<=m)) ) ) == 1:
                    print(d,m,z,r)