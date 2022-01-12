class Solution:
    def setZeroes(self, M):
        m, n = len(M[0]), len(M)
        r1 = any(M[0][j] == 0 for j in range(m))
        c1 = any(M[i][0] == 0 for i in range(n))
        for i in range(1, n):
            for j in range(1, m):
                if M[i][j] == 0: M[i][0] = M[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if M[i][0] * M[0][j] == 0: M[i][j] = 0

        if r1:
            for i in range(m): M[0][i] = 0

        if c1:
            for j in range(n): M[j][0] = 0
