# Time: O(n)
# Space: O(1)
def linear_search(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return -1


# Time: O(logn)
# Space: O(1)
def binary_search(lst, n):
    l = 0
    h = len(lst) - 1
    while l <= h:
        m = (l + h) // 2
        if lst[m] == n:
            return m
        if lst[m] < n:
            l = m + 1
        else:
            h = m - 1
    return -1
