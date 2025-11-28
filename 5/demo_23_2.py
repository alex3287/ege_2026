def alg(N):
    bin_N = bin(N)[2:]
    suma = bin_N.count('1')
    if suma % 2 == 0:
        bin_N = '10' + bin_N[2:] + '0'
    else:
        bin_N = '11' + bin_N[2:] + '1'
    R = int(bin_N, 2)
    return R


print(alg(6))

for N in range(1, 100):
    R = alg(N)
    if R >= 40:
        print(f'N:{N} -> R:{R}')