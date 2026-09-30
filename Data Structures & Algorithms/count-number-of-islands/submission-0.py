class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            visit.add((r, c))

            dirs = [[1,0], [-1, 0], [0, -1], [0, 1]]
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and grid[row][col] == "1" and (row, col) not in visit:
                    dfs(row,  col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands