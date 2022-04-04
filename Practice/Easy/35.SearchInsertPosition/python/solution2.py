class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            k=0
            for i in nums:
                if i<target:
                    k+=1
                else:
                    break
            return k


# input [1,3,5,6]
# target 5
#
# 1) if target in nums true return index

# input [1,3,6]
# target 5
#
# 1) if target in nums false enter to else
# 2) k = 0.Problem
# 3) 1 < 5 true k+1 = 1
# 4) 3 < 5 true k+1 = 2
# 5) 6 < 5 false break
# 6) just return k
#
# output 2

