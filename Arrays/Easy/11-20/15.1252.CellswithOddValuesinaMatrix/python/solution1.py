class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rowCount = [0 for i in range(n)]
        columnCount = [0 for i in range(m)]
        ret = 0

        for i in range(len(indices)):
            rowCount[indices[i][0]] += 1
            columnCount[indices[i][1]] += 1

        for i in range(n):
            for j in range(m):
                if (rowCount[i] + columnCount[j]) % 2 != 0:
                    ret+=1

        return ret

