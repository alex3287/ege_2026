# +1 * 2  win >= 129  1 <= s <= 128

# task 19
# def F(s, pos):
#     if s >= 129 and pos == 2: return True  #fixme
#     if s < 129 and pos == 2: return False  #fixme
#     if s >= 129: return False
#
#     if pos % 2 == 0:  #fixme
#         return F(s+1, pos+1) and F(s*2, pos+1)
#     return F(s+1, pos+1) or F(s*2, pos+1)
# 64

# task 20
# def F(s, pos):
#     if s >= 129 and pos == 3: return True  #fixme
#     if s < 129 and pos == 3: return False  #fixme
#     if s >= 129: return False
#
#     if pos % 2 == 1:  #fixme
#         return F(s+1, pos+1) and F(s*2, pos+1)
#     return F(s+1, pos+1) or F(s*2, pos+1)
# 32 63

# task 21
def F(s, pos):
    if s >= 129 and (pos == 2 or pos == 4): return True  #fixme
    if s < 129 and pos == 4: return False  #fixme
    if s >= 129: return False

    if pos % 2 == 0:  #fixme
        return F(s+1, pos+1) and F(s*2, pos+1)
    return F(s+1, pos+1) or F(s*2, pos+1)
# 62

for s in range(1, 129):
    if F(s, 0):
        print(s)