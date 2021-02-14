class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        length1 = len(arr1)
        length2 = len(arr2)

        distance = length1;

        for i in range(length1):
            for j in range(length2):
                if abs(arr1[i] - arr2[j]) <= d:
                    distance -= 1
                    break

        return distance
