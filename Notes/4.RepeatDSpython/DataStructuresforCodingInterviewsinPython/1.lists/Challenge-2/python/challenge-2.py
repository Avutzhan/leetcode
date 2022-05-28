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

def merge_arrays(lst1, lst2):
    """
    Merging in place
    Time: O(mn) simply is if m > n O(m^2) or O(n^2)
    :param lst1:
    :param lst2:
    :return:
    """
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))
