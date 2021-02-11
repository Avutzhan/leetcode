class Solution:
    def canCapture(self, board: List[List[str]], i: int, j: int) -> int:
        captures = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for k in range(len(dirs)):
            r = i + dirs[k][0]
            c = j + dirs[k][1]

            while r >= 0 and r < 8 and c >= 0  and c < 8:
                if board[r][c] == 'p':
                    captures += 1
                if board[r][c] != '.':
                    break

                r += dirs[k][0]
                c += dirs[k][1]

        return captures

    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return self.canCapture(board, i, j)


