from itertools import product

# ABC = 'ЛЕМУР'
# ABC =''.join(sorted(ABC))
# print(ABC)
ABC = 'ЕЛМРУ'
cnt = 0
# for a in ABC:
#     for b in ABC:
#         for c in ABC:
#             for d in ABC:
#                 word = a+b+c+d
#                 cnt += 1
#                 if word[0] == 'Л':
#                     print(cnt, word)

for i in product(ABC, repeat=4):
    word = ''.join(i)
    cnt += 1
    if word[0] == 'Л':
        print(cnt, word)