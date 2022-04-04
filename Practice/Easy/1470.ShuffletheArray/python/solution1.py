class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ## APPROACH : GREEDY ##
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

#nums = [2,5,1,3,4,7] n = 3
#in loop i = 0.Problem, 1, 2; i + n = 3, 4, 5
        