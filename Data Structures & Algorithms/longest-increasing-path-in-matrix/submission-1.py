class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        memo = {}
        def dfs(i, j, prev):

            if i not in range(ROWS) or j not in range(COLS) or matrix[i][j] <= prev:
                return 0
            
            if (i, j) in memo: return memo[(i, j)]
            res = 1
            for dr, dc in dirs:
                row, col = i + dr, j + dc
                
                res = max(res, 1 + dfs(row, col, matrix[i][j]))
            memo[(i, j)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(memo.values())