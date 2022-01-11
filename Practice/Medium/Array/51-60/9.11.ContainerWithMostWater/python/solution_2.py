# Brute Force O(n^2)
def max_water_2(height):
    res = 0
    n = len(height)

    for l in range(n):
        for r in range(l + 1, n):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res


print(max_water_2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
