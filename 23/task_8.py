def com_2(num):
    e = num % 10
    d = num // 10
    if e < 9:
        e += 1
    if d < 9:
        d += 1
    return d*10 + e

# print(com_2(29))


def F(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    return F(start+1, finish) + \
        F(com_2(start), finish)


print(F(24, 46))

