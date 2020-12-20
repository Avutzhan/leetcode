class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            cur = points[i]
            prev = points[i - 1]
            ans += max(map(abs, (prev[0] - cur[0], prev[1] - cur[1])))
        return ans

