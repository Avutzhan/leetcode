class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = 1
        summ = 0

        for i in range(len(nums)):
            summ = summ+nums[i]
            minn = min(minn,summ)

        if minn == 1:
            return minn

        return (-1*minn)+1