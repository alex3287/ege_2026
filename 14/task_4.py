def count_0(number):
    cnt = 0
    while number:
        if number % 11 == 0:
            cnt += 1
        number //= 11
    return cnt

for x in range(1, 3001):
    number = 9*11**210 + 8*11**150 - x
    if count_0(number) == 60:
        print(x)