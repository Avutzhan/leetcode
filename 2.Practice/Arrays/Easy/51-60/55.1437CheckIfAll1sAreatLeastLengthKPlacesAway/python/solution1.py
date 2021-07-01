class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = -k-1

        for j in range(len(nums)):
            if nums[j] == 1:
                if j-i-1 < k:
                    return False
                i = j
        return True