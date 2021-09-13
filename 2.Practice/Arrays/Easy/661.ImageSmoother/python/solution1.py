class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M: return M
        new = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        directions = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        for i in range(len(new)):
            for j in range(len(new[0])):
                total = 0
                count = 0
                for r, c in directions:
                    if i + r < 0 or j + c < 0 or i + r >= len(M) or j + c >= len(M[0]):
                        continue
                    total += M[i + r][j + c]
                    count += 1
                new[i][j] = total//count
        return new