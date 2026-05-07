class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ignored = set()
        queue = deque()
        ROW, COL = len(board), len(board[0])
        for row in range(ROW):
            for col in range(COL):
                val = board[row][col]
                if val == 'X':
                    continue
                if row == 0 or row == ROW - 1 or col == 0 or col == COL - 1:
                    ignored.add((row, col))
                    queue.append((row, col))

        def is_valid(row: int, col: int) -> bool:
            return not (row < 0 or col < 0 or row >= ROW or col >= COL)
        dirs = [0, 1, 0, -1, 0]
        while len(queue) > 0:
            row, col = queue.popleft()
            for dx, dy in pairwise(dirs):
                new_row, new_col = row + dx, col + dy
                if not is_valid(new_row, new_col):
                    continue
                if board[new_row][new_col] != 'O':
                    continue
                if (new_row, new_col) in ignored:
                    continue
                queue.append((new_row, new_col))
                ignored.add((new_row, new_col))
        for row in range(ROW):
            for col in range(COL):
                val = board[row][col]
                if val == 'O' and (row, col) not in ignored:
                    board[row][col] = 'X'
        