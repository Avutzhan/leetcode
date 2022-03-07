def tail_recursion_factorial(n, acc):
    if n == 0:
        return acc
    return tail_recursion_factorial(n - 1, acc * n)


def tailed(n):
    return tail_recursion_factorial(n, 1)


print(tailed(5))
