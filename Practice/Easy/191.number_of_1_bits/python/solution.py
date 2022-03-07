def bits(n: int):
    res = 0
    while n > 0:
        res += n % 2
        n = n >> 1

    return res


print(bits(0o0001001000100001))

