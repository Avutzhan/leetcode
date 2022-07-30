def find_sum(lst, k):
    # Write your code here Brute Force T: O(n^2)
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == k and i != j:
                return [lst[i], lst[j]]
