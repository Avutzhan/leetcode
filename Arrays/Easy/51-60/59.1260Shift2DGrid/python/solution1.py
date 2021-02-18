class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = deque()
                for sublist in grid:
                    for item in sublist:
                        arr.append(item)

                for i in range(k):
                    popped = arr.pop()
                    print(popped)
                    arr.appendleft(popped)

                newarr = list(arr)
                result = []
                length = len(grid[0])

                for i in range(0, len(newarr), length):
                    print(newarr[i:i+length])
                    result.append(newarr[i:i+length])

                return result