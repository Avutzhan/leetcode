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


# Time: O(n)
# Space: O(n)
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
