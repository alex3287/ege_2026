# -3 -5 //4 win <= 30  s >= 31

# task 19
# def F(s, pos):
#     if s <= 30 and pos == 2: return True  #fixme
#     if s > 30 and pos == 2: return False  #fixme
#     if s <= 30: return False
#
#     if pos % 2 == 0:  #fixme
#         return F(s-3, pos+1) and F(s-5, pos+1) and F(s//4, pos+1)
#     return F(s-3, pos+1) or F(s-5, pos+1) or F(s//4, pos+1)
# 124, 125, 126

# task 20
# def F(s, pos):
#     if s <= 30 and pos == 3: return True  #fixme
#     if s > 30 and pos == 3: return False  #fixme
#     if s <= 30: return False
#
#     if pos % 2 == 1:  #fixme
#         return F(s-3, pos+1) and F(s-5, pos+1) and F(s//4, pos+1)
#     return F(s-3, pos+1) or F(s-5, pos+1) or F(s//4, pos+1)
# 127 128 129 130 131 496

# task 21
def F(s, pos):
    if s <= 30 and (pos == 2 or pos == 4): return True  #fixme
    if s > 30 and pos == 4: return False  #fixme
    if s <= 30: return False

    if pos % 2 == 0:  #fixme
        return F(s-3, pos+1) and F(s-5, pos+1) and F(s//4, pos+1)
    return F(s-3, pos+1) or F(s-5, pos+1) or F(s//4, pos+1)
# 132

for s in range(31, 1000):
    if F(s, 0):
        print(s)