# Brute Force
def two_sum2(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum2([2, 7, 11, 15], 9))  # [0.Problem, 1]
