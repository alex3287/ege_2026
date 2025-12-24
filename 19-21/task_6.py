# +1 *4  win >= 108  s1 = 6  1 <= s2 <= 101

#task 19
# def F(s1, s2, pos):
#     if s1+s2 >= 108 and pos == 2: return True  #fixme
#     if s1+s2 < 108  and pos == 2: return False  #fixme
#     if s1+s2 >= 108: return False

    # if pos % 2 == 0: #fixme
    #     return F(s1+1, s2, pos+1) and F(s1*4, s2, pos+1) and F(s1, s2+1, pos+1)and F(s1, s2*4, pos+1)
    # return F(s1+1, s2, pos+1) or F(s1*4, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*4, pos+1)
# 7

#task 20
# def F(s1, s2, pos):
#     if s1+s2 >= 108 and pos == 3: return True  #fixme
#     if s1+s2 < 108  and pos == 3: return False  #fixme
#     if s1+s2 >= 108: return False
#
#     if pos % 2 == 1: #fixme
#         return F(s1+1, s2, pos+1) and F(s1*4, s2, pos+1) and F(s1, s2+1, pos+1)and F(s1, s2*4, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*4, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*4, pos+1)
# 11 25

#task 21
def F(s1, s2, pos):
    if s1+s2 >= 108 and (pos == 2 or pos == 4): return True  #fixme
    if s1+s2 < 108  and pos == 4: return False  #fixme
    if s1+s2 >= 108: return False

    if pos % 2 == 0: #fixme
        return F(s1+1, s2, pos+1) and F(s1*4, s2, pos+1) and F(s1, s2+1, pos+1)and F(s1, s2*4, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*4, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*4, pos+1)
# 11 25

for s in range(1, 102):
    if F(6, s, 0):
        print(s)