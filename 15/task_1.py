# not, and, or, <=, ==
for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        F = ((x % A == 0) and (x % 21 == 0)) <= (x % 18 == 0)
        if F == 0:
            flag = 0
            break
    if flag == 1:
        print(A)