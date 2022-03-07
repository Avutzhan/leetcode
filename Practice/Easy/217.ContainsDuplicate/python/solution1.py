class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        T: O(n)
        M: O(n)
        :param nums:
        :return:
        """
        rec = set()
        for n in nums:
            if n in rec:
                return True
            else:
                rec.add(n)
        return False