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


# Merge list1 and list2 and return resulted list
def merge_lists(lst1, lst2):
    """
    Merge two sorted lists. Intuituve with new list.
    Time: O(n + m) n and m lengths of the lists. Both lists are iterated over atleast once.
    Steps:
    1 Create 3 indexes
    2 Create new array
    3
    :param lst1:
    :param lst2:
    :return:
    """
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1) + len(lst2)):
        result.append(0)

    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if (lst1[index_arr1] < lst2[index_arr2]):
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1

    # [0, 0, 0, 0, 0, 0, 0, 0]
    # len 4 4
    # list [1, 3, 4, 5] [2, 6, 7, 8]
    # condition 1 2
    # [0, 0, 0, 0, 0, 0, 0, 0]
    # index_result 1
    # if index 1 0
    # condition 3 2
    # [1, 0, 0, 0, 0, 0, 0, 0]
    # else index 1 1
    # condition 3 6
    # [1, 2, 0, 0, 0, 0, 0, 0]
    # index_result 3
    # if index 2 1
    # condition 4 6
    # [1, 2, 3, 0, 0, 0, 0, 0]
    # index_result 4
    # if index 3 1
    # condition 5 6
    # [1, 2, 3, 4, 0, 0, 0, 0]
    # index_result 5
    # if index 4 1
    # [1, 2, 3, 4, 5, 0, 0, 0]

    while (index_arr1 < len(lst1)):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1

    while (index_arr2 < len(lst2)):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1

    # here we fill missing last numbers

    return result


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
