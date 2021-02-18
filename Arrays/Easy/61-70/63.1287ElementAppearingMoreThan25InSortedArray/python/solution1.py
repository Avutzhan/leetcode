class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ws = len(arr) // 4

        for i in range(len(arr) - ws):
            if arr[i] == arr[i + ws]:
                return arr[i]

        return -1