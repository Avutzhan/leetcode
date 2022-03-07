def climb_stairs(n: int) -> int:
    """
    1DP Bottom Up
    Time: Linear O(n)
    Memory: O(1)
    :param n:
    :return:
    """
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one
