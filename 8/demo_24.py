from itertools import product

ABC = '0234567'
cnt = 0

for i in product(ABC, repeat=5):
    word = ''.join(i)
    unique =set(word)
    if word[0] != '0' and len(unique) == 5:
        word = word.replace('5', '3').replace('7', '3')
        word = word.replace('0', '2').replace('4', '2').replace('6', '2')
        if '22' not in word and '33' not in word:
            print(word)
            cnt += 1

print(cnt)