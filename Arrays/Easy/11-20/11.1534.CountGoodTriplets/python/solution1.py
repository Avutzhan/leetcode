class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n - 1):
                if (abs(arr[i] - arr[j]) > a):
                    continue

                for k in range(j + 1, n):
                    if (abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c):
                        res += 1

        return res
