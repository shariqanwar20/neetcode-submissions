class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row through binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bott = 0, ROWS-1

        while top <= bott:
            m = top + (bott-top) // 2
            if target < matrix[m][0]:
                bott = m-1
            elif target > matrix[m][-1]:
                top = m+1
            else: 
                break
        if not (top <= bott):
            return False
        
        mid = top + (bott-top)//2
        l, r = 0, COLS-1

        while l <= r:
            m = l + (r-l)//2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] < target:
                l = m+1
            else:
                r = m-1
        return False