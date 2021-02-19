class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1,numRows+1):
            tmp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    tmp.append(1)
                else:
                    tmp.append(res[-1][j-1]+res[-1][j])

            res.append(tmp)

        return res