class Solution:
    def longestSubarray(self, A, limit):
        i, L = 0, []
        for j in range(len(A)):
            bisect.insort(L, A[j])
            if L[-1] - L[0] > limit:
                L.pop(bisect.bisect(L, A[i]) - 1)
                i += 1
        return j - i + 1
