class Solution:
    def matrixReshape(self, nums: List[List[int]], h: int, w: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        if m * n != h * w:
            return nums

        vals = [val for row in nums for val in row]

        res = [[None] * w for _ in range(h)]

        i = 0
        for r in range(h):
            for c in range(w):
                res[r][c] = vals[i]
                i += 1

        return res