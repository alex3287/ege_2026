# (), not, and, or, <=, ==
for A in range(500):
    flag = 1
    for x in range(1, 500):
        for y in range(1, 500):
            F = (x + y <= 30) or (y <= x + 2) or (y >= A)
            if F == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        print(A)