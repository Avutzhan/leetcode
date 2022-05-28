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