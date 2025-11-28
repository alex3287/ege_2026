from itertools import product

ABC = 'ЕЛМРУ'
cnt = 0

for i in product(ABC, repeat=4):
    word = ''.join(i)
    cnt += 1
    if word[0] == 'Л':
        print(cnt, word)

