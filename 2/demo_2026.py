print('x y z w')
for x in range(2):
    for y in 0, 1:
        for z in range(2):
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
