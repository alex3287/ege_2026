from itertools import combinations

def F(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 35
    A = a1 <= x <= a2
    return A and not (P or Q)

Ox = [i/4 for i in range(11*4, 36*4+1)]
arr = []

for a1, a2 in combinations(Ox, 2):
    if all(F(x)==0  for x in Ox):
        arr.append(a2-a1)

print(max(arr))

