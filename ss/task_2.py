# Перевод из 10СС в 2, 8, 16 СС

# 256 в 10CC -> 2, 8, 16 CC
print(bin(255))
print(oct(255))
print(hex(255))

# чистый перевод (без префикса)
print(bin(255)[2:])
print(oct(255)[2:])
print(hex(255)[2:])

# с помощью f строк
print(f'{255:b}')
print(f'{255:o}')
print(f'{255:x}')