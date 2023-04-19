# Time: O(n)
# Space: O(n)
def remove_even(lst):
    return [item for item in lst if item % 2 != 0]


# Time: O(n^2)
# Space: O(1)
def find_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == k and i != j:
                return [lst[i], lst[j]]


# Time: O(n^2)
# Space: O(n)
def find_product_brute_force(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if i != j:
                product = product * lst[j]
        res.append(product)
    return res


# Time: O(n)
# Space: O(n)
# Description: Given a list, modify it so that each index stores the product of all elements
# in the list except the element at the index itself.
def find_product(lst):
    left = 1
    products = []
    for i in lst:
        products.append(left)
        left = left * i

    right = 1
    for i in range(len(lst) - 1, -1, -1):
        products[i] = products[i] * right
        right = right * lst[i]

    return products


def find_minimum(lst):
    minimum = lst[0]
    for i in lst:
        if minimum > i:
            minimum = i
    return minimum


def find_unique(lst):
    for i in lst:
        if counter(lst, i) == 1:
            return lst[i]

    return -1


def counter(lst, n):
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count


# Time: O(nlogn)
# Space: O(1)
# This solution not working correctly with list with dublicates
def find_second_maximum_sorting(lst):
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    return -1


def find_second_maximum(lst):
    mx = float('-inf')
    secondmax = float('-inf')
    for val in lst:
        if val > mx:
            secondmax = mx
            mx = val
        elif val > secondmax:
            secondmax = val
    return secondmax


def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


def rearrange(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


def max_min(lst):
    result = []
    for i in range(len(lst) // 2):
        result.append(lst[-(i + 1)])
        result.append(lst[i])
    if len(lst) % 2:
        result.append(lst[len(lst) // 2])
    return result


def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0

    curr_max = lst[0]
    global_max = lst[0]
    length_array = len(lst)
    for i in range(1, length_array):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max
