class Solution:
    def arrayNesting(self, A: List[int]) -> int:
        seen, res = [0] * len(A), 0
        for i in A:
            cnt = 0
            while not seen[i]:
                seen[i], cnt, i = 1, cnt + 1, A[i]
            res = max(res, cnt)
        return res