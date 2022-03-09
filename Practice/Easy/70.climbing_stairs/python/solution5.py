class Solution:
    """
    Classic and easy to understand DP solution
    Reverse Bottom Up
    Time: Linear O(n)
    Memory: O(n) list
    :param n:
    :return:
    """
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n] #also you can do dp[-1]


