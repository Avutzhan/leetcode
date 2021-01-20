class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        unsorted = nums.copy()
        nums.sort()
        for n in unsorted:
            result.append(nums.index(n))
        return result


