class Solution:
    def countTriplets(self, A: List[int]) -> int:
        A.insert(0, 0)
        n = len(A)
        for i in range(n - 1):
            A[i + 1] ^= A[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if A[i] == A[j]:
                    res += j - i - 1
        return res