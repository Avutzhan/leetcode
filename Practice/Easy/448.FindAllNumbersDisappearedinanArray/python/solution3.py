class Solution:
    """
    Time Complexity : O(n), we require O(n) time to insert all elements into hashset and another O(n)
    time to iterate over range and insert elements not present in hashset into ans, thus giving a total time of O(n).
    Space Complexity : O(n), required to maintain the hashset.
    According to Python wiki: Time complexity, set is implemented as a hash table. So you can expect to
    lookup/insert/delete in O(1) average. Unless your hash table's load factor is too high, then you face collisions
    and O(n).
    P.S. for some reason they claim O(n) for delete operation which looks like a mistype.
    P.P.S. This is true for CPython, pypy is a different story.
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]

