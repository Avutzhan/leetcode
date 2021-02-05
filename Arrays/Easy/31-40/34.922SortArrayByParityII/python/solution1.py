class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        even = 0
        odd = 1

        for i in range(len(A)):
            if A[i] % 2 == 0:

                result[even] = A[i]
                even += 2
            else:
                result[odd] = A[i]
                odd += 2

        return result;
