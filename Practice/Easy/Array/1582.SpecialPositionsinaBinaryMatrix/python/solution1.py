class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])
        cnt = 0
        row = [0] * M
        col = [0] * N
        for i in range(M):
            for j in range(N):
                if mat[i][j]:
                    row[i]+=1
                    col[j]+=1

        for i in range(M):
            for j in range(N):
                if mat[i][j] and row[i] == 1 and col[j] == 1:
                    cnt+=1

        return cnt