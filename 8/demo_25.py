from itertools import product

ABC = '0123456789AB'
cnt = 0

for i in product(ABC, repeat=5):
    number = ''.join(i)
    cnt_9 = number.count('9')
    cnt_a = number.count('A')
    cnt_b = number.count('B')
    suma = cnt_9 + cnt_a + cnt_b
    if number[0] != '0' and number.count('7') == 1:
        if suma < 4:
            print(number)
            cnt += 1
        # input()
print(cnt)