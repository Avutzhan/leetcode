class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt = len(nums) // 2
        return nums[cnt];