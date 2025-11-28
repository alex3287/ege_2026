from itertools import product

ABC = 'АКОРСТ'
cnt = 0

for i in product(ABC, repeat=5):
    word = ''.join(i)
    cnt += 1
    if word[0] not in 'АСТ' and word.count('О') == 2:
        if cnt % 2 == 0:
            print(cnt, word)
