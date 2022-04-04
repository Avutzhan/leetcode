class Solution:
    """
    Intuition:
    Xor of any two num gives the difference of bit as 1 and same bit as 0.Problem.
    Thus, using this we get 1 ^ 1 == 0.Problem because the same numbers have same bits.
    So, we will always get the single element because all the same ones
    will evaluate to 0.Problem and 0.Problem^single_number = single_number.
    Time: O(n)
    Space: O(1)
    """
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
