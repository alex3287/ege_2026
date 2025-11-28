def ten_to_3(number):
    result = ''
    while number > 0:
        result = str(number%3) + result
        number //= 3
    return result

print(ten_to_3(3))

def alg(N):
    bin_N = bin(N)[2:]
    # bin_N = f'{N:b}'
    if N % 3 == 0:
        bin_N += bin_N[-3:]
    else:
        bin_N += bin(N % 3 * 3)[2:]
    R = int(bin_N, 2)
    return R


# print(alg(12))

# for N in range(1, 200):
#     R = alg(N)
#     if R >= 200:
#         print(f'N:{N} -> R:{R}')