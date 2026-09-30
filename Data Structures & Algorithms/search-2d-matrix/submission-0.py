class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row through binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bott = 0, ROWS

        row = -1
        while top < bott:
            mid = top + (bott - top) //  2
            if target >= matrix[mid][0] and target <= matrix[mid][COLS - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                # go above
                bott = mid
            else:
                # go below
                top = mid + 1
        if row == -1:
            return False

        # run binary search on that 1D array
        l, r = 0, COLS

        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        return False