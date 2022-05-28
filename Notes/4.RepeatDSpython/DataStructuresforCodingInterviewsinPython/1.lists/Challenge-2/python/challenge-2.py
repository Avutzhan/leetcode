def merge_lists(lst1, lst2):
    """
    merge two sorted lists my approach
    Time: O(n logn)
    Why O(n + m) and sorting O(nlogn) so in the end we have O(nlogn)
    :param lst1:
    :param lst2:
    :return:
    """
    res = []
    for i in lst1:
        res.append(i)
    for i in lst2:
        res.append(i)
    res.sort()
    return res

print(merge_lists([1, 3, 4, 5], [2, 6, 7, 8]))