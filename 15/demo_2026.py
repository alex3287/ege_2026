from itertools import combinations

def F(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return (P) <= ((Q and (not A)) <= (not P))

Ox = [i/4 for i in range(24*4, 116*4+1)]
arr = []

for a1, a2 in combinations(Ox, 2):
    if all(F(x)==1 for x in Ox):
        arr.append(a2-a1)

print(arr)
print(min(arr))