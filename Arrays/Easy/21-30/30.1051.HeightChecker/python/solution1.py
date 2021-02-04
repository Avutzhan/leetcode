class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedarr = heights.copy()
        sortedarr.sort()

        count = 0

        for i in range(len(heights)):
            if heights[i] != sortedarr[i]:
                count += 1

        return count


