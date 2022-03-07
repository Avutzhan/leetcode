class Solution:
    """
    BS solution
    T: O(nlogn)
    M: O(n)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums) + 1):
            if nums[self.bs(i, nums)] != i:
                res.append(i)

        return res

    def bs(self, num, nums):
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


