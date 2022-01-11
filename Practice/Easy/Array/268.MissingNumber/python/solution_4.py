def miss_bin(nums):
    res = 0
    for i in range(len(nums)):
        res ^= nums[i]
    for i in range(0, len(nums) + 1):
        res ^= i
    return res


print(miss_bin([3, 0, 1, 2]))

