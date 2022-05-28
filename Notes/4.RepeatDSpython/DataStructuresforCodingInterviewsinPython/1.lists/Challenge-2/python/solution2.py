def merge(arr1, arr2):
    """
    In place solution
    Time: O(n^2)
    Space: O(1)
    :param arr1:
    :param arr2:
    :return:
    """
    index1 = 0
    index2 = 0

    while (index1 < len(arr1)) and (index2 < len(arr2)):
        if arr1[index1] < arr2[index2]:
            arr1.insert(index1, arr2[index2])
            index1 += 1
            index2 += 1
        else:
            index1 += 1

    while index2 < len(arr2):
        arr1.extend(arr2[index2:])

    return arr1


result = merge([1, 3, 4, 5], [2, 6, 7, 8])

expected = [1, 2, 3, 4, 5, 6, 7, 8]

result.sort()
expected.sort()

if result == expected:
    print("Success")
else:
    print("Failure")