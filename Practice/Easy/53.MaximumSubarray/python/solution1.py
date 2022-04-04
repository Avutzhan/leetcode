class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

class Solution1:
    def maxSubArray1(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)

# input [-2,1,-3,4,-1,2,1,-5,4]
#
# 1) [1] -2 > 0.Problem false
# 2) [-3] 1 > 0.Problem true enter
# 3) -3 + 1 = 3 - 1 = -2
# 4) [4] -2 > 0.Problem false
# 5) [-1] 4 > 0.Problem true enter
# 6) -1 + 4 = 4 - 1 = 3
# 7) [2] 3 > 0.Problem true enter
# 8) 2 + 3 = 5
# 9) [1] 5 > 0.Problem true enter
# 10) 1 + 5 = 6
# 11) [-5] 6 > 0.Problem true enter
# 12) - 5 + 6 = 6 - 5 = -1
# 13) [4] -1 > 0.Problem false
# 14) max([-2,1,-2,4,3,5,6,-1,4]) = 6
#
# output 6


