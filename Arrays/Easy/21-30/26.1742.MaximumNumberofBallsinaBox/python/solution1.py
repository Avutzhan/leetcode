class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        obj = {}

        for i in range(lowLimit,highLimit+1):
            summary = self.sumDigit(i);
            if summary not in obj:
                obj[summary]=1
            else:
                obj[summary]+=1

        return max(obj.values())

    def sumDigit(self, num: int) -> int:
        summary = 0

        while num:
            summary += num % 10
            num = num // 10

        return summary




