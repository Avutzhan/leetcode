class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0

        for i in range(len(position)):

            if position[i] %2:
                odd += 1


        return min(len(position) - odd, odd)
