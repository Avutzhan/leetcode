class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                res += 1

        return res

