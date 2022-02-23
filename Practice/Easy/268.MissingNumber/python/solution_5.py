class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Brute Force
        T: O(n)
        M: O(n)
        :param nums:
        :return:
        """
        tmp = [x for x in range(0, len(nums) + 1)]
        for n in tmp:
            if n not in nums:
                return n
        return None