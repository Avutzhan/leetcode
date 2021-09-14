class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curMax, res = -1, 0
        for i, v in enumerate(arr):
            curMax = max(curMax, v)
            res += curMax == i
        return res