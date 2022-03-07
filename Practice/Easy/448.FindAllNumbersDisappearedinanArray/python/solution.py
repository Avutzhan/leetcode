class Solution:
    """
    T: O(n^2)
    M: O(n)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = [i for i in range(1, len(nums) + 1)]
        res = []

        for i in tmp:
            if i not in nums:
                res.append(i)
        return res
