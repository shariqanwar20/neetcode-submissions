class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row through binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        
        i, j = 0, COLS - 1

        while i in range(ROWS) and j in range(COLS):
            print(i, j)
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False
