from dataclasses import dataclass
from collections import namedtuple
# type Coord = Tuple[int, int]
Coord = namedtuple('Coord', ['row', 'col'])

class Solution:
    def is_valid(self, coord: Coord, grid: List[List[int]]) -> bool:
        if coord.row < 0 or coord.col < 0:
            return False
        if coord.row >= len(grid) or coord.col >= len(grid[0]):
            return False
        return True

    def is_fresh(self, coord: Coord, grid: List[List[int]]) -> bool:
        return grid[coord.row][coord.col] == 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges: Deque[Tuple[int, int]] = deque()
        fresh_oranges = 0
        minutes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                if val == 2:
                    rotten_oranges.append(Coord(row, col))
                elif val == 1:
                    fresh_oranges += 1
        dirs = [0, 1, 0, -1, 0]


        while len(rotten_oranges) > 0:
            temp = deque()
            count = 0
            # print(rotten_oranges)
            while len(rotten_oranges) > 0:
                curr = rotten_oranges.popleft()
                # print(curr)
                for dx, dy in pairwise(dirs):
                    new_coord = Coord(curr.row + dy, curr.col + dx)
                    if not self.is_valid(new_coord, grid):
                        # print(new_coord)
                        continue
                    if not self.is_fresh(new_coord, grid):
                        continue
                    grid[new_coord.row][new_coord.col] = 2
                    fresh_oranges -= 1
                    # fresh_oranges.remove(Coord(new_coord.row, new_coord.col))
                    count += 1
                    temp.append(new_coord)
            if count > 0:
                minutes += 1
            # print(temp)
            rotten_oranges = temp
        if fresh_oranges > 0:
            return -1
        return minutes