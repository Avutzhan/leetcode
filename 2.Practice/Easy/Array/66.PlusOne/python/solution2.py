class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                return digits
        digits.insert(0, 1)
        return digits

# input = [1,2,3] this is actually 123
# you must add 1 to 123 but as array

