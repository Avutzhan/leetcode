class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            prev = prices[i - 1]
            current = prices[i]

            if prev < current:
                profit += current - prev

        return profit
