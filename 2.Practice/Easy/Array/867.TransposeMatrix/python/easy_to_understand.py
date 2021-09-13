class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R = len(A)
        C = len(A[0])
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(A[r][c])
            transpose.append(newRow)
        return transpose
