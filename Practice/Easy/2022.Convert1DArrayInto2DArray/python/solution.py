class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        N = len(original)

        if N != m * n:
            return []

        ans = []
        for i in range(m):
            ans.append(original[i * n:i * n + n])
        return ans