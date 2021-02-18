class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_copy=arr.copy()
        arr_copy.sort()
        d={}
        a=[]
        rank=1

        for i in arr_copy:
            if i not in d:
                d[i]=rank
                rank+=1

        for i in arr:
            a.append(d[i])

        return a