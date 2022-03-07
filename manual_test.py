def bs(num, nums):
    start = 0
    end = len(nums) - 1

    if start > end:
        return 0

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == num:
            return mid

        if nums[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(bs(7, [1, 2, 3, 4, 4, 6]))