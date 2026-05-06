class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        overallMaxArea = 0
        dirs = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        def is_valid(row, col) -> bool:
            if row < 0 or col < 0:
                return False
            if row >= len(grid) or col >= len(grid[0]):
                return False
            return True
        def is_one(row, col) -> bool:
            return grid[row][col] == 1
        def paint(row, col) -> int:
            if not is_valid(row, col):
                return 0
            if not is_one(row, col):
                return 0
            total = 1
            grid[row][col] = 0
            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy
                total += paint(new_row, new_col)
            return total
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                overallMaxArea = max(overallMaxArea, paint(row, col))
        return overallMaxArea