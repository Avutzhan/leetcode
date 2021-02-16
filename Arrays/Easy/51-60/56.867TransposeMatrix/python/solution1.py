class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(A) for _ in range(len(A[0]))]

        for i in range(len(A[0])):
            for j in range(len(A)):
                res[i][j] = A[j][i]

        return res
        