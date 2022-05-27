def find_sum(lst, k):
    # Find Two Numbers that Add up to "k"
    # Moving indices
    lst.sort()
    first = 0
    last = len(lst) - 1
    result = []
    sum = 0
    while first != last:
        sum = lst[first] + lst[last]
        if sum < k:
            first += 1
        elif sum > k:
            last -=1
        else:
            result.append(lst[first])
            result.append(lst[last])
            return result
    return False


def find_sum(lst, k):
    # iterate lst with i Brute Force
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i], lst[j]]


print(find_sum([1, 2, 3, 4], 5))


def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k - lst[j]]


print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))