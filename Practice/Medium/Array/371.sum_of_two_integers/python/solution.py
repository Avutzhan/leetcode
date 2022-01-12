def sum_two(a, b):
    while b != 0:
        tmp = (a & b) << 1
        a = a ^ b
        b = tmp

    return a


print(sum_two(10, 40))



