# Hash Table
def two_sum(arr, target):
    hash = {}

    for i in range(len(arr)):
        tmp = target - arr[i]
        if tmp in hash.keys():
            return [hash[tmp], i]
        hash[arr[i]] = i


print(two_sum([1, 2, 3, 4, 6], 10))
