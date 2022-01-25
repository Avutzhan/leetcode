def find_smallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


def selection_sort(arr):
    """
    Selection sort
    Time Complexity: O(n^2)
    Memory: O(n)
    :param arr:
    :return:
    """
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort([5, 6, 3, 2, 4, 1]))


