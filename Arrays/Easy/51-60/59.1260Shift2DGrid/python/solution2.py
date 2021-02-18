class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        lst = []
        for row in grid:
            lst.extend(row)
        items = deque(lst)

        # k %= len(items)

        items.rotate(k)
        print(items)
        items = list(items)
        lst = []
        for i in range(0, len(items), cols):
            lst.append(items[i:i+cols])
        return lst