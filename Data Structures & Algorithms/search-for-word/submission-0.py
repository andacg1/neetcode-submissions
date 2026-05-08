class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [0, 1, 0, -1, 0]
        ROW, COL = len(board), len(board[0])

        def is_valid(row: int, col: int) -> bool:
            if row < 0 or col < 0 or row >= ROW or col >= COL:
                return False
            return True
        found = False

        """
        [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
        """

        def search(word_i: int, cell: Tuple[int, int], seen: Set[Tuple[int, int]]):
            row, col = cell
            nonlocal found
            if found:
                return
            if word_i + 1 >= len(word):
                found = True
                return
            
            for dx, dy in pairwise(dirs):
                new_row, new_col = row + dx, col + dy
                if not is_valid(new_row, new_col):
                    continue
                if (new_row, new_col) in seen:
                    continue
                if board[new_row][new_col] != word[word_i + 1]:
                    continue
                seen.add(cell)
                search(word_i + 1, (new_row, new_col), seen)
                seen.remove(cell)
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == word[0]:
                    search(0, (row, col), set())
                    if found:
                        return True
        return False
