class Solution:
    def sumZero(self, n: int) -> List[int]:
        list = [None] * n;

        for i in range(n):
            list[i] = i * 2 - n + 1

        return list

