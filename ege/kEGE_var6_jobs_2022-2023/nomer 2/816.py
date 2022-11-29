print('x', 'y', 'z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x==(y<=z))) == 1 and ((x + y + z) == 1):
                print(x,y,z,1)
            if (not(x==(y<=z))) == 0 and ((x + y + z) == 2):
                print(x,y,z,0)




