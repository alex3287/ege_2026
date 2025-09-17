from itertools import combinations

def F(x):
    P = 13 <= x <= 21
    Q = 17 <= x <= 30
    R = 24 <= x <= 38
    A = a1 <= x <= a2
    return (not (Q <= (P or R))) <= ((not A) <= (not Q))


Ox = [i/8 for i in range(12*8, 39*8)]

arr = []
for a1, a2 in combinations(Ox, 2):
    if all(F(x) == 1 for x in Ox):
        arr.append(a2-a1)

print(min(arr))