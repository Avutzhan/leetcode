class Solution:
    def matrixReshape(self, nums: List[List[int]], h: int, w: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        if m * n != h * w:
            return nums

        result = []
        row = []
        for num in nums:
            for n in num:
                row.append(n)
                if len(row) == w:
                    result.append(row)
                    row = []


        return result
