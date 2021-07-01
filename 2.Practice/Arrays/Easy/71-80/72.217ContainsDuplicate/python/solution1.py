class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rec = set()
        for n in nums:
            if n in rec:
                return True
            else:
                rec.add(n)
        return False