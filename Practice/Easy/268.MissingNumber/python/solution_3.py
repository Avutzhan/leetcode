# O(n) time and O(1) memory
def miss_3(nums):
    res = len(nums)
    for i in range(len(nums)):
        res += (i - nums[i])

    return res


print(miss_3([3, 0, 1]))

