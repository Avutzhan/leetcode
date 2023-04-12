# Time: O(n)
# Space: O(n)
def remove_even(lst):
    return [item for item in lst if item % 2 != 0]


# Find Two Numbers that Add up to "K"
# Time: O(n^2)
# Space: O(1)
def find_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == k and i != j:
                return [lst[i], lst[j]]
