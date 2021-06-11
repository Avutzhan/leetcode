class Solution:
    def countLargestGroup(self, n: int) -> int:
        m = {}
        maxx = 0

        for i in range(1, n + 1):
            summ = self.getSum(i)
            if summ in m:
                m[summ] += 1
            else:
                m[summ] = 1

        maxx = max(m.values())

        ans = list(filter(lambda x:x[1]==maxx,m.items()))

        return len(ans)

    def getSum(self, n: int) -> int:
        summ = 0
        while n > 0:
            summ += n % 10
            n //= 10
        return summ
