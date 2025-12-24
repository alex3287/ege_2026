# +2 *2  win >= 100  s1 = 9  1 <= s2 <= 80

# task 19
# def F(s1, s2, pos):
#     if s1+s2 >= 100 and pos == 2: return True  #fixme
#     if s1+s2 < 100 and pos == 2: return False  #fixme
#     if s1+s2 >= 100: return False

    # if pos % 2 == 0:  #fixme
    #     return F(s1+2, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*2, pos+1)
    # return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 23

# task 20
# def F(s1, s2, pos):
#     if s1+s2 >= 100 and pos == 3: return True  #fixme
#     if s1+s2 < 100 and pos == 3: return False  #fixme
#     if s1+s2 >= 100: return False
#
#     if pos % 2 == 1:  #fixme
#         return F(s1+2, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 40 43 44

# task 21
def F(s1, s2, pos):
    if s1+s2 >= 100 and (pos == 2 or pos == 4): return True  #fixme
    if s1+s2 < 100 and pos == 4: return False  #fixme
    if s1+s2 >= 100: return False

    if pos % 2 == 0:  #fixme
        return F(s1+2, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 38 42

for s in range(1, 81):
    if F(9, s, 0):
        print(s)