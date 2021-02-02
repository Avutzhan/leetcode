class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = m - 1
        c = 0
        cnt = 0

        while r >= 0 and c < n:
            if grid[r][c] < 0:
                r -= 1
                cnt += n - c
            else:
                c += 1

        return cnt