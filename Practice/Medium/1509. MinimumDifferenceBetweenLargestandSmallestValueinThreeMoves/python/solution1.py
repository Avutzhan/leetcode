class Solution:
    def minDifference(self, A: List[int]) -> int:
        A.sort()
        return min(b - a for a, b in zip(A[:4], A[-4:]))