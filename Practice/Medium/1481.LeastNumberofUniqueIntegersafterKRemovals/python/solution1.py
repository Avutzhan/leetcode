class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = [(val, key) for key, val in collections.Counter(arr).items()]
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)[0]
        return len(hp) + (k < 0)
