class Solution:
    def trimMean(self, arr: List[int]) -> float:
        N = len(arr)
        K = N // 20
        return sum(sorted(arr)[K:-K]) / (N - 2 * K)