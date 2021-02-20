class Solution:
    def check(self, A: List[int]) -> bool:
        return sum(a > b for a, b in zip(A, A[1:] + A[:1])) <= 1