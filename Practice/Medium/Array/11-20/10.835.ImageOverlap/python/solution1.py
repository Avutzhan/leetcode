class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
        count = collections.Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        return max(count.values() or [0])  # if the input has no 1, count will be None, that why we need or [0]