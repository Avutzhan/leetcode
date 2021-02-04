class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]):
                    t = []
                    for r in range(len(matrix)):
                        t.append(matrix[r][j])
                    if matrix[i][j] == max(t):
                        return [matrix[i][j]]
        return []