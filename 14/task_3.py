# from sys import set_int_max_str_digits
#
# set_int_max_str_digits(10000)

def count_more_9(number):
    cnt = 0
    while number:
        if number % 27 > 9:
            cnt += 1
        number //= 27
    return cnt


number = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
# print(number)
print(count_more_9(number))