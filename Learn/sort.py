# Time: O(n^2)
# Space: O(n^2)
# this algorithm can't sort dublicated values
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left = [i for i in lst[1:] if i < pivot]
        right = [i for i in lst[1:] if i > pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)


# Time: O(n + m)
# Space: O(n + m)
def merge(lst1, lst2):
    idx1 = 0
    idx2 = 0
    idx_res = 0
    res = []

    for i in range(len(lst1) + len(lst2)):
        res.append(i)

    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            res[idx_res] = lst1[idx1]
            idx_res += 1
            idx1 += 1
        else:
            res[idx_res] = lst2[idx2]
            idx_res += 1
            idx2 += 1

    while idx1 < len(lst1):
        res[idx_res] = lst1[idx1]
        idx_res += 1
        idx1 += 1

    while idx2 < len(lst2):
        res[idx_res] = lst2[idx2]
        idx_res += 1
        idx2 += 1

    return res


# Time: O(nlogn)
# Space: O(n)
def merge_sort(lst):
    if len(lst) <= 1:  # base case
        return lst
    else:
        # divide array in half and merge sort recursively
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)
