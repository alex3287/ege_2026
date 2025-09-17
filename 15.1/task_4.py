from itertools import combinations

def F(x):
    P = 10 <= x <= 20
    Q = 15 <= x <= 28
    A = a1 <= x <= a2
    return (A and not P) <= Q

Ox = [i/4 for i in range(9*4, 29*4+1)]
arr = []

for a1, a2 in combinations(Ox, 2):
    if all(F(x)==1  for x in Ox):
        arr.append(a2-a1)

print(max(arr))

