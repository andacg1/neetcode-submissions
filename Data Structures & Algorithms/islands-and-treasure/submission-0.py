from queue import *
"""
[
[2,-1,0,1],
[2,2,1,-1],
[1,-1,2,-1],
[0,-1,2,3]
]
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        def is_valid(row, col) -> bool:
            if row < 0 or col < 0:
                return False
            if row >= len(grid) or col >= len(grid[0]):
                return False
            if (row, col) in visited:
                return False
            return True
        def is_land(row, col) -> bool:
            return grid[row][col] > 0
        treasure_chests = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasure_chests.append((row, col))
        dirs = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        queue = treasure_chests
        dist = 1
        
        while len(queue) > 0:
            temp_queue = deque()
            while len(queue) > 0:
                row, col = queue.popleft()
                # if is_land(row, col):
                #     grid[row][col] = dist
                for dx, dy in dirs:
                    new_row, new_col = row + dx, col + dy
                    if is_valid(new_row, new_col):
                        if is_land(new_row, new_col):
                            grid[new_row][new_col] = dist
                        else:
                            continue
                        temp_queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            dist += 1
            queue = temp_queue
        
