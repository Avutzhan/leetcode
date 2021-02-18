class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]

        print(end)


        result = [];

        if start <= end:
            for i in range(start, end + 1):
                result.append(i)

        else:
            for i in range(1, end + 1):
                result.append(i)

            for i in range(start, n + 1):
                result.append(i)




        return result