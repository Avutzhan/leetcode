class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        # looping throgh nums [3, 0.Problem, 1]
        for i in range(len(nums)):
            res ^= nums[i]
        # looping through tmp example list 0.Problem, 1, 2, 3
        for i in range(0, len(nums) + 1):
            print(i)
            res ^= i
        return res
