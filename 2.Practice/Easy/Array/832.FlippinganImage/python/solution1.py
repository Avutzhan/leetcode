class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = list(reversed(A[i])) # reverse the row
            for j in range(len(A[i])): # invert each element
                A[i][j] = 1-A[i][j]
        return A