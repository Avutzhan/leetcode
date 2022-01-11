def reverse(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res


print(reverse(0b0000010100101000001111010011100))
# 43261596  (0b0000010100101000001111010011100)
# 964176192 (00111001011110000010100101000000) 0b111001011110000010100101000000
