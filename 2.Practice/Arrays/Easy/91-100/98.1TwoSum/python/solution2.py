class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# 1) 7 + 2 == 9 true so wee return indexes

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 1) 2 + 3 == 6 false go on
# 2) 4 + 2 == 6 true return indexes


