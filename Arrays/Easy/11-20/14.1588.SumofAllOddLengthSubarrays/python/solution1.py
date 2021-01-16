class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0

        for i in range(len(arr)):
            currSum = 0

            for j in range(i, len(arr)):
                currSum += arr[j]
                if ((j - i + 1) % 2 == 1):
                    result += currSum

        return result
