class Solution:
    def shipWithinDays(self, a, d):
        lo, hi = max(a), sum(a)
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in a:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= d:
                hi = mid
            else:
                lo = mid+1
        return lo