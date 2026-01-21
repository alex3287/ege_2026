def F(start, finish):
    if start == finish:
        return 1
    if start < finish or start == 7:
        return 0
    return F(start-1, finish) + \
        F(start-4, finish) +\
        F(start//3, finish)


print(F(19, 13) * F(13, 2))

