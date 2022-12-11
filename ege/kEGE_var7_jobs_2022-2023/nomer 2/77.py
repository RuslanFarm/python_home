print('x', 'y', 'z', 'w', '  F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or (y and (not z))) and (not w)) == 0 and (x+y+z+w == 2) and (x+y == 0):
                    print(x,y,z,w, " ", 0)
                if ((x or (y and (not z))) and (not w)) == 1 and (x+y+z+w == 1):
                    print(x,y,z,w, " ", 1)