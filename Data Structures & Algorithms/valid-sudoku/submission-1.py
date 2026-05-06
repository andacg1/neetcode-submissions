import itertools
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicates(arrays: List[List[str]]):
            #print(arrays)
            merged = list(filter(lambda x: x != ".",chain.from_iterable(arrays)))
            if len(merged) != len(set(merged)):
                print(merged)
            return len(merged) != len(set(merged))
        # check rows
        for row in board:
            if hasDuplicates([row]):
                return False
        # check cols
        for col in itertools.zip_longest(*board):
            if hasDuplicates([list(col)]):
                return False
        # check squares
        for i in range(3):
            for j in range(3):
                square = map(lambda x: x[i*3:i*3+3], board[j*3:j*3+3])
                #print(list(square))
                if hasDuplicates(list(square)):
                    return False
        return True