class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0

        for i in range(len(nums)):
            if (len(str(nums[i])) % 2 == 0):
                ret += 1

        return ret
