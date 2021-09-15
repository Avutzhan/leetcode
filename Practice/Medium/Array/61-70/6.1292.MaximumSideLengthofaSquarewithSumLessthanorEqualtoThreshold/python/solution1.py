class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        res = 0
        for r in range(1, n+1):
            for c in range(1, m+1):
                dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + mat[r-1][c-1]
                k = res + 1
                if r >= k and c >= k and threshold >= dp[r][c] - dp[r-k][c] - dp[r][c-k] + dp[r-k][c-k]:
                    res = k
        return res