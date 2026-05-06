class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]
        ones = []
        def is_valid(row, col):
            if row < 0 or col < 0:
                return False
            if row >= len(grid) or col >= len(grid[0]):
                return False
            return grid[row][col] == '1'

        islands = 0
        def fill(row, col):
            queue = deque([(row, col)])
            while len(queue) > 0:
                # print(queue)
                curr = queue.popleft()
                # print(curr)
                for dx, dy in dirs:
                    candidate = (curr[0] + dx, curr[1] + dy)
                    if is_valid(candidate[0], candidate[1]):
                        queue.append(candidate)
                        grid[candidate[0]][candidate[1]] = '0'

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    fill(i, j)
                    islands += 1
        # islands += 1
        return islands