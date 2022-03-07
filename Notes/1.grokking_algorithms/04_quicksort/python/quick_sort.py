def quick_sort(arr):
    """
    Pivot is first elemnt of array so time complexity is O(n^2)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            less.append(arr[i])

    greater = []
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            greater.append(arr[i])

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 4, 3, 2, 5]))
