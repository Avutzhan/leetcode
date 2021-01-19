##best solution simple

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        running = 0
        result = []

        for i in range(len(nums)):

            running += nums[i]
            result.append(running)

        return result