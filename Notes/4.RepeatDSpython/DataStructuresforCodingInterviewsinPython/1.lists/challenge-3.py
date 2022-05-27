def find_sum(lst, k):
    # Write your code here Find Two Numbers that Add up to "k"
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