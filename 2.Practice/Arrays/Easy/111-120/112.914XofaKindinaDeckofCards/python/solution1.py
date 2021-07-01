class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        mini = min(count.values())

        if mini < 2:
            return False
        for i in range(mini+1,1,-1):
            res = all(value % i ==0 for value in count.values())
            if res: return True
        return False