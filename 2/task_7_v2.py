from itertools import product, permutations

def F(x, y, z, w):
    return ((y <= x) or (not z and w)) == (w == x)

for a1, a2, a3 in product([0,1], repeat=3):
    table = [(a1, 1, 0, 0), (0, 0, 0, 1), (0, 1, a2, a3)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p)
