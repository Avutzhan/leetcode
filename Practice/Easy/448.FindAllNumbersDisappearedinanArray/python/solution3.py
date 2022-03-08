class Solution:
    """
    Time Complexity : O(n), we require O(n) time to insert all elements into hashset and another O(n)
    time to iterate over range and insert elements not present in hashset into ans, thus giving a total time of O(n).
    Space Complexity : O(n), required to maintain the hashset.
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]

