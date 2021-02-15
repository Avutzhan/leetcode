class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        x = 0
        for i in range(len(arr)):
            if arr[i] % 2:
                x = x | [1, 2, 4][i % 3]
            else:
                x = 0

            if 7 == x:
                return True

        return False
        