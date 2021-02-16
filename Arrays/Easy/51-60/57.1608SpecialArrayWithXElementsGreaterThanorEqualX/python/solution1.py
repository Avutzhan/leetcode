class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            c = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    c+=1
            if c == i:
                return i
        return -1

