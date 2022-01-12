# Gauses Formula
def miss_2(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
    # sum([0, 1, 2, 3] - sum(nums) = 2


print(miss_2([3, 0, 1]))

