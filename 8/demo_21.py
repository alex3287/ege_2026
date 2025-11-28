# ABC = 'ШКОЛА'
# cnt = 0
# for a in ABC:
#     for b in ABC:
#         for c in ABC:
#             word = a+b+c
#             if word.count('К') == 1:
#                 print(word)
#                 cnt += 1
# print(cnt)

from itertools import product

ABC = 'ШКОЛА'
cnt = 0

for i in product(ABC, repeat=3):
    word = ''.join(i)
    if word.count('К') == 1:
        print(word)
        cnt += 1
print(cnt)
