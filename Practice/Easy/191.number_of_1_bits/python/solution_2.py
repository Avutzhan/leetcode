def bits2(n: int):
    res = 0
    while n > 0:
        n &= n-1
        res += 1

    return res


print(bits2(0o0001001000100001))

