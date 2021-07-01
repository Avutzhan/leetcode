class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ## APPROACH : GREEDY ##
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
        