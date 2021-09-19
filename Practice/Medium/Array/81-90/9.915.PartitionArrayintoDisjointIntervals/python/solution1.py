class Solution:
    def partitionDisjoint(self, A):
        t1 = list(accumulate(A, max))
        t2 = list(accumulate(A[::-1], min))[::-1]
        for i in range(1, len(A)):
            if t1[i - 1] <= t2[i]: return i
