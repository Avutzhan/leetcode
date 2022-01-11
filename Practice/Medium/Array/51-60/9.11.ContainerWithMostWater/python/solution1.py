# Two Pointers O(n)
def max_water(height):
    l, r, res = 0, len(height) - 1, 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res


print(max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
