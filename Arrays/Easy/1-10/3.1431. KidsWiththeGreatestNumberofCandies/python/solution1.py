class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        maxval = max(candies)

        for i in candies:
            ret.append(i + extraCandies >= maxval)

        return ret