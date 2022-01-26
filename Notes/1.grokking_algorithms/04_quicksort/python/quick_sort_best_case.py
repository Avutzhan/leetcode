import random


def quick_sort(arr):
    """
    We can use midle of array every time or random index
    both cases i will write here in code
    Time complexity: Best Case O(n log n)
    Stack Height is O(log n)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr

    # we use middle of array
    # idx = len(arr) // 2
    idx = random.randrange(len(arr))
    pivot = arr[idx]
    less = []
    # in past example we used first element as pivot and started loop from 1
    # here we don't use it so we start from 0
    for i in range(len(arr)):
        # if we met our idx in loop just skip it to avoid bullshit in result
        if i == idx:
            continue
        if arr[i] <= pivot:
            less.append(arr[i])

    greater = []
    for i in range(len(arr)):
        if i == idx:
            continue
        if arr[i] > pivot:
            greater.append(arr[i])

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 4, 3, 2, 5]))
