def count_3(number):
    cnt = 0
    while number:
        if number % 4 == 3:
            cnt += 1
        number //= 4
    return cnt


number = 64**30 + 2**300 - 32
print(number)
print(count_3(number))