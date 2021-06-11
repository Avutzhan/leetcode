class Solution:
    def average(self, salary: List[int]) -> float:
        m = min(salary)
        x = max(salary)
        s = sum(salary) - m - x

        return s / (len(salary) - 2)
