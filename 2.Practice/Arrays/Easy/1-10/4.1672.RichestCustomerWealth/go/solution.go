class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []

        for i in accounts:
            wealth.append(sum(i))

        return max(wealth)


