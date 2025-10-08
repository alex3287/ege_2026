# Перевод в большую СС имеет проблему, нам нужны буквы
from string import *


print(ascii_letters)
print(ascii_lowercase)
print(ascii_uppercase)

# 25 CC
letters = ascii_uppercase[:15]
ABC = '0123456789' + letters
print(ABC)

def ten_to_25(number):
    result = ''
    while number:
        result = ABC[number%25] + result
        number //= 25
    return result

print(ten_to_25(24))