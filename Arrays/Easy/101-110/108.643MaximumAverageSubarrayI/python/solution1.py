class Solution:
    def findMaxAverage(self, A: List[int], K: int) -> float:
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        ma = max(P[i+K] - P[i]
        for i in range(len(A) - K + 1))
        return ma / float(K)