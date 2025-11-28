def alg(N):
    bin_N = bin(N)[2:]
    if N % 3 == 0:
        bin_N += bin_N[-3:]
    else:
        bin_N += bin(N % 3 * 3)[2:]
    R = int(bin_N, 2)
    return R


print(alg(12))

for N in range(1, 100):
    R = alg(N)
    if R > 151:
        print(f'N:{N} -> R:{R}')