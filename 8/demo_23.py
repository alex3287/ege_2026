from itertools import product

ABC = '01234567'
cnt = 0

for i in product(ABC, repeat=5):
    number = ''.join(i)

    if number[0] != '0' and number.count('6') == 1:
        number = number.replace('3', '1').replace('5','1').replace('7','1')
        if number.count('16') + number.count('61') == 0:
            print(number)
            cnt += 1

print(cnt)