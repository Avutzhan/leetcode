class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ret = [0] * k
        visited = [0] * m
        idx = 0

        for i in range(n):
            for j in range(m):
                if visited[j] == 0 and mat[j][i] == 0:
                    ret[idx] = j
                    visited[j] = 1
                    idx += 1
                    if idx == k:
                        return ret

        for i in range(m):
            if visited[i] == 0:
                ret[idx] = i
                idx += 1
                if idx == k:
                    return ret


