class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        T: O(n log n)
        M: O(1)
        :param nums:
        :return:
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False