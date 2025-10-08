# Первод из 10 СС в любую другую

# 34 в 10СС -> 3 CC
def ten_to_3(number):
    result = ''
    while number:
        result = str(number%3) + result
        number //= 3
    return result

print(ten_to_3(34))
#проверка
print(int('1021', 3))
