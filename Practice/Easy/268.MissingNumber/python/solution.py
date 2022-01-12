# Brute Force O(n)
def miss(nums):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = True
    for i in range(0, len(nums) + 1):
        # print(i)
        if i not in hash.keys():
            return i


print(miss([0, 1]))
