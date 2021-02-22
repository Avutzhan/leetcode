class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0

        for i,n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest*2:
            highestIndex = -1

        return highestIndex