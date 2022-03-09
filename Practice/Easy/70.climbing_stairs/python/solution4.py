def climbing_stairs_reverse(n):
    """
    Reverse Bottom Up is iterative solution
    Time: Linear O(n)
    Memory: O(n) list
    :param n:
    :return:
    """
    dp = [1] * (n + 1)
    for i in range(len(dp) - 3, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2]

    return dp[0]


print(climbing_stairs_reverse(3))
