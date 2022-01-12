class Solution:
    def averageWaitingTime(self, A: List[List[int]]) -> float:
        wait = cur = 0.
        for t, d in A:
            cur = max(cur, t) + d
            wait += cur - t
        return wait / len(A)