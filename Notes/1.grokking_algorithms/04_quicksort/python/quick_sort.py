def quick_sort(arr):
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
