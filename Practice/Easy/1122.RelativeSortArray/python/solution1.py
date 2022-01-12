class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        o=[]
        arr1.sort()
        c=Counter(arr1)
        for i in arr2:                     #to add the elements refering from arr2
            for j in range(0,c[i]):
                o.append(i)
        for i in c:                       #to add the elements not present in arr2
            if i not in o:
                for j in range(0,c[i]):
                    o.append(i)
        return o