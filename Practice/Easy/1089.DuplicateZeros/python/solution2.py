class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy = arr.copy()
        counter = 0
        for i in range(len(copy)):
            if copy[i] == 0:
                arr.insert(i + counter, 0)
                counter += 1
                arr.pop()



