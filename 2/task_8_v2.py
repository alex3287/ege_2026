from itertools import product, permutations

def F(x, y, z, w):
    return (w == (z <= x)) and y

for a1, a2, a3, a4, a5 in product([0,1], repeat=5):
    table = [(a1, 0, a2, 0), (1, a3, 1, 1), (a4, a5, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [1, 0, 1]:
                print(*p)

A = ['x', 'y', 'z', 'w']
B = [1, 2, 3, 4]

for i in zip(A, B):
    print(i)

D = dict(zip(A, B))
print(D)

def fi(x, y, z, w):
    return x+y+z+w

print(fi(**D))