# DP but without array just used main idea of one dimensional dp one two
def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one
