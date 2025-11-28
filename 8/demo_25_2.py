from itertools import product

ABC = '0123456789AB'
cnt = 0

for i in product(ABC, repeat=5):
    word = ''.join(i)

    cnt_9 = word.count('9')
    cnt_a = word.count('A')
    cnt_b = word.count('B')
    suma = cnt_9 + cnt_a + cnt_b

    if word[0] != '0' and word.count('7') == 1 and suma < 4:
        print(word)
        # input()
        cnt += 1
print(cnt)