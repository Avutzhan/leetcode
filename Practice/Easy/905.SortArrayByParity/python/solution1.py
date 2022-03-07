class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        size = len(A)
        res = [None] * size
        start = 0
        end = size - 1
        for val in A:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res