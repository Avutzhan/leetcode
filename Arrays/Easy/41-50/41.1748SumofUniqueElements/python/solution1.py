class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ =0
        a = nums


        for i in range(len(a)):
            count = 0

            for q in range(len(nums)):
                if nums[q] == a[i]:
                    count += 1
            
            if count <= 1:
                summ += a[i]

        return summ