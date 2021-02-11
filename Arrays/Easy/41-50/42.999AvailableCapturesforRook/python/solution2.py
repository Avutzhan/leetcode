class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = 0
        y = 0
        ret = 0 # return just ret with 0 if we reach the edge (nothing was found)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = i
                    y = j

        for i in range(x + 1, 8): # increasing col
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                ret += 1 # sum all directions up
                break

        for i in range(x - 1, -1, -1): # decreasing col
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                ret += 1 # sum all directions up
                break

        for i in range(y + 1, 8): # increasing row
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                ret += 1 # sum all directions up
                break

        for i in range(y - 1, -1, -1): # decreasing col
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                ret += 1 # sum all directions up
                break


        return ret



