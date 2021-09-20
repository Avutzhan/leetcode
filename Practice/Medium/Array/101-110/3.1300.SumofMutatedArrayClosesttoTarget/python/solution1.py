class Solution:
    def findBestValue(self, A, target):
        A.sort(reverse=1)
        maxA = A[0]
        while A and target >= A[-1] * len(A):
            target -= A.pop()
        return int(round((target - 0.0001) / len(A))) if A else maxA
