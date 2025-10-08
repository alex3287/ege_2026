from string import ascii_uppercase

ABC = '0123456789' + ascii_uppercase[:19]
# print(len(ABC), ABC)
for x in ABC:
    number_1 = f'923{x}874'
    number_2 = f'524{x}6152'
    suma = int(number_1, 29) + int(number_2, 29)
    if suma % 28 == 0:
        print(x, suma // 28)