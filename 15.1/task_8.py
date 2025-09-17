from itertools import combinations

def F(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not R)) and A and (not P)


Ox = [i/4 for i in range(9*4, 41*4)]

arr = []
for a1, a2 in combinations(Ox, 2):
    if all(F(x) == 0 for x in Ox):
        arr.append(a2-a1)

print(max(arr))