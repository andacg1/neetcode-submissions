class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_cells = set()
        atlantic_cells = set()
        pacific_queue = deque()
        atlantic_queue = deque()
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pacific_cells.add((row, col))
                    pacific_queue.append((row, col))
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    atlantic_cells.add((row, col))
                    atlantic_queue.append((row, col))

        def is_valid(row: int, col: int) -> bool:
            if row < 0 or col < 0:
                return False
            if row >= len(heights) or col >= len(heights[0]):
                return False
            return True

        def is_higher(row: int, col: int, curr: int) -> bool:
            return heights[row][col] >= curr
        dirs = [0, 1, 0, -1, 0]
        # print(pacific_queue)
        # print(atlantic_queue)

        def get_peaks(queue: Deque, cells: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
            while len(queue) > 0:
                row, col = queue.popleft()
                cells.add((row, col))
                for dx, dy in pairwise(dirs):
                    new_row, new_col = row + dx, col + dy
                    if not is_valid(new_row, new_col):
                        continue
                    if not is_higher(new_row, new_col, heights[row][col]):
                        continue
                    if (new_row, new_col) in cells:
                        continue
                    queue.append((new_row, new_col))
        get_peaks(pacific_queue, pacific_cells)
        get_peaks(atlantic_queue, atlantic_cells)
        # print(pacific_cells)
        # print(atlantic_cells)
        return list(pacific_cells & atlantic_cells)
