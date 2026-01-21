def F(start, finish):
    if start == finish:
        return 1
    if start > finish or start == 21:
        return 0
    return F(start+1, finish) + \
        F(2*start+1, finish)



print(F(1, 25))

