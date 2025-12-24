# +2 *3  47 <= win <= 59  s1 = 5  1 <= s2 <= 41

# task 19
# def F(s1, s2, pos):
#     if 47 <= s1+s2 <= 59 and pos == 2: return True  #fixme
#     if s1+s2 > 59 and pos == 1: return True  #fixme
#     if s1+s2 < 47  and pos == 2: return False  #fixme
#     if s1+s2 >= 47: return False
#
#     if pos % 2 == 0: #fixme
#         return F(s1+2, s2, pos+1) and F(s1*3, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*3, pos+1)
#     return F(s1+2, s2, pos+1) or F(s1*3, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*3, pos+1)
# 2

# task 20
# def F(s1, s2, pos):
#     if 47 <= s1+s2 <= 59 and pos == 3: return True  #fixme
#     if s1+s2 > 59 and pos == 2: return True  #fixme
#     if s1+s2 < 47  and pos == 3: return False  #fixme
#     if s1+s2 >= 47: return False
#
#     if pos % 2 == 1: #fixme
#         return F(s1+2, s2, pos+1) and F(s1*3, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*3, pos+1)
#     return F(s1+2, s2, pos+1) or F(s1*3, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*3, pos+1)
# 1 29
# task 21
def F(s1, s2, pos):
    if 47 <= s1+s2 <= 59 and (pos == 2 or pos ==4): return True  #fixme
    if s1+s2 > 59 and (pos == 1 or pos == 3): return True  #fixme
    if s1+s2 < 47  and pos == 4: return False  #fixme
    if s1+s2 >= 47: return False

    if pos % 2 == 0: #fixme
        return F(s1+2, s2, pos+1) and F(s1*3, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*3, pos+1)
    return F(s1+2, s2, pos+1) or F(s1*3, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*3, pos+1)

for s in range(1, 42):
    if F(5, s, 0):
        print(s)