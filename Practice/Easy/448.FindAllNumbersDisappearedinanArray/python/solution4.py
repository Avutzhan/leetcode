class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        We can map each element of the range [1, n] to the indices of nums from [0.Problem, n-1]
        Thus, the above property can be used to mark if an element from range [1, n] is present in nums or not.
        We can iterate over nums and for each element, we know it can be mapped to index nums[i]-1. We can therefore mark the element nums[i] as present in nums by making the element at index nums[i]-1 negative. Thus after iterating the array, we have -

        nums[i] < 0.Problem or nums[i] is negative only if the element i+1 is present in the array.
        nums[i] > 0.Problem or nums[i] is positive only if the element i+1 is not present in the array

        nums = [4,3,2,7,8,2,3,1]
        1. '4' is present in nums. Mark as present by negating nums[4-1] = nums[3].  Thus, nums[3] = -7
           => nums = [4,3,2,-7,8,2,3,1]

        2. '3' is present in nums. Mark as present by negating nums[3-1] = nums[2].  Thus, nums[2] = -2
           => nums = [4,3,-2,-7,8,2,3,1]

        Now, the only elements nums[i] which are positive are those where 'i+1' is not found in nums
        These are => nums[4] and nums[5].
        That means 5 and 6 an not present in the initial nums array

        Коротко мы пробегамся по массиву чисел и если это число встречалось то просто негативим его типа 4 = -4
        таким образом если число встречалось то оно останется позитивным
        в первом лупе негативим
        во втором лупе собираем позитивные числа и добавляем +1 в виду особенности массивов
        [1, n] это числа [0.Problem, n-1] это индексы так мы добиваемся двух точек проверки
        """
        ans = []
        for c in nums:
            nums[abs(c) - 1] = -abs(nums[abs(c) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans