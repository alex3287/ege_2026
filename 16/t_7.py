from sys import setrecursionlimit
# setrecursionlimit(800_000)

def F(n):
    if n < 3:
        return n+1
    if n % 2 == 0:
        return 2 * F(n+2) + n
    return F(n-2) + n - 2

cnt = 0
for i in range(1, 1001):
    try:
        res = F(i)
        if '1' not in str(res):
            print(i, res)
            cnt += 1
    except:
        pass

print(cnt)