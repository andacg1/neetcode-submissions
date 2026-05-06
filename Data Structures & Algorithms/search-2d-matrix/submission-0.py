class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(row: List[int]):
            lo = 0
            hi = len(row) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    lo = mid + 1
                elif row[mid] > target:
                    hi = mid - 1
            return False
        def insideRow(row: List[int]):
            return row[0] <= target <= row[-1]
        lo = 0
        hi = len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row = matrix[mid]
            if insideRow(row):
                return searchRow(row)
            elif target > row[-1]:
                lo = mid + 1
            elif target < row[0]:
                hi = mid - 1
        return False