class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0,-1):
            print(nums[i-1])
            if nums[i] == nums[i-1]:
                nums.pop(i)

# input [1,1,2]
#
# 1) For loop from end to start
# 2) 2 == 1 false not in condition
# 3) 1 == 1 true in condition
# 4) remove last element i and leave i - 1 element
#
# output [1,2]

