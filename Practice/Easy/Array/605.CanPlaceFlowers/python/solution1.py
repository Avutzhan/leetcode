class Solution:
    def canPlaceFlowers(self, A: List[int], N: int) -> bool:
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0)
                    and (i == len(A)-1 or A[i+1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0