def F(start, finish):
    if start == finish:
        return 1
    if start > finish or start == 11:
        return 0
    return F(start+1, finish) + \
        F(start*2, finish) + \
        F(start**2, finish)

print(F(2, 20))