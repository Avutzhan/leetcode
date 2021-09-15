class Solution:
    def prevPermOpt1(self, a: List[int]) -> List[int]:
        left = len(a)-1
        while left-1>0 and a[left-1]<=a[left]:
            left-=1
        if left==0: return a
        right = left
        for i in range(left,len(a)):
            if a[i]>a[right] and a[i]<a[left-1]: right = i
        a[right],a[left-1]=a[left-1],a[right]
        return a