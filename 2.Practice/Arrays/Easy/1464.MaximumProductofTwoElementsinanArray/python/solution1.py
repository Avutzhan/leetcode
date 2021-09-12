class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = 0
        m2 = 0

        for i in range(len(nums)):
            m2 = max(m2, min(m1, nums[i]))
            m1 = max(m1, nums[i])

        return (m1 - 1) * (m2 - 1)

