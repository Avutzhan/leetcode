class Solution:
    def filterRestaurants(self, A: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        A.sort(key=lambda x: (-x[1], -x[0]))
        return [i for i, _, v, p, d in A if v >= veganFriendly and p <= maxPrice and d <= maxDistance]