class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
                j+=1

        return prices

