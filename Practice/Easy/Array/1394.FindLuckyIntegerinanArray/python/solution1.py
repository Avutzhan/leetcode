class Solution:
    def findLucky(self, arr: List[int]) -> int:
        li_dict = {}
        maximum = 0

        for n in arr:
            if n in li_dict:
                li_dict[n] += 1
            else:
                li_dict[n] = 1

        for key, value in li_dict.items():
            if key == value:
                maximum = max(maximum, value)

        if maximum > 0:
            return maximum
        else:
            return -1
        