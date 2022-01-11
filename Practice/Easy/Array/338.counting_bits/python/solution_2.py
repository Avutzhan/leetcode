# Brute Force
def count_bit_2(n):
    res = []
    nums = [x for x in range(n + 1)]
    for n in nums:
        count = 0
        while n > 0:
            count += n % 2
            n = n // 2

        res.append(count)
    return res


print(count_bit_2(3))
