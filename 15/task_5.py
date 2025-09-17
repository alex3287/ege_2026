# not, and, or, <=, ==
for A in range(1, 500):
    flag = 1
    for x in range(1, 500):
        for y in range(1, 500):
            F = (y + 2*x < A) or (x > 20) or (y > 30)
            if F == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        print(A)