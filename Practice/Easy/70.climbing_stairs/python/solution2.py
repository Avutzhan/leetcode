def climbing_stairs(n):
    """
    Recursion
    Time: Exponential O(2^n)
    Memory: O(Stack Size) = O(n)
    :return:
    """
    def stairs(i):
        if i == 0:
            return 1
        if i < 0:
            return 0

        way_one = stairs(i - 1)
        way_two = stairs(i - 2)

        return way_one + way_two
    return stairs(n)


print(climbing_stairs(3))
