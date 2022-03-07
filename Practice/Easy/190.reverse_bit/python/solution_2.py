def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        res <<= 1
        if n & 1 > 0:
            res += 1
        n >>= 1

    return res
