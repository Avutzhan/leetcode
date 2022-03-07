def climbing_stairs(n):
    """
    Recursion + Memoization(Top Down DP is recursion + memoization technique)
    Time: Linear O(n)
    Memory: O(Stack Size) = O(n)
    :return:
    """

    def stairs(i, dp):
        if i == 0:
            return 1
        if i < 0:
            return 0

        if dp[i] != -1:
            return dp[i]

        way_one = stairs(i - 1, dp)
        way_two = stairs(i - 2, dp)

        dp[i] = way_one + way_two
        print(dp)
        return dp[i]

    dp = [-1] * (n + 1)
    return stairs(n, dp)


print(climbing_stairs(6))
